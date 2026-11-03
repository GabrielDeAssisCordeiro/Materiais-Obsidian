---
tags: [rust, referencia, comparacao]
aliases: ["Rust para quem vem de outras linguagens", "Tradução de conceitos", "Rosetta"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Rust vs C, C++, Go, Python e Java]]", "[[Traits]]", "[[Option e Result]]", "[[Ownership e regras]]", "[[Casos de uso do Rust]]"]
---

# Conceitos equivalentes em outras linguagens

Uma tabela de "tradução" para acelerar quem já programa em outra linguagem. Para uma comparação mais ampla de filosofia e desempenho, veja [[Rust vs C, C++, Go, Python e Java]].

| Conceito | Python | Java | C++ | Go | **Rust** |
|---|---|---|---|---|---|
| Ausência de valor | `None` | `null` | ponteiro nulo / `optional` | `nil` | `Option<T>` |
| Erros | exceções | exceções | exceções/códigos | `error` retornado | `Result<T, E>` e `?` |
| Memória | GC | GC | manual / RAII | GC | **ownership** + RAII |
| Interface | duck typing / ABC | `interface` | classe abstrata / concepts | `interface` (estrutural) | `trait` |
| Herança | sim | sim | sim | não (embedding) | **não** (composição + traits) |
| Genéricos | tipagem dinâmica | genéricos com *erasure* | templates | genéricos | genéricos monomorfizados |
| Imutabilidade | convenção | `final` | `const` | convenção | **padrão**: precisa de `mut` |
| Enum | `Enum` (simples) | `enum` (simples) | `enum` / `variant` | constantes | **soma de tipos** com dados |
| Pattern matching | `match` (3.10+) | `switch` (modernizando) | `switch` | `switch` | `match` exaustivo |
| Concorrência | threads/asyncio (GIL) | threads | threads | goroutines | threads + `async` + `Send/Sync` |
| Gerenciador de pacotes | pip | Maven/Gradle | CMake/Conan | go mod | **Cargo** |
| Testes | pytest | JUnit | GoogleTest | `testing` | integrados (`#[test]`) |
| Null-safe | não | não | não | não | **sim** |

## A mesma tarefa em duas linguagens

Python:

```python
def media(valores):
    if not valores:
        return None
    return sum(valores) / len(valores)

print(media([1, 2, 3]))
```

Rust:

```rust
fn media(valores: &[f64]) -> Option<f64> {
    if valores.is_empty() {
        None
    } else {
        Some(valores.iter().sum::<f64>() / valores.len() as f64)
    }
}

fn main() {
    println!("{:?}", media(&[1.0, 2.0, 3.0]));
    println!("{:?}", media(&[]));
}
```

> [!info] Diferença-chave
> Em Rust, o *tipo* informa que o resultado pode não existir; quem chama é **obrigado** a tratar o caso `None` antes de usar o valor.

## Armadilhas para quem vem de...

| Origem | Cuidado |
|---|---|
| **Python/JS** | tipos são estáticos; `String` não é `&str`; sem *duck typing* |
| **Java/C#** | sem herança nem `null`; objetos são movidos, não referenciados por padrão |
| **C/C++** | o compilador **recusa** o que você sabe que "funciona"; confie no borrow checker |
| **Go** | sem `nil` interfaces implícitas; erros com `?` em vez de `if err != nil` |

## Veja também

- [[Rust vs C, C++, Go, Python e Java]]
- [[Traits]]
- [[Option e Result]]
- [[Ownership e regras]]
- [[Casos de uso do Rust]]
