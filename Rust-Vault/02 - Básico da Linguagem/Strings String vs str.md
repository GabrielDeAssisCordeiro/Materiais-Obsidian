---
tags: [rust, basico, strings]
aliases: ["&str", "texto"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Slices]]", "[[Formatação com println]]", "[[Entrada e saída no console]]"]
---

# Strings String vs str

Rust tem dois tipos de texto principais:

| Tipo | Dono dos dados? | Mutável? | Onde fica |
|---|---|---|---|
| `&str` | Não (é uma fatia emprestada) | Não | Binário, heap ou pilha |
| `String` | Sim | Sim (se `mut`) | Heap |

Ambos guardam **UTF-8** válido.

```rust
fn main() {
    let literal: &str = "olá";            // literal: &'static str
    let mut dono: String = String::from("olá");
    dono.push_str(", mundo");
    dono.push('!');
    println!("{literal} | {dono}");

    // De &str para String e de volta
    let outro = literal.to_string();
    let fatia: &str = &outro;
    println!("{fatia}");

    // Concatenação
    let a = String::from("a");
    let b = String::from("b");
    let ab = a + &b; // a foi movida, b continua disponível
    println!("{ab} {b}");
    let c = format!("{ab}-{b}");
    println!("{c}");
}
```

## UTF-8 e indexação

Não é possível indexar texto por posição (`s[0]`), porque um caractere pode ocupar de 1 a 4 bytes.

```rust
fn main() {
    let s = "ação";
    println!("bytes: {}", s.len());           // 6
    println!("chars: {}", s.chars().count()); // 4
    for c in s.chars() {
        print!("[{c}]");
    }
    println!();
    // Fatiar por bytes exige limites válidos de caractere
    println!("{}", &s[0..1]); // "a"
}
```

> [!warning] Panic ao fatiar no meio de um caractere
> `&s[0..2]` em `"ação"` faz *panic*, pois o byte 2 está no meio de `ç`.

> [!tip] Regra prática
> Parâmetro de função: `&str`. Valor que a struct possui: `String`.

## Exercício

Conte quantos caracteres e quantos bytes tem `"coração"`.

## Veja também

- [[Slices]]
- [[Formatação com println]]
- [[Entrada e saída no console]]
