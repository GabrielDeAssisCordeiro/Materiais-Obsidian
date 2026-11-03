---
titulo: "new e delete"
tags: [cpp, memoria, delete, heap]
aliases: ["new", "delete", "new[]", "delete[]", "Alocação dinâmica", "placement new", "malloc e free"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Stack vs Heap]]", "[[Vazamentos e Dangling Pointers]]", "[[nullptr]]"]
---

# `new` e `delete`

`new` aloca memória no **heap** **e** constrói o objeto; `delete` destrói o objeto **e** libera a memória.

> [!warning] Em C++ moderno, evite `new`/`delete` diretos
> Prefira `std::vector`, `std::string`, `std::make_unique` e `std::make_shared`. Aqui o objetivo é **entender** o mecanismo que esses tipos encapsulam.

## Uso básico

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

struct Ponto {
    int x, y;
    Ponto(int x_, int y_) : x(x_), y(y_) { std::cout << "construído\n"; }
    ~Ponto() { std::cout << "destruído\n"; }
};

int main() {
    int* n = new int(42);              // um int, inicializado com 42
    int* zeros = new int[5]{};         // array de 5 ints, zerados
    Ponto* p = new Ponto(1, 2);        // aloca e chama o construtor

    std::cout << *n << ' ' << zeros[0] << ' ' << p->x << '\n';

    delete n;                          // libera um objeto
    delete[] zeros;                    // libera ARRAY: sempre delete[] para new[]
    delete p;                          // chama o destrutor e libera
}
```

## Regras de pareamento

| Alocação | Liberação |
|---|---|
| `new T` / `new T(args)` | `delete p` |
| `new T[n]` | `delete[] p` |
| `malloc` / `calloc` | `free` |

> [!danger] Misturar formas é UB
> ```cpp
> int* a = new int[10];
> delete a;              // COMPORTAMENTO INDEFINIDO: deveria ser delete[]
>
> int* b = (int*)malloc(4);
> delete b;              // UB: malloc exige free
>
> int* c = new int;
> delete c;
> delete c;              // UB: double free
> ```

## Falhas de alocação

`new` lança `std::bad_alloc` quando não há memória. Para obter `nullptr` em vez de exceção, use `new (std::nothrow) T`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <new>

int main() {
    try {
        char* gigante = new char[static_cast<std::size_t>(-1) / 2];   // pedido absurdo
        delete[] gigante;
    } catch (const std::bad_alloc& e) {
        std::cout << "falha de alocação: " << e.what() << '\n';
    }

    int* p = new (std::nothrow) int[1000];   // não lança: retorna nullptr em falha
    if (!p) { std::cout << "sem memória\n"; return 1; }
    delete[] p;
}
```

## O mesmo programa com RAII (forma recomendada)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <vector>

struct Ponto { int x, y; };

int main() {
    auto n = std::make_unique<int>(42);                   // sem delete
    std::vector<int> zeros(5);                            // array dinâmico seguro
    auto p = std::make_unique<Ponto>(Ponto{1, 2});

    std::cout << *n << ' ' << zeros[0] << ' ' << p->x << '\n';
}   // tudo liberado automaticamente, inclusive se uma exceção fosse lançada
```

## *Placement new* (avançado)

Constrói um objeto em memória **já alocada**: base de alocadores e `std::vector`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <new>

struct Item { int v; explicit Item(int x) : v(x) {} ~Item() { std::cout << "~Item\n"; } };

int main() {
    alignas(Item) unsigned char buffer[sizeof(Item)];    // memória bruta com alinhamento correto
    Item* it = new (buffer) Item(7);                     // constrói em 'buffer'
    std::cout << it->v << '\n';
    it->~Item();                                         // destrutor chamado manualmente; sem delete!
}
```

## `operator new` e `operator delete`

`new T` faz **duas** coisas: chama `operator new(sizeof(T))` (alocação) e depois o construtor. Os operadores podem ser **sobrecarregados** globalmente ou por classe para instrumentar ou personalizar a alocação ([[Alocadores Introdução]]).

## Veja também

- [[Stack vs Heap]]
- [[Vazamentos e Dangling Pointers]]
- [[nullptr]]
- [[Alocadores Introdução]]
- [[Ponteiros]]

## Exercício

1. Escreva um programa com `new int[3]` e `delete` (sem `[]`). Compile com `-fsanitize=address` e leia o relatório.
2. Reescreva o primeiro exemplo usando apenas `std::unique_ptr` e `std::vector`.
