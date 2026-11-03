---
titulo: "Tipos fundamentais"
tags: [cpp, basico, tipos]
aliases: ["Tipos fundamentais", "Tipos primitivos", "int, double, char, bool", "Tipos de tamanho fixo"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Variáveis e Inicialização]]", "[[Conversões e Casts]]", "[[Operadores - Cpp]]"]
---

# Tipos fundamentais

Tipos fundamentais são os "tijolos" da linguagem: inteiros, caracteres, booleano, ponto flutuante e `void`.

## Quadro geral

| Categoria | Tipos | Observações |
|---|---|---|
| Booleano | `bool` | `true`/`false`; converte para `int` como 1/0 |
| Caracteres | `char`, `signed char`, `unsigned char`, `wchar_t`, `char8_t` (C++20), `char16_t`, `char32_t` | `sizeof(char) == 1` sempre; `char` pode ser com ou sem sinal (depende da plataforma) |
| Inteiros | `short`, `int`, `long`, `long long` (e versões `unsigned`) | Só há **tamanhos mínimos** garantidos |
| Ponto flutuante | `float`, `double`, `long double` | Geralmente IEEE 754 (`float` 32 bits, `double` 64 bits) |
| Vazio | `void` | Sem valores; funções que não retornam, `void*` |
| Ponteiro nulo | `std::nullptr_t` | Tipo de `nullptr` |

## Tamanhos mínimos garantidos pelo padrão

| Tipo | Mínimo (bits) | Típico em x86-64 Linux/Windows |
|---|---|---|
| `short` | 16 | 16 |
| `int` | 16 | 32 |
| `long` | 32 | 64 (Linux) / 32 (Windows) |
| `long long` | 64 | 64 |

> [!warning] `long` não é portável
> `long` tem 64 bits no Linux/macOS x86-64 e 32 bits no Windows. Quando o tamanho importa, use os tipos de largura fixa.

## Tipos de largura fixa (`<cstdint>`)

`std::int8_t`, `std::uint8_t`, `std::int16_t`, `std::uint16_t`, `std::int32_t`, `std::uint32_t`, `std::int64_t`, `std::uint64_t`, além de `std::size_t` (tamanhos e índices), `std::ptrdiff_t` (diferença entre ponteiros) e `std::intptr_t`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <limits>

int main() {
    std::cout << "char:      " << sizeof(char) << '\n';        // sempre 1
    std::cout << "short:     " << sizeof(short) << '\n';
    std::cout << "int:       " << sizeof(int) << '\n';
    std::cout << "long:      " << sizeof(long) << '\n';
    std::cout << "long long: " << sizeof(long long) << '\n';
    std::cout << "float:     " << sizeof(float) << '\n';
    std::cout << "double:    " << sizeof(double) << '\n';
    std::cout << "size_t:    " << sizeof(std::size_t) << '\n';

    std::cout << "int max:   " << std::numeric_limits<int>::max() << '\n';
    std::cout << "int min:   " << std::numeric_limits<int>::min() << '\n';
    // O '+' promove uint8_t para int; sem ele, o valor seria impresso como caractere
    std::cout << "uint8 max: " << +std::numeric_limits<std::uint8_t>::max() << '\n';
    std::cout << "double eps: " << std::numeric_limits<double>::epsilon() << '\n';
}
```

## Literais

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    int dec = 255;
    int hex = 0xFF;                  // hexadecimal
    int oct = 0377;                  // octal (zero à esquerda!)
    int bin = 0b1111'1111;           // binário (C++14) com separador de dígitos (C++14)
    long long grande = 1'000'000'000'000LL;
    unsigned u = 42u;
    float f = 1.5f;                  // sufixo f: float
    double d = 1.5e3;                // notação científica
    char c = 'A';                    // literal de caractere
    bool b = true;

    std::cout << dec << ' ' << hex << ' ' << oct << ' ' << bin << ' ' << grande << '\n';
    std::cout << u << ' ' << f << ' ' << d << ' ' << c << ' ' << b << '\n';
}
```

> [!bug] Zero à esquerda significa octal
> `int x = 010;` vale **8**, não 10. Evite zeros à esquerda em literais decimais.

## Inteiros: sinal e estouro

- **Sem sinal (`unsigned`)**: o estouro dá a volta (aritmética módulo 2ⁿ) — comportamento **definido**.
- **Com sinal (`int`)**: estouro é **comportamento indefinido**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <iostream>

int main() {
    std::uint8_t u = 255;
    u = static_cast<std::uint8_t>(u + 1);   // 256 não cabe: volta a 0 (definido)
    std::cout << +u << '\n';                // 0

    unsigned int zero = 0;
    --zero;                                 // dá a volta: UINT_MAX
    std::cout << zero << '\n';              // 4294967295 (com 32 bits)
}
```

> [!danger] Estouro de `int` com sinal é UB
> ```cpp
> int x = std::numeric_limits<int>::max();
> x = x + 1;   // COMPORTAMENTO INDEFINIDO: o compilador pode assumir que isso nunca acontece
> ```
> **Correção:** use um tipo maior (`std::int64_t`), verifique antes de somar, ou use `unsigned` se o módulo for desejado. Compile com `-fsanitize=undefined` para detectar.

## Ponto flutuante: cuidado com igualdade

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cmath>
#include <iostream>

int main() {
    double a = 0.1 + 0.2;
    std::cout << (a == 0.3) << '\n';                     // 0 (falso!) por erro de representação
    std::cout << (std::fabs(a - 0.3) < 1e-9) << '\n';    // 1: compare com tolerância
}
```

> [!tip] Dicas
> - Prefira `double` a `float`, exceto quando memória/GPU justificar.
> - Use `std::size_t` para tamanhos e índices de contêineres.
> - Use `bool` para condições, não `int`.
> - Para texto, veja `char8_t` e `std::string` nas notas de strings.

## Veja também

- [[Variáveis e Inicialização]]
- [[Conversões e Casts]]
- [[Operadores - Cpp]]
- [[const e constexpr]]

## Exercício

1. Descubra o `sizeof` de `long` na sua máquina e explique por que usar `std::int64_t` é mais portável.
2. Escreva um programa que some `std::numeric_limits<unsigned>::max()` e 1 e explique o resultado.
