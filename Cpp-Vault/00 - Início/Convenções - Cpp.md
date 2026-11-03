---
titulo: "Convenções - Cpp"
tags: [cpp, inicio]
aliases: ["Legenda do vault"]
tipo: guia
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Como Usar este Vault - Cpp]]", "[[Home - Cpp]]"]
---

# Convenções - Cpp

## Frontmatter

Toda nota tem:

| Campo | Significado |
|---|---|
| `titulo` | Título da nota (igual ao H1, sem emoji) |
| `tags` | Assunto (`cpp`, `stl`, `concorrencia`...) |
| `aliases` | Nomes alternativos para busca e links |
| `tipo` | `conceito`, `procedimento`, `referencia`, `ferramenta`, `comparacao`, `projeto`, `exercicio`, `guia` ou `moc` |
| `nivel` | `iniciante`, `intermediario` ou `avancado` |
| `padrao` | Padrão C++ **mínimo** exigido (C++98, C++11, C++14, C++17, C++20, C++23, C++26) |
| `criado` | Data de criação |
| `relacionados` | Links para notas próximas |

## Callouts

| Callout | Uso |
|---|---|
| `> [!info]` | Contexto, padrão em que o recurso foi introduzido, suporte de compiladores |
| `> [!tip]` | Boa prática e atalhos |
| `> [!warning]` | Armadilhas e cuidados |
| `> [!bug]` | Erros comuns e exemplos **propositalmente inválidos** |
| `> [!danger]` | **Comportamento indefinido** (UB) e riscos de segurança |
| `> [!example]` | Exemplos extras |
| `> [!question] Verificar na documentação oficial` | Detalhe que pode variar ou não foi confirmado |

## Blocos de código

- Blocos compiláveis começam com a linha de compilação: `// g++ -std=c++20 -Wall -Wextra`.
- Blocos de recursos experimentais ou indisponíveis em muitos compiladores indicam isso no início (por exemplo, `// [nv] g++ -std=c++26 ...`, "não verificado em ambiente de teste").
- Exemplos inválidos ou com UB vêm em callouts `[!bug]`/`[!danger]`, com a **correção** logo em seguida.

## Nomes de arquivo

- "C++" aparece como `Cpp` nos nomes de arquivo; o título interno e os `aliases` mantêm "C++".
- O nome do arquivo é único em todo o vault. Se o nome se repetir em outro material, acrescente ` - Cpp` (como em `Home - Cpp`).
- Cada pasta tem um `MOC - <Seção>.md`.

## Seções finais

Toda nota termina com `## Veja também` e, quando faz sentido, `## Exercício`.

## Veja também

- [[Como Usar este Vault - Cpp]]
- [[Home - Cpp]]
- [[MOC - Fundamentos - Cpp]]
