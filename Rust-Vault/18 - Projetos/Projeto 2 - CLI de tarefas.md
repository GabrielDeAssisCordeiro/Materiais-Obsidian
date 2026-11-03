---
tags: [rust, projeto, iniciante, cli, io]
aliases: ["Todo CLI"]
tipo: projeto
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[CLI com Rust]]", "[[Erros customizados]]", "[[Conversão de erros com From]]", "[[Operador de interrogação]]", "[[Vec]]", "[[Structs]]", "[[Enums]]", "[[Testes unitários]]"]
---

# Projeto 2 - CLI de tarefas

## Objetivos

Uma ferramenta de linha de comando para gerenciar uma lista de tarefas persistida em arquivo texto:

```bash
tarefas add Comprar pão
tarefas list
tarefas done 1
tarefas rm 1
```

**Você vai praticar:** `std::env::args`, leitura/escrita de arquivos, `struct`, enum de erros próprio, `From` + `?`, `ExitCode` e testes com arquivos temporários.

## Estrutura

```text
tarefas/
├── Cargo.toml
└── src/
    └── main.rs
```

O arquivo `tarefas.txt` guarda uma tarefa por linha, no formato `id<TAB>feita<TAB>título`.

## Código completo

```rust
use std::env;
use std::fmt;
use std::fs;
use std::io;
use std::path::Path;
use std::process::ExitCode;

const ARQUIVO: &str = "tarefas.txt";

#[derive(Debug, Clone, PartialEq)]
struct Tarefa {
    id: u32,
    feita: bool,
    titulo: String,
}

// ---------- Erros ----------

#[derive(Debug)]
enum Erro {
    Io(io::Error),
    IdInvalido(String),
    NaoEncontrada(u32),
    Uso(&'static str),
}

impl fmt::Display for Erro {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Erro::Io(e) => write!(f, "erro de E/S: {e}"),
            Erro::IdInvalido(s) => write!(f, "'{s}' não é um id válido"),
            Erro::NaoEncontrada(id) => write!(f, "tarefa {id} não encontrada"),
            Erro::Uso(msg) => write!(f, "uso: tarefas {msg}"),
        }
    }
}

impl std::error::Error for Erro {}

// Permite usar `?` em funções que devolvem io::Result dentro de Result<_, Erro>
impl From<io::Error> for Erro {
    fn from(e: io::Error) -> Self {
        Erro::Io(e)
    }
}

// ---------- Persistência ----------

fn parse_linha(linha: &str) -> Option<Tarefa> {
    let mut partes = linha.splitn(3, '\t');
    let id = partes.next()?.parse().ok()?;
    let feita = partes.next()? == "1";
    let titulo = partes.next()?.to_string();
    Some(Tarefa { id, feita, titulo })
}

fn carregar(caminho: &Path) -> Result<Vec<Tarefa>, Erro> {
    match fs::read_to_string(caminho) {
        Ok(texto) => Ok(texto.lines().filter_map(parse_linha).collect()),
        // Arquivo ainda não existe: lista vazia
        Err(e) if e.kind() == io::ErrorKind::NotFound => Ok(Vec::new()),
        Err(e) => Err(e.into()),
    }
}

fn salvar(caminho: &Path, tarefas: &[Tarefa]) -> io::Result<()> {
    let texto: String = tarefas
        .iter()
        .map(|t| format!("{}\t{}\t{}\n", t.id, if t.feita { 1 } else { 0 }, t.titulo))
        .collect();
    fs::write(caminho, texto)
}

// ---------- Comandos ----------

fn parse_id(arg: Option<&String>) -> Result<u32, Erro> {
    let s = arg.ok_or(Erro::Uso("done|rm <id>"))?;
    s.parse().map_err(|_| Erro::IdInvalido(s.clone()))
}

/// Executa um comando e devolve o texto a imprimir (facilita os testes).
fn executar(args: &[String], caminho: &Path) -> Result<String, Erro> {
    let mut tarefas = carregar(caminho)?;

    match args.first().map(String::as_str) {
        Some("add") => {
            let titulo = args[1..].join(" ");
            if titulo.trim().is_empty() {
                return Err(Erro::Uso("add <título>"));
            }
            let id = tarefas.iter().map(|t| t.id).max().unwrap_or(0) + 1;
            tarefas.push(Tarefa { id, feita: false, titulo });
            salvar(caminho, &tarefas)?;
            Ok(format!("tarefa {id} adicionada"))
        }
        Some("list") => {
            if tarefas.is_empty() {
                return Ok("nenhuma tarefa".to_string());
            }
            let linhas: Vec<String> = tarefas
                .iter()
                .map(|t| format!("[{}] {:>3}  {}", if t.feita { "x" } else { " " }, t.id, t.titulo))
                .collect();
            Ok(linhas.join("\n"))
        }
        Some("done") => {
            let id = parse_id(args.get(1))?;
            let tarefa = tarefas
                .iter_mut()
                .find(|t| t.id == id)
                .ok_or(Erro::NaoEncontrada(id))?;
            tarefa.feita = true;
            salvar(caminho, &tarefas)?;
            Ok(format!("tarefa {id} concluída"))
        }
        Some("rm") => {
            let id = parse_id(args.get(1))?;
            let antes = tarefas.len();
            tarefas.retain(|t| t.id != id);
            if tarefas.len() == antes {
                return Err(Erro::NaoEncontrada(id));
            }
            salvar(caminho, &tarefas)?;
            Ok(format!("tarefa {id} removida"))
        }
        _ => Err(Erro::Uso("add <título> | list | done <id> | rm <id>")),
    }
}

fn main() -> ExitCode {
    let args: Vec<String> = env::args().skip(1).collect();
    match executar(&args, Path::new(ARQUIVO)) {
        Ok(saida) => {
            println!("{saida}");
            ExitCode::SUCCESS
        }
        Err(e) => {
            eprintln!("erro: {e}");
            ExitCode::FAILURE
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn args(v: &[&str]) -> Vec<String> {
        v.iter().map(|s| s.to_string()).collect()
    }

    fn arquivo_temp(nome: &str) -> std::path::PathBuf {
        let mut p = env::temp_dir();
        p.push(format!("tarefas_teste_{}_{}.txt", nome, std::process::id()));
        let _ = fs::remove_file(&p);
        p
    }

    #[test]
    fn fluxo_completo() {
        let p = arquivo_temp("fluxo");
        assert_eq!(executar(&args(&["list"]), &p).unwrap(), "nenhuma tarefa");
        executar(&args(&["add", "Comprar", "pão"]), &p).unwrap();
        executar(&args(&["add", "Estudar Rust"]), &p).unwrap();
        executar(&args(&["done", "1"]), &p).unwrap();

        let lista = executar(&args(&["list"]), &p).unwrap();
        assert!(lista.contains("[x]   1  Comprar pão"));
        assert!(lista.contains("[ ]   2  Estudar Rust"));

        executar(&args(&["rm", "1"]), &p).unwrap();
        assert!(!executar(&args(&["list"]), &p).unwrap().contains("Comprar"));
        let _ = fs::remove_file(&p);
    }

    #[test]
    fn erros() {
        let p = arquivo_temp("erros");
        assert!(matches!(executar(&args(&["done", "9"]), &p), Err(Erro::NaoEncontrada(9))));
        assert!(matches!(executar(&args(&["done", "x"]), &p), Err(Erro::IdInvalido(_))));
        assert!(matches!(executar(&args(&[]), &p), Err(Erro::Uso(_))));
        assert!(matches!(executar(&args(&["add"]), &p), Err(Erro::Uso(_))));
    }
}
```

## Como funciona

- **Separação de responsabilidades:** `carregar`/`salvar` (E/S), `executar` (lógica, devolve `String`) e `main` (imprime e converte em código de saída). Isso torna a lógica testável sem capturar `stdout`.
- **`Erro` + `From<io::Error>`:** o `?` converte automaticamente erros de E/S no seu tipo; veja [[Conversão de erros com From]] e [[Erros customizados]].
- **`Option` em `parse_linha`:** o `?` também funciona com `Option`, abortando a função com `None`.

## Extensões

- [ ] Usar o crate [[clap]] para subcomandos e `--help` automáticos.
- [ ] Armazenar em JSON com [[serde e serde_json]].
- [ ] Prioridades e datas de vencimento (struct com mais campos).
- [ ] Comando `edit <id> <novo título>` e `clear` para remover as concluídas.
- [ ] Respeitar a variável de ambiente `TAREFAS_ARQUIVO` para escolher o arquivo.

## Exercício

Adicione o comando `list --pendentes` que mostra somente as tarefas não concluídas, com um teste que o cubra.

## Veja também

- [[CLI com Rust]]
- [[Erros customizados]]
- [[Conversão de erros com From]]
- [[Operador de interrogação]]
- [[Vec]]
- [[Structs]]
- [[Enums]]
- [[Testes unitários]]
