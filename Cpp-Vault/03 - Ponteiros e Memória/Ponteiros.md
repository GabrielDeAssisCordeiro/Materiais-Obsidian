---
titulo: "Ponteiros"
tags: [cpp, memoria, ponteiros]
aliases: ["Ponteiros", "Pointers", "Endereço e desreferência", "void*", "Ponteiro para função"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Aritmética de Ponteiros]]", "[[Referências - Cpp]]", "[[nullptr]]"]
---

# Ponteiros

Um **ponteiro** é um objeto que guarda o **endereço de memória** de outro objeto.

## Operadores essenciais

| Operador | Nome | Uso |
|---|---|---|
| `&x` | Endereço de | Obtém o endereço de `x` |
| `*p` | Desreferência | Acessa o objeto apontado por `p` |
| `p->m` | Acesso por seta | Atalho para `(*p).m` |
| `T* p` | Declaração | `p` aponta para um `T` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void troca(int* a, int* b) {          // dois ponteiros: troca os valores apontados
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

struct Ponto { int x; int y; };

int main() {
    int x = 10;
    int* p = &x;                      // p guarda o endereço de x
    std::cout << *p << '\n';          // 10 (desreferência)
    *p = 20;                          // altera x através de p
    std::cout << x << '\n';           // 20

    int a = 1, b = 2;
    troca(&a, &b);
    std::cout << a << b << '\n';      // 21

    Ponto pt{3, 4};
    Ponto* pp = &pt;
    std::cout << pp->x << ' ' << (*pp).y << '\n';   // 3 4

    int** pp2 = &p;                   // ponteiro para ponteiro
    **pp2 = 30;
    std::cout << x << '\n';           // 30
}
```

## Ponteiros e `const`

| Declaração | Pode mudar o destino? | Pode mudar o valor apontado? |
|---|---|---|
| `int* p` | Sim | Sim |
| `const int* p` | Sim | **Não** |
| `int* const p` | **Não** | Sim |
| `const int* const p` | Não | Não |

(Veja [[const e constexpr]].)

## `void*`

Ponteiro genérico: guarda qualquer endereço de objeto, mas **não pode ser desreferenciado** nem usado em aritmética. Para usar, converta com `static_cast`. É comum em APIs C; em C++ moderno prefira templates.

## Ponteiro para função

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int soma(int a, int b) { return a + b; }
int mult(int a, int b) { return a * b; }

int main() {
    int (*op)(int, int) = soma;       // ponteiro para função (int,int)->int
    std::cout << op(2, 3) << '\n';    // 5
    op = mult;
    std::cout << op(2, 3) << '\n';    // 6

    using Binaria = int (*)(int, int);   // alias facilita a leitura
    Binaria vetor[] = {soma, mult};
    std::cout << vetor[1](4, 5) << '\n'; // 20
}
```

## Ponteiros não inicializados e nulos

> [!danger] Desreferenciar ponteiro não inicializado, nulo ou pendente é UB
> ```cpp
> int* p;          // valor indeterminado
> *p = 5;          // UB: escreve em endereço desconhecido
>
> int* q = nullptr;
> *q = 5;          // UB: tipicamente "segmentation fault", mas não é garantido
> ```
> **Correção:** inicialize sempre (`int* p = nullptr;`) e **teste antes de usar**: `if (p) { ... }`. Veja [[nullptr]].

## Quando usar ponteiros em C++ moderno

- **Observadores sem posse**: `T*` ou `T&` para "ver" um objeto que outro dono controla.
- **Posse** de objetos no heap → **smart pointers** (`std::unique_ptr`, `std::shared_ptr`), nunca `new`/`delete` soltos.
- **Opcional**: `T*` pode ser nulo; `std::optional<T>` modela "valor ou nada" quando há posse do valor.
- Prefira **referências** quando o argumento não pode ser nulo ([[Referências - Cpp]]).

## Veja também

- [[Aritmética de Ponteiros]]
- [[Referências - Cpp]]
- [[nullptr]]
- [[new e delete]]
- [[Vazamentos e Dangling Pointers]]

## Exercício

1. Escreva uma função `void minmax(const int* v, int n, int* min, int* max)` e teste com um array.
2. Explique a diferença entre `const char* s` e `char* const s`.
