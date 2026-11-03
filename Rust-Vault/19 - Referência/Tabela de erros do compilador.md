---
tags: [rust, referencia, erros, compilador]
aliases: ["rustc error index", "E0382"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Erros comuns do borrow checker]]", "[[Erros comuns de iniciantes]]", "[[Regras do borrow checker]]", "[[Lifetimes]]", "[[Trait bounds e where]]"]
---

# Tabela de erros do compilador

O compilador explica seus próprios erros: rode `rustc --explain E0382` (ou `cargo` mostra a dica). Índice oficial: doc.rust-lang.org/error_codes.

> [!question] Verificar na documentação oficial
> O texto exato das mensagens varia entre versões do compilador. Os códigos (`E0xxx`) são estáveis; confira em doc.rust-lang.org/error_codes.

## Ownership, empréstimos e lifetimes

| Código | Mensagem (resumo) | Causa típica | Como resolver |
|---|---|---|---|
| E0382 | borrow of moved value | usou um valor depois de movê-lo | emprestar (`&x`) ou `.clone()` |
| E0499 | cannot borrow as mutable more than once | dois `&mut` simultâneos | um por vez; `split_at_mut` |
| E0502 | cannot borrow as mutable because it is also borrowed as immutable | `&` vivo enquanto pede `&mut` | encurtar o empréstimo `&`; copiar o dado antes |
| E0505 | cannot move out of `x` because it is borrowed | mover com referência ainda em uso | usar a referência antes de mover |
| E0506 | cannot assign to `x` because it is borrowed | atribuir enquanto emprestado | terminar o empréstimo antes |
| E0507 | cannot move out of borrowed content | mover campo/elemento por trás de `&` | `.clone()`, `Option::take`, `mem::replace` |
| E0515 | cannot return reference to local variable | devolver `&` para dado local | devolver o valor (owned) |
| E0597 | borrowed value does not live long enough | dono morre antes da referência | declarar o dono em escopo maior |
| E0716 | temporary value dropped while borrowed | referência a temporário | guardar o valor em uma variável |
| E0106 | missing lifetime specifier | retorno com `&` sem origem clara | anotar `'a` |
| E0373 | closure may outlive the current function | closure em thread/`'static` captura por referência | `move` |
| E0384 | cannot assign twice to immutable variable | faltou `mut` | `let mut` |
| E0596 | cannot borrow as mutable | `&mut` de variável imutável | `let mut` / receber `&mut` |
| E0594 | cannot assign to field of immutable binding | atribuição em campo | `mut` |

## Tipos, traits e genéricos

| Código | Mensagem (resumo) | Causa típica | Como resolver |
|---|---|---|---|
| E0308 | mismatched types | tipos diferentes; `;` no último valor | converter (`as`, `into`); remover `;` |
| E0277 | the trait bound `T: Trait` is not satisfied | tipo sem a trait exigida | `derive`/`impl`; ajustar limites |
| E0599 | no method named `x` found | método inexistente ou trait não importada | `use Trait;` ou revisar o tipo |
| E0282 | type annotations needed | inferência impossível | `::<T>` ou anotar |
| E0369 | binary operation cannot be applied | `+`, `==` sem impl | implementar `Add`/`PartialEq` |
| E0046 | not all trait items implemented | faltou método da trait | implementar |
| E0038 | trait is not dyn compatible (object safe) | método genérico/`Self` em `dyn` | `where Self: Sized`; ver [[Object safety]] |
| E0117 | only traits defined in the current crate can be implemented for types defined outside | [[Orphan rule]] | [[Newtype]] |
| E0392 | type parameter is never used | parâmetro genérico sem uso | `PhantomData` — [[PhantomData]] |
| E0004 | non-exhaustive patterns | `match` sem cobrir todos os casos | adicionar braços ou `_` |
| E0023 / E0026 | número/campos de pattern errados | pattern não casa com a variante | revisar desestruturação |
| E0061 | wrong number of arguments | argumentos faltando/sobrando | corrigir a chamada |

## Nomes, módulos e visibilidade

| Código | Mensagem (resumo) | Causa típica | Como resolver |
|---|---|---|---|
| E0425 | cannot find value in this scope | nome inexistente/typo | declarar ou importar |
| E0412 | cannot find type | tipo não importado | `use` |
| E0432 | unresolved import | caminho errado/crate ausente | corrigir `use`; `cargo add` |
| E0433 | failed to resolve: use of undeclared type or module | módulo não declarado | `mod`, `use`, `Cargo.toml` |
| E0603 | item is private | item sem `pub` | `pub` ou `pub(crate)` |
| E0616 | field is private | campo sem `pub` | expor método de acesso |

## Outros

| Código | Mensagem (resumo) | Causa típica | Como resolver |
|---|---|---|---|
| E0133 | use of unsafe is unsafe | operação `unsafe` fora de bloco | `unsafe { }` e `// SAFETY:` |
| E0015 | cannot call non-const function in constants | função comum em `const` | `const fn` ou `LazyLock` |
| E0658 | use of unstable feature | recurso só da nightly | evitar ou usar nightly |
| E0728 | `await` is only allowed inside `async` | `.await` em função comum | tornar `async` |

## Exemplos reais

```rust
// ❌ NÃO COMPILA: E0382
fn main() {
    let a = String::from("oi");
    let b = a;
    println!("{a} {b}");
}
```

```text
error[E0382]: borrow of moved value: `a`
```

```rust
// ❌ NÃO COMPILA: E0502
fn main() {
    let mut v = vec![1, 2, 3];
    let primeiro = &v[0];
    v.push(4);
    println!("{primeiro}");
}
```

```text
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as immutable
```

```rust
// Correção: terminar de usar a referência antes de mutar
fn main() {
    let mut v = vec![1, 2, 3];
    let primeiro = v[0]; // copia o i32
    v.push(4);
    println!("{primeiro} {v:?}");
}
```

```rust
// ❌ NÃO COMPILA: E0308 (ponto e vírgula no valor de retorno)
fn dobro(x: i32) -> i32 {
    x * 2;
}

fn main() {
    println!("{}", dobro(2));
}
```

```text
error[E0308]: mismatched types
  expected `i32`, found `()`
```

## Veja também

- [[Erros comuns do borrow checker]]
- [[Erros comuns de iniciantes]]
- [[Regras do borrow checker]]
- [[Lifetimes]]
- [[Trait bounds e where]]
