---
titulo: "Threads e jthread"
tags: [cpp, concorrencia, jthread, cpp20]
aliases: ["std::jthread", "hardware_concurrency", "detach"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Mutex e Locks]]", "[[stop_token e Cancelamento]]", "[[Data Races e Deadlocks]]"]
---

# Threads e `jthread`

> [!info] Introdução
> `std::thread`: **C++11** (`<thread>`). `std::jthread` (junta sozinha e aceita cancelamento cooperativo): **C++20** — GCC 10+, Clang 18+ com libc++ (parcial antes), MSVC 2019 16.9+. Em Linux/GCC compile com `-pthread`.

Uma **thread** é um fluxo de execução dentro do processo, compartilhando o mesmo espaço de memória. Compartilhar memória é poderoso e perigoso: veja [[Data Races e Deadlocks]].

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <iostream>
#include <string>
#include <thread>
#include <vector>

void trabalho(int id, const std::string& msg) {
    // saída concorrente pode intercalar; aqui cada thread escreve em posições distintas abaixo
    (void)id; (void)msg;
}

int main() {
    std::thread t{trabalho, 1, "olá"};                // argumentos são COPIADOS/movidos para a thread
    t.join();                                          // espera terminar (obrigatório antes do destrutor)

    std::vector<int> resultados(4);
    std::vector<std::jthread> pool;
    for (int i = 0; i < 4; ++i)
        pool.emplace_back([&resultados, i] { resultados[i] = i * i; });   // cada thread escreve no SEU índice
    pool.clear();                                      // jthread::~jthread faz join

    for (int r : resultados) std::cout << r << ' ';    // 0 1 4 9
    std::cout << '\n' << std::thread::hardware_concurrency() << " núcleos lógicos (dica)\n";
}
```

## Regras essenciais

| Regra | Motivo |
|---|---|
| Faça `join()` ou `detach()` antes de destruir `std::thread` | Senão `std::terminate` |
| Prefira `std::jthread` | Faz `join` automático (RAII) e suporta [[stop_token e Cancelamento]] |
| Evite `detach()` | A thread pode sobreviver aos objetos que ela referencia (dangling) |
| Passe referências com `std::ref` | Por padrão os argumentos são copiados |
| Exceção não tratada na thread | Chama `std::terminate`; capture e propague via [[future promise e async]] |

> [!bug] Captura por referência de variável local
> ```cpp
> void f() { int x = 0; std::thread t{[&] { /* usa x */ }}; t.detach(); }   // x some, thread continua: UB
> ```
> Use `join`, ou copie/mova os dados para a thread.

## `thread_local`

Cada thread tem sua própria cópia da variável: útil para contadores e caches sem sincronização.

```cpp
// g++ -std=c++20 -Wall -Wextra -pthread
#include <iostream>
#include <thread>

thread_local int contador = 0;                         // uma instância por thread

int main() {
    auto f = [] { for (int i = 0; i < 3; ++i) ++contador; return contador; };
    int a = 0, b = 0;
    std::jthread t1{[&] { a = f(); }}, t2{[&] { b = f(); }};
    t1.join(); t2.join();
    std::cout << a << ' ' << b << ' ' << contador << '\n';   // 3 3 0
}
```

> [!tip] Quantas threads?
> Para trabalho de CPU, comece com `hardware_concurrency()`. Criar uma thread por tarefa pequena é caro: use um *pool*, algoritmos paralelos ([[Algoritmos Paralelos]]) ou bibliotecas ([[TBB e OpenMP]]).

## Veja também

- [[Mutex e Locks]]
- [[Data Races e Deadlocks]]
- [[stop_token e Cancelamento]]
- [[future promise e async]]
- [[RAII]]

## Exercício

1. Some os elementos de um vetor grande dividindo em N `jthread`s, cada um escrevendo sua soma parcial.
2. Reproduza o erro de `detach()` com variável local e explique por que é UB.
