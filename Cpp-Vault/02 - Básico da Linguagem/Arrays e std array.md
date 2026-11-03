---
titulo: "Arrays e std::array"
tags: [cpp, basico, arrays]
aliases: ["std::array", "Arrays C", "Array decay", "Arrays multidimensionais", "std::to_array"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Strings C e std string]]", "[[string_view]]", "[[Structured Bindings]]"]
---

# Arrays e `std::array`

## Arrays de estilo C

Tamanho **fixo, conhecido em tempo de compilação**, elementos contíguos na memória, **sem verificação de limites**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <iterator>   // std::size

int main() {
    int a[5] = {1, 2, 3};                    // restantes zerados: {1,2,3,0,0}
    int b[] = {10, 20, 30, 40};              // tamanho deduzido: 4

    std::cout << sizeof b / sizeof b[0] << '\n';   // 4 (truque clássico do sizeof)
    std::cout << std::size(b) << '\n';             // 4 (C++17, mais seguro)

    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};          // 2 linhas x 3 colunas, contíguo
    std::cout << m[1][2] << '\n';                  // 6

    for (int x : a) std::cout << x << ' ';
    std::cout << '\n';
}
```

### *Array decay*: o array "vira" ponteiro

Ao passar para uma função, o array decai para ponteiro e **perde o tamanho**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void f(int p[]) {                  // na verdade: int* p
    std::cout << sizeof p << '\n'; // tamanho de um ponteiro (8 em 64 bits), NÃO do array
}

int main() {
    int a[10] = {};
    std::cout << sizeof a << '\n'; // 40 (10 * 4)
    f(a);
}
```

> [!danger] Acesso fora dos limites é UB
> ```cpp
> int a[3] = {1, 2, 3};
> int x = a[3];      // ERRO: índices válidos são 0..2. COMPORTAMENTO INDEFINIDO
> a[10] = 0;         // corrompe memória adjacente
> ```
> **Correção:** use `std::array` com `.at()`, `std::vector`, ou verifique o índice. Compile com `-fsanitize=address` para detectar.

## `std::array` (C++11, `<array>`)

Envolve um array de tamanho fixo em uma classe **sem overhead**, com interface de contêiner: `size()`, `begin()/end()`, `front()/back()`, `at()`, `fill()`, comparação, cópia por atribuição.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <array>
#include <iostream>

int main() {
    std::array<int, 5> a{5, 3, 1, 4, 2};

    std::sort(a.begin(), a.end());                    // funciona com algoritmos da STL
    for (int x : a) std::cout << x << ' ';            // 1 2 3 4 5
    std::cout << '\n';

    std::cout << a.size() << ' ' << a.front() << ' ' << a.back() << '\n';   // 5 1 5

    try {
        std::cout << a.at(10) << '\n';                // at() verifica limites e lança exceção
    } catch (const std::out_of_range& e) {
        std::cout << "fora dos limites\n";
    }

    auto b = a;                                        // cópia profunda por atribuição
    b.fill(0);
    std::cout << (a == b) << '\n';                     // 0

    auto c = std::to_array({1, 2, 3});                 // C++20: deduz tipo e tamanho
    static_assert(c.size() == 3);

    constexpr std::array<int, 3> k{7, 8, 9};           // pode ser constexpr
    static_assert(k[1] == 8);
}
```

> [!info] `std::out_of_range`
> Vem de `<stdexcept>` (incluído indiretamente por `<array>`/`<string>`, mas inclua explicitamente em código real).

## Comparação

| | `T[N]` | `std::array<T,N>` | `std::vector<T>` |
|---|---|---|---|
| Tamanho | Fixo (compilação) | Fixo (compilação) | Dinâmico |
| Local típico | Pilha / estático | Pilha / estático | Heap |
| Conhece o próprio tamanho | Não (decai) | **Sim** | Sim |
| Atribuição/cópia | Não | **Sim** | Sim |
| Verificação de limites | Não | `at()` | `at()` |

> [!tip] Regra prática
> Tamanho fixo e pequeno → `std::array`. Tamanho que varia ou desconhecido → `std::vector`. Arrays C ficam para APIs legadas.

> [!warning] Arrays grandes na pilha
> `int big[10'000'000];` como variável local pode estourar a pilha (típico de 1 a 8 MB). Use `std::vector` ou `static`.

## Veja também

- [[Strings C e std string]]
- [[string_view]]
- [[Structured Bindings]]
- [[Aritmética de Ponteiros]]
- [[Stack vs Heap]]

## Exercício

1. Escreva uma função template que recebe `std::array<int, N>&` e retorna a soma dos elementos.
2. Mostre, com `sizeof`, a diferença entre um array dentro e fora de uma função (decay).
