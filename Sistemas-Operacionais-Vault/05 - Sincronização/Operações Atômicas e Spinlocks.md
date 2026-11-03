---
titulo: "Operações Atômicas e Spinlocks"
tags:
  - sistemas-operacionais
  - conceito
  - sincronizacao
tipo: conceito
nivel: avancado
relacionados:
  - "[[Seção Crítica]]"
  - "[[Mutex]]"
  - "[[Condições de Corrida]]"
  - "[[Interrupções]]"
---

# Operações Atômicas e Spinlocks

## Resumo

Operações **atômicas** são executadas pelo hardware de forma **indivisível**: nenhuma outra CPU observa um estado intermediário. São o alicerce de todas as primitivas de sincronização. Um **spinlock** usa essas operações para implementar uma trava com **espera ocupada**.

## Instruções de hardware

| Instrução | Efeito | Arquitetura |
|---|---|---|
| **Test-and-Set (TAS)** | Grava 1 e retorna o valor antigo | x86 `xchg`, ARM `swp` |
| **Compare-and-Swap (CAS)** | Se `*p == esperado`, grava novo; retorna sucesso | x86 `lock cmpxchg` |
| **Fetch-and-Add** | Soma e retorna o valor anterior | x86 `lock xadd` |
| **LL/SC** | Load-linked + store-conditional | ARM, RISC-V, MIPS, POWER |

## Spinlock com test-and-set

```c
#include <stdatomic.h>

typedef struct { atomic_flag f; } spinlock_t;

void spin_lock(spinlock_t *l) {
    while (atomic_flag_test_and_set_explicit(&l->f, memory_order_acquire))
        __builtin_ia32_pause();          // dica à CPU: reduz consumo e contenção
}
void spin_unlock(spinlock_t *l) {
    atomic_flag_clear_explicit(&l->f, memory_order_release);
}
```

Melhoria **test-and-test-and-set**: gira lendo (cache local) e só tenta o TAS quando a trava parece livre, reduzindo tráfego de coerência.

## Contador atômico e CAS

```c
#include <stdatomic.h>
atomic_long contador = 0;

void incrementa(void) {
    atomic_fetch_add(&contador, 1);       // sem trava, sem corrida
}

// Padrão CAS em laço (ex.: atualizar máximo)
void atualiza_max(atomic_long *m, long v) {
    long atual = atomic_load(m);
    while (v > atual && !atomic_compare_exchange_weak(m, &atual, v))
        ;   // se falhou, 'atual' foi atualizado; tenta de novo
}
```

> [!warning] Problema ABA
> Em estruturas lock-free, o CAS pode ter sucesso mesmo que o valor tenha mudado de A para B e voltado a A, ocultando alterações. Soluções: ponteiros com contador de versão, *hazard pointers*, RCU.

## Ordenação de memória

Compiladores e CPUs **reordenam** acessos. Modelos de memória (`memory_order_relaxed`, `acquire`, `release`, `seq_cst`) controlam o que é visível e quando. Em x86 o modelo é relativamente forte (TSO); em ARM e RISC-V, fraco: exige barreiras explícitas.

## Spinlock x Mutex

| Critério | Spinlock | Mutex (com bloqueio) |
|---|---|---|
| Espera | Ocupada (gasta CPU) | Dorme; libera a CPU |
| Custo se livre | Muito baixo | Baixo (fast path com atômica) |
| Custo se contendido | Desperdício de CPU | Troca de contexto |
| Ideal para | Seções muito curtas; kernel; contexto de interrupção | Seções longas ou com E/S |
| Em monoprocessador | Inútil (a trava nunca será liberada enquanto gira) | Adequado |

> [!info] No kernel Linux
> `spin_lock_irqsave()` desabilita interrupções locais antes de pegar a trava, para evitar que uma ISR na mesma CPU tente pegar a mesma trava (deadlock). Em contexto de interrupção só se pode usar spinlocks, nunca mutex ([[Interrupções]]).

## Exemplo: contador atômico em Python/Rust

```rust
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;

fn main() {
    let c = Arc::new(AtomicUsize::new(0));
    let hs: Vec<_> = (0..4).map(|_| {
        let c = Arc::clone(&c);
        thread::spawn(move || for _ in 0..100_000 { c.fetch_add(1, Ordering::Relaxed); })
    }).collect();
    for h in hs { h.join().unwrap(); }
    println!("{}", c.load(Ordering::SeqCst));   // 400000
}
```

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Latência mínima sem troca de contexto | Espera ocupada desperdiça CPU |
| Funciona em contexto de interrupção | Pode causar inanição (sem justiça) |
| Base de estruturas lock-free | Programação lock-free é sutil (ABA, ordenação) |

## Pontos-chave

- Atômicas (TAS, CAS, fetch-add) são a base de toda sincronização.
- Spinlock = espera ocupada; bom para seções curtas.
- Modelos de memória e barreiras importam em multicore.

## Veja também

[[Mutex]] · [[Seção Crítica]] · [[MOC - Sincronização]]
