---
tags: [rust, basico, controle-de-fluxo, pattern-matching]
aliases: ["if let", "let else", "let chains"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[match]]", "[[while let]]", "[[Option e Result]]"]
---

# if let e let else

## `if let`

Atalho para um `match` com um único padrão de interesse.

```rust
fn main() {
    let talvez: Option<i32> = Some(7);

    if let Some(v) = talvez {
        println!("tem {v}");
    } else {
        println!("vazio");
    }
}
```

## `let else`

Desestrutura ou **sai do escopo** (return, break, continue, panic). Deixa o "caminho feliz" sem aninhamento.

```rust
fn dobra_texto(s: &str) -> Option<i32> {
    let Ok(n) = s.parse::<i32>() else {
        return None; // o else DEVE divergir
    };
    Some(n * 2)
}

fn main() {
    println!("{:?}", dobra_texto("21"));
    println!("{:?}", dobra_texto("abc"));
}
```

> [!info] let chains
> Na edição 2024, combinações como `if let Some(x) = a && x > 0` (let chains) foram estabilizadas em versões recentes do compilador.

> [!question] Verificar na documentação oficial
> Confirme em qual versão exata as *let chains* foram estabilizadas e se estão disponíveis na sua toolchain antes de usá-las.

## Veja também

- [[match]]
- [[while let]]
- [[Option e Result]]
