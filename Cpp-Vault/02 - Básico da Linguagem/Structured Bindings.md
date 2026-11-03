---
titulo: "Structured bindings"
tags: [cpp, basico, cpp17]
aliases: ["Structured bindings", "Decomposição", "auto [a, b]", "Ligações estruturadas"]
tipo: conceito
nivel: iniciante
padrao: C++17
criado: 2026-10-24
relacionados: ["[[auto e decltype]]", "[[Range-for e Inicializadores]]", "[[Funções - Cpp]]"]
---

# Structured bindings

> [!info] Introdução
> **C++17.** Suporte: GCC 7+, Clang 4+, MSVC 2017 15.3+.

Permitem **decompor** um objeto em vários nomes com uma única declaração: `auto [a, b] = expr;`.

## Onde funciona

| Origem | Exemplo |
|---|---|
| `std::pair` / `std::tuple` | `auto [it, ok] = m.insert(...)` |
| `struct` sem campos privados | `auto [x, y] = Ponto{1, 2}` |
| Array de tamanho fixo | `auto [a, b, c] = arr` |
| Tipos "tipo-tupla" personalizados | Especializando `std::tuple_size` e `get` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>
#include <map>
#include <string>
#include <tuple>

struct Ponto { int x; int y; };

std::tuple<int, double, std::string> dados() { return {1, 2.5, "oi"}; }

int main() {
    // Struct
    Ponto p{3, 4};
    auto [x, y] = p;                                   // cópia dos membros
    std::cout << x << ',' << y << '\n';                // 3,4

    // Tuple
    auto [i, d, s] = dados();
    std::cout << i << ' ' << d << ' ' << s << '\n';    // 1 2.5 oi

    // Array
    std::array<int, 3> arr{7, 8, 9};
    auto [a, b, c] = arr;
    std::cout << a + b + c << '\n';                    // 24

    // Referência: modifica o original
    auto& [rx, ry] = p;
    rx = 100;
    std::cout << p.x << '\n';                          // 100

    // Inserir em map: pair<iterator, bool>
    std::map<std::string, int> m;
    auto [it, inserido] = m.insert({"ana", 1});
    std::cout << it->first << ' ' << inserido << '\n'; // ana 1

    // Percorrer map
    for (const auto& [chave, valor] : m)
        std::cout << chave << '=' << valor << '\n';
}
```

## Qualificadores

- `auto [a, b] = obj;` → **cópia** do objeto; os nomes são partes da cópia.
- `auto& [a, b] = obj;` → nomes referem-se aos membros do original.
- `const auto& [a, b] = obj;` → leitura sem cópia (padrão em laços).

## Limitações

- Precisa nomear **todos** os elementos; não há como "pular" um. Em C++26 o placeholder `_` permite nomes descartáveis; antes, use um nome como `ignorado`.
- Não é possível declarar o binding como `constexpr`.
- Em lambdas, capturar um *structured binding* só é permitido a partir do C++20 (suporte varia entre compiladores).

> [!bug] Número de nomes errado
> ```cpp
> auto [a, b] = std::tuple{1, 2, 3};   // erro: 3 elementos, 2 nomes
> ```

> [!tip] Ótimo para retornos múltiplos
> Combine com funções que retornam `struct` nomeada: `auto [quociente, resto] = dividir(17, 5);` ([[Funções - Cpp]]).

## Veja também

- [[auto e decltype]]
- [[Range-for e Inicializadores]]
- [[Funções - Cpp]]
- [[Arrays e std array]]

## Exercício

1. Escreva `std::pair<int, int> min_max(const std::vector<int>&)` e consuma com structured bindings.
2. Percorra um `std::map<std::string,int>` e imprima chave e valor, modificando o valor via `auto& [k, v]`.
