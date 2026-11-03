---
titulo: "Aritmética de ponteiros"
tags: [cpp, memoria, ponteiros]
aliases: ["Aritmética de ponteiros", "Pointer arithmetic", "Ponteiro one-past-end", "ptrdiff_t"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Ponteiros]]", "[[Arrays e std array]]", "[[sizeof e alignof]]"]
---

# Aritmética de ponteiros

Somar ou subtrair inteiros de um ponteiro **move-o em unidades do tipo apontado**, não em bytes.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>

int main() {
    int a[] = {10, 20, 30, 40, 50};
    int* p = a;                       // array decai para ponteiro ao primeiro elemento

    std::cout << *p << '\n';          // 10
    std::cout << *(p + 2) << '\n';    // 30 : avança 2 * sizeof(int) bytes
    std::cout << p[3] << '\n';        // 40 : p[i] é, por definição, *(p + i)
    ++p;                              // agora aponta para a[1]
    std::cout << *p << '\n';          // 20

    int* fim = a + 5;                 // "um além do fim": válido para comparar, NÃO para desreferenciar
    std::ptrdiff_t n = fim - p;       // diferença em ELEMENTOS (tipo std::ptrdiff_t)
    std::cout << n << '\n';           // 4

    for (int* q = a; q != fim; ++q)   // laço clássico com par início/fim
        std::cout << *q << ' ';
    std::cout << '\n';
}
```

## Operações válidas

| Operação | Resultado |
|---|---|
| `p + n`, `p - n` | Ponteiro `n` elementos adiante/atrás |
| `p++`, `--p` | Move um elemento |
| `p - q` | `std::ptrdiff_t` com o número de elementos entre eles (mesmo array) |
| `p < q`, `p == q` | Comparação (dentro do mesmo array) |
| `p[i]` | Equivalente a `*(p + i)` |

Operações **inválidas**: somar dois ponteiros, multiplicar, aritmética em `void*` (padrão), aritmética em ponteiro para função.

## Regras de validade

Um ponteiro só pode apontar para: um elemento do array, **ou uma posição além do último** (*one-past-the-end*). Qualquer outro valor — mesmo sem desreferenciar — é **UB**.

> [!danger] Sair dos limites é UB
> ```cpp
> int a[3] = {1, 2, 3};
> int* p = a + 4;       // UB só por CRIAR este ponteiro (além de one-past-the-end)
> int x = *(a + 3);     // UB: one-past-the-end não pode ser desreferenciado
> ```
> **Correção:** mantenha o par `[início, fim)` e use `std::span`, `std::vector` ou iteradores, que expressam o intervalo.

## Ponteiros e iteradores

Iteradores da STL generalizam ponteiros: `begin()`/`end()` formam um intervalo meio-aberto `[begin, end)`, exatamente como `a` e `a + n`. Algoritmos como `std::sort(a, a + n)` aceitam ponteiros porque ponteiros **são** iteradores de acesso aleatório.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <iterator>

int main() {
    int a[] = {5, 2, 9, 1};
    std::sort(std::begin(a), std::end(a));        // ponteiros funcionam como iteradores
    for (int x : a) std::cout << x << ' ';        // 1 2 5 9
    std::cout << '\n';
}
```

## Conversões e *strict aliasing*

Não acesse um objeto por um ponteiro de **tipo incompatível** (exceto `char`/`unsigned char`/`std::byte`): isso viola as regras de *aliasing* e é UB. Veja [[Conversões e Casts]].

> [!tip] Em código moderno
> Aritmética de ponteiros crua deve ser rara. Prefira `std::vector`, `std::array`, `std::span` (C++20) e algoritmos/ranges.

## Veja também

- [[Ponteiros]]
- [[Arrays e std array]]
- [[sizeof e alignof]]
- [[Conversões e Casts]]

## Exercício

1. Percorra um array de `double` de trás para frente usando apenas ponteiros.
2. Calcule, sem executar, o valor de `(&a[4]) - (&a[1])` para `int a[5]`.
