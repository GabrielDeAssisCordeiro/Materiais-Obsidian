---
titulo: "Declaração vs definição e a ODR"
tags: [cpp, organizacao, odr, linker]
aliases: ["ODR", "One Definition Rule", "Declaração", "Definição", "multiple definition"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Headers vs Sources]]", "[[Linkage]]", "[[Comportamento Indefinido e Não Especificado]]"]
---

# Declaração vs definição e a ODR

- **Declaração**: apresenta um nome e seu tipo (`int f(int);`, `extern int g;`, `class C;`).
- **Definição**: declara **e** cria a entidade (corpo da função, alocação da variável, membros da classe).

Toda definição é declaração; nem toda declaração é definição.

| Entidade | Declaração | Definição |
|---|---|---|
| Função | `int f(int);` | `int f(int x) { return x; }` |
| Variável global | `extern int n;` | `int n = 0;` |
| Classe | `class C;` (incompleta) | `class C { int v; };` |
| Variável estática de classe | `static int c;` (dentro da classe) | `int C::c = 0;` no `.cpp` (ou `inline static`, C++17) |

## One Definition Rule (ODR)

Resumo prático:

1. Em **todo o programa**, funções e variáveis não-`inline` com *linkage* externo devem ter **exatamente uma** definição → senão o linker reclama (*multiple definition*) ou, sem diagnóstico, há UB.
2. Em **cada TU**, cada entidade pode ser definida **no máximo uma vez**.
3. Classes, templates e funções `inline` podem ser definidas em várias TUs, desde que as definições sejam **idênticas** (token a token).

> [!danger] Violar a ODR é UB, muitas vezes sem diagnóstico
> Duas TUs com `struct S` de definições **diferentes** (por exemplo por macros que mudam os membros) compilam e ligam; o programa resultante tem comportamento indefinido. Veja [[Comportamento Indefinido e Não Especificado]].

## Erros típicos

```cpp
// arquivo: config.hpp  — ERRO INTENCIONAL
// Incluído em dois .cpp, gera "multiple definition of `limite'" no link.
// Correção: usar `inline constexpr int limite = 10;` (C++17) ou `extern` + definição em um .cpp.
int limite = 10;
```

```cpp
// arquivo: config.hpp  — correto (C++17)
#pragma once

inline constexpr int limite = 10;          // inline: uma "definição lógica" em todas as TUs

inline int quadrado(int x) { return x * x; }   // função inline em header
```

| Mensagem do linker | Causa | Correção |
|---|---|---|
| `undefined reference to 'f'` | Declarou, mas **ninguém definiu** (ou faltou ligar o `.o`/biblioteca) | Adicione o `.cpp` ao build / `-l`lib |
| `multiple definition of 'f'` | Definição não-`inline` em header incluído em várias TUs | `inline`, ou mova para `.cpp` |
| `redefinition of 'struct S'` | Header sem guard incluído duas vezes | [[Include Guards e pragma once]] |

> [!tip] Variáveis globais compartilhadas
> Prefira `inline constexpr`/`inline` variáveis (C++17) em vez do par `extern`+definição. Melhor ainda: evite estado global mutável.

## Veja também

- [[Headers vs Sources]]
- [[Linkage]]
- [[Include Guards e pragma once]]
- [[Comportamento Indefinido e Não Especificado]]
- [[Argumentos Padrão e inline]]

## Exercício

1. Provoque `multiple definition` e `undefined reference` e corrija cada um.
2. Explique por que `template<class T> T max(T,T)` em um header **não** viola a ODR.
