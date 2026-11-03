---
tags: [rust, unsafe, ferramentas]
aliases: ["Miri", "cargo miri", "detector de UB"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Unsafe Rust]]", "[[Invariantes e boas práticas de unsafe]]", "[[CI com GitHub Actions]]"]
---

# Miri

**Miri** é um interpretador do MIR do Rust que **detecta comportamento indefinido** em tempo de execução: acessos fora dos limites, uso após liberação, ponteiros desalinhados, violações de aliasing (*Stacked/Tree Borrows*), data races, valores inválidos e vazamentos.

```bash
rustup +nightly component add miri
cargo +nightly miri run
cargo +nightly miri test          # roda a suíte de testes sob o Miri
```

## Exemplo: bug que o compilador não vê

```rust
// Compila normalmente, mas tem comportamento indefinido: lê além do array
fn main() {
    let a = [1, 2, 3];
    let p = a.as_ptr();
    let valor = unsafe { *p.add(5) }; // fora dos limites!
    println!("{valor}");
}
```

Sob o Miri, a execução é interrompida com um erro parecido com:

```text
error: Undefined Behavior: dereferencing pointer failed: ... is out-of-bounds
```

> [!info] Mensagem aproximada
> O texto exato varia entre versões do Miri.

| Detecta | Não detecta |
|---|---|
| UB em código `unsafe` Rust | bugs em código C ligado por FFI (suporte limitado) |
| Vazamentos de memória | falhas dependentes de hardware real |
| Data races (em threads simuladas) | problemas só observáveis em escala (é lento) |

> [!tip] Use na CI
> Rodar `cargo +nightly miri test` em crates com `unsafe` é uma das melhores formas de manter a confiança. Combine com *sanitizers* (`-Zsanitizer=address`) e fuzzing (`cargo-fuzz`).

> [!warning] É lento
> O Miri é dezenas de vezes mais lento que a execução normal; use em testes pequenos e focados.

## Veja também

- [[Unsafe Rust]]
- [[Invariantes e boas práticas de unsafe]]
- [[CI com GitHub Actions]]
