---
tags: [rust, projeto, iniciante, cli]
aliases: ["Adivinhação", "Guessing game"]
tipo: projeto
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[loop e break]]", "[[Pattern matching avançado]]", "[[Option e Result]]", "[[Primeiro programa Hello World]]", "[[Testes unitários]]"]
---

# Projeto 1 - Jogo de adivinhação

## Objetivos

Construir um jogo de terminal em que o computador sorteia um número de 1 a 100 e a pessoa tenta adivinhá-lo, recebendo dicas "maior" ou "menor".

**Você vai praticar:** leitura de `stdin`, `loop`, `match`, `enum`, tratamento de entrada inválida com `Result` e testes unitários.

> [!info] Sem dependências
> Para manter o projeto sem crates externos, o número "aleatório" vem de um gerador congruencial linear (LCG) semeado pelo relógio. Na vida real use o crate `rand` (veja [[rand]]).

## Estrutura

```text
adivinhacao/
├── Cargo.toml
└── src/
    └── main.rs
```

```bash
cargo new adivinhacao
cd adivinhacao
# substitua src/main.rs pelo código abaixo
cargo run
cargo test
```

## Código completo

```rust
use std::cmp::Ordering;
use std::io::{self, Write};
use std::time::{SystemTime, UNIX_EPOCH};

/// Gerador pseudoaleatório simples (LCG de Knuth/PCG-like).
struct Lcg(u64);

impl Lcg {
    /// Semeia com o relógio do sistema.
    fn nova() -> Self {
        let semente = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .map(|d| d.as_nanos() as u64)
            .unwrap_or(42);
        Lcg(semente)
    }

    fn proximo(&mut self) -> u64 {
        self.0 = self
            .0
            .wrapping_mul(6364136223846793005)
            .wrapping_add(1442695040888963407);
        self.0 >> 33 // descarta os bits menos aleatórios
    }

    /// Número no intervalo fechado [min, max].
    fn entre(&mut self, min: u32, max: u32) -> u32 {
        min + (self.proximo() % u64::from(max - min + 1)) as u32
    }
}

#[derive(Debug, PartialEq)]
enum Dica {
    Maior,
    Menor,
    Acertou,
}

/// Compara o palpite com o segredo e devolve a dica.
fn avaliar(palpite: u32, segredo: u32) -> Dica {
    match palpite.cmp(&segredo) {
        Ordering::Less => Dica::Maior, // palpite baixo: o segredo é maior
        Ordering::Greater => Dica::Menor,
        Ordering::Equal => Dica::Acertou,
    }
}

/// Converte a linha digitada em número dentro do intervalo.
fn interpretar(linha: &str, min: u32, max: u32) -> Result<u32, String> {
    let n: u32 = linha
        .trim()
        .parse()
        .map_err(|_| format!("'{}' não é um número válido", linha.trim()))?;
    if (min..=max).contains(&n) {
        Ok(n)
    } else {
        Err(format!("digite um número entre {min} e {max}"))
    }
}

fn main() {
    const MIN: u32 = 1;
    const MAX: u32 = 100;

    let segredo = Lcg::nova().entre(MIN, MAX);
    let mut tentativas = 0;

    println!("Adivinhe o número entre {MIN} e {MAX}!");

    loop {
        print!("Seu palpite: ");
        io::stdout().flush().expect("falha ao descarregar stdout");

        let mut linha = String::new();
        // read_line devolve 0 bytes em fim de entrada (Ctrl+D)
        if io::stdin().read_line(&mut linha).expect("falha ao ler") == 0 {
            println!("\nAté mais! O número era {segredo}.");
            return;
        }

        let palpite = match interpretar(&linha, MIN, MAX) {
            Ok(n) => n,
            Err(msg) => {
                println!("⚠️  {msg}");
                continue; // não conta como tentativa
            }
        };

        tentativas += 1;
        match avaliar(palpite, segredo) {
            Dica::Maior => println!("Maior ⬆️"),
            Dica::Menor => println!("Menor ⬇️"),
            Dica::Acertou => {
                println!("🎉 Acertou em {tentativas} tentativa(s)!");
                break;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn dicas_corretas() {
        assert_eq!(avaliar(10, 50), Dica::Maior);
        assert_eq!(avaliar(90, 50), Dica::Menor);
        assert_eq!(avaliar(50, 50), Dica::Acertou);
    }

    #[test]
    fn interpreta_entradas() {
        assert_eq!(interpretar(" 42 \n", 1, 100), Ok(42));
        assert!(interpretar("abc", 1, 100).is_err());
        assert!(interpretar("0", 1, 100).is_err());
        assert!(interpretar("101", 1, 100).is_err());
    }

    #[test]
    fn lcg_respeita_intervalo() {
        let mut g = Lcg(1);
        for _ in 0..1000 {
            let n = g.entre(1, 100);
            assert!((1..=100).contains(&n));
        }
    }
}
```

## Como funciona

1. `Lcg` implementa um gerador; cada chamada a `proximo` atualiza o estado com aritmética *wrapping* (sem pânico em overflow).
2. `interpretar` usa `?` para transformar o erro de `parse` em `String` e valida o intervalo com `RangeInclusive::contains`.
3. O `loop` só termina com `break` (acerto) ou `return` (fim da entrada).

## Extensões

- [ ] Limite de tentativas (ex.: 7) e mensagem de derrota.
- [ ] Níveis de dificuldade (intervalos diferentes) escolhidos por argumento de linha de comando.
- [ ] Trocar o `Lcg` pelo crate `rand` ([[rand]]).
- [ ] Guardar o recorde de menos tentativas em um arquivo.
- [ ] Inverter o jogo: o computador adivinha usando **busca binária**.

## Exercício

Implemente o modo invertido: você pensa em um número e o programa adivinha por busca binária, recebendo "m" (maior), "n" (menor) ou "a" (acertou).

## Veja também

- [[loop e break]]
- [[Pattern matching avançado]]
- [[Option e Result]]
- [[Primeiro programa Hello World]]
- [[Testes unitários]]
