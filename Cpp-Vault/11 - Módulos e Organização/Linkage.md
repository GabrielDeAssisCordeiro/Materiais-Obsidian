---
titulo: "Linkage (ligação)"
tags: [cpp, organizacao, static]
aliases: ["Ligação", "extern", "Namespace anônimo", "internal linkage", "external linkage"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Declaração vs Definição e ODR]]", "[[Escopo e Duração de Armazenamento]]", "[[Namespaces - Cpp]]"]
---

# Linkage (ligação)

*Linkage* define se um nome em TUs diferentes refere-se à **mesma entidade**.

| Tipo | Significado | Exemplos |
|---|---|---|
| **Externa** | Visível em outras TUs | Funções e variáveis globais não-`static`; classes/enums com nome; funções-membro |
| **Interna** | Visível apenas na TU | `static` em escopo de arquivo; namespace anônimo; `const`/`constexpr` globais (não `inline`) |
| **Nenhuma** | Locais | Variáveis locais, parâmetros |
| **Módulo** (C++20) | Visível dentro do mesmo módulo | Entidades não exportadas de módulos ([[Módulos Cpp20]]) |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

namespace {                                  // namespace anônimo: linkage interna (preferido a static)
int contador_interno = 0;
}

static int outro_interno = 10;               // também interno (forma antiga)
int visivel_a_todos = 5;                     // externo

int incrementa() { return ++contador_interno + outro_interno; }

int main() { std::cout << incrementa() << ' ' << visivel_a_todos << '\n'; }   // 11 5
```

## `extern`

`extern int n;` **declara** `n` sem definir (definição em outra TU). `extern "C"` muda a **convenção de nomes** (sem *name mangling*) — usada para interoperar com C ([[ABI]]).

```cpp
// arquivo: util.hpp
#pragma once
extern int contagem_global;                  // declaração; definir em um único util.cpp
```

```cpp
// arquivo: util.cpp
#include "util.hpp"
int contagem_global = 0;                     // definição
```

> [!warning] `static` tem três significados
> 1. Em escopo de arquivo: linkage interna. 2. Em função: variável com duração estática. 3. Em classe: membro compartilhado. Em C++ moderno, para (1) prefira **namespace anônimo**.

> [!tip] `inline` e linkage
> Funções/variáveis `inline` têm linkage externa mas podem ser definidas em vários TUs (cada TU com a mesma definição). Veja [[Declaração vs Definição e ODR]].

> [!info] Visibilidade em bibliotecas dinâmicas
> Linkage externa ≠ exportado da `.so`/`.dll`. Símbolos de biblioteca compartilhada dependem de `__attribute__((visibility("default")))`/`__declspec(dllexport)` — veja [[Bibliotecas Estáticas e Dinâmicas]].

## Veja também

- [[Declaração vs Definição e ODR]]
- [[Escopo e Duração de Armazenamento]]
- [[Namespaces - Cpp]]
- [[ABI]]

## Exercício

1. Duas TUs definem `static int x`; verifique com `nm` que não colidem.
2. Troque `static` por namespace anônimo e compare os símbolos exportados (`nm -C`).
