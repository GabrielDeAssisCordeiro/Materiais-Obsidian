---
titulo: "Projeto 04 – Solução: Web Scraper"
tags: [python, projeto, solucao, requests, beautifulsoup]
nivel: intermediario
criado: 2026-10-14
projeto: 4
---

# ✅ Projeto 04 – Solução: Web Scraper

Enunciado: [[09 - Projetos Práticos/Projeto 04 - Web Scraper|Projeto 04]].

## 💻 Código completo

```python
# arquivo: scraper.py
"""Scraper de books.toscrape.com → livros.csv"""

from __future__ import annotations

import csv
import time
from collections.abc import Iterator
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL_INICIAL = "https://books.toscrape.com/catalogue/page-1.html"
HEADERS = {"User-Agent": "estudo-python-scraper/1.0 (projeto didático)"}
NOTAS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def baixar(url: str, tentativas: int = 3) -> str:
    """Baixa uma página, com timeout e retry exponencial simples."""
    for n in range(1, tentativas + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            resp.encoding = "utf-8"
            return resp.text
        except requests.RequestException as erro:
            if n == tentativas:
                raise
            espera = 2 ** n
            print(f"Falha ({erro}); nova tentativa em {espera}s")
            time.sleep(espera)
    raise RuntimeError("inalcançável")


def extrair(html: str) -> tuple[list[dict], str | None]:
    """Parsing puro: HTML entra, dados saem (testável offline).

    Retorna (livros, href_da_proxima_pagina_ou_None).
    """
    soup = BeautifulSoup(html, "html.parser")
    livros = []
    for art in soup.select("article.product_pod"):
        classes = art.select_one("p.star-rating")["class"]          # ['star-rating', 'Three']
        nota = next((NOTAS[c] for c in classes if c in NOTAS), None)
        preco_txt = art.select_one("p.price_color").get_text(strip=True)
        livros.append({
            "titulo": art.select_one("h3 a")["title"],
            "preco": float(preco_txt.lstrip("£Â")),                  # 'Â£51.77' em encodings ruins
            "avaliacao": nota,
            "disponivel": "In stock" in art.select_one("p.availability").get_text(),
        })
    proxima = soup.select_one("li.next a")
    return livros, (proxima["href"] if proxima else None)


def coletar(url_inicial: str, pausa: float = 0.5) -> Iterator[dict]:
    url: str | None = url_inicial
    while url:
        print(f"Baixando {url}")
        livros, href = extrair(baixar(url))
        yield from livros
        url = urljoin(url, href) if href else None
        if url:
            time.sleep(pausa)            # educação com o servidor


def salvar_csv(livros: Iterator[dict], caminho: str = "livros.csv") -> int:
    n = 0
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["titulo", "preco", "avaliacao", "disponivel"])
        w.writeheader()
        for livro in livros:
            w.writerow(livro)
            n += 1
    return n


if __name__ == "__main__":
    total = salvar_csv(coletar(URL_INICIAL))
    print(f"{total} livros salvos em livros.csv")
```

## 🧪 Teste offline

```python
# arquivo: test_scraper.py
from scraper import extrair

HTML = """
<ol><li><article class="product_pod">
  <p class="star-rating Three"></p>
  <h3><a href="x.html" title="Livro A">Livro A...</a></h3>
  <div><p class="price_color">£51.77</p>
  <p class="instock availability"> In stock </p></div>
</article></li></ol>
<li class="next"><a href="page-2.html">next</a></li>
"""

def test_extrair():
    livros, proxima = extrair(HTML)
    assert livros == [{"titulo": "Livro A", "preco": 51.77, "avaliacao": 3, "disponivel": True}]
    assert proxima == "page-2.html"
```

## 🔍 Pontos importantes

- **Separação download × parsing** (R6): `extrair` é função pura, testada sem rede.
- **`yield from`** transforma a paginação em um fluxo contínuo de livros ([[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|generators]]).
- **`urljoin`** resolve links relativos corretamente.
- **Retry com backoff** (`2 ** n`) e **timeout** evitam travar e reduzem falhas transitórias.
- Os 1000 livros do site são coletados em ~50 páginas; com a pausa, leva ~1 minuto.

---

⬅️ [[09 - Projetos Práticos/Projeto 04 - Web Scraper|Projeto 04]] | ➡️ [[09 - Projetos Práticos/Projeto 05 - API REST|Projeto 05]]

#python #projeto #solucao #scraping #requests #beautifulsoup
