---
tags: [rust, projeto, iniciante, cli, lifetimes]
aliases: ["minigrep", "Busca em arquivos"]
tipo: projeto
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[CLI com Rust]]", "[[Lifetimes]]", "[[Box dyn Error]]", "[[Operador de interrogação]]", "[[Iteradores]]", "[[Testes unitários]]"]
---

# Projeto 3 - Minigrep

## Objetivos

Uma versão simplificada do `grep`: procura um texto em um arquivo e imprime as linhas que o contêm, com número da linha.

```bash
minigrep rust poema.txt
minigrep -i RUST poema.txt        # ignora maiúsculas/minúsculas
IGNORAR_CAIXA=1 minigrep rust poema.txt
```

**Você vai praticar:** lifetimes em funções que devolvem referências ao texto de entrada, `Box<dyn Error>`, variáveis de ambiente, iteradores e TDD.

## Estrutura

```text
minigrep/
├── Cargo.toml
└── src/
    └── main.rs
```

## Código completo

```rust
use std::env;
use std::error::Error;
use std::fs;
use std::process::ExitCode;

struct Config {
    padrao: String,
    caminho: String,
    ignorar_caixa: bool,
}

impl Config {
    fn de_args(args: &[String]) -> Result<Config, &'static str> {
        // A variável de ambiente ativa o modo por padrão; -i também
        let mut ignorar_caixa = env::var("IGNORAR_CAIXA").is_ok();
        let mut posicionais: Vec<&String> = Vec::new();

        for arg in args {
            if arg == "-i" {
                ignorar_caixa = true;
            } else {
                posicionais.push(arg);
            }
        }

        match posicionais.as_slice() {
            [padrao, caminho] => Ok(Config {
                padrao: padrao.to_string(),
                caminho: caminho.to_string(),
                ignorar_caixa,
            }),
            _ => Err("uso: minigrep [-i] <padrão> <arquivo>"),
        }
    }
}

/// Devolve (número da linha, linha) para cada linha que contém `padrao`.
/// O lifetime `'a` diz: as linhas devolvidas vivem tanto quanto `texto`.
fn buscar<'a>(padrao: &str, texto: &'a str) -> Vec<(usize, &'a str)> {
    texto
        .lines()
        .enumerate()
        .filter(|(_, linha)| linha.contains(padrao))
        .map(|(i, linha)| (i + 1, linha))
        .collect()
}

fn buscar_ignorando_caixa<'a>(padrao: &str, texto: &'a str) -> Vec<(usize, &'a str)> {
    let padrao = padrao.to_lowercase();
    texto
        .lines()
        .enumerate()
        .filter(|(_, linha)| linha.to_lowercase().contains(&padrao))
        .map(|(i, linha)| (i + 1, linha))
        .collect()
}

fn executar(config: &Config) -> Result<usize, Box<dyn Error>> {
    let texto = fs::read_to_string(&config.caminho)?;

    let resultados = if config.ignorar_caixa {
        buscar_ignorando_caixa(&config.padrao, &texto)
    } else {
        buscar(&config.padrao, &texto)
    };

    for (n, linha) in &resultados {
        println!("{n}: {linha}");
    }
    Ok(resultados.len())
}

fn main() -> ExitCode {
    let args: Vec<String> = env::args().skip(1).collect();

    let config = match Config::de_args(&args) {
        Ok(c) => c,
        Err(msg) => {
            eprintln!("{msg}");
            return ExitCode::from(2);
        }
    };

    match executar(&config) {
        // Como o grep: 0 = encontrou, 1 = não encontrou
        Ok(0) => ExitCode::from(1),
        Ok(_) => ExitCode::SUCCESS,
        Err(e) => {
            eprintln!("erro ao ler '{}': {e}", config.caminho);
            ExitCode::from(2)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEXTO: &str = "\
Rust é rápido.
Segurança de memória.
rust não tem coletor de lixo.";

    #[test]
    fn diferencia_caixa() {
        assert_eq!(buscar("rust", TEXTO), vec![(3, "rust não tem coletor de lixo.")]);
    }

    #[test]
    fn ignora_caixa() {
        let r = buscar_ignorando_caixa("rust", TEXTO);
        assert_eq!(r.len(), 2);
        assert_eq!(r[0].0, 1);
        assert_eq!(r[1].0, 3);
    }

    #[test]
    fn sem_resultados() {
        assert!(buscar("python", TEXTO).is_empty());
    }

    #[test]
    fn config_valida_argumentos() {
        let ok = vec!["-i".to_string(), "a".to_string(), "b.txt".to_string()];
        assert!(Config::de_args(&ok).unwrap().ignorar_caixa);
        assert!(Config::de_args(&["a".to_string()]).is_err());
    }
}
```

## Como funciona

- **Lifetimes:** `buscar<'a>` devolve fatias de `texto`; o compilador garante que `resultados` não sobreviva a `texto`. Em `executar`, `texto` é uma variável local que vive até o final, logo `resultados` é válido. Veja [[Lifetimes]].
- **`Box<dyn Error>`:** permite que `executar` devolva erros de tipos diferentes (`io::Error` aqui) com `?`; veja [[Box dyn Error]].
- **Códigos de saída** seguem a convenção do `grep`.

## Extensões

- [ ] Contagem de linhas com `-c` e inversão do filtro com `-v`.
- [ ] Buscar em vários arquivos e em diretórios recursivamente (`std::fs::read_dir`).
- [ ] Destacar o trecho encontrado com cores ANSI.
- [ ] Suportar expressões regulares com o crate [[regex]].
- [ ] Ler da entrada padrão quando nenhum arquivo for indicado.

## Exercício

Adicione a opção `-n` para ocultar os números de linha e `-c` para imprimir só a contagem de linhas encontradas.

## Veja também

- [[CLI com Rust]]
- [[Lifetimes]]
- [[Box dyn Error]]
- [[Operador de interrogação]]
- [[Iteradores]]
- [[Testes unitários]]
