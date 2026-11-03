---
titulo: "Projeto 03 – Análise de Dados com CSV"
tags: [python, projeto, iniciante, csv, dados, collections]
nivel: intermediario
criado: 2026-10-14
projeto: 3
---

# 📊 Projeto 03 – Análise de Dados com CSV

> [!note] Pré-requisitos
> [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|CSV]], [[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|collections]] e [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|generators]].

## 🎯 Objetivo

Analisar um arquivo `vendas.csv` e gerar um **relatório em Markdown** com totais por categoria, por mês, produtos mais vendidos e estatísticas — usando **somente a biblioteca padrão**.

## 📥 Dados de entrada

Primeiro, um gerador de dados fictícios (reprodutível):

```python
# arquivo: gerar_dados.py
import csv, random
from datetime import date, timedelta

random.seed(42)
PRODUTOS = {
    "Notebook": ("Eletrônicos", 3500), "Mouse": ("Eletrônicos", 80),
    "Caneta": ("Papelaria", 3), "Caderno": ("Papelaria", 18),
    "Cadeira": ("Móveis", 650), "Mesa": ("Móveis", 900),
}
with open("vendas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["data", "produto", "categoria", "quantidade", "preco_unitario"])
    inicio = date(2026, 1, 1)
    for _ in range(500):
        nome = random.choice(list(PRODUTOS))
        cat, preco = PRODUTOS[nome]
        dia = inicio + timedelta(days=random.randint(0, 179))
        w.writerow([dia.isoformat(), nome, cat, random.randint(1, 5), preco])
```

## ✅ Requisitos

| # | Requisito |
|---|---|
| R1 | Ler o CSV com `csv.DictReader`, convertendo tipos (`date`, `int`, `float`) |
| R2 | Ignorar e **contar** linhas inválidas (sem derrubar o programa) |
| R3 | Faturamento total, ticket médio, mediana |
| R4 | Faturamento por categoria e por mês |
| R5 | Top 3 produtos por quantidade |
| R6 | Gerar `relatorio.md` com tabelas |
| R7 | Ler em *streaming* (generator), sem carregar tudo em lista |

## 🪜 Passo a passo

1. **Modelo:** `@dataclass(frozen=True) class Venda` com propriedade `total`.
2. **Leitura:** generator `ler_vendas(caminho)` que faz `yield Venda(...)` e captura `ValueError`/`KeyError` por linha.
3. **Agregação:** `defaultdict(float)` para categorias/meses; `Counter` para produtos.
4. **Estatística:** `statistics.mean/median`.
5. **Relatório:** função que monta o Markdown.

> [!warning] ❌ Armadilha: float para dinheiro
> `0.1 + 0.2 != 0.3`. Para um sistema financeiro real, use `decimal.Decimal`. Neste projeto, arredonde na **apresentação** (`:.2f`) e discuta o problema no desafio 3.

> [!tip] Dica
> Um iterador só pode ser percorrido **uma vez** ([[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|Generators]]). Se precisar de várias agregações, calcule todas em **um único laço**.

## 🏆 Desafios extras

1. Receber o caminho via `argparse`.
2. Trocar `float` por `Decimal`.
3. Comparar com `pandas` (`groupby`) e medir tempo ([[08 - Avançado/05 - Performance e Profiling|Profiling]]).
4. Gráfico com `matplotlib` salvo em PNG e embutido no relatório (embutido com um embed de imagem do Obsidian).
5. Filtros por período (`--de`, `--ate`).

> [!success] Solução
> [[09 - Projetos Práticos/Projeto 03 - Solução|Projeto 03 – Solução]]

---

⬅️ [[09 - Projetos Práticos/Projeto 02 - Solução|Solução do Projeto 02]] | ➡️ [[09 - Projetos Práticos/Projeto 03 - Solução|Solução]]

#python #projeto #csv #dados #collections #estatistica
