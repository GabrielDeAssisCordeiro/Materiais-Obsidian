---
tags: [rust, exercicios, ownership, lifetimes]
aliases: ["Exercícios de borrowing"]
tipo: exercicio
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Ownership e regras]]", "[[Borrowing e referências]]", "[[Lifetimes]]", "[[Erros comuns do borrow checker]]", "[[Exercícios de fundamentos]]", "[[Exercícios de tipos e pattern matching]]"]
---

# Exercícios de ownership

## Exercícios

1. **Conserte.** O código abaixo não compila. Corrija **sem** usar `.clone()`.

```rust
// ❌ NÃO COMPILA
fn main() {
    let nomes = vec![String::from("Ana"), String::from("Bia")];
    for n in nomes {
        println!("{n}");
    }
    println!("total: {}", nomes.len());
}
```

```text
error[E0382]: borrow of moved value: `nomes`
```

2. **Inversão no lugar.** Escreva `inverter(s: &mut String)` que inverte os caracteres da própria `String`.
3. **Maior palavra.** Escreva `maior_palavra` que devolve a palavra mais longa de um texto **sem alocar**. Qual assinatura de lifetime ela precisa?
4. **Duas metades.** Escreva uma função que dobre os elementos da primeira metade de uma fatia e zere os da segunda, usando `split_at_mut`. Por que não é possível fazer isso com dois `&mut v[..]` normais?
5. **Struct com referência.** Crie `Trecho<'a>` que guarda um `&'a str` e tem métodos `palavras()` e `primeira()` devolvendo fatias do texto original.

Notas relacionadas: [[Ownership e regras]], [[Borrowing e referências]], [[Lifetimes]], [[Lifetimes em structs]], [[Cheat sheet de ownership]].

## Gabarito

<details>
<summary>Solução 1</summary>

```rust
fn main() {
    let nomes = vec![String::from("Ana"), String::from("Bia")];
    // `for n in nomes` consumia o vetor (into_iter). Emprestar resolve:
    for n in &nomes {
        println!("{n}");
    }
    assert_eq!(nomes.len(), 2);
    println!("total: {}", nomes.len());
}
```

</details>
<details>
<summary>Solução 2</summary>

```rust
fn inverter(s: &mut String) {
    *s = s.chars().rev().collect();
}

fn main() {
    let mut texto = String::from("rust");
    inverter(&mut texto);
    assert_eq!(texto, "tsur");
    println!("{texto}");
}
```

</details>
<details>
<summary>Solução 3</summary>

```rust
// 'a: o resultado é uma fatia do próprio `texto`; vive tanto quanto ele.
fn maior_palavra<'a>(texto: &'a str) -> &'a str {
    texto
        .split_whitespace()
        .max_by_key(|p| p.chars().count())
        .unwrap_or("")
}

fn main() {
    let t = String::from("um dois três quatro");
    let m = maior_palavra(&t);
    assert_eq!(m, "quatro");
    assert_eq!(maior_palavra("   "), "");
    println!("{m}");
}
```

</details>
<details>
<summary>Solução 4</summary>

```rust
// Dois `&mut v[..]` sobrepostos violariam "um &mut por vez".
// `split_at_mut` prova ao compilador que as metades não se sobrepõem.
fn processar(v: &mut [i32]) {
    let meio = v.len() / 2;
    let (primeira, segunda) = v.split_at_mut(meio);
    for x in primeira.iter_mut() {
        *x *= 2;
    }
    for x in segunda.iter_mut() {
        *x = 0;
    }
}

fn main() {
    let mut v = [1, 2, 3, 4];
    processar(&mut v);
    assert_eq!(v, [2, 4, 0, 0]);
    println!("{v:?}");
}
```

</details>
<details>
<summary>Solução 5</summary>

```rust
struct Trecho<'a> {
    texto: &'a str,
}

impl<'a> Trecho<'a> {
    fn novo(texto: &'a str) -> Self {
        Trecho { texto }
    }

    // O retorno usa 'a (o lifetime do texto), não o do empréstimo de &self:
    // assim as fatias podem sobreviver ao `Trecho`.
    fn palavras(&self) -> Vec<&'a str> {
        self.texto.split_whitespace().collect()
    }

    fn primeira(&self) -> Option<&'a str> {
        self.texto.split_whitespace().next()
    }
}

fn main() {
    let dono = String::from("olá mundo rust");
    let primeira = {
        let t = Trecho::novo(&dono);
        assert_eq!(t.palavras().len(), 3);
        t.primeira()
    }; // `t` morreu, mas a fatia aponta para `dono`
    assert_eq!(primeira, Some("olá"));
    println!("{primeira:?}");
}
```

</details>

## Veja também

- [[Ownership e regras]]
- [[Borrowing e referências]]
- [[Lifetimes]]
- [[Erros comuns do borrow checker]]
- [[Exercícios de fundamentos]]
- [[Exercícios de tipos e pattern matching]]
