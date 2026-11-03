---
tags: [rust, testes, documentacao]
aliases: ["testes na documentação"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Comentários e doc comments]]", "[[cargo doc]]", "[[cargo test]]"]
---

# Doc tests

Blocos de código em comentários `///` (e `//!`) são **compilados e executados** por `cargo test`. Assim, a documentação nunca fica desatualizada.

```rust
// trecho: src/lib.rs de um crate chamado meu_crate
/// Soma dois números.
///
/// # Exemplos
///
/// ```
/// use meu_crate::soma;
///
/// assert_eq!(soma(2, 3), 5);
/// ```
///
/// Linhas iniciadas por `# ` ficam ocultas na documentação, mas executam:
///
/// ```
/// # use meu_crate::soma;
/// # fn principal() -> Result<(), String> {
/// let r = soma(1, 1);
/// assert_eq!(r, 2);
/// # Ok(())
/// # }
/// # principal().unwrap();
/// ```
pub fn soma(a: i32, b: i32) -> i32 {
    a + b
}
```

## Atributos do bloco

| Marcador (após a abertura do bloco) | Efeito |
|---|---|
| `no_run` | compila, mas não executa (ex.: acesso a rede) |
| `ignore` | não compila nem executa |
| `should_panic` | passa se houver panic |
| `compile_fail` | passa se **não** compilar (demonstrar erros) |
| `text` | não é código Rust |

Exemplo: abrir o bloco com três crases seguidas de `no_run` (na mesma linha).

> [!tip] Seções padronizadas
> Documente `# Panics`, `# Errors` e `# Safety` (para `unsafe fn`). Veja [[Boas práticas de tratamento de erros]].

> [!info] Só para bibliotecas
> Doc tests existem em crates de **biblioteca**; binários não têm API pública a documentar.

## Veja também

- [[Comentários e doc comments]]
- [[cargo doc]]
- [[cargo test]]
