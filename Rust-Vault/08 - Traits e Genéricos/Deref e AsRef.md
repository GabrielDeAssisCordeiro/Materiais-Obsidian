---
tags: [rust, traits, ponteiros]
aliases: ["Deref", "DerefMut", "AsRef", "deref coercion"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Box]]", "[[Traits padrão]]", "[[Strings String vs str]]"]
---

# Deref e AsRef

## Deref

`Deref` permite que um tipo se comporte como uma referência: o operador `*` e a **deref coercion** (conversão automática de `&Tipo` para `&Alvo`).

```rust
use std::ops::Deref;

struct MinhaCaixa<T>(T);

impl<T> Deref for MinhaCaixa<T> {
    type Target = T;

    fn deref(&self) -> &T {
        &self.0
    }
}

fn ola(nome: &str) {
    println!("Olá, {nome}");
}

fn main() {
    let y = MinhaCaixa(5);
    assert_eq!(5, *y); // *y == *(y.deref())

    let c = MinhaCaixa(String::from("Rust"));
    ola(&c); // &MinhaCaixa<String> -> &String -> &str (coercão em cadeia)
}
```

É por isso que você passa `&String` onde se espera `&str` e `&Vec<T>` onde se espera `&[T]`.

> [!warning] Não abuse de Deref
> Use `Deref` para **ponteiros inteligentes**. Usá-lo para simular herança é considerado um antipadrão.

## AsRef

`AsRef<T>` converte barato em `&T`; ótimo para APIs que aceitam vários tipos.

```rust
use std::path::Path;

fn tamanho<S: AsRef<str>>(s: S) -> usize {
    s.as_ref().len()
}

fn extensao<P: AsRef<Path>>(p: P) -> Option<String> {
    p.as_ref().extension().map(|e| e.to_string_lossy().into_owned())
}

fn main() {
    println!("{} {}", tamanho("abc"), tamanho(String::from("abcd")));
    println!("{:?}", extensao("relatorio.pdf"));
}
```

## Veja também

- [[Box]]
- [[Traits padrão]]
- [[Strings String vs str]]
