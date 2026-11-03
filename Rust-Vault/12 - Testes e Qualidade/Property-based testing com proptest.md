---
tags: [rust, testes, crates]
aliases: ["proptest", "property-based testing", "quickcheck", "shrinking"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Testes unitários]]", "[[cargo test]]", "[[Iteradores]]"]
---

# Property-based testing com proptest

Em vez de exemplos fixos, você descreve **propriedades** que devem valer para **qualquer entrada**; a ferramenta gera centenas de casos aleatórios e, ao achar uma falha, **reduz** (*shrinking*) a entrada ao menor contraexemplo.

```toml
[dev-dependencies]
proptest = "1"
```

```rust
// requer crate: proptest
use proptest::prelude::*;

fn inverte(v: &[i32]) -> Vec<i32> {
    v.iter().rev().copied().collect()
}

proptest! {
    // Propriedade: inverter duas vezes devolve o original
    #[test]
    fn inverter_duas_vezes(v in prop::collection::vec(any::<i32>(), 0..100)) {
        prop_assert_eq!(inverte(&inverte(&v)), v);
    }

    // Propriedade: soma é comutativa
    #[test]
    fn soma_comutativa(a in -1000i32..1000, b in -1000i32..1000) {
        prop_assert_eq!(a + b, b + a);
    }

    // Propriedade: ordenar produz saída ordenada com o mesmo tamanho
    #[test]
    fn sort_ordena(mut v in prop::collection::vec(any::<u8>(), 0..50)) {
        let n = v.len();
        v.sort();
        prop_assert_eq!(v.len(), n);
        prop_assert!(v.windows(2).all(|w| w[0] <= w[1]));
    }
}
```

## Propriedades úteis

| Tipo de propriedade | Exemplo |
|---|---|
| Ida e volta | `decode(encode(x)) == x` |
| Idempotência | `normaliza(normaliza(x)) == normaliza(x)` |
| Invariante | resultado de `sort` está ordenado |
| Oráculo | implementação otimizada == implementação simples |
| Não entra em panic | `parse(entrada_qualquer)` não derruba o programa |

> [!tip] Falhas reproduzíveis
> O proptest salva sementes de falhas em `proptest-regressions/`; versione esses arquivos.

## Veja também

- [[Testes unitários]]
- [[cargo test]]
- [[Iteradores]]
