---
tags: [rust, memoria]
aliases: ["Drop", "destrutor", "drop()", "mem::forget"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Ownership e regras]]", "[[Box]]", "[[Weak e ciclos de referência]]", "[[Traits padrão]]"]
---

# Drop e RAII

**RAII** (*Resource Acquisition Is Initialization*): um recurso é adquirido ao criar o objeto e **liberado automaticamente** quando ele sai de escopo. Em Rust, o gancho é a trait `Drop`.

```rust
struct Guarda(&'static str);

impl Drop for Guarda {
    fn drop(&mut self) {
        println!("liberando {}", self.0);
    }
}

fn main() {
    let _a = Guarda("a");
    let b = Guarda("b");
    {
        let _c = Guarda("c");
        println!("fim do bloco interno");
    } // _c é liberado aqui

    drop(b); // libera antecipadamente (std::mem::drop)
    println!("fim de main");
} // _a é liberado aqui; ordem: inversa à da declaração
```

Saída:

```text
fim do bloco interno
liberando c
liberando b
fim de main
liberando a
```

```rust
// ❌ NÃO COMPILA: não se chama .drop() manualmente
struct G;

impl Drop for G {
    fn drop(&mut self) {}
}

fn main() {
    let g = G;
    g.drop();
}
```

```text
error[E0040]: explicit use of destructor method
```

**Correção:** `drop(g);` (função livre, que toma posse do valor).

## Exemplos de RAII na biblioteca padrão

| Tipo | O que a liberação faz |
|---|---|
| `File` | fecha o descritor |
| `MutexGuard` | libera o lock |
| `Vec`, `String`, `Box` | devolvem a memória da heap |
| `Rc`/`Arc` | decrementam a contagem; liberam em zero |
| `JoinHandle` | (não faz join automaticamente) |

> [!info] Ordem de destruição
> Variáveis locais: ordem **inversa** da declaração. Campos de struct: na ordem em que foram declarados.

> [!warning] `mem::forget`
> `std::mem::forget(valor)` impede o `drop` (vazamento). É seguro, porém raramente desejável.

## Exercício

Crie um `struct Timer` cujo `Drop` imprima "tempo decorrido" usando `std::time::Instant`.

## Veja também

- [[Ownership e regras]]
- [[Box]]
- [[Weak e ciclos de referência]]
- [[Traits padrão]]
