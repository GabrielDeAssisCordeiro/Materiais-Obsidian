---
tags: [rust, exercicios, colecoes, iteradores]
aliases: ["Exercícios de iteradores"]
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Vec]]", "[[HashMap]]", "[[Iteradores]]", "[[Implementando Iterator]]", "[[Exercícios de tipos e pattern matching]]", "[[Exercícios de erros, traits e genéricos]]"]
---

# Exercícios de coleções e iteradores

## Exercícios

1. **Palavras mais frequentes.** `top_palavras(texto, n)` devolve as `n` palavras mais comuns (minúsculas, sem pontuação), desempatando em ordem alfabética.
2. **Anagramas.** `agrupar_anagramas(&["amor", "roma", ...])` agrupa palavras que são anagramas entre si.
3. **Cadeia de iteradores.** Calcule, em uma expressão, a soma dos quadrados dos números pares de 1 a 100.
4. **Fibonacci como `Iterator`.** Implemente `Iterator` para uma struct `Fibonacci` que termina de forma segura ao estourar `u64`.
5. **Deduplicar.** `deduplicar<T>(&[T]) -> Vec<T>` remove repetidos **preservando a ordem** da primeira ocorrência.

Notas relacionadas: [[HashMap]], [[HashSet]], [[Vec]], [[Iteradores]], [[Adaptadores de iterador]], [[Consumidores de iterador]], [[Implementando Iterator]], [[Cheat sheet de iteradores]].

## Gabarito

<details>
<summary>Solução 1</summary>

```rust
use std::collections::HashMap;

fn top_palavras(texto: &str, n: usize) -> Vec<(String, usize)> {
    let mut contagem: HashMap<String, usize> = HashMap::new();
    for p in texto.split_whitespace() {
        let p = p.trim_matches(|c: char| !c.is_alphanumeric()).to_lowercase();
        if !p.is_empty() {
            *contagem.entry(p).or_default() += 1;
        }
    }
    let mut v: Vec<(String, usize)> = contagem.into_iter().collect();
    // mais frequente primeiro; empate: ordem alfabética
    v.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    v.truncate(n);
    v
}

fn main() {
    let r = top_palavras("A casa, a casa! A porta. Porta?", 2);
    assert_eq!(r, vec![("a".to_string(), 3), ("casa".to_string(), 2)]);
    println!("{r:?}");
}
```

</details>
<details>
<summary>Solução 2</summary>

```rust
use std::collections::HashMap;

fn agrupar_anagramas(palavras: &[&str]) -> Vec<Vec<String>> {
    let mut grupos: HashMap<String, Vec<String>> = HashMap::new();
    for p in palavras {
        // Chave: as letras ordenadas. Anagramas têm a mesma chave.
        let mut letras: Vec<char> = p.chars().collect();
        letras.sort_unstable();
        let chave: String = letras.into_iter().collect();
        grupos.entry(chave).or_default().push(p.to_string());
    }
    let mut resultado: Vec<Vec<String>> = grupos.into_values().collect();
    for g in &mut resultado {
        g.sort();
    }
    resultado.sort(); // ordem determinística
    resultado
}

fn main() {
    let r = agrupar_anagramas(&["amor", "roma", "ramo", "gato", "toga", "rato"]);
    assert_eq!(
        r,
        vec![
            vec!["amor", "ramo", "roma"],
            vec!["gato", "toga"],
            vec!["rato"],
        ]
    );
    println!("{r:?}");
}
```

</details>
<details>
<summary>Solução 3</summary>

```rust
fn main() {
    let soma: u32 = (1..=100u32)
        .filter(|n| n % 2 == 0)
        .map(|n| n * n)
        .sum();
    assert_eq!(soma, 171_700);
    println!("{soma}");
}
```

</details>
<details>
<summary>Solução 4</summary>

```rust
struct Fibonacci {
    a: u64,
    b: u64,
}

impl Fibonacci {
    fn novo() -> Self {
        Fibonacci { a: 0, b: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<u64> {
        let atual = self.a;
        // checked_add evita overflow: ao estourar, o iterador termina
        let proximo = self.a.checked_add(self.b)?;
        self.a = self.b;
        self.b = proximo;
        Some(atual)
    }
}

fn main() {
    let primeiros: Vec<u64> = Fibonacci::novo().take(10).collect();
    assert_eq!(primeiros, vec![0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);
    assert_eq!(Fibonacci::novo().take_while(|&n| n < 100).last(), Some(89));
    // termina sozinho em vez de dar panic por overflow
    let total = Fibonacci::novo().count();
    assert!(total > 80 && total < 100);
    println!("{primeiros:?} (a sequência cabe em u64 por {total} termos)");
}
```

</details>
<details>
<summary>Solução 5</summary>

```rust
use std::collections::HashSet;
use std::hash::Hash;

fn deduplicar<T: Eq + Hash + Clone>(v: &[T]) -> Vec<T> {
    let mut vistos = HashSet::new();
    v.iter()
        // insert devolve true se o valor ainda não existia
        .filter(|x| vistos.insert((**x).clone()))
        .cloned()
        .collect()
}

fn main() {
    assert_eq!(deduplicar(&[3, 1, 3, 2, 1, 4]), vec![3, 1, 2, 4]);
    assert_eq!(deduplicar(&["a", "b", "a"]), vec!["a", "b"]);
    assert_eq!(deduplicar::<i32>(&[]), Vec::<i32>::new());
    println!("ok");
}
```

</details>

## Veja também

- [[Vec]]
- [[HashMap]]
- [[Iteradores]]
- [[Implementando Iterator]]
- [[Exercícios de tipos e pattern matching]]
- [[Exercícios de erros, traits e genéricos]]
