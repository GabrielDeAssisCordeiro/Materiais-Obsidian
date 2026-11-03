---
tags: [rust, basico, sintaxe]
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Variáveis e mutabilidade]]", "[[Shadowing]]", "[[Tipos escalares]]"]
---

# Constantes e statics

## `const`

Valor **calculado em tempo de compilação**, sempre imutável, com tipo obrigatório e nome em `MAIÚSCULAS_COM_UNDERSCORE`. É "colado" (inlined) onde usado.

```rust
const SEGUNDOS_POR_HORA: u32 = 60 * 60;

fn main() {
    println!("{SEGUNDOS_POR_HORA}");
}
```

## `static`

Possui **um endereço fixo** na memória durante todo o programa (lifetime `'static`).

```rust
static SAUDACAO: &str = "olá";

fn main() {
    println!("{SAUDACAO}");
}
```

| | `const` | `static` |
|---|---|---|
| Endereço próprio | Não (inline) | Sim |
| Mutável | Nunca | Só `static mut` (exige `unsafe`) |
| Uso típico | Constantes numéricas, tamanhos | Dados globais, strings, tabelas |

> [!warning] `static mut`
> Acessar `static mut` exige `unsafe` e, na edição 2024, referências a ele são negadas por lint. Prefira atômicos ou `Mutex` em [[Atômicos]].

> [!info] const fn
> Funções marcadas `const fn` podem ser avaliadas em tempo de compilação e usadas para inicializar `const`.

## Veja também

- [[Variáveis e mutabilidade]]
- [[Shadowing]]
- [[Tipos escalares]]
