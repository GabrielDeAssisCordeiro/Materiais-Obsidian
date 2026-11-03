---
titulo: "std::bitset e utilitários de bits"
tags: [cpp, stl, bits, flags]
aliases: ["std::bitset", "bitset", "Conjunto de bits", "std::popcount", "std::bit"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Operadores - Cpp]]", "[[vector]]", "[[Tipos Fundamentais]]"]
---

# `std::bitset` e utilitários de bits

`std::bitset<N>` (`<bitset>`) é um conjunto de **N bits** de tamanho **fixo em compilação**, com operações lógicas e acesso por índice.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <bit>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <string>

int main() {
    std::bitset<8> b{0b10110010};                          // construção a partir de inteiro
    std::bitset<8> c{"00001111"};                          // ou de string

    std::cout << b << ' ' << c << '\n';                    // 10110010 00001111
    std::cout << b.count() << ' ' << b.size() << '\n';     // 4 8 (bits ligados / tamanho)
    std::cout << b[1] << b.test(0) << b.any() << b.none() << b.all() << '\n';   // 1 0 1 0 0

    b.set(0);                                              // liga o bit 0
    b.reset(7);                                            // desliga o bit 7
    b.flip(1);                                             // inverte o bit 1
    std::cout << b << '\n';

    std::cout << (b & c) << (b | c) << (b ^ c) << (~c) << '\n';   // operadores bit a bit
    std::cout << (b << 2) << (b >> 2) << '\n';                    // deslocamentos
    std::cout << b.to_ulong() << ' ' << b.to_string() << '\n';

    // Utilitários de <bit> (C++20) para inteiros
    std::uint32_t x = 0b1011000;
    std::cout << std::popcount(x) << ' '                   // 3: bits ligados
              << std::countr_zero(x) << ' '                // 3: zeros à direita
              << std::bit_width(x) << ' '                  // 7: bits necessários
              << std::has_single_bit(8u) << ' '            // 1: potência de 2?
              << std::bit_ceil(5u) << '\n';                // 8: próxima potência de 2
}
```

## Quando usar

| Necessidade | Escolha |
|---|---|
| Conjunto de flags **de tamanho fixo** conhecido | `std::bitset<N>` |
| Máscara em um único inteiro | `uint32_t` + operadores bit a bit |
| Bits em **tamanho dinâmico** | `std::vector<bool>` ou `boost::dynamic_bitset` |
| Conjunto de opções tipadas | `enum class` com operadores de bit, ou `std::bitset<enum_count>` |

> [!warning] Detalhes
> - `operator[]` fora do intervalo é UB; `test(i)` lança `std::out_of_range`.
> - `to_ulong()` lança `std::overflow_error` se não couber.
> - O tamanho vive **na pilha** (`N/8` bytes arredondados): `bitset<1'000'000'000>` na stack estoura.

## Peneira de Eratóstenes com `bitset`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <bitset>
#include <iostream>

int main() {
    constexpr std::size_t N = 100;
    std::bitset<N + 1> composto;                           // todos falsos
    for (std::size_t i = 2; i * i <= N; ++i)
        if (!composto[i])
            for (std::size_t j = i * i; j <= N; j += i) composto.set(j);

    int primos = 0;
    for (std::size_t i = 2; i <= N; ++i) primos += !composto[i];
    std::cout << primos << '\n';                           // 25
}
```

## Veja também

- [[Operadores - Cpp]]
- [[vector]]
- [[Tipos Fundamentais]]
- [[Visão Geral da STL]]

## Exercício

1. Represente permissões `rwx` com `bitset<3>` e escreva funções `pode_ler`, `pode_escrever`.
2. Conte os bits ligados de todos os números de 0 a 1 000 000 com `std::popcount` e confirme com `bitset::count`.
