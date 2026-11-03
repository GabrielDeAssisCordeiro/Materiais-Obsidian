---
titulo: "sizeof, alignof e alinhamento"
tags: [cpp, memoria, alinhamento]
aliases: ["sizeof", "alignof", "alignas", "Padding", "offsetof"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Layout de Memória de um Programa]]", "[[Aritmética de Ponteiros]]", "[[Alocadores Introdução]]"]
---

# `sizeof`, `alignof` e alinhamento

## `sizeof`

Retorna o tamanho em **bytes** de um tipo ou objeto (tipo `std::size_t`), calculado em tempo de compilação. Em um *array* de objetos locais, `sizeof(arr)` dá o tamanho total; em um **ponteiro** ou parâmetro-array, dá o tamanho do ponteiro.

## Alinhamento

Cada tipo tem um **alinhamento**: seus objetos devem ficar em endereços múltiplos desse valor. Isso é exigido (ou favorece desempenho) pela CPU.

- `alignof(T)` — alinhamento exigido por `T` (C++11).
- `alignas(N)` — impõe alinhamento maior em uma variável ou tipo (C++11).
- `std::max_align_t` — alinhamento máximo "fundamental".

## *Padding* em structs

O compilador insere bytes de preenchimento para alinhar membros. **A ordem dos membros altera o tamanho.**

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>

struct Ruim {         // ordem ineficiente
    char  a;          // 1 byte + 7 de padding
    double b;         // 8 bytes (alinhado a 8)
    char  c;          // 1 byte + 7 de padding no fim
};                    // 24 bytes

struct Bom {          // do maior para o menor
    double b;         // 8
    char   a;         // 1
    char   c;         // 1 (+6 de padding no fim)
};                    // 16 bytes

struct alignas(32) Alinhada { int x; };    // alinhamento de 32 bytes (linha de cache/SIMD)

int main() {
    std::cout << "Ruim: " << sizeof(Ruim) << " alinh " << alignof(Ruim) << '\n';       // 24 8
    std::cout << "Bom:   " << sizeof(Bom) << " alinh " << alignof(Bom) << '\n';        // 16 8
    std::cout << "Alinhada: " << sizeof(Alinhada) << " alinh " << alignof(Alinhada) << '\n';   // 32 32
    std::cout << "offset de b em Ruim: " << offsetof(Ruim, b) << '\n';                 // 8

    int arr[10];
    int* p = arr;
    std::cout << sizeof(arr) << ' ' << sizeof(p) << '\n';   // 40 8 (em 64 bits)
    std::cout << sizeof(arr) / sizeof(arr[0]) << '\n';      // 10
}
```

> [!info] Valores típicos
> Os números (24, 16, 8) valem para plataformas de 64 bits comuns (x86-64, ARM64). O padrão **não** os garante.

> [!tip] Ordene membros do maior para o menor
> Reduz *padding* e melhora o uso de cache. Verifique com `static_assert(sizeof(Tipo) == N)` em tipos críticos.

> [!bug] `sizeof` em parâmetro-array
> ```cpp
> void f(int arr[10]) {                       // 'arr' é na verdade int*
>     std::size_t n = sizeof(arr) / sizeof(arr[0]);   // 8/4 = 2: ERRADO
> }
> ```
> **Correção:** passe `std::span<int>`, `std::array` ou o tamanho como argumento. Veja [[Arrays e std array]].

## Struct empacotada

`#pragma pack(1)` ou `__attribute__((packed))` removem padding, mas acessos desalinhados podem ser lentos ou causar falha em algumas arquiteturas; use apenas para protocolos/arquivos binários, e prefira serializar campo a campo.

## Alocação alinhada

`new` respeita `alignof(T)` até `__STDCPP_DEFAULT_NEW_ALIGNMENT__` e, desde o C++17, também para tipos *over-aligned*. Para blocos brutos: `std::aligned_alloc` (`<cstdlib>`) ou `new (std::align_val_t{64}) ...`.

## Veja também

- [[Layout de Memória de um Programa]]
- [[Aritmética de Ponteiros]]
- [[Alocadores Introdução]]
- [[Tipos Fundamentais]]

## Exercício

1. Reordene os membros de `struct { char a; int b; short c; char d; }` para minimizar o tamanho e confirme com `sizeof`.
2. Por que `alignas(64)` é usado em estruturas compartilhadas entre threads (*false sharing*)?
