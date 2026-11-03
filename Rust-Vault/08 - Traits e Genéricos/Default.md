---
tags: [rust, traits]
aliases: ["valor padrão", "Default::default"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[derive]]", "[[Traits padrão]]", "[[Builder]]"]
---

# Default

`Default` define um valor "inicial razoável" para um tipo.

```rust
#[derive(Debug)]
struct Opcoes {
    tentativas: u32,
    timeout_ms: u64,
    verboso: bool,
}

// Implementação manual quando o padrão não é "zero"
impl Default for Opcoes {
    fn default() -> Self {
        Self { tentativas: 3, timeout_ms: 1000, verboso: false }
    }
}

fn main() {
    let o = Opcoes::default();
    let o2 = Opcoes { verboso: true, ..Default::default() }; // sobrescreve só um campo
    println!("{:?} {:?}", o, o2);

    // Padrões da std: 0, false, "", Vec vazio, None...
    let (a, b, c): (i32, bool, String) = Default::default();
    println!("{a} {b} {:?} {:?}", c, Vec::<u8>::default());
    let talvez: Option<i32> = None;
    println!("{}", talvez.unwrap_or_default()); // 0
}
```

> [!info] Combinação com o padrão builder
> `..Default::default()` e o *builder* são as duas formas mais comuns de construir tipos com muitas opções.

## Veja também

- [[derive]]
- [[Traits padrão]]
- [[Builder]]
