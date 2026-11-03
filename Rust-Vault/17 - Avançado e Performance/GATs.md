---
tags: [rust, avancado, traits, lifetimes]
aliases: ["Generic Associated Types", "GAT", "LendingIterator", "tipos associados genéricos"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Tipos associados]]", "[[Lifetimes]]", "[[Iteradores]]", "[[Implementando Iterator]]"]
---

# GATs

**GATs** (*Generic Associated Types*, estáveis desde o Rust 1.65) permitem que um tipo associado tenha **parâmetros próprios**, em geral lifetimes. O exemplo clássico é o **iterador que empresta** (*lending iterator*), em que cada item referencia o próprio iterador.

O `Iterator` padrão não consegue isto, pois `Item` não pode depender do lifetime de `&mut self`.

```rust
trait IteradorEmprestador {
    // Item depende do lifetime do empréstimo de self
    type Item<'a>
    where
        Self: 'a;

    fn proximo<'a>(&'a mut self) -> Option<Self::Item<'a>>;
}

// Janelas sobrepostas e mutáveis sobre uma fatia
struct JanelasMut<'s> {
    fatia: &'s mut [i32],
    pos: usize,
    tam: usize,
}

impl<'s> IteradorEmprestador for JanelasMut<'s> {
    type Item<'a>
        = &'a mut [i32]
    where
        Self: 'a;

    fn proximo<'a>(&'a mut self) -> Option<Self::Item<'a>> {
        let fim = self.pos + self.tam;
        if fim > self.fatia.len() {
            return None;
        }
        let janela = &mut self.fatia[self.pos..fim];
        self.pos += 1;
        Some(janela)
    }
}

fn main() {
    let mut v = [1, 2, 3, 4];
    let mut it = JanelasMut { fatia: &mut v, pos: 0, tam: 2 };
    while let Some(j) = it.proximo() {
        j[1] += j[0]; // soma acumulada: janelas se sobrepõem
    }
    println!("{:?}", v); // [1, 3, 6, 10]
}
```

| Sem GAT | Com GAT |
|---|---|
| `Iterator::Item` não pode emprestar de `self` | `type Item<'a>` pode |
| Itens independentes entre si | itens podem se sobrepor (mutáveis) |
| Soluções: copiar/clonar ou `unsafe` | API segura e sem cópias |

> [!tip] Quando usar
> GATs são uma ferramenta de **autores de bibliotecas** (coleções, parsers sem cópia, bancos de dados). No código de aplicação você raramente precisará.

## Veja também

- [[Tipos associados]]
- [[Lifetimes]]
- [[Iteradores]]
- [[Implementando Iterator]]
