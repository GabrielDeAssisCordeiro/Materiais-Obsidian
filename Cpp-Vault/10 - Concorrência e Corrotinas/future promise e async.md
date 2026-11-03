---
titulo: "future, promise e async"
tags: [cpp, concorrencia, future, async]
aliases: ["std::future", "std::promise", "std::async", "packaged_task", "shared_future", "launch::async"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Threads e jthread]]", "[[Tratamento de Erros com expected]]", "[[Exceções try catch throw]]"]
---

# `future`, `promise` e `async`

Um canal **de uma só vez**: um lado produz um valor (ou exceção), outro o espera.

| Tipo | Papel |
|---|---|
| `std::promise<T>` | Lado de **escrita**: `set_value` / `set_exception` |
| `std::future<T>` | Lado de **leitura**: `get()` (bloqueia), `wait_for`, `valid` |
| `std::shared_future<T>` | Vários consumidores |
| `std::packaged_task<R(A...)>` | Empacota um callable e liga ao future |
| `std::async` | Executa uma função e devolve um future |

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <chrono>
#include <future>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <thread>
#include <vector>

long soma_parcial(const std::vector<int>& v, std::size_t a, std::size_t b) {
    return std::accumulate(v.begin() + static_cast<long>(a), v.begin() + static_cast<long>(b), 0L);
}

int main() {
    std::vector<int> v(1000, 1);

    // async: política explícita; sem ela o runtime pode adiar a execução (deferred)
    auto f1 = std::async(std::launch::async, soma_parcial, std::cref(v), 0, 500);
    auto f2 = std::async(std::launch::async, soma_parcial, std::cref(v), 500, 1000);
    std::cout << f1.get() + f2.get() << '\n';              // 1000

    // promise + future: comunicação entre threads
    std::promise<int> p;
    std::future<int> f = p.get_future();
    std::jthread t{[&p] { p.set_value(42); }};
    std::cout << f.get() << '\n';

    // exceções atravessam o future
    auto g = std::async(std::launch::async, []() -> int { throw std::runtime_error{"falhou"}; });
    try { g.get(); } catch (const std::exception& e) { std::cout << "capturada: " << e.what() << '\n'; }

    // packaged_task: controla QUANDO e ONDE a tarefa roda
    std::packaged_task<int(int)> task{[](int x) { return x * 2; }};
    auto r = task.get_future();
    std::jthread t2{std::move(task), 21};
    std::cout << r.get() << '\n';                           // 42

    auto h = std::async(std::launch::async, [] { std::this_thread::sleep_for(std::chrono::milliseconds(50)); return 1; });
    std::cout << (h.wait_for(std::chrono::milliseconds(1)) == std::future_status::timeout) << '\n';   // 1
}
```

> [!danger] Armadilha do destrutor do `std::future` de `async`
> O *future* retornado por `std::async` **bloqueia no destrutor** até a tarefa terminar. Escrever `std::async(std::launch::async, f);` sem guardar o resultado torna a chamada **síncrona** na prática (o temporário é destruído imediatamente).

> [!warning] Outros cuidados
> - `get()` só pode ser chamado **uma vez** em `std::future` (use `shared_future` para vários).
> - Sem `std::launch::async`, o padrão (`async | deferred`) deixa o runtime decidir.
> - Para muitas tarefas pequenas, `async` cria threads demais: use um pool.
> - `future` não é *composável* (sem `then`); para encadear, veja [[Corrotinas Cpp20]] e [[std execution Senders e Receivers]].

## Veja também

- [[Threads e jthread]]
- [[Corrotinas Cpp20]]
- [[Exceções try catch throw]]
- [[condition_variable]]

## Exercício

1. Calcule em paralelo os primos até N dividindo o intervalo entre 4 `async`s.
2. Mostre a diferença entre `launch::async` e `launch::deferred` imprimindo o ID da thread.
