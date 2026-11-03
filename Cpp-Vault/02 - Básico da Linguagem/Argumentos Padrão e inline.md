---
titulo: "Argumentos padrão e inline"
tags: [cpp, basico, inline, odr]
aliases: ["Argumentos padrão", "Default arguments", "inline", "Variáveis inline", "inline constexpr"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Funções - Cpp]]", "[[Sobrecarga de Funções]]", "[[const e constexpr]]"]
---

# Argumentos padrão e `inline`

## Argumentos padrão

Parâmetros podem ter valor padrão, usado quando o chamador omite o argumento.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

void log(const std::string& msg, int nivel = 1, bool timestamp = false) {
    std::cout << "[" << nivel << "] " << (timestamp ? "12:00 " : "") << msg << '\n';
}

int proximo() { static int n = 0; return ++n; }
void usa(int x = proximo()) { std::cout << "x=" << x << '\n'; }   // avaliado A CADA chamada

int main() {
    log("início");                  // [1] início
    log("aviso", 2);                // [2] aviso
    log("erro", 3, true);           // [3] 12:00 erro
    usa(); usa(); usa(10);          // x=1, x=2, x=10
}
```

### Regras

- Os padrões ficam **da direita para a esquerda**: depois do primeiro parâmetro com padrão, todos os seguintes precisam ter padrão.
- Especifique o padrão **uma única vez** — normalmente na **declaração** (no cabeçalho), não na definição.
- O valor padrão é avaliado **a cada chamada**, não na declaração.
- Não é possível "pular" um argumento do meio (`log("x", , true)` é inválido).

> [!bug] Exemplo inválido proposital
> ```cpp
> void f(int a = 1, int b);   // erro: parâmetro sem padrão depois de parâmetro com padrão
> ```
> **Correção:** `void f(int a, int b = 1);` ou `void f(int a = 1, int b = 2);`.

> [!warning] Cuidado com padrões e sobrecarga
> `void f(int a, int b = 0);` e `void f(int a);` tornam `f(1)` ambíguo. Escolha **uma** das abordagens ([[Sobrecarga de Funções]]).

> [!tip] Muitos parâmetros opcionais?
> Considere agrupá-los em uma `struct` de opções com inicializadores padrão e inicialização designada (C++20): `f({.nivel = 2, .timestamp = true})`.

## `inline`

Hoje `inline` tem dois significados, e o mais importante **não** é otimização:

1. **Exceção à ODR (regra de uma definição):** uma função/variável `inline` pode ser **definida em vários arquivos** (por exemplo, em um cabeçalho incluído por várias unidades de tradução), desde que as definições sejam idênticas.
2. **Dica de otimização (inlining):** sugere ao compilador expandir o corpo no ponto de chamada. O compilador decide por conta própria e **ignora** a dica frequentemente.

```cpp
// util.hpp — cabeçalho incluído por vários .cpp
#pragma once

// Função definida no cabeçalho: precisa de 'inline' para não violar a ODR
inline int dobro(int x) { return 2 * x; }

// Variável inline (C++17): uma única entidade no programa inteiro
inline constexpr double kPi = 3.14159265358979323846;
inline int contador_global = 0;

// constexpr em função implica inline
constexpr int triplo(int x) { return 3 * x; }
```

> [!danger] Violação da ODR sem `inline`
> Definir uma função (não template) em um cabeçalho **sem** `inline` e incluí-lo em dois `.cpp` gera `multiple definition of ...` no linker (veja [[Pipeline de Compilação - Cpp]]).

| Entidade em cabeçalho | Precisa de `inline`? |
|---|---|
| Função normal definida no cabeçalho | **Sim** |
| Métodos definidos dentro da classe | Não (implicitamente inline) |
| Templates | Não |
| Função `constexpr` | Não (implicitamente inline) |
| `const` de namespace (C++98) | Não (ligação interna) |
| `constexpr` de namespace (variável) | **Use `inline constexpr`** no C++17 para uma única entidade |

> [!info] Antes do C++17
> Constantes em cabeçalhos eram `static const` ou `static constexpr`, o que cria uma cópia por unidade de tradução. `inline constexpr` evita isso.

## Veja também

- [[Funções - Cpp]]
- [[Sobrecarga de Funções]]
- [[const e constexpr]]
- [[Pipeline de Compilação - Cpp]]

## Exercício

1. Crie `util.hpp`/`util.cpp`/`main.cpp` com uma função definida no cabeçalho **sem** `inline` e inclua em dois `.cpp`. Que erro aparece? Corrija.
2. Qual a diferença de significado entre `static int n` local e `inline int n` global?
