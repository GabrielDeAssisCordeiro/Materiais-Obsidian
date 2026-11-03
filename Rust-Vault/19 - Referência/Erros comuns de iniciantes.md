---
tags: [rust, referencia, erros, iniciante]
aliases: ["Pegadinhas de iniciante", "Erros de quem está começando"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Tabela de erros do compilador]]", "[[Erros comuns do borrow checker]]", "[[Strings String vs str]]", "[[Shadowing]]", "[[Option e Result]]"]
---

# Erros comuns de iniciantes

Os tropeços mais frequentes de quem começa em Rust, com o erro, a explicação e a correção.

## 1. Usar um valor depois de movê-lo

```rust
// ❌ NÃO COMPILA
fn main() {
    let nome = String::from("Ana");
    let outro = nome;
    println!("{nome}");
}
```

```text
error[E0382]: borrow of moved value: `nome`
```

**Por quê:** `String` não é `Copy`; `let outro = nome` transfere o ownership.
**Correção:** emprestar (`let outro = &nome;`) ou clonar (`nome.clone()`). Veja [[Move, Copy e Clone]].

## 2. Esquecer o `mut`

```rust
// ❌ NÃO COMPILA
fn main() {
    let contador = 0;
    contador += 1;
    println!("{contador}");
}
```

```text
error[E0384]: cannot assign twice to immutable variable `contador`
```

**Correção:** `let mut contador = 0;`. Veja [[Variáveis e mutabilidade]].

## 3. Indexar uma `String` por posição

```rust
// ❌ NÃO COMPILA
fn main() {
    let s = String::from("olá");
    let c = s[0];
    println!("{c}");
}
```

```text
error[E0277]: the type `str` cannot be indexed by `{integer}`
```

**Por quê:** strings são UTF-8; `á` ocupa 2 bytes, então "o 1º caractere" não é um índice de byte.
**Correção:**

```rust
fn main() {
    let s = String::from("olá");
    let primeiro = s.chars().next(); // Some('o')
    let terceiro = s.chars().nth(2); // Some('á')
    let fatia = &s[0..1];            // "o" (só em limites de caractere!)
    println!("{primeiro:?} {terceiro:?} {fatia}");
}
```

Veja [[Strings String vs str]].

## 4. Misturar tipos numéricos

```rust
// ❌ NÃO COMPILA
fn main() {
    let a: i32 = 5;
    let b: i64 = 10;
    println!("{}", a + b);
}
```

```text
error[E0308]: mismatched types
```

**Correção:** conversão explícita: `i64::from(a) + b` (sem perda) ou `a as i64 + b`. Veja [[Conversão entre tipos]].

## 5. Ponto e vírgula no final de uma expressão de retorno

```rust
// ❌ NÃO COMPILA
fn quadrado(x: i32) -> i32 {
    x * x;
}

fn main() {
    println!("{}", quadrado(3));
}
```

```text
error[E0308]: mismatched types: expected `i32`, found `()`
```

**Correção:** remova o `;` (o último valor sem `;` é o retorno). Veja [[Expressões vs instruções]].

## 6. `match` que não cobre todos os casos

```rust
// ❌ NÃO COMPILA
enum Cor {
    Vermelho,
    Verde,
    Azul,
}

fn nome(c: Cor) -> &'static str {
    match c {
        Cor::Vermelho => "vermelho",
        Cor::Verde => "verde",
    }
}

fn main() {
    println!("{}", nome(Cor::Azul));
}
```

```text
error[E0004]: non-exhaustive patterns: `Cor::Azul` not covered
```

**Correção:** cobrir `Cor::Azul`. Evite `_` quando quiser que o compilador avise ao adicionar variantes novas. Veja [[match]].

## 7. Devolver referência para variável local

```rust
// ❌ NÃO COMPILA
fn saudacao() -> &str {
    let s = String::from("oi");
    &s
}

fn main() {
    println!("{}", saudacao());
}
```

```text
error[E0106]: missing lifetime specifier
```

**Correção:** devolva o valor: `fn saudacao() -> String`. Veja [[Lifetimes]].

## 8. `unwrap()` por todo lado (compila, mas é frágil)

```rust
fn parse_idade(s: &str) -> Result<u8, std::num::ParseIntError> {
    s.trim().parse::<u8>() // propaga o erro ao chamador
}

fn main() {
    // em vez de: parse_idade("abc").unwrap()  // panic!
    match parse_idade("abc") {
        Ok(i) => println!("idade {i}"),
        Err(e) => println!("entrada inválida: {e}"),
    }
}
```

`unwrap`/`expect` são ótimos em protótipos e testes, mas em código real prefira `?` e `match`. Veja [[Operador de interrogação]] e [[Boas práticas de tratamento de erros]].

## 9. `.clone()` para "calar" o borrow checker

```rust
fn soma(v: &[i32]) -> i32 {
    v.iter().sum() // empresta uma fatia: sem clone
}

fn main() {
    let v = vec![1, 2, 3];
    // ruim: soma(&v.clone())  -> cópia desnecessária
    println!("{}", soma(&v));
    println!("{v:?}");
}
```

Clonar não é pecado, mas é um **sinal**: pergunte se emprestar resolve. Receba `&[T]` e `&str` nos parâmetros em vez de `Vec<T>` e `String`.

## 10. Esperar herança

Rust não tem herança de classes. Use **composição** (campos) e **traits** (comportamento compartilhado). Veja [[Traits]] e [[Rust vs C, C++, Go, Python e Java]].

> [!tip] Leia a mensagem inteira
> O compilador do Rust costuma sugerir a correção (`help:`). Antes de pesquisar na internet, leia o erro até o final.

## Veja também

- [[Tabela de erros do compilador]]
- [[Erros comuns do borrow checker]]
- [[Strings String vs str]]
- [[Shadowing]]
- [[Option e Result]]
