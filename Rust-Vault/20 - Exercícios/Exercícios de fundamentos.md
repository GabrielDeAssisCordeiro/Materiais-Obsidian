---
tags: [rust, exercicios, fundamentos]
aliases: []
tipo: exercicio
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Variáveis e mutabilidade]]", "[[Funções]]", "[[if e else]]", "[[Cheat sheet de sintaxe]]", "[[Exercícios de ownership]]"]
---

# Exercícios de fundamentos

Escreva cada solução **antes** de abrir o gabarito. Todas as soluções compilam e rodam (`cargo run`) com `assert!`s que as validam.

## Exercícios

1. **FizzBuzz.** Escreva `fizzbuzz(n: u32) -> String`: devolve `"Fizz"` para múltiplos de 3, `"Buzz"` para múltiplos de 5, `"FizzBuzz"` para ambos e o próprio número (como texto) nos demais casos. *Dica:* `match (n % 3, n % 5)`.
2. **Temperatura.** Implemente `c_para_f` e `f_para_c` com `f64` e verifique que converter de ida e volta devolve o valor original (dentro de uma tolerância).
3. **Primos.** Escreva `eh_primo(n: u64) -> bool` e `crivo(limite: usize) -> Vec<usize>` (Crivo de Eratóstenes).
4. **Vogais.** Conte as vogais de um `&str`, inclusive acentuadas, sem diferenciar maiúsculas de minúsculas.
5. **Collatz.** Dado `n >= 1`, conte quantos passos levam até 1 (se par, divida por 2; se ímpar, `3n + 1`).

Notas relacionadas: [[match]], [[while e for]], [[Funções]], [[Strings String vs str]], [[Tipos escalares]].

## Gabarito

<details>
<summary>Solução 1</summary>

```rust
fn fizzbuzz(n: u32) -> String {
    match (n % 3, n % 5) {
        (0, 0) => "FizzBuzz".to_string(),
        (0, _) => "Fizz".to_string(),
        (_, 0) => "Buzz".to_string(),
        _ => n.to_string(),
    }
}

fn main() {
    let saida: Vec<String> = (1..=15).map(fizzbuzz).collect();
    assert_eq!(saida[0], "1");
    assert_eq!(saida[2], "Fizz");
    assert_eq!(saida[4], "Buzz");
    assert_eq!(saida[14], "FizzBuzz");
    println!("{}", saida.join(" "));
}
```

</details>
<details>
<summary>Solução 2</summary>

```rust
fn c_para_f(c: f64) -> f64 {
    c * 9.0 / 5.0 + 32.0
}

fn f_para_c(f: f64) -> f64 {
    (f - 32.0) * 5.0 / 9.0
}

fn main() {
    assert_eq!(c_para_f(100.0), 212.0);
    assert_eq!(f_para_c(32.0), 0.0);
    // Comparar floats com tolerância, nunca com ==
    assert!((f_para_c(c_para_f(37.0)) - 37.0).abs() < 1e-9);
    println!("37 °C = {:.1} °F", c_para_f(37.0));
}
```

</details>
<details>
<summary>Solução 3</summary>

```rust
fn eh_primo(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    let mut d = 2;
    while d * d <= n {
        if n % d == 0 {
            return false;
        }
        d += 1;
    }
    true
}

fn crivo(limite: usize) -> Vec<usize> {
    let mut eh_primo = vec![true; limite + 1];
    let mut primos = Vec::new();
    for i in 2..=limite {
        if eh_primo[i] {
            primos.push(i);
            let mut j = i * i;
            while j <= limite {
                eh_primo[j] = false;
                j += i;
            }
        }
    }
    primos
}

fn main() {
    assert!(eh_primo(97));
    assert!(!eh_primo(1));
    assert!(!eh_primo(91)); // 7 * 13
    assert_eq!(crivo(30), vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29]);
    println!("{:?}", crivo(50));
}
```

</details>
<details>
<summary>Solução 4</summary>

```rust
fn contar_vogais(s: &str) -> usize {
    s.to_lowercase()
        .chars()
        .filter(|c| "aeiouáàâãéêíóôõúü".contains(*c))
        .count()
}

fn main() {
    assert_eq!(contar_vogais("Rust é Rápido"), 5);
    assert_eq!(contar_vogais("RHYTHM"), 0);
    assert_eq!(contar_vogais("ÁÉÍÓÚ"), 5);
    println!("ok");
}
```

</details>
<details>
<summary>Solução 5</summary>

```rust
fn collatz(mut n: u64) -> u32 {
    assert!(n >= 1, "n deve ser positivo (0 nunca chega a 1)");
    let mut passos = 0;
    while n != 1 {
        n = if n % 2 == 0 { n / 2 } else { 3 * n + 1 };
        passos += 1;
    }
    passos
}

fn main() {
    assert_eq!(collatz(1), 0);
    assert_eq!(collatz(6), 8); // 6 3 10 5 16 8 4 2 1
    assert_eq!(collatz(27), 111);
    println!("collatz(27) = {}", collatz(27));
}
```

</details>

## Veja também

- [[Variáveis e mutabilidade]]
- [[Funções]]
- [[if e else]]
- [[Cheat sheet de sintaxe]]
- [[Exercícios de ownership]]
