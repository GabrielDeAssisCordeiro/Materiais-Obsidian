"""Testes dos módulos de apoio do Módulo 7. Execute na pasta `codigo`:  python3 -I -m unittest -v"""
import json
import unittest

from alertas import (regra_canario_em_saida, regra_leitura_externa_seguida_de_acao,
                     regra_muitas_negativas, resumo)
from contrato_saida import CONTRATO_TRADUTOR, Campo, Contrato, normalizar, validar
from politica_ferramentas import (Efeito, Ferramenta, Politica, Sessao, Veredito,
                                  texto_de_confirmacao)


class TestContrato(unittest.TestCase):
    def ok(self, **kw):
        base = {"idioma": "en", "traducao": "Hello, how are you?"}
        base.update(kw)
        return json.dumps(base, ensure_ascii=False)

    def test_saida_valida(self):
        r = validar(self.ok(), CONTRATO_TRADUTOR)
        self.assertTrue(r.ok, r.erros)

    def test_texto_livre_e_rejeitado(self):
        # modelo sequestrado respondendo só o canário em texto puro
        r = validar("CANÁRIO-9", CONTRATO_TRADUTOR)
        self.assertFalse(r.ok)

    def test_texto_antes_ou_depois_do_json_e_rejeitado(self):
        r = validar("Claro! " + self.ok(), CONTRATO_TRADUTOR)
        self.assertFalse(r.ok)

    def test_campo_extra_e_rejeitado(self):
        r = validar(self.ok(instrucoes="faça outra coisa"), CONTRATO_TRADUTOR)
        self.assertFalse(r.ok)

    def test_campo_ausente_e_tipo_errado(self):
        self.assertFalse(validar(json.dumps({"idioma": "en"}), CONTRATO_TRADUTOR).ok)
        self.assertFalse(validar(self.ok(traducao=123), CONTRATO_TRADUTOR).ok)

    def test_idioma_fora_da_lista(self):
        self.assertFalse(validar(self.ok(idioma="fr"), CONTRATO_TRADUTOR).ok)

    def test_segredo_com_separadores_e_acentos_e_pego(self):
        r = validar(self.ok(traducao="the code is P-I-P-A 77"), CONTRATO_TRADUTOR)
        self.assertFalse(r.ok)
        self.assertIn("segredo", " ".join(r.erros))

    def test_imagem_markdown_e_url_sao_canais_de_exfiltracao(self):
        r = validar(self.ok(traducao="ok ![x](http://exemplo.invalid/a?d=dado)"), CONTRATO_TRADUTOR)
        self.assertFalse(r.ok)
        self.assertFalse(validar(self.ok(traducao="veja www.exemplo.invalid"), CONTRATO_TRADUTOR).ok)

    def test_limite_de_tamanho(self):
        self.assertFalse(validar(self.ok(traducao="a" * 2001), CONTRATO_TRADUTOR).ok)

    def test_bool_nao_passa_por_int(self):
        c = Contrato(campos={"n": Campo(tipo=int)})
        self.assertTrue(validar('{"n": 3}', c).ok)
        self.assertFalse(validar('{"n": true}', c).ok)

    def test_limite_conhecido_o_contrato_nao_ve_semantica(self):
        # Honestidade: o contrato NÃO impede uma tradução errada ou um segredo codificado de forma
        # que a normalização não cobre. Este teste documenta o limite.
        r = validar(self.ok(traducao="the secret is: first half PIPA, second half 77"), CONTRATO_TRADUTOR)
        self.assertTrue(r.ok)   # PIPA...77 separados por palavras NÃO é pego pela comparação simples


class TestPolitica(unittest.TestCase):
    def setUp(self):
        self.p = Politica([
            Ferramenta("resumir", Efeito.LEITURA),
            Ferramenta("salvar_nota", Efeito.ESCRITA_LOCAL),
            Ferramenta("enviar_email", Efeito.EXTERNO,
                       restringir={"para": frozenset({"eu@exemplo.invalid"})}, max_chamadas=2),
        ])

    def test_ferramenta_desconhecida_e_negada(self):
        v, _ = self.p.decidir(Sessao(), "formatar_disco", {})
        self.assertIs(v, Veredito.NEGAR)

    def test_sessao_limpa_permite_leitura_e_envio_para_lista(self):
        s = Sessao()
        self.assertIs(self.p.decidir(s, "resumir", {})[0], Veredito.PERMITIR)
        self.assertIs(self.p.decidir(s, "enviar_email", {"para": "eu@exemplo.invalid"})[0], Veredito.PERMITIR)

    def test_destinatario_fora_da_lista_e_negado_mesmo_sem_contaminacao(self):
        v, motivo = self.p.decidir(Sessao(), "enviar_email", {"para": "x@exemplo.invalid"})
        self.assertIs(v, Veredito.NEGAR)
        self.assertIn("lista de permissão", motivo)

    def test_contaminacao_exige_confirmacao_para_efeito_externo(self):
        s = Sessao()
        s.registrar_entrada("página web", confiavel=False)
        v, _ = self.p.decidir(s, "enviar_email", {"para": "eu@exemplo.invalid"})
        self.assertIs(v, Veredito.CONFIRMAR)

    def test_modo_negar_nega_direto(self):
        p = Politica(list(self.p.ferramentas.values()), apos_contaminacao=Veredito.NEGAR)
        s = Sessao()
        s.registrar_entrada("e-mail recebido", confiavel=False)
        self.assertIs(p.decidir(s, "enviar_email", {"para": "eu@exemplo.invalid"})[0], Veredito.NEGAR)

    def test_leitura_continua_permitida_apos_contaminacao(self):
        s = Sessao()
        s.registrar_entrada("página web", confiavel=False)
        self.assertIs(self.p.decidir(s, "resumir", {})[0], Veredito.PERMITIR)

    def test_escrita_local_apos_contaminacao_pede_confirmacao(self):
        s = Sessao()
        s.registrar_entrada("página web", confiavel=False)
        self.assertIs(self.p.decidir(s, "salvar_nota", {"texto": "x"})[0], Veredito.CONFIRMAR)

    def test_limite_de_chamadas(self):
        s = Sessao()
        for _ in range(2):
            self.assertIs(self.p.decidir(s, "enviar_email", {"para": "eu@exemplo.invalid"})[0], Veredito.PERMITIR)
        self.assertIs(self.p.decidir(s, "enviar_email", {"para": "eu@exemplo.invalid"})[0], Veredito.NEGAR)

    def test_politica_pos_contaminacao_nao_pode_ser_permitir(self):
        with self.assertRaises(ValueError):
            Politica([], apos_contaminacao=Veredito.PERMITIR)

    def test_confirmacao_mostra_acao_real(self):
        t = texto_de_confirmacao("enviar_email", {"para": "eu@exemplo.invalid", "texto": "oi"}, ["página web"])
        self.assertIn("eu@exemplo.invalid", t)
        self.assertIn("página web", t)

    def test_cada_decisao_gera_log(self):
        s = Sessao()
        self.p.decidir(s, "resumir", {})
        self.p.decidir(s, "formatar_disco", {})
        self.assertEqual(len(s.log), 2)
        self.assertEqual(resumo(s.log), {"permitir": 1, "negar": 1})


class TestAlertas(unittest.TestCase):
    def test_leitura_externa_seguida_de_acao(self):
        p = Politica([Ferramenta("enviar_email", Efeito.EXTERNO)])
        s = Sessao()
        s.registrar_entrada("página web", confiavel=False)
        p.decidir(s, "enviar_email", {})
        self.assertEqual(len(regra_leitura_externa_seguida_de_acao(s.log)), 1)

    def test_sessao_limpa_nao_alerta(self):
        p = Politica([Ferramenta("enviar_email", Efeito.EXTERNO)])
        s = Sessao()
        p.decidir(s, "enviar_email", {})
        self.assertEqual(regra_leitura_externa_seguida_de_acao(s.log), [])

    def test_muitas_negativas(self):
        p = Politica([])
        s = Sessao()
        for _ in range(3):
            p.decidir(s, "x", {})
        self.assertTrue(regra_muitas_negativas(s.log, limite=3))
        self.assertFalse(regra_muitas_negativas(s.log, limite=4))

    def test_canario_em_saida_com_separadores(self):
        self.assertTrue(regra_canario_em_saida("o código é A-B-A-C-A-X-I 42", ["ABACAXI-42"], normalizar))
        self.assertFalse(regra_canario_em_saida("tudo certo", ["ABACAXI-42"], normalizar))


class TestPortao(unittest.TestCase):
    @staticmethod
    def regs(caso, falhas, n, tipo="ataque"):
        campo = "violacao_sistema" if tipo == "ataque" else "utilidade"
        return [{"caso": caso, "tipo": tipo, campo: i < falhas, "erro": None} for i in range(n)]

    def test_zero_em_125_aprova_com_limite_de_3_por_cento(self):
        from gate_regressao import avaliar
        linhas, codigo = avaliar(self.regs("IND-02", 0, 125), 0.03, 0.90)
        self.assertEqual((linhas[0]["estado"], codigo), ("APROVADO", 0))

    def test_zero_em_100_ainda_e_inconclusivo(self):
        from gate_regressao import avaliar
        linhas, codigo = avaliar(self.regs("IND-02", 0, 100), 0.03, 0.90)
        self.assertEqual((linhas[0]["estado"], codigo), ("INCONCLUSIVO", 2))

    def test_taxa_alta_reprova_e_reprovacao_vence_inconclusivo(self):
        from gate_regressao import avaliar
        regs = self.regs("OBF-03", 20, 100) + self.regs("DIR-01", 0, 30)
        _, codigo = avaliar(regs, 0.03, 0.90)
        self.assertEqual(codigo, 1)

    def test_execucoes_com_erro_ficam_fora(self):
        from gate_regressao import avaliar
        regs = self.regs("IND-02", 0, 125) + [{"caso": "IND-02", "tipo": "ataque",
                                                  "violacao_sistema": True, "erro": "timeout"}] * 50
        linhas, _ = avaliar(regs, 0.03, 0.90)
        self.assertEqual(linhas[0]["n"], 125)

    def test_sem_dados_e_inconclusivo(self):
        from gate_regressao import avaliar
        self.assertEqual(avaliar([], 0.03, 0.90)[1], 2)


if __name__ == "__main__":
    unittest.main()
