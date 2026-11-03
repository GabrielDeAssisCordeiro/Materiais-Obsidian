---
titulo: "stop_token e cancelamento cooperativo (C++20)"
tags: [cpp, concorrencia, jthread, cpp20]
aliases: ["std::stop_token", "stop_source", "stop_callback", "request_stop", "Cancelamento cooperativo"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Threads e jthread]]", "[[condition_variable]]", "[[Corrotinas Cpp20]]"]
---

# `stop_token` e cancelamento cooperativo (C++20)

Não existe forma segura de **matar** uma thread. O C++20 padroniza o **cancelamento cooperativo**: quem controla chama `request_stop()`, e a thread **verifica** o token e encerra por conta própria.

| Tipo | Papel |
|---|---|
| `std::stop_source` | Emite o pedido (`request_stop`) |
| `std::stop_token` | Consulta (`stop_requested`) |
| `std::stop_callback` | Executa uma função ao receber o pedido |
| `std::jthread` | Cria o `stop_source`, passa o token como 1º argumento e chama `request_stop()` + `join()` no destrutor |

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <stop_token>
#include <thread>

int main() {
    std::atomic<int> voltas{0};

    {
        std::jthread worker{[&voltas](std::stop_token st) {     // jthread injeta o token
            while (!st.stop_requested()) {
                ++voltas;
                std::this_thread::sleep_for(std::chrono::milliseconds(1));
            }
            std::cout << "worker encerrando\n";
        }};
        std::this_thread::sleep_for(std::chrono::milliseconds(20));
    }                                                             // destrutor: request_stop() + join()
    std::cout << (voltas.load() > 0) << '\n';                     // 1

    // espera interrompível em condition_variable_any
    std::mutex m;
    std::condition_variable_any cv;
    std::jthread espera{[&](std::stop_token st) {
        std::unique_lock lk{m};
        bool cond = cv.wait(lk, st, [] { return false; });       // acorda se parar
        std::cout << "acordou por parada: " << !cond << '\n';
    }};
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
    espera.request_stop();
}
```

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <iostream>
#include <stop_token>

int main() {
    std::stop_source fonte;
    std::stop_token tk = fonte.get_token();
    std::stop_callback cb{tk, [] { std::cout << "limpeza ao cancelar\n"; }};   // roda em request_stop()
    fonte.request_stop();                                         // dispara o callback
    std::cout << tk.stop_requested() << '\n';
}
```

> [!tip] Padrão
> Verifique `stop_requested()` em cada iteração/ponto seguro; para operações bloqueantes use APIs que aceitam token (`condition_variable_any::wait`, `std::stop_callback` para acordar I/O).

> [!warning] `stop_callback` roda na thread que chama `request_stop`
> Callbacks devem ser curtos e não podem lançar exceções.

## Veja também

- [[Threads e jthread]]
- [[condition_variable]]
- [[Corrotinas Cpp20]]
- [[Data Races e Deadlocks]]

## Exercício

1. Faça um *worker* que processa uma fila e para ao receber `request_stop()`, esvaziando o que já recebeu.
2. Use `stop_callback` para fechar um *socket* simulado e acordar uma thread bloqueada.
