---
titulo: "Sites e Documentação Oficial"
tags: [python, recursos, documentacao]
nivel: todos
criado: 2026-10-14
---

# 🌐 Sites e Documentação Oficial

> [!tip] Hábito de ouro
> Antes de buscar no Google, tente `help(objeto)` e `dir(objeto)` no REPL. Depois, consulte a documentação oficial. Ela é, na maioria das vezes, a fonte mais precisa.

## 📖 Documentação oficial do Python

| Recurso | Endereço | Para quê |
|---|---|---|
| Documentação (pt-BR) | `docs.python.org/pt-br/3/` | Tradução comunitária; algumas páginas podem estar defasadas em relação ao inglês |
| **Tutorial oficial** | `docs.python.org/3/tutorial/` | Visão geral progressiva da linguagem |
| **Referência da Biblioteca** | `docs.python.org/3/library/` | Todos os módulos (os, pathlib, itertools…) |
| **Referência da Linguagem** | `docs.python.org/3/reference/` | Gramática e semântica formais |
| **O que há de novo** | `docs.python.org/3/whatsnew/` | Novidades de cada versão (3.12, 3.13…) |
| Python HOWTOs | `docs.python.org/3/howto/` | Guias temáticos (descriptors, logging, regex, asyncio…) |
| Downloads | `python.org/downloads` | Instaladores |
| Status das versões | `devguide.python.org/versions/` | Quais versões ainda recebem suporte |

## 📜 PEPs (Python Enhancement Proposals)

Índice: `peps.python.org`

| PEP | Assunto | Onde aparece neste vault |
|---|---|---|
| **PEP 8** | Guia de estilo | [[01 - Fundamentos/06 - Comentários e Boas Práticas|Boas Práticas]] |
| **PEP 20** | *The Zen of Python* (`import this`) | [[01 - Fundamentos/06 - Comentários e Boas Práticas|Boas Práticas]] |
| **PEP 257** | Docstrings | [[03 - Funções e Modularização/06 - Docstrings|Docstrings]] |
| **PEP 484** | Type hints | [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|Type Hints]] |
| **PEP 634–636** | Pattern matching (`match/case`) | [[02 - Controle de Fluxo e Estruturas de Dados/01 - if elif else e match case|match/case]] |
| **PEP 695** | Sintaxe de generics e `type` (3.12) | [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|Type Hints]] |
| **PEP 518 / 621** | `pyproject.toml` | [[08 - Avançado/07 - Packaging e Distribuição|Packaging]] |
| **PEP 3156** | Base do `asyncio` | [[08 - Avançado/02 - Asyncio|Asyncio]] |

## 🧑‍🏫 Aprendizado e referência

| Site | O que oferece |
|---|---|
| **Real Python** (`realpython.com`) | Tutoriais longos e muito bem explicados (parte do conteúdo é paga) |
| **Python Tutor** (`pythontutor.com`) | Visualiza a execução passo a passo — excelente para entender variáveis, referências e recursão |
| **Python Brasil / Grupy** | Comunidade brasileira: conferência anual (PyCon Brasil) e grupos regionais (Grupy-SP, Grupy-DF etc.) |
| **Stack Overflow / Stack Overflow em Português** | Perguntas e respostas. Leia a pergunta **e** a data da resposta |
| **Python Discord** e comunidades em português (Telegram/Discord) | Tirar dúvidas |

## 🏋️ Praticar

| Plataforma | Perfil |
|---|---|
| **Exercism** (trilha Python) | Exercícios com *mentoria* e feedback |
| **Codewars** | "Katas" curtos, comparação com soluções de outros |
| **HackerRank** / **LeetCode** | Problemas de entrevista e algoritmos |
| **Advent of Code** | Puzzles todo mês de dezembro |
| **Project Euler** | Problemas matemáticos + programação |
| **Beecrowd** (ex-URI) | Plataforma brasileira de problemas |

## 🧰 Documentação das ferramentas que usamos

| Ferramenta | Documentação | Módulo |
|---|---|---|
| pytest | `docs.pytest.org` | [[08 - Avançado/06 - Testes com unittest e pytest|Testes]] |
| mypy / pyright | `mypy.readthedocs.io` / `microsoft.github.io/pyright` | [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|Type Hints]] |
| Packaging Guide | `packaging.python.org` | [[08 - Avançado/07 - Packaging e Distribuição|Packaging]] |
| PyPI | `pypi.org` | Repositório de pacotes |
| FastAPI | `fastapi.tiangolo.com` | [[09 - Projetos Práticos/Projeto 05 - API REST|Projeto 05]] |
| python-telegram-bot | `docs.python-telegram-bot.org` | [[09 - Projetos Práticos/Projeto 06 - Bot|Projeto 06]] |
| Requests / Beautiful Soup | `requests.readthedocs.io` / `crummy.com/software/BeautifulSoup/bs4/doc/` | [[09 - Projetos Práticos/Projeto 04 - Web Scraper|Projeto 04]] |
| Ruff / uv / Black | linters, formatadores e gerenciadores de projeto modernos — veja a documentação de cada projeto | [[08 - Avançado/07 - Packaging e Distribuição|Packaging]] |
| Obsidian | `help.obsidian.md` | Este vault |

> [!warning] Cuidado com fontes desatualizadas
> Python evolve rápido: tutoriais anteriores ao 3.10 não mencionam `match/case`; os anteriores ao 3.12 usam `TypeVar`/`Generic` em vez de `def f[T]`. Sempre verifique **a data** e **a versão** do que está lendo.

> [!note] Endereços podem mudar
> Os endereços acima são os conhecidos na data de escrita. Se algum não abrir, procure o nome do recurso em um buscador.

---

⬅️ [[10 - Recursos e Referências/01 - Livros Recomendados|Livros Recomendados]] | ➡️ [[10 - Recursos e Referências/03 - Canais e Cursos|Canais e Cursos]]

#python #recursos #documentacao #pep #sites
