---
titulo: "constexpr, consteval e constinit"
tags: [cpp, templates, constexpr]
aliases: ["consteval", "constinit", "Funções imediatas", "is_constant_evaluated", "constexpr cada vez mais"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[const e constexpr]]", "[[Metaprogramação em Compilação]]", "[[if constexpr]]"]
---

# `constexpr`, `consteval` e `constinit`

Complementa [[const e constexpr]] com os recursos do C++20 e posteriores.

| Palavra | Padrão | Significado |
|---|---|---|
| `constexpr` função | C++11 (ampliado em 14, 17, 20, 23) | **Pode** ser avaliada em compilação; também funciona em execução |
| `constexpr` variável | C++11 | Valor conhecido em compilação (e `const`) |
| `consteval` | **C++20** | Função **imediata**: **deve** ser avaliada em compilação; chamar em runtime é erro |
| `constinit` | **C++20** | Variável com **duração estática/thread** **inicializada** por expressão constante, mas **mutável** |
| `if consteval` | C++23 | Distingue contexto de avaliação constante |
| `std::is_constant_evaluated()` | C++20 | Mesma ideia (função, em `<type_traits>`) |

## O que cresceu em `constexpr`

| Padrão | Passou a ser permitido |
|---|---|
| C++14 | Variáveis locais, `if`/`for`/`while`, múltiplos `return` |
| C++17 | Lambdas `constexpr`, `if constexpr`, `std::array` (parcial), `constexpr` em muitos algoritmos |
| C++20 | `new`/`delete` **transientes**, `std::vector` e `std::string` **dentro** de avaliação constante, `virtual`, `try`, `union` ativa, `std::sort` etc. |
| C++23 | `constexpr` em mais partes (`std::unique_ptr`, `<cmath>` parcial, `static` locais constantes em 23) |
| C++26 | `constexpr` para exceções e mais algoritmos |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

constexpr int soma_ordenada() {
    std::vector<int> v{5, 3, 8, 1};            // vector em compilação (C++20): a memória não vaza para o runtime
    std::sort(v.begin(), v.end());
    int s = 0;
    for (int x : v) s = s * 10 + x;
    return s;                                  // 1358
}

static_assert(soma_ordenada() == 1358);

int main() { std::cout << soma_ordenada() << '\n'; }
```

## `consteval`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

consteval int quadrado(int n) { return n * n; }       // só em compilação

constexpr int calculado = quadrado(12);               // OK

int main() {
    std::cout << calculado << '\n';
    int n = 5;
    // std::cout << quadrado(n);                      // erro: 'n' não é constante de compilação
    std::cout << quadrado(7) << '\n';                 // OK: argumento constante
}
```

Usos: garantir validação **em compilação** (formatos de `std::format`, literais definidos pelo usuário que validam, tabelas, *hashes* de strings).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <iostream>
#include <string_view>

consteval std::uint32_t hash(std::string_view s) {     // FNV-1a em compilação
    std::uint32_t h = 2166136261u;
    for (char c : s) { h ^= static_cast<unsigned char>(c); h *= 16777619u; }
    return h;
}

int comando(std::uint32_t h) {
    switch (h) {
        case hash("iniciar"): return 1;                // usado como rótulo de case
        case hash("parar"):   return 2;
        default:              return 0;
    }
}

int main() { std::cout << comando(hash("parar")) << '\n'; }   // 2
```

## `constinit`: evita o *static initialization order fiasco*

`constinit` **obriga** a inicialização constante (em compilação) de variáveis estáticas, eliminando a inicialização dinâmica (e a ordem indefinida entre unidades de tradução). Diferente de `constexpr`, a variável **pode ser alterada** depois.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

constexpr int base() { return 40; }

constinit int contador = base() + 2;       // inicializado em compilação; ainda mutável
// constexpr: const e imutável. constinit: só garante a INICIALIZAÇÃO.

int main() {
    ++contador;
    std::cout << contador << '\n';         // 43
}
```

> [!bug] Exemplo inválido proposital
> ```cpp
> int calcula();                  // não constexpr
> constinit int x = calcula();    // erro: inicialização não constante
> ```

## `std::is_constant_evaluated()`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <type_traits>

constexpr int f(int x) {
    if (std::is_constant_evaluated()) return x * 2;        // caminho de compilação
    return x * 3;                                           // caminho de execução
}

int main() {
    constexpr int a = f(5);          // 10
    int n = 5;
    std::cout << a << ' ' << f(n) << '\n';   // 10 15
}
```

> [!warning] Cuidado
> Os dois caminhos devem ser **semanticamente equivalentes**; caso contrário, o programa se comporta de forma diferente conforme o contexto. Em `if constexpr (std::is_constant_evaluated())` o resultado é **sempre** verdadeiro (armadilha clássica): use `if consteval` (C++23).

## Veja também

- [[const e constexpr]]
- [[Metaprogramação em Compilação]]
- [[if constexpr]]
- [[Escopo e Duração de Armazenamento]]

## Exercício

1. Implemente `consteval int pot(int base, int exp)` e use em `std::array<int, pot(2, 5)>`.
2. Qual a diferença prática entre `constexpr int x = 5;` e `constinit int x = 5;` em um arquivo `.cpp`?
