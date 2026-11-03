---
tags: [rust, structs, enums]
aliases: ["modelagem de domínio"]
tipo: exemplo
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Structs]]", "[[Enums]]", "[[Métodos e funções associadas]]", "[[Option e Result]]"]
---

# Estruturas aninhadas e modelagem

Exemplo que combina structs, enums, `Option` e métodos: um pequeno modelo de pedidos.

```rust
#[derive(Debug, Clone, PartialEq)]
enum Status {
    Novo,
    Pago { valor_centavos: u64 },
    Enviado { codigo: String },
    Cancelado,
}

#[derive(Debug)]
struct Pedido {
    id: u32,
    cliente: String,
    status: Status,
}

impl Pedido {
    fn novo(id: u32, cliente: &str) -> Self {
        Self { id, cliente: cliente.to_string(), status: Status::Novo }
    }

    fn pagar(&mut self, valor_centavos: u64) -> Result<(), String> {
        match self.status {
            Status::Novo => {
                self.status = Status::Pago { valor_centavos };
                Ok(())
            }
            _ => Err(format!("pedido {} não pode ser pago agora", self.id)),
        }
    }

    fn enviar(&mut self, codigo: &str) -> Result<(), String> {
        if let Status::Pago { .. } = self.status {
            self.status = Status::Enviado { codigo: codigo.to_string() };
            Ok(())
        } else {
            Err(String::from("só pedidos pagos podem ser enviados"))
        }
    }

    fn codigo_rastreio(&self) -> Option<&str> {
        match &self.status {
            Status::Enviado { codigo } => Some(codigo),
            _ => None,
        }
    }
}

fn main() {
    let mut p = Pedido::novo(1, "Ana");
    println!("{:?}", p.enviar("BR123")); // Err
    p.pagar(4990).unwrap();
    p.enviar("BR123").unwrap();
    println!("{:?} {:?}", p.codigo_rastreio(), p.status);
}
```

> [!info] Máquina de estados
> O enum garante que `codigo` só existe quando o estado é `Enviado`. Para validar transições em **tempo de compilação**, veja o padrão typestate em [[Typestate]].

## Veja também

- [[Structs]]
- [[Enums]]
- [[Métodos e funções associadas]]
- [[Option e Result]]
