---
titulo: "latch, barrier e semaphore (C++20)"
tags: [cpp, concorrencia, cpp20]
aliases: ["std::latch", "std::barrier", "counting_semaphore", "binary_semaphore", "Primitivas de sincronização C++20"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[condition_variable]]", "[[Mutex e Locks]]", "[[Threads e jthread]]"]
---

# `latch`, `barrier` e `semaphore` (C++20)

> [!info] Introdução
> Cabeçalhos `<latch>`, `<barrier>`, `<semaphore>`. GCC 11+, MSVC 2019 16.9+, libc++ 11+/Clang (confirmar versão exata). Evitam reescrever lógica com [[condition_variable]].

| Primitiva | Reutilizável | Uso |
|---|---|---|
| `std::latch` | **Não** (uso único) | Esperar N eventos (`count_down`, `wait`) — largada de corrida |
| `std::barrier` | **Sim** (por fase) | N threads se encontram a cada fase; executa uma função de conclusão |
| `std::counting_semaphore<N>` | Sim | Limitar acesso a N recursos |
| `std::binary_semaphore` | Sim | Sinalização 0/1 (como mutex sem posse) |

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <barrier>
#include <iostream>
#include <latch>
#include <semaphore>
#include <thread>
#include <vector>

int main() {
    // latch: a thread principal espera 3 workers terminarem a inicialização
    std::latch pronto{3};
    std::vector<std::jthread> workers;
    for (int i = 0; i < 3; ++i)
        workers.emplace_back([&] { /* inicializa */ pronto.count_down(); });
    pronto.wait();
    std::cout << "todos inicializados\n";

    // barrier: 3 threads, 2 fases; a função de conclusão roda uma vez por fase
    int fase = 0;
    std::barrier ponto{3, [&]() noexcept { ++fase; }};
    {
        std::vector<std::jthread> ts;
        for (int i = 0; i < 3; ++i)
            ts.emplace_back([&] { ponto.arrive_and_wait(); ponto.arrive_and_wait(); });
    }
    std::cout << "fases: " << fase << '\n';                // 2

    // semáforo: no máximo 2 "conexões" simultâneas
    std::counting_semaphore<2> conexoes{2};
    conexoes.acquire();
    conexoes.acquire();
    std::cout << "terceira conseguiu? " << conexoes.try_acquire() << '\n';   // 0
    conexoes.release(2);
}
```

> [!warning] Cuidados
> - `latch` não reinicia: crie outro para nova rodada.
> - Semáforos **não têm dono**: qualquer thread pode `release` — mais flexível, mais fácil de errar que um mutex.
> - Um `barrier` com participante que nunca chega trava todos (deadlock).

## Veja também

- [[condition_variable]]
- [[Mutex e Locks]]
- [[Threads e jthread]]
- [[Data Races e Deadlocks]]

## Exercício

1. Use `barrier` para simular simulação em passos (cada thread atualiza uma fatia e todas sincronizam por passo).
2. Limite a 3 downloads simultâneos com `counting_semaphore`.
