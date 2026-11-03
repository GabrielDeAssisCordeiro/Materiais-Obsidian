---
titulo: "Alocadores (introdução)"
tags: [cpp, memoria, alocadores, pmr]
aliases: ["std::allocator", "Allocator", "Arena allocator", "Introdução a alocadores"]
tipo: conceito
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[new e delete]]", "[[Stack vs Heap]]", "[[sizeof e alignof]]"]
---

# Alocadores (introdução)

Um **alocador** (*allocator*) encapsula **como** a memória é obtida e liberada. Contêineres da STL aceitam um alocador como parâmetro de template, por padrão `std::allocator<T>` (que usa `operator new`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <vector>

int main() {
    std::allocator<int> alloc;
    int* mem = alloc.allocate(3);                // memória BRUTA para 3 ints (sem construir)
    std::construct_at(mem + 0, 10);              // constrói elementos manualmente (C++20)
    std::construct_at(mem + 1, 20);
    std::construct_at(mem + 2, 30);
    std::cout << mem[0] + mem[1] + mem[2] << '\n';   // 60
    std::destroy_n(mem, 3);                      // destrói (ints triviais, mas é o contrato)
    alloc.deallocate(mem, 3);                    // devolve a memória
}
```

## Por que alocadores customizados

| Motivo | Exemplo |
|---|---|
| **Desempenho** | *Arena/bump allocator*: alocação em O(1), liberação em lote |
| **Localidade de cache** | Objetos contíguos em um *pool* |
| **Previsibilidade** (tempo real) | Sem chamadas ao heap do sistema |
| **Embarcados** | Memória estática pré-alocada |
| **Depuração** | Contar/registrar alocações, detectar vazamentos |

## Um alocador mínimo (C++11+)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>
#include <new>
#include <vector>

template <typename T>
struct ContadorAlloc {
    using value_type = T;
    static inline std::size_t alocacoes = 0;

    ContadorAlloc() = default;
    template <typename U> ContadorAlloc(const ContadorAlloc<U>&) noexcept {}

    T* allocate(std::size_t n) {
        ++alocacoes;
        return static_cast<T*>(::operator new(n * sizeof(T)));
    }
    void deallocate(T* p, std::size_t) noexcept { ::operator delete(p); }

    template <typename U> bool operator==(const ContadorAlloc<U>&) const noexcept { return true; }
};

int main() {
    std::vector<int, ContadorAlloc<int>> v;
    for (int i = 0; i < 100; ++i) v.push_back(i);
    std::cout << "alocações: " << ContadorAlloc<int>::alocacoes << '\n';   // poucas (crescimento geométrico)

    std::vector<int, ContadorAlloc<int>> w;
    w.reserve(100);                                  // uma só alocação
    std::cout << "alocações: " << ContadorAlloc<int>::alocacoes << '\n';
}
```

## Alocadores polimórficos: `std::pmr` (C++17)

`std::pmr` (`<memory_resource>`) troca o alocador **em tempo de execução**, sem alterar o tipo do contêiner.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>
#include <memory_resource>
#include <vector>

int main() {
    std::array<std::byte, 1024> buffer;                              // memória na stack
    std::pmr::monotonic_buffer_resource arena{buffer.data(), buffer.size()};

    std::pmr::vector<int> v{&arena};                                 // usa a arena, não o heap
    for (int i = 0; i < 50; ++i) v.push_back(i);                     // sem ir ao heap (até 1 KB)

    std::cout << v.size() << '\n';
}   // a arena libera tudo de uma vez; destrutores dos elementos ainda são chamados
```

> [!info] Mais detalhes
> `std::pmr`, arenas e *pool allocators* são aprofundados na seção de desempenho deste vault.

> [!warning] Alocador customizado não é a primeira solução
> Meça antes. `reserve()`, evitar cópias e boa estrutura de dados costumam ter muito mais impacto.

## Veja também

- [[new e delete]]
- [[Stack vs Heap]]
- [[sizeof e alignof]]
- [[Layout de Memória de um Programa]]

## Exercício

1. Modifique `ContadorAlloc` para contar também as liberações e imprima ao final.
2. Compare o tempo de inserir 1 milhão de `int` em `std::vector<int>` com e sem `reserve`.
