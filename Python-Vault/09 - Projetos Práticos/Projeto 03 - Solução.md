---
titulo: "Projeto 03 – Solução: Análise de CSV"
tags: [python, projeto, solucao, csv, dados]
nivel: intermediario
criado: 2026-10-14
projeto: 3
---

# ✅ Projeto 03 – Solução: Análise de CSV

Enunciado: [[09 - Projetos Práticos/Projeto 03 - Análise de Dados com CSV|Projeto 03]]. Gere `vendas.csv` com o script `gerar_dados.py` do enunciado.

## 💻 Código completo

```python
# arquivo: analise.py
"""Analisa vendas.csv e gera relatorio.md (apenas biblioteca padrão)."""

from __future__ import annotations

import csv
import statistics
import sys
from collections import Counter, defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Venda:
    data: date
    produto: str
    categoria: str
    quantidade: int
    preco_unitario: float

    @property
    def total(self) -> float:
        return self.quantidade * self.preco_unitario


def ler_vendas(caminho: Path, invalidas: list[int]) -> Iterator[Venda]:
    """Gera vendas válidas; guarda o número das linhas inválidas em `invalidas`."""
    with caminho.open(newline="", encoding="utf-8") as f:
        for n, linha in enumerate(csv.DictReader(f), start=2):  # 1 = cabeçalho
            try:
                yield Venda(
                    data=date.fromisoformat(linha["data"]),
                    produto=linha["produto"].strip(),
                    categoria=linha["categoria"].strip(),
                    quantidade=int(linha["quantidade"]),
                    preco_unitario=float(linha["preco_unitario"]),
                )
            except (ValueError, KeyError, TypeError):
                invalidas.append(n)


def analisar(vendas: Iterator[Venda]) -> dict:
    """Um único laço calcula todas as agregações."""
    por_categoria: defaultdict[str, float] = defaultdict(float)
    por_mes: defaultdict[str, float] = defaultdict(float)
    qtd_produto: Counter[str] = Counter()
    totais: list[float] = []

    for v in vendas:
        por_categoria[v.categoria] += v.total
        por_mes[v.data.strftime("%Y-%m")] += v.total
        qtd_produto[v.produto] += v.quantidade
        totais.append(v.total)

    if not totais:
        raise ValueError("nenhuma venda válida encontrada")

    return {
        "n": len(totais),
        "faturamento": sum(totais),
        "ticket_medio": statistics.mean(totais),
        "mediana": statistics.median(totais),
        "por_categoria": dict(sorted(por_categoria.items(), key=lambda kv: -kv[1])),
        "por_mes": dict(sorted(por_mes.items())),
        "top_produtos": qtd_produto.most_common(3),
    }


def moeda(valor: float) -> str:
    # formato brasileiro: 1.234,56
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def gerar_markdown(r: dict, invalidas: list[int]) -> str:
    linhas = [
        "# Relatório de Vendas",
        "",
        f"- **Vendas válidas:** {r['n']}",
        f"- **Linhas ignoradas:** {len(invalidas)} {invalidas[:10] if invalidas else ''}",
        f"- **Faturamento total:** {moeda(r['faturamento'])}",
        f"- **Ticket médio:** {moeda(r['ticket_medio'])}",
        f"- **Mediana:** {moeda(r['mediana'])}",
        "",
        "## Por categoria",
        "",
        "| Categoria | Faturamento |",
        "|---|---:|",
        *(f"| {c} | {moeda(v)} |" for c, v in r["por_categoria"].items()),
        "",
        "## Por mês",
        "",
        "| Mês | Faturamento |",
        "|---|---:|",
        *(f"| {m} | {moeda(v)} |" for m, v in r["por_mes"].items()),
        "",
        "## Top 3 produtos (quantidade)",
        "",
        "| # | Produto | Unidades |",
        "|---:|---|---:|",
        *(f"| {i} | {p} | {q} |" for i, (p, q) in enumerate(r["top_produtos"], 1)),
        "",
    ]
    return "\n".join(linhas)


def main() -> int:
    caminho = Path(sys.argv[1] if len(sys.argv) > 1 else "vendas.csv")
    if not caminho.exists():
        print(f"Arquivo não encontrado: {caminho}", file=sys.stderr)
        return 1
    invalidas: list[int] = []
    try:
        resultado = analisar(ler_vendas(caminho, invalidas))
    except ValueError as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1
    Path("relatorio.md").write_text(gerar_markdown(resultado, invalidas), encoding="utf-8")
    print(f"relatorio.md gerado ({resultado['n']} vendas, {len(invalidas)} ignoradas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 🔍 Pontos importantes

- **Generator + lista de inválidas:** `ler_vendas` não carrega o arquivo todo; linhas ruins são registradas (R2) e o processamento segue.
- **`@dataclass(frozen=True, slots=True)`:** imutável, leve em memória e com `total` calculado ([[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots|Dataclasses e Slots]]).
- **Um único laço** serve a todas as métricas (R7).
- **Número da linha:** `enumerate(..., start=2)` porque a linha 1 é o cabeçalho.
- **Formato BR de moeda** sem depender de `locale` (que varia por sistema).

## 🔁 Variação com `Decimal`

```python
from decimal import Decimal
preco_unitario=Decimal(linha["preco_unitario"])   # e use Decimal nas somas
```

---

⬅️ [[09 - Projetos Práticos/Projeto 03 - Análise de Dados com CSV|Projeto 03]] | ➡️ [[09 - Projetos Práticos/Projeto 04 - Web Scraper|Projeto 04]]

#python #projeto #solucao #csv #dados #collections
