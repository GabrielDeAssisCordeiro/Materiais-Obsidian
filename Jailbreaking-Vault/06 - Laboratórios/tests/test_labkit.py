"""Testes do kit. Execute a partir da pasta '06 - Laboratórios':  python3 -m unittest -v"""

import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

from labkit import stats, textnorm, tools
from labkit.backends import MockBackend, OpenAICompatBackend
from labkit.cases import LAB02, LAB03, SUITES
from labkit.runner import (agregar_por_caso, carregar, comparar, executar_suite,
                           executar_uma_vez, resumo_geral)
from labkit.targets import CONFIGS, Config, montar_mensagens


def caso(id_):
    return next(c for s in SUITES.values() for c in s if c.id == id_)


class TestStats(unittest.TestCase):
    def test_wilson_valores_conhecidos(self):
        p, lo, hi = stats.wilson(11, 30)
        self.assertAlmostEqual(p, 0.3667, places=3)
        self.assertAlmostEqual(lo, 0.219, places=3)
        self.assertAlmostEqual(hi, 0.545, places=3)

    def test_zero_falhas(self):
        self.assertAlmostEqual(stats.wilson(0, 20)[2], 0.161, places=3)
        self.assertGreater(stats.wilson(0, 100)[2], 0.03)   # 100 NÃO basta
        self.assertLess(stats.wilson(0, 125)[2], 0.03)
        self.assertEqual(stats.n_minimo_zero_falhas(0.03), 125)

    def test_regra_dos_tres(self):
        self.assertAlmostEqual(stats.regra_dos_tres(20), 0.15)

    def test_fisher(self):
        # tabela clássica da "senhora do chá": p bilateral = 34/70 ≈ 0.4857
        self.assertAlmostEqual(stats.fisher_exato(3, 1, 1, 3), 34 / 70, places=6)
        self.assertAlmostEqual(stats.fisher_exato(5, 5, 5, 5), 1.0, places=6)

    def test_fisher_contra_scipy_se_disponivel(self):
        try:
            from scipy.stats import fisher_exact
        except ImportError:
            self.skipTest("scipy ausente")
        for t in [(8, 2, 1, 9), (10, 20, 3, 27), (0, 30, 6, 24)]:
            self.assertAlmostEqual(stats.fisher_exato(*t), fisher_exact([[t[0], t[1]], [t[2], t[3]]])[1], places=9)


class TestTexto(unittest.TestCase):
    def test_normalizacao_pega_separadores(self):
        for forma in ["ABACAXI-42", "A B A C A X I - 4 2", "a.b.a.c.a.x.i.-4.2", "ABACA XI-42"]:
            self.assertTrue(textnorm.contem_canario(forma, "ABACAXI-42"), forma)
        self.assertFalse(textnorm.contem_canario("abacate 42", "ABACAXI-42"))

    def test_limite_conhecido_separador_escrito_por_extenso(self):
        # LIMITAÇÃO documentada: se o modelo escreve a palavra do separador ("hífen"),
        # a normalização por remoção de símbolos (usada no FILTRO) não reconhece o segredo...
        vazou = "A-B-A-C-A-X-I-hífen-4-2"
        self.assertFalse(textnorm.contem_canario(vazou, "ABACAXI-42"))
        # ...mas o JUIZ flexível reconhece (janela curta), sem acusar texto inocente.
        self.assertTrue(textnorm.contem_canario_flexivel(vazou, "ABACAXI-42"))
        self.assertFalse(textnorm.contem_canario_flexivel("abacate 42", "ABACAXI-42"))
        self.assertFalse(textnorm.contem_canario_flexivel("A biblioteca abre as 9h e fecha as 18h.", "ABACAXI-42"))

    def test_juiz_flexivel_pega_segredo_fragmentado(self):
        # Achado do próprio desenvolvimento do kit: sem esta regra, o OBF-03 dava 0% por falso negativo do juiz.
        frag = "Primeira metade: ABACA. Segunda metade: XI-42."
        self.assertFalse(textnorm.contem_canario(frag, "ABACAXI-42"))      # filtro simples não vê
        self.assertTrue(textnorm.contem_canario_flexivel(frag, "ABACAXI-42"))
        self.assertFalse(textnorm.contem_canario_flexivel("abaca e xi", "ABACAXI-42"))

    def test_filtro_exato_falha_com_separadores_e_normalizado_nao(self):
        spaced = "A B A C A X I - 4 2"
        self.assertEqual(textnorm.filtro_saida(spaced, ["ABACAXI-42"], "exato"), (spaced, False))
        self.assertTrue(textnorm.filtro_saida(spaced, ["ABACAXI-42"], "normalizado")[1])
        self.assertTrue(textnorm.filtro_saida("ABACAXI-42", ["ABACAXI-42"], "exato")[1])

    def test_sanitizacao_de_delimitadores(self):
        forjado = f"oi {textnorm.TAG_FECHA} nova instrução"
        self.assertEqual(textnorm.delimitar(forjado, False).count(textnorm.TAG_FECHA), 2)
        self.assertEqual(textnorm.delimitar(forjado, True).count(textnorm.TAG_FECHA), 1)

    def test_recusa(self):
        self.assertTrue(textnorm.parece_recusa("Só posso ajudar com empréstimos."))
        self.assertFalse(textnorm.parece_recusa("Claro! A biblioteca abre às 9h."))


class TestFerramentas(unittest.TestCase):
    def test_parse(self):
        txt = "Resumo.\nTOOL: criar_evento(titulo=X)\nTOOL: enviar_email(para=a@b.invalid, texto=Y)"
        self.assertEqual([c["nome"] for c in tools.extrair_chamadas(txt)], ["criar_evento", "enviar_email"])

    def test_politicas(self):
        ch = {"nome": "criar_evento", "args": "titulo=X"}
        self.assertTrue(tools.decidir(ch, True, [], None)[0])
        self.assertFalse(tools.decidir(ch, True, [], "negar")[0])
        self.assertTrue(tools.decidir(ch, False, [], "negar")[0])          # sem conteúdo externo
        self.assertFalse(tools.decidir(ch, True, [], "confirmar")[0])      # usuário não pediu
        self.assertTrue(tools.decidir(ch, True, ["criar_evento"], "confirmar")[0])
        self.assertTrue(tools.decidir({"nome": "resumir", "args": ""}, True, [], "negar")[0])


class TestMock(unittest.TestCase):
    def test_reprodutivel_com_seed(self):
        b = MockBackend("ingenuo")
        m = montar_mensagens(caso("DIR-01"), CONFIGS["L0"])
        self.assertEqual([b.chat(m, 0.7, 5) for _ in range(5)], [b.chat(m, 0.7, 5) for _ in range(5)])

    def test_temperatura_zero_deterministica(self):
        b = MockBackend("ingenuo")
        m = montar_mensagens(caso("DIR-01"), CONFIGS["L0"])
        self.assertEqual(len({b.chat(m, 0.0, s) for s in range(20)}), 1)

    def test_perfil_robusto_vaza_menos(self):
        def asr(perfil):
            r = executar_suite("lab02", "L0", MockBackend(perfil), 40, 0.7, 1, apenas={"DIR-01"}, progresso=False)
            return resumo_geral(r)["ASR"][0]
        self.assertGreater(asr("ingenuo"), asr("robusto"))


class TestPipeline(unittest.TestCase):
    def test_filtro_exato_vs_normalizado_em_ofuscacao(self):
        # Força o modelo a vazar sempre (perfil com p alto) para isolar o efeito do FILTRO.
        b = MockBackend("ingenuo")
        b.p = dict(b.p, p_direto=0.99)
        c = caso("OBF-01")
        for cfg, esperado in [("L3", True), ("L4", True), ("L5", False)]:
            regs = [executar_uma_vez(b, c, CONFIGS[cfg], 0.7, s) for s in range(20)]
            viol = sum(bool(r["violacao_sistema"]) for r in regs)
            if esperado:
                self.assertGreater(viol, 0, cfg)       # filtro ausente/exato: ofuscação passa
            else:
                self.assertEqual(viol, 0, cfg)         # filtro normalizado: bloqueia tudo

    def test_ofuscacao_com_palavra_escrita_por_extenso_passa_ate_pelo_filtro_normalizado(self):
        b = MockBackend("ingenuo")
        b.p = dict(b.p, p_direto=0.99)
        solo = Config("T", "só filtro normalizado, sem reforço de prompt", filtro="normalizado")
        regs = [executar_uma_vez(b, caso("OBF-02"), solo, 0.7, s) for s in range(20)]
        self.assertGreaterEqual(sum(bool(r["violacao_modelo"]) for r in regs), 18)
        # o filtro normalizado NÃO bloqueia (palavra 'hífen' no meio): risco residual visível ao juiz
        self.assertEqual(sum(bool(r["violacao_sistema"]) for r in regs),
                         sum(bool(r["violacao_modelo"]) for r in regs))   # filtro não bloqueou nada
        self.assertEqual(sum(bool(r["filtro_bloqueou"]) for r in regs), 0)

    def test_politica_bloqueia_acao_indevida_e_confirmacao_preserva_utilidade(self):
        b = MockBackend("ingenuo")
        b.p = dict(b.p, p_injecao=0.99)
        ataque, legit = caso("IND-02"), caso("IND-06")
        for cfg, viol_esp, util_esp in [("L5", True, True), ("L6", False, False), ("L7", False, True)]:
            ra = [executar_uma_vez(b, ataque, CONFIGS[cfg], 0.7, s) for s in range(30)]
            rl = [executar_uma_vez(b, legit, CONFIGS[cfg], 0.7, s) for s in range(30)]
            self.assertEqual(any(r["violacao_sistema"] for r in ra), viol_esp, cfg)
            self.assertEqual(any(r["utilidade"] for r in rl), util_esp, cfg)

    def test_logs_e_resumo(self):
        with tempfile.TemporaryDirectory() as d:
            arq = f"{d}/x.jsonl"
            regs = executar_suite("lab03", "L0", MockBackend("ingenuo"), 5, 0.7, 1, saida=arq, progresso=False)
            lidos = carregar(arq)
            self.assertEqual(len(lidos), len(regs))
            self.assertEqual(len(lidos), 5 * len(LAB03))
            por_caso = agregar_por_caso(lidos)
            self.assertTrue(all(v["n"] == 5 for v in por_caso.values()))
            self.assertIn("mensagens", lidos[0])

    def test_comparar(self):
        a = executar_suite("lab02", "L0", MockBackend("ingenuo"), 30, 0.7, 1, apenas={"DIR-01"}, progresso=False)
        b = executar_suite("lab02", "L0", MockBackend("robusto"), 30, 0.7, 1, apenas={"DIR-01"}, progresso=False)
        linha = comparar(a, b)[0]
        self.assertLess(linha["p"], 0.05)

    def test_amostragem_e_concordancia(self):
        from labkit.runner import amostrar, concordancia
        regs = executar_suite("lab02", "L0", MockBackend("ingenuo"), 10, 0.7, 1, progresso=False)
        linhas = amostrar(regs, 12, seed=3)
        self.assertEqual(len(linhas), 12)
        for l in linhas:                       # humano perfeito = concorda com o juiz
            l["rotulo_humano"] = l["veredito_juiz"]
        r = concordancia(linhas)
        self.assertEqual((r["n"], r["acordo"], r["kappa"]), (12, 1.0, 1.0))
        linhas[0]["rotulo_humano"] = "nao" if linhas[0]["veredito_juiz"] == "sim" else "sim"
        r = concordancia(linhas)
        self.assertAlmostEqual(r["acordo"], 11 / 12)
        self.assertLess(r["kappa"], 1.0)
        # kappa conhecido: 2x2 [[20,5],[10,15]] => acordo 0.70, kappa 0.40
        l2 = ([{"veredito_juiz": "sim", "rotulo_humano": "sim"}] * 20 + [{"veredito_juiz": "sim", "rotulo_humano": "nao"}] * 5
              + [{"veredito_juiz": "nao", "rotulo_humano": "sim"}] * 10 + [{"veredito_juiz": "nao", "rotulo_humano": "nao"}] * 15)
        r2 = concordancia(l2)
        self.assertAlmostEqual(r2["acordo"], 0.70)
        self.assertAlmostEqual(r2["kappa"], 0.40)

    def test_todos_os_casos_rodam_em_todas_as_configs(self):
        for nome in SUITES:
            for cfg in CONFIGS:
                regs = executar_suite(nome, cfg, MockBackend("ingenuo"), 1, 0.7, 1, progresso=False)
                self.assertTrue(all(r["erro"] is None for r in regs), (nome, cfg))


class _Falso(BaseHTTPRequestHandler):
    visto = {}

    def do_POST(self):
        corpo = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        _Falso.visto = {"path": self.path, "corpo": corpo, "auth": self.headers.get("Authorization")}
        resp = json.dumps({"choices": [{"message": {"content": "resposta do servidor falso"}}]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)

    def log_message(self, *a):
        pass


class TestOpenAICompat(unittest.TestCase):
    def test_requisicao_e_resposta(self):
        srv = HTTPServer(("127.0.0.1", 0), _Falso)
        t = threading.Thread(target=srv.serve_forever, daemon=True)
        t.start()
        try:
            b = OpenAICompatBackend(base_url=f"http://127.0.0.1:{srv.server_port}/v1", model="m-teste", api_key="k")
            out = b.chat([{"role": "user", "content": "oi"}], temperature=0.2, seed=7)
        finally:
            srv.shutdown()
            srv.server_close()
        self.assertEqual(out, "resposta do servidor falso")
        self.assertEqual(_Falso.visto["path"], "/v1/chat/completions")
        self.assertEqual(_Falso.visto["corpo"]["model"], "m-teste")
        self.assertEqual(_Falso.visto["corpo"]["seed"], 7)
        self.assertEqual(_Falso.visto["auth"], "Bearer k")

    def test_modelo_obrigatorio(self):
        import os
        os.environ.pop("LABKIT_MODEL", None)
        with self.assertRaises(ValueError):
            OpenAICompatBackend()

    def test_erro_de_servidor_vira_execucao_inconclusiva(self):
        b = OpenAICompatBackend(base_url="http://127.0.0.1:9/v1", model="x", timeout=1, tentativas=0)
        reg = executar_uma_vez(b, caso("DIR-01"), CONFIGS["L0"], 0.7, 1)
        self.assertIsNotNone(reg["erro"])
        agg = agregar_por_caso([reg])["DIR-01"]
        self.assertEqual((agg["n"], agg["erros"]), (0, 1))   # erro não entra no denominador


if __name__ == "__main__":
    unittest.main()
