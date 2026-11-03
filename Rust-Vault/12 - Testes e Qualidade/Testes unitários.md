---
tags: [rust, testes, qualidade]
aliases: ["#[test]", "#[cfg(test)]", "should_panic", "unit tests"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[cargo test]]", "[[Testes de integração]]", "[[Doc tests]]", "[[Mocks e injeção de dependência]]"]
---

# Testes unitários

Testes unitários vivem **no mesmo arquivo** do código, em um módulo marcado com `#[cfg(test)]` (compilado só em `cargo test`). Isso permite testar também itens privados.

```rust
pub fn soma(a: i32, b: i32) -> i32 {
    a + b
}

pub fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err("divisão por zero".to_string())
    } else {
        Ok(a / b)
    }
}

fn privada(x: i32) -> i32 {
    x * 2
}

#[cfg(test)]
mod testes {
    use super::*; // traz os itens do módulo pai, inclusive privados

    #[test]
    fn soma_basica() {
        assert_eq!(soma(2, 3), 5);
    }

    #[test]
    fn testa_funcao_privada() {
        assert_eq!(privada(4), 8);
    }

    // Testes podem retornar Result: use ? dentro deles
    #[test]
    fn divide_ok() -> Result<(), String> {
        assert_eq!(divide(6, 3)?, 2);
        Ok(())
    }

    #[test]
    fn divide_erro() {
        assert_eq!(divide(1, 0), Err("divisão por zero".to_string()));
    }

    // Espera um panic (opcionalmente com trecho da mensagem)
    #[test]
    #[should_panic(expected = "divisão")]
    fn unwrap_em_erro_entra_em_panico() {
        divide(1, 0).unwrap();
    }

    #[test]
    #[ignore = "demorado: rode com --ignored"]
    fn teste_lento() {
        assert!(true);
    }

    #[test]
    fn mensagem_personalizada() {
        let x = 7;
        assert!(x % 2 == 1, "esperava ímpar, veio {x}");
        assert_ne!(x, 8);
        assert!(matches!(divide(4, 2), Ok(2)));
    }
}
```

## Macros de asserção

| Macro | Falha quando |
|---|---|
| `assert!(cond)` | `cond` é falsa |
| `assert_eq!(a, b)` | `a != b` (mostra os dois valores; exige `Debug + PartialEq`) |
| `assert_ne!(a, b)` | `a == b` |
| `debug_assert!` | só verifica em build de debug |
| `matches!` dentro de `assert!` | valor não casa com o padrão |

> [!tip] Estrutura AAA
> Organize cada teste em **Arrange** (preparar), **Act** (executar) e **Assert** (verificar). Um teste, um comportamento.

> [!info] Isolamento
> Testes rodam em **paralelo**, em threads diferentes. Não compartilhe estado global mutável entre eles.

## Exercício

Escreva testes para uma função `eh_palindromo(&str) -> bool`, incluindo string vazia e maiúsculas.

## Veja também

- [[cargo test]]
- [[Testes de integração]]
- [[Doc tests]]
- [[Mocks e injeção de dependência]]
