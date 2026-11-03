---
tags: [rust, fundamentos, comparacao]
aliases: []
tipo: comparacao
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Filosofia do Rust]]", "[[O que é Rust]]", "[[Casos de uso do Rust]]"]
---

# Rust vs C, C++, Go, Python e Java

| Aspecto | Rust | C | C++ | Go | Python | Java |
|---|---|---|---|---|---|---|
| Gerenciamento de memória | Ownership (compilação) | Manual | Manual + RAII | GC | GC | GC |
| Segurança de memória | Garantida (código seguro) | Não | Parcial | Sim | Sim | Sim |
| Desempenho | Muito alto | Muito alto | Muito alto | Alto | Baixo a médio | Alto |
| Concorrência | Verificada pelo compilador | Manual | Manual | Goroutines | GIL (threads) | Threads |
| Tipagem | Estática forte | Estática fraca | Estática | Estática | Dinâmica | Estática |
| Nulo | `Option<T>` | `NULL` | `nullptr` | `nil` | `None` | `null` |
| Erros | `Result` | códigos | exceções/códigos | `error` retornado | exceções | exceções |
| Curva de aprendizado | Íngreme | Média | Íngreme | Suave | Suave | Média |

## Em poucas palavras

- **C/C++**: mesma classe de desempenho, mas Rust impede bugs de memória em código seguro.
- **Go**: mais simples e rápido de aprender; usa GC. Rust dá mais controle e menos latência imprevisível.
- **Python**: Rust costuma ser usado para acelerar partes críticas (veja PyO3 em [[Casos de uso do Rust]]).
- **Java**: ambos têm tipagem forte; Rust não tem JVM nem GC.

> [!tip] Mesma ideia, sintaxe diferente
> Um laço somando números em Rust:

```rust
fn main() {
    // Soma dos quadrados de 1 a 10
    let soma: u32 = (1..=10).map(|n| n * n).sum();
    println!("{soma}"); // 385
}
```

## Veja também

- [[Filosofia do Rust]]
- [[O que é Rust]]
- [[Casos de uso do Rust]]
