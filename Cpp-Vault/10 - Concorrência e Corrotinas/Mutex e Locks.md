---
titulo: "Mutex e locks"
tags: [cpp, concorrencia]
aliases: ["std::mutex", "lock_guard", "unique_lock", "scoped_lock", "shared_mutex", "Exclusão mútua"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Threads e jthread]]", "[[Data Races e Deadlocks]]", "[[RAII]]"]
---

# Mutex e locks

Um **mutex** (*mutual exclusion*) garante que apenas uma thread por vez execute a **seção crítica**. Nunca chame `lock()`/`unlock()` à mão: use *locks* RAII ([[RAII]]), que liberam mesmo com exceção.

| Tipo | Padrão | Uso |
|---|---|---|
| `std::mutex` | C++11 | Exclusão simples |
| `std::recursive_mutex` | C++11 | A mesma thread pode travar de novo (geralmente sinal de design ruim) |
| `std::timed_mutex` | C++11 | `try_lock_for/until` |
| `std::shared_mutex` | C++17 | Muitos leitores **ou** um escritor |
| `std::lock_guard` | C++11 | Trava no construtor, libera no destrutor |
| `std::unique_lock` | C++11 | Flexível: destravar, mover, usar com `condition_variable` |
| `std::scoped_lock` | C++17 | Trava **vários** mutexes sem deadlock |
| `std::shared_lock` | C++14 | Trava compartilhada (leitura) |

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <iostream>
#include <map>
#include <mutex>
#include <shared_mutex>
#include <string>
#include <thread>
#include <vector>

class ContaBancaria {
public:
    void depositar(int v) { std::lock_guard<std::mutex> g{m_}; saldo_ += v; }
    int saldo() const { std::lock_guard<std::mutex> g{m_}; return saldo_; }

    friend void transferir(ContaBancaria& de, ContaBancaria& para, int v) {
        std::scoped_lock g{de.m_, para.m_};              // trava os dois com algoritmo anti-deadlock
        de.saldo_ -= v;
        para.saldo_ += v;
    }
private:
    mutable std::mutex m_;                                // mutable: permite travar em métodos const
    int saldo_ = 0;
};

class Cache {
public:
    std::string ler(int k) const {
        std::shared_lock g{m_};                           // vários leitores simultâneos
        auto it = dados_.find(k);
        return it == dados_.end() ? "" : it->second;
    }
    void escrever(int k, std::string v) {
        std::unique_lock g{m_};                           // escritor exclusivo
        dados_[k] = std::move(v);
    }
private:
    mutable std::shared_mutex m_;
    std::map<int, std::string> dados_;
};

int main() {
    ContaBancaria a, b;
    a.depositar(100);
    {
        std::vector<std::jthread> ts;
        for (int i = 0; i < 4; ++i) ts.emplace_back([&] { for (int j = 0; j < 1000; ++j) { a.depositar(1); } });
    }
    transferir(a, b, 50);
    std::cout << a.saldo() << ' ' << b.saldo() << '\n';   // 4050 50

    Cache c;
    c.escrever(1, "um");
    std::cout << c.ler(1) << '\n';
}
```

## `unique_lock` e escopo mínimo

Mantenha a seção crítica **curta**: nada de I/O, chamadas desconhecidas ou callbacks com o mutex travado.

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <iostream>
#include <mutex>
#include <vector>

std::mutex m;
std::vector<int> fila;

int main() {
    std::unique_lock lk{m};                               // trava
    fila.push_back(1);
    lk.unlock();                                          // libera cedo, antes de trabalho lento
    std::cout << "processando fora da seção crítica\n";
    lk.lock();                                            // pode travar de novo
    fila.push_back(2);
    std::cout << fila.size() << '\n';
}
```

> [!warning] Boas práticas
> - Guarde o mutex **junto aos dados** que ele protege (em uma classe).
> - Não retorne referências/ponteiros para dados protegidos.
> - Defina uma **ordem global** de travamento ou use `scoped_lock` ([[Data Races e Deadlocks]]).
> - `std::mutex` não é copiável nem movível; classes que o contêm perdem cópia/movimento implícitos.
> - Para contadores e flags simples, [[Atomics e Modelo de Memória]] é mais barato.

## Veja também

- [[Threads e jthread]]
- [[condition_variable]]
- [[Data Races e Deadlocks]]
- [[Atomics e Modelo de Memória]]

## Exercício

1. Escreva uma fila thread-safe com `std::mutex` e `std::queue`.
2. Faça duas threads transferirem dinheiro em sentidos opostos com `lock_guard` (deadlock) e depois corrija com `scoped_lock`.
