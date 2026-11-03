---
tags: [rust, testes, traits]
aliases: ["mockall", "injeção de dependência", "test double"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Testes unitários]]", "[[impl Trait e dyn Trait]]"]
---

# Mocks e injeção de dependência

Rust não tem mocks mágicos: o caminho idiomático é **depender de traits** e injetar uma implementação falsa nos testes.

```rust
use std::time::{SystemTime, UNIX_EPOCH};

// 1. Abstração para a dependência externa
pub trait Relogio {
    fn hora_utc(&self) -> u64; // 0..=23
}

pub struct RelogioReal;

impl Relogio for RelogioReal {
    fn hora_utc(&self) -> u64 {
        let seg = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
        (seg / 3600) % 24
    }
}

// 2. A lógica depende da trait, não do relógio real
pub fn horario_comercial(r: &impl Relogio) -> bool {
    (9..18).contains(&r.hora_utc())
}

fn main() {
    println!("{}", horario_comercial(&RelogioReal));
}

#[cfg(test)]
mod testes {
    use super::*;

    // 3. Fake controlado pelo teste
    struct Fixo(u64);

    impl Relogio for Fixo {
        fn hora_utc(&self) -> u64 {
            self.0
        }
    }

    #[test]
    fn dentro_do_expediente() {
        assert!(horario_comercial(&Fixo(10)));
    }

    #[test]
    fn fora_do_expediente() {
        assert!(!horario_comercial(&Fixo(22)));
    }
}
```

## Espião (verifica chamadas)

```rust
use std::cell::RefCell;

trait Notificador {
    fn envia(&self, msg: &str);
}

struct Espiao {
    enviadas: RefCell<Vec<String>>,
}

impl Notificador for Espiao {
    fn envia(&self, msg: &str) {
        self.enviadas.borrow_mut().push(msg.to_string());
    }
}

fn processa(n: &dyn Notificador, valor: i32) {
    if valor > 100 {
        n.envia("valor alto");
    }
}

#[cfg(test)]
mod testes {
    use super::*;

    #[test]
    fn notifica_quando_alto() {
        let e = Espiao { enviadas: RefCell::new(vec![]) };
        processa(&e, 500);
        processa(&e, 5);
        assert_eq!(*e.enviadas.borrow(), vec!["valor alto".to_string()]);
    }
}

fn main() {}
```

## Crates de mock

O crate `mockall` gera mocks automaticamente a partir de traits:

```rust
// requer crate: mockall
use mockall::automock;

#[automock]
trait Banco {
    fn busca(&self, id: u32) -> Option<String>;
}

#[test]
fn usa_mock() {
    let mut m = MockBanco::new();
    m.expect_busca().with(mockall::predicate::eq(1)).returning(|_| Some("Ana".into()));
    assert_eq!(m.busca(1), Some("Ana".to_string()));
}
```

> [!tip] Design para testabilidade
> Se algo é difícil de testar, geralmente falta uma fronteira: extraia a dependência (relógio, rede, disco, aleatoriedade) para uma trait.

## Veja também

- [[Traits]]
- [[Testes unitários]]
- [[impl Trait e dyn Trait]]
