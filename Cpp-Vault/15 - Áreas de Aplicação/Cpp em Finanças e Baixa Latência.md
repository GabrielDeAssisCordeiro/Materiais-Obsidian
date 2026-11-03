---
titulo: "C++ em finanças e baixa latência"
tags: [cpp, aplicacoes, lock-free]
aliases: ["HFT", "High-Frequency Trading", "Baixa latência", "Finanças", "Ring buffer", "SPSC", "Trading"]
tipo: area
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Atomics e Modelo de Memória]]", "[[Cache e Localidade de Dados]]", "[[Profiling e Benchmarking]]"]
---

# C++ em finanças e baixa latência

Em **HFT** e *market making*, a latência é medida em **nanossegundos a microssegundos** e a **cauda** (p99, p99.9) importa mais que a média. C++ permite controle total de memória, layout e instruções.

## Princípios

| Princípio | Prática |
|---|---|
| Sem alocação no caminho crítico | Pré-alocar, pools, arenas ([[Alocadores Introdução]]) |
| Sem exceções/I/O/locks no *hot path* | Retornos por código, `expected`, filas *lock-free* |
| Dados amigáveis ao cache | SoA, tipos pequenos, alinhar a 64 B, evitar *false sharing* ([[Cache e Localidade de Dados]]) |
| Evitar chamadas virtuais e *branches* imprevisíveis | CRTP, templates, `[[likely]]`/`[[unlikely]]` |
| **Pré-aquecer** código/dados | Executar o caminho crítico antes do mercado abrir |
| Isolamento de CPU | *Pinning* de threads, `isolcpus`, desativar *hyperthreading*, `nohz_full` |
| Rede | Kernel bypass (**DPDK**, **Solarflare/Onload**, **RDMA**), `SO_BUSY_POLL` |
| Medição | Timestamps de hardware, histogramas (HdrHistogram), `rdtsc` ([[Profiling e Benchmarking]]) |
| Determinismo | Compilar com mesmas flags/compilador, `-O3 -march=native`, PGO/LTO |

## Fila SPSC *lock-free* (produtor único, consumidor único)

```cpp
// g++ -std=c++20 -Wall -Wextra -O2 -pthread
#include <array>
#include <atomic>
#include <cstddef>
#include <iostream>
#include <new>
#include <optional>
#include <thread>

template <typename T, std::size_t N>
class FilaSPSC {
    static_assert((N & (N - 1)) == 0, "N deve ser potência de 2");
public:
    bool push(const T& v) {
        const auto h = head_.load(std::memory_order_relaxed);
        if (h - tail_.load(std::memory_order_acquire) == N) return false;     // cheia
        buf_[h & (N - 1)] = v;
        head_.store(h + 1, std::memory_order_release);                         // publica o item
        return true;
    }
    std::optional<T> pop() {
        const auto t = tail_.load(std::memory_order_relaxed);
        if (t == head_.load(std::memory_order_acquire)) return std::nullopt;   // vazia
        T v = buf_[t & (N - 1)];
        tail_.store(t + 1, std::memory_order_release);
        return v;
    }
private:
    alignas(64) std::atomic<std::size_t> head_{0};                             // linhas de cache separadas
    alignas(64) std::atomic<std::size_t> tail_{0};                             // evita false sharing
    alignas(64) std::array<T, N> buf_{};
};

int main() {
    FilaSPSC<int, 1024> fila;
    long soma = 0;
    std::jthread produtor{[&] { for (int i = 1; i <= 100000; ++i) while (!fila.push(i)) {} }};
    for (int recebidos = 0; recebidos < 100000;) {
        if (auto v = fila.pop()) { soma += *v; ++recebidos; }
    }
    std::cout << soma << '\n';                                                   // 5000050000
}
```

> [!danger] Armadilhas
> - Estruturas *lock-free* são difíceis de acertar: valide com **TSan**, testes de estresse e provas de ordenação ([[Atomics e Modelo de Memória]]).
> - Otimizar sem medir; microbenchmarks em máquina diferente da produção.
> - Aritmética financeira: **não use `double`** para dinheiro em contabilidade; use inteiros em centavos ou decimais de precisão fixa.
> - Conformidade/regulação: logs, auditoria e *kill switches*.

## Veja também

- [[Atomics e Modelo de Memória]]
- [[Cache e Localidade de Dados]]
- [[Profiling e Benchmarking]]
- [[Idiomas e Padrões de Projeto em Cpp]]
- [[MOC - Áreas de Aplicação - Cpp]]

## Exercício

1. Meça a latência de ida e volta de `push`/`pop` com `rdtsc` e produza um histograma.
2. Adicione `std::hardware_destructive_interference_size` para alinhar os índices.
