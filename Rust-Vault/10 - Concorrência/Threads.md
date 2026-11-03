---
tags: [rust, concorrencia, threads]
aliases: ["spawn", "thread::scope", "move closure"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Concorrência sem medo]]", "[[Closures]]", "[[Canais mpsc]]", "[[Send e Sync]]"]
---

# Threads

Rust usa **threads do sistema operacional** (modelo 1:1). Cada `thread::spawn` cria uma thread nativa.

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..=3 {
            println!("thread filha: {i}");
            thread::sleep(Duration::from_millis(10));
        }
        42 // valor de retorno da thread
    });

    for i in 1..=2 {
        println!("main: {i}");
        thread::sleep(Duration::from_millis(10));
    }

    // join espera a thread terminar e devolve Result<T, ...>
    let resultado = handle.join().unwrap();
    println!("resultado = {resultado}");
}
```

> [!info] Saída não determinística
> A intercalação das mensagens varia a cada execução: é o agendador do sistema operacional que decide.

## `move`: levando dados para a thread

A thread pode viver mais que a função que a criou, então a closure precisa **ser dona** dos dados (ou eles precisam ser `'static`).

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];
    let h = thread::spawn(move || {
        println!("{v:?}"); // v foi movido para a thread
    });
    h.join().unwrap();
    // println!("{v:?}"); // erro: v foi movido
}
```

## Panic em thread

```rust
use std::thread;

fn main() {
    let h = thread::spawn(|| {
        if true {
            panic!("falhou!");
        }
    });
    // join devolve Err se a thread entrou em pânico; a main continua viva
    println!("thread terminou com erro: {}", h.join().is_err());
}
```

## `thread::scope`: threads que emprestam dados

Threads com escopo têm a garantia de terminar antes de o escopo acabar, então podem **emprestar** dados locais sem `move`.

```rust
use std::thread;

fn main() {
    let dados = vec![1, 2, 3, 4, 5, 6];
    let (esq, dir) = dados.split_at(3);

    let total = thread::scope(|s| {
        let h1 = s.spawn(|| esq.iter().sum::<i32>());
        let h2 = s.spawn(|| dir.iter().sum::<i32>());
        h1.join().unwrap() + h2.join().unwrap()
    });
    println!("{total}"); // 21
}
```

## Outras utilidades

```rust
use std::thread;

fn main() {
    let n = thread::available_parallelism().map(|n| n.get()).unwrap_or(1);
    println!("núcleos disponíveis: {n}");

    let h = thread::Builder::new()
        .name("trabalhador".to_string())
        .stack_size(64 * 1024)
        .spawn(|| thread::current().name().map(|s| s.to_string()))
        .unwrap();
    println!("{:?}", h.join().unwrap());
}
```

> [!tip] Quantas threads?
> Para trabalho de CPU, algo próximo do número de núcleos. Para muita E/S concorrente, considere [[Async e await]] em vez de milhares de threads.

## Exercício

Divida a soma dos números de 1 a 1.000.000 entre 4 threads com `thread::scope` e some os resultados parciais.

## Veja também

- [[Concorrência sem medo]]
- [[Closures]]
- [[Canais mpsc]]
- [[Send e Sync]]
