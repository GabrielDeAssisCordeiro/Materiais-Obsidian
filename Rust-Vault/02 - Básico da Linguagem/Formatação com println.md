---
tags: [rust, basico, formatacao]
aliases: ["format specifiers", "{:?}", "{:#?}"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Macros básicas]]", "[[Strings String vs str]]", "[[Entrada e saída no console]]"]
---

# Formatação com println

```rust
fn main() {
    let nome = "Rust";
    let v = 3.14159;

    println!("{}", nome);            // Display
    println!("{nome}");              // captura de variável (inline)
    println!("{0} {1} {0}", "a", "b"); // posicional
    println!("{x} {y}", x = 1, y = 2); // nomeado

    println!("{:?}", vec![1, 2]);    // Debug
    println!("{:#?}", (1, "dois"));  // Debug "bonito" (multilinha)

    println!("{:.2}", v);            // 3.14
    println!("{:8.3}|", v);          // largura 8, 3 casas
    println!("{:<6}|{:^6}|{:>6}|", "e", "c", "d"); // alinhamento
    println!("{:*^9}", "meio");      // preenchimento com *
    println!("{:05}", 42);           // 00042
    println!("{:+}", 5);             // +5
    println!("{:x} {:X} {:b} {:o}", 255, 255, 5, 8); // hex, HEX, binário, octal
    println!("{:#x} {:#b}", 255, 5); // com prefixo
    println!("{{literal}}");         // chaves escapadas
}
```

> [!info] Traits por trás
> `{}` usa a trait `Display` e `{:?}` usa `Debug` (`#[derive(Debug)]` é o caminho mais comum). Veja [[Traits padrão]].

## Veja também

- [[Macros básicas]]
- [[Strings String vs str]]
- [[Entrada e saída no console]]
