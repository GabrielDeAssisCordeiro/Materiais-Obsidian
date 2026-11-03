---
tags: [rust, macros, metaprogramacao]
aliases: ["macro_rules!", "macros declarativas", "macros por exemplo", "repetições"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Macros procedurais]]", "[[Quando usar e evitar macros]]", "[[Macros básicas]]"]
---

# macro_rules

`macro_rules!` define **macros declarativas**: você descreve padrões de entrada (como um `match` sobre sintaxe) e o código que cada padrão gera. A expansão acontece em compilação, antes da checagem de tipos.

## Estrutura

```text
macro_rules! nome {
    (padrão) => { expansão };
    (outro padrão) => { outra expansão };
}
```

## Fragmentos (*specifiers*)

| Fragmento | Casa com |
|---|---|
| `$x:expr` | uma expressão |
| `$x:ident` | um identificador (nome) |
| `$x:ty` | um tipo |
| `$x:pat` | um padrão |
| `$x:stmt` | uma instrução |
| `$x:block` | um bloco `{ ... }` |
| `$x:item` | um item (fn, struct, impl...) |
| `$x:path` | um caminho (`std::fmt::Debug`) |
| `$x:literal` | um literal (`42`, `"oi"`) |
| `$x:lifetime` | um lifetime (`'a`) |
| `$x:vis` | visibilidade (`pub`, vazio) |
| `$x:tt` | uma *token tree* (o mais flexível) |

## Repetições

`$( ... ) sep rep` onde `rep` é `*` (zero ou mais), `+` (uma ou mais) ou `?` (zero ou uma).

```rust
// Macro simples: $x:expr é tratado como UMA expressão (sem os problemas de precedência do C)
macro_rules! quadrado {
    ($x:expr) => {
        $x * $x
    };
}

// Recursão: máximo de N valores
macro_rules! maximo {
    ($x:expr) => ($x);
    ($x:expr, $($resto:expr),+) => {{
        let a = $x;
        let b = maximo!($($resto),+);
        if a > b { a } else { b }
    }};
}

// Repetição: um vec! simplificado, aceitando vírgula final
macro_rules! meu_vec {
    ( $( $x:expr ),* $(,)? ) => {{
        let mut v = Vec::new();
        $( v.push($x); )*
        v
    }};
}

// Sintaxe própria: mapa!{ chave => valor, ... }
macro_rules! mapa {
    ( $( $k:expr => $v:expr ),* $(,)? ) => {{
        let mut m = std::collections::HashMap::new();
        $( m.insert($k, $v); )*
        m
    }};
}

// Gera itens: uma struct com Debug e Default
macro_rules! cria_struct {
    ($nome:ident { $( $campo:ident : $tipo:ty ),* $(,)? }) => {
        #[derive(Debug, Default)]
        struct $nome {
            $( $campo: $tipo ),*
        }
    };
}

cria_struct!(Ponto { x: i32, y: i32 });

fn main() {
    println!("{}", quadrado!(1 + 2));           // 9, e não 1 + 2 * 1 + 2
    println!("{}", maximo!(3, 9, 4));           // 9
    println!("{:?}", meu_vec![1, 2, 3,]);
    let m = mapa! { "a" => 1, "b" => 2 };
    println!("{}", m["b"]);
    println!("{:?}", Ponto::default());
}
```

## Higiene

Variáveis criadas dentro da macro **não colidem** com as do chamador.

```rust
macro_rules! soma_com_cem {
    ($e:expr) => {{
        let x = 100; // este x é "higiênico": é outro x
        $e + x
    }};
}

fn main() {
    let x = 1;
    println!("{}", soma_com_cem!(x)); // 101: o `x` passado é o de fora (1)
}
```

## Quando nenhum padrão casa

```rust
// ❌ NÃO COMPILA: nenhum padrão aceita zero argumentos
macro_rules! dobra {
    ($x:expr) => {
        $x * 2
    };
}

fn main() {
    let _ = dobra!();
}
```

```text
error: unexpected end of macro invocation
```

> [!info] Exportando macros
> Em bibliotecas, use `#[macro_export]` (a macro vai para a raiz do crate) e `$crate::caminho` dentro dela para referenciar itens do próprio crate com segurança.

> [!tip] Depuração
> `cargo expand` (ferramenta externa) mostra o código gerado; `compile_error!("mensagem")` permite emitir erros claros em ramos inválidos.

## Exercício

Escreva a macro `minimo!` análoga a `maximo!`, aceitando 1 ou mais expressões.

## Veja também

- [[Macros procedurais]]
- [[Quando usar e evitar macros]]
- [[Macros básicas]]
