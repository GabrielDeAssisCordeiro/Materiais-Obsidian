---
tags: [rust, macros, boas-praticas]
aliases: ["macros: quando usar", "alternativas a macros"]
tipo: comparacao
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[macro_rules]]", "[[Macros procedurais]]", "[[Genéricos]]", "[[Traits]]"]
---

# Quando usar e evitar macros

Macros são poderosas, mas **dificultam leitura, ferramentas e mensagens de erro**. Antes de escrever uma, tente as alternativas.

| Necessidade | Prefira | Use macro quando |
|---|---|---|
| Reaproveitar lógica | **função** | precisa operar sobre sintaxe (nomes, tipos, itens) |
| Código para vários tipos | **genéricos / traits** | gera impls para uma lista de tipos (`impl_trait_for!(i8, i16, i32)`) |
| Número variável de argumentos | slice, iterador, builder | sintaxe tipo `println!`/`vec!` |
| Valores computados em compilação | **`const fn`** / `const` | |
| Reduzir boilerplate de `derive` | **`#[derive]`** existente | nenhum derive faz o que você precisa |
| DSL embutida (SQL, HTML, rotas) | **macro** (function-like/atributo) | a sintaxe do domínio vale o custo |

## Vantagens e custos

| Vantagens | Custos |
|---|---|
| Elimina repetição que funções não conseguem | Erros de compilação obscuros |
| Sintaxe sob medida (DSL) | IDE e rust-analyzer entendem pior |
| Executa em compilação (zero custo em runtime) | Mais tempo de compilação (proc macros) |
| Variádicas e geração de itens | Código gerado é "invisível" ao leitor |

## Exemplo: função resolve

```rust
// Não precisa de macro: uma função genérica basta
fn maior<T: PartialOrd>(a: T, b: T) -> T {
    if a > b { a } else { b }
}

// Macro faz sentido para gerar muitas impls repetitivas
trait Nome {
    fn nome() -> &'static str;
}

macro_rules! impl_nome {
    ($($t:ty => $s:expr),* $(,)?) => {
        $( impl Nome for $t {
            fn nome() -> &'static str { $s }
        } )*
    };
}

impl_nome!(i32 => "inteiro", f64 => "real", bool => "booleano");

fn main() {
    println!("{} {}", maior(3, 8), maior("a", "b"));
    println!("{} {} {}", i32::nome(), f64::nome(), bool::nome());
}
```

## Depurando macros

```bash
cargo install cargo-expand
cargo expand                  # mostra o código final
cargo expand caminho::item    # só um item
```

> [!tip] Regra de bolso
> Escreva primeiro com funções e genéricos. Só introduza uma macro quando a repetição for realmente irredutível ou a sintaxe do domínio justificar.

## Veja também

- [[macro_rules]]
- [[Macros procedurais]]
- [[Genéricos]]
- [[Traits]]
