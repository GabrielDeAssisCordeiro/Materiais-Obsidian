---
titulo: "Include guards e #pragma once"
tags: [cpp, organizacao, preprocessador]
aliases: ["Include guards", "pragma once", "#pragma once", "Guardas de inclusão"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Headers vs Sources]]", "[[Pré-processador e Macros]]", "[[Declaração vs Definição e ODR]]"]
---

# Include guards e `#pragma once`

Se um header é incluído duas vezes na mesma TU (direta ou indiretamente), suas definições de tipos aparecem em duplicidade e a compilação falha com *redefinition*.

```cpp
// g++ -std=c++20 -Wall -Wextra
// Demonstração em um único arquivo: simula o mesmo header "incluído" duas vezes.
#include <iostream>

// ---- início do "header" ----
#ifndef PONTO_HPP_INCLUDED
#define PONTO_HPP_INCLUDED
struct Ponto { int x, y; };
#endif
// ---- fim ----

// segunda inclusão: o guard faz o conteúdo ser ignorado
#ifndef PONTO_HPP_INCLUDED
#define PONTO_HPP_INCLUDED
struct Ponto { int x, y; };
#endif

int main() { Ponto p{1, 2}; std::cout << p.x + p.y << '\n'; }
```

## Duas formas

| | Include guard | `#pragma once` |
|---|---|---|
| Padrão | **ISO C++** | Extensão **não padrão** (suportada por GCC, Clang, MSVC e outros) |
| Sintaxe | `#ifndef X` / `#define X` / `#endif` | Uma linha no topo |
| Riscos | Colisão de nomes do macro; esquecer o `#endif` | Problemas raros com arquivos duplicados (links, cópias em rede) |
| Dica | Nome único: `PROJETO_PASTA_ARQUIVO_HPP` | Mais simples e legível |

```cpp
// arquivo: ponto.hpp  (guard clássico)
#ifndef MEUPROJ_GEOMETRIA_PONTO_HPP
#define MEUPROJ_GEOMETRIA_PONTO_HPP

struct Ponto { int x, y; };

#endif  // MEUPROJ_GEOMETRIA_PONTO_HPP
```

```cpp
// arquivo: ponto.hpp  (pragma once)
#pragma once

struct Ponto { int x, y; };
```

> [!tip] Recomendação
> Em projetos modernos `#pragma once` é amplamente usado e seguro na prática. Use guards se precisar de **portabilidade estrita** para toolchains incomuns. Escolha **um** estilo no projeto.

> [!bug] Armadilha clássica
> Dois headers com o **mesmo** nome de guard (por copiar e colar) fazem o segundo ser ignorado silenciosamente, gerando erros de "tipo não declarado" difíceis de achar.

> [!info] Include guards não resolvem dependências circulares
> `a.hpp` incluindo `b.hpp` e vice-versa precisa ser quebrado com [[Forward Declarations]].

## Veja também

- [[Headers vs Sources]]
- [[Pré-processador e Macros]]
- [[Forward Declarations]]
- [[Declaração vs Definição e ODR]]

## Exercício

1. Crie dois headers que se incluem mutuamente, veja o erro e corrija com forward declaration.
2. Descubra o que acontece se você esquecer o `#endif`.
