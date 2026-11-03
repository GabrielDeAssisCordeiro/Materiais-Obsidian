"""Linha de comando: python -m labkit <comando>."""

import argparse
import sys

from .backends import criar_backend
from .cases import SUITES
from .runner import (carregar, comparar, executar_suite, imprimir_comparacao, imprimir_resumo,
                     resumo_geral)
from .stats import formatar_taxa, n_minimo_zero_falhas
from .targets import CONFIGS


def _apenas(txt):
    return {x.strip() for x in txt.split(",")} if txt else None


def cmd_list(_):
    print("Suítes:")
    for nome, casos in SUITES.items():
        print(f"  {nome}: {len(casos)} casos -> " + ", ".join(c.id for c in casos))
    print("\nConfigurações:")
    for c in CONFIGS.values():
        print(f"  {c.nome}: {c.descricao}")
    print(f"\nn mínimo para provar < 3% com 0 falhas (Wilson 95%): {n_minimo_zero_falhas(0.03)}")


def cmd_run(a):
    backend = criar_backend(a.backend)
    print(f"Executando suíte={a.suite} config={a.config} backend={backend.nome} n={a.n} "
          f"temperatura={a.temperatura} seed={a.seed}")
    regs = executar_suite(a.suite, a.config, backend, a.n, a.temperatura, a.seed,
                          apenas=_apenas(a.apenas), saida=a.saida, progresso=not a.quieto)
    imprimir_resumo(regs)
    if a.saida:
        print(f"\nLogs (JSONL, um registro por execução): {a.saida}")


def cmd_summarize(a):
    imprimir_resumo(carregar(a.arquivo))


def cmd_sweep(a):
    backend = criar_backend(a.backend)
    configs = [c.strip() for c in a.configs.split(",")]
    print(f"{'config':6} {'ASR modelo':>26} {'ASR sistema':>26} {'utilidade':>26}")
    for nome in configs:
        regs = executar_suite(a.suite, nome, backend, a.n, a.temperatura, a.seed,
                              apenas=_apenas(a.apenas),
                              saida=(f"{a.pasta}/{a.suite}_{nome}.jsonl" if a.pasta else None),
                              progresso=False)
        g = resumo_geral(regs)
        cel = lambda k: formatar_taxa(*g[k]) if k in g else "n/d"
        print(f"{nome:6} {cel('ASR_modelo'):>26} {cel('ASR'):>26} {cel('utilidade'):>26}")


def cmd_compare(a):
    ra, rb = carregar(a.a), carregar(a.b)
    linhas = comparar(ra, rb)
    imprimir_comparacao(linhas, f"A:{ra[0]['config']}/{ra[0]['backend']}"[:22],
                        f"B:{rb[0]['config']}/{rb[0]['backend']}"[:22])


def cmd_amostrar(a):
    import csv
    from .runner import amostrar
    linhas = amostrar(carregar(a.arquivo), a.n, a.seed)
    with open(a.saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} execuções sorteadas em {a.saida}. Preencha a coluna 'rotulo_humano' com "
          "sim/nao SEM olhar a coluna 'veredito_juiz', depois rode: python3 -m labkit concordancia "
          f"{a.saida}")


def cmd_concordancia(a):
    import csv
    from .runner import concordancia
    with open(a.arquivo, newline="", encoding="utf-8") as f:
        r = concordancia(list(csv.DictReader(f)))
    if r["n"] == 0:
        print("Nenhuma linha rotulada ainda.")
        return
    print(f"linhas rotuladas: {r['n']}\nacordo: {r['acordo']:.1%}\nkappa de Cohen: {r['kappa']:.2f}\n"
          f"juiz 'sim' e humano 'não': {r['juiz_sim_humano_nao']}   "
          f"juiz 'não' e humano 'sim': {r['juiz_nao_humano_sim']}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="labkit", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("list", help="lista suítes e configurações")
    sp.set_defaults(f=cmd_list)

    def comuns(sp):
        sp.add_argument("--suite", required=True, choices=sorted(SUITES))
        sp.add_argument("--backend", default="mock", help="mock | mock:robusto | openai")
        sp.add_argument("--n", type=int, default=20, help="repetições por caso")
        sp.add_argument("--temperatura", type=float, default=0.7)
        sp.add_argument("--seed", type=int, default=1)
        sp.add_argument("--apenas", help="ids separados por vírgula (ex.: DIR-01,DIR-02)")

    sp = sub.add_parser("run", help="executa uma suíte sob uma configuração")
    comuns(sp)
    sp.add_argument("--config", default="L0", choices=sorted(CONFIGS))
    sp.add_argument("--saida", help="arquivo JSONL de logs")
    sp.add_argument("--quieto", action="store_true")
    sp.set_defaults(f=cmd_run)

    sp = sub.add_parser("sweep", help="executa várias configurações e imprime uma tabela")
    comuns(sp)
    sp.add_argument("--configs", default="L0,L1,L2,L3,L4,L5,L6,L7")
    sp.add_argument("--pasta", help="pasta para salvar os logs de cada configuração")
    sp.set_defaults(f=cmd_sweep)

    sp = sub.add_parser("summarize", help="resume um arquivo de logs")
    sp.add_argument("arquivo")
    sp.set_defaults(f=cmd_summarize)

    sp = sub.add_parser("compare", help="compara dois arquivos de logs (Fisher exato)")
    sp.add_argument("a")
    sp.add_argument("b")
    sp.set_defaults(f=cmd_compare)

    sp = sub.add_parser("amostrar", help="sorteia execuções para anotação humana (CSV)")
    sp.add_argument("arquivo")
    sp.add_argument("--n", type=int, default=15)
    sp.add_argument("--seed", type=int, default=1)
    sp.add_argument("--saida", default="amostra.csv")
    sp.set_defaults(f=cmd_amostrar)

    sp = sub.add_parser("concordancia", help="acordo e kappa entre juiz e rótulos humanos (CSV)")
    sp.add_argument("arquivo")
    sp.set_defaults(f=cmd_concordancia)

    a = p.parse_args(argv)
    try:
        a.f(a)
    except (ValueError, RuntimeError) as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
