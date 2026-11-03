---
titulo: "Alocadores e std::pmr"
tags: [cpp, performance, alocadores, pmr]
aliases: ["std::pmr", "polymorphic_allocator", "memory_resource", "monotonic_buffer_resource", "Pool", "tcmalloc"]
tipo: conceito
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Alocadores Introdução]]", "[[new e delete]]", "[[Cache e Localidade de Dados]]"]
---

# Alocadores e `std::pmr`

Aprofundamento de [[Alocadores Introdução]]. `new`/`malloc` são de **propósito geral**: custam travas, fragmentação e latência variável. Estratégias especializadas:

| Estratégia | Ideia | Uso |
|---|---|---|
| **Arena / monotônica** | Aloca avançando um ponteiro; libera tudo de uma vez | Dados por requisição/frame, parsers |
| **Pool** | Blocos de tamanho fixo reutilizáveis | Muitos objetos pequenos iguais |
| **Pilha (stack allocator)** | LIFO | Escopos aninhados |
| **Free list** | Lista de blocos livres | Alocação de tamanho fixo |
| *Allocators* globais alternativos | **jemalloc, tcmalloc, mimalloc** substituem `malloc` sem mudar o código | Servidores multithread |

## `std::pmr` (C++17)

*Polymorphic memory resources*: o **mesmo tipo** de contêiner (`std::pmr::vector<T>`) aceita **recursos de memória diferentes** em tempo de execução, sem mudar o tipo (ao contrário de alocadores como parâmetro de template).

| Componente | Função |
|---|---|
| `std::pmr::memory_resource` | Interface (`allocate`, `deallocate`, `is_equal`) |
| `std::pmr::monotonic_buffer_resource` | Arena sobre um buffer; só libera ao destruir/`release()` |
| `std::pmr::unsynchronized_pool_resource` / `synchronized_pool_resource` | Pools por tamanho |
| `std::pmr::new_delete_resource()`, `null_memory_resource()` | Padrão e "falha ao alocar" |
| `std::pmr::vector`, `string`, `map`, ... | Contêineres com `polymorphic_allocator` |

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <array>
#include <iostream>
#include <memory_resource>
#include <string>
#include <vector>

int main() {
    std::array<std::byte, 4096> buffer;                              // memória na PILHA
    std::pmr::monotonic_buffer_resource arena{buffer.data(), buffer.size(),
                                              std::pmr::null_memory_resource()};   // se acabar: lança bad_alloc

    std::pmr::vector<std::pmr::string> nomes{&arena};                // vector E strings usam a arena
    for (int i = 0; i < 10; ++i) nomes.emplace_back("nome_longo_para_forcar_alocacao_" + std::to_string(i));

    std::cout << nomes.size() << ' ' << nomes[3] << '\n';
}                                                                    // tudo liberado de uma vez; sem malloc
```

> [!tip] Propagação
> Strings dentro de `pmr::vector` usam o **mesmo** recurso automaticamente (*uses-allocator construction*), desde que sejam `std::pmr::string`.

## Alocador próprio mínimo (C++11+)

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <new>
#include <vector>

template <typename T>
struct AlocadorContador {
    using value_type = T;
    static inline std::size_t alocacoes = 0;

    AlocadorContador() = default;
    template <typename U> AlocadorContador(const AlocadorContador<U>&) noexcept {}

    T* allocate(std::size_t n) {
        ++alocacoes;
        if (auto* p = static_cast<T*>(std::malloc(n * sizeof(T)))) return p;
        throw std::bad_alloc{};
    }
    void deallocate(T* p, std::size_t) noexcept { std::free(p); }

    template <typename U> bool operator==(const AlocadorContador<U>&) const noexcept { return true; }
};

int main() {
    std::vector<int, AlocadorContador<int>> v;
    for (int i = 0; i < 1000; ++i) v.push_back(i);
    std::cout << AlocadorContador<int>::alocacoes << " alocações\n";   // ~11 (crescimento geométrico)
    v.reserve(5000);                                                    // +1
}
```

> [!warning] Cuidados
> - **Tempo de vida**: o recurso (arena) deve viver mais que os contêineres que o usam.
> - `monotonic_buffer_resource` **não libera** memória individual: um `vector` que cresce muito desperdiça espaço antigo.
> - Não é *thread-safe* (versão `unsynchronized_*`).
> - Verifique o **alinhamento** exigido pelos tipos ([[sizeof e alignof]]).

## Veja também

- [[Alocadores Introdução]]
- [[new e delete]]
- [[Cache e Localidade de Dados]]
- [[Cpp em Sistemas Embarcados]]
- [[Profiling e Benchmarking]]

## Exercício

1. Meça o tempo de criar 10⁶ `std::pmr::string` com arena vs `std::string` normal.
2. Implemente um pool de objetos de tamanho fixo e compare com `new`/`delete`.
