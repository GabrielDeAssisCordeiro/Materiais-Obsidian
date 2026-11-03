---
titulo: "Exercícios de Concorrência - Cpp"
tags: [cpp, exercicios, concorrencia, threads]
aliases: ["Lista 7"]
tipo: exercicio
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Concorrência e Corrotinas]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de Concorrência - Cpp

Compile com `-pthread`. Teoria: [[Threads e jthread]], [[Mutex e Locks]], [[Atomics e Modelo de Memória]], [[condition_variable]], [[future promise e async]].

## 1. Soma paralela

Some um vetor de 1 milhão de `1`s dividindo o trabalho em 4 `std::jthread`, cada um escrevendo em **sua** posição de um vetor de parciais.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <iostream>
#include <numeric>
#include <thread>
#include <vector>

int main() {
    std::vector<int> dados(1'000'000, 1);
    constexpr int T = 4;
    std::vector<long long> parciais(T, 0);
    {
        std::vector<std::jthread> ts;
        const std::size_t bloco = dados.size() / T;
        for (int i = 0; i < T; ++i)
            ts.emplace_back([&, i] {
                auto ini = dados.begin() + i * bloco;
                auto fim = (i == T - 1) ? dados.end() : ini + bloco;
                parciais[i] = std::accumulate(ini, fim, 0LL);
            });
    }   // jthreads fazem join aqui
    std::cout << std::accumulate(parciais.begin(), parciais.end(), 0LL) << '\n';   // 1000000
}
```

> [!tip] Por que vetor de parciais?
> Cada thread escreve em um elemento diferente: sem *data race*. (Para evitar [[False Sharing]], alinhe/espace as posições em código de alto desempenho.)

## 2. Contador: `mutex` vs `atomic`

Incremente um contador 100 mil vezes em 4 threads, das duas formas.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <atomic>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

int main() {
    std::atomic<int> a{0};
    int m = 0;
    std::mutex mtx;
    {
        std::vector<std::jthread> ts;
        for (int t = 0; t < 4; ++t)
            ts.emplace_back([&] {
                for (int i = 0; i < 100'000; ++i) {
                    ++a;                                            // atômico
                    std::lock_guard lk(mtx);                        // exclusão mútua
                    ++m;
                }
            });
    }
    std::cout << a << ' ' << m << '\n';   // 400000 400000
}
```

## 3. Produtor e consumidor

Uma fila protegida por `mutex` + `condition_variable`; o produtor envia 1..5 e um sinal de fim.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <optional>
#include <queue>
#include <thread>

int main() {
    std::queue<std::optional<int>> fila;     // nullopt = fim
    std::mutex m;
    std::condition_variable cv;

    std::jthread consumidor([&] {
        while (true) {
            std::unique_lock lk(m);
            cv.wait(lk, [&] { return !fila.empty(); });   // predicado: evita spurious wakeup
            auto item = fila.front();
            fila.pop();
            lk.unlock();
            if (!item) break;
            std::cout << *item << ' ';
        }
        std::cout << '\n';
    });

    for (int i = 1; i <= 5; ++i) {
        { std::lock_guard lk(m); fila.push(i); }
        cv.notify_one();
    }
    { std::lock_guard lk(m); fila.push(std::nullopt); }
    cv.notify_one();
}
```

## 4. `std::async`

Calcule `fib(30)` e `fib(31)` em paralelo com `std::async` e some os resultados.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <future>
#include <iostream>

long fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }

int main() {
    auto a = std::async(std::launch::async, fib, 30);
    auto b = std::async(std::launch::async, fib, 31);
    std::cout << a.get() + b.get() << '\n';   // 832040 + 1346269 = 2178309
}
```

## Veja também

- [[Threads e jthread]]
- [[Data Races e Deadlocks]]
- [[Atomics e Modelo de Memória]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Rode o exercício 2 com `-fsanitize=thread` e depois remova o `lock_guard` (deixando `++m` desprotegido) para ver o relatório de *data race* ([[Sanitizers]]).
