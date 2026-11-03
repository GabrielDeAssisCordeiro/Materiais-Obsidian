---
titulo: "MOC — Concorrência e Corrotinas"
tags: [cpp, moc, concorrencia, corrotinas]
aliases: ["MOC Concorrência e Corrotinas", "Concorrência e Corrotinas"]
tipo: moc
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - RAII e Move]]", "[[MOC - STL e Ranges]]"]
---

# MOC — Concorrência e Corrotinas

```mermaid
flowchart TD
    T[Threads e jthread] --> M[Mutex e Locks]
    M --> CV[condition_variable]
    T --> F[future / promise / async]
    M --> A[Atomics e memória]
    A --> D[Data races e deadlocks]
    M --> D
    CV --> L[latch / barrier / semaphore]
    T --> S[stop_token]
    F --> C[Corrotinas]
    C --> EX[std::execution]
    T --> P[Algoritmos paralelos]
    P --> TB[TBB e OpenMP]
```

## Fundamentos de threads

- [[Threads e jthread]]
- [[Mutex e Locks]]
- [[condition_variable]]
- [[future promise e async]]
- [[stop_token e Cancelamento]]
- [[latch barrier e semaphore]]

## Memória e correção

- [[Atomics e Modelo de Memória]]
- [[Data Races e Deadlocks]]

## Paralelismo e assincronia

- [[Algoritmos Paralelos]]
- [[TBB e OpenMP]]
- [[Corrotinas Cpp20]]
- [[std execution Senders e Receivers]]

## Ordem sugerida

[[Threads e jthread]] → [[Mutex e Locks]] → [[Data Races e Deadlocks]] → [[condition_variable]] → [[future promise e async]] → [[Atomics e Modelo de Memória]] → [[stop_token e Cancelamento]] → [[latch barrier e semaphore]] → [[Algoritmos Paralelos]] → [[TBB e OpenMP]] → [[Corrotinas Cpp20]] → [[std execution Senders e Receivers]]

> [!tip] Ferramentas
> Use `-fsanitize=thread` e [[Comportamento Indefinido e Não Especificado|conhecimento de UB]] como rede de segurança.

## Veja também

- [[Home - Cpp]]
- [[MOC - RAII e Move]]
- [[MOC - STL e Ranges]]
- [[MOC - Strings e IO]]
