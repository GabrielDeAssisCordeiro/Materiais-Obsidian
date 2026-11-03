---
tags: [rust, colecoes]
aliases: ["Vec<T>", "vetor", "lista dinâmica"]
tipo: tipo-de-dado
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Escolhendo uma coleção]]", "[[Iteradores]]", "[[Arrays]]", "[[Slices]]", "[[Ordenação e busca]]"]
---

# Vec

`Vec<T>` é um vetor **redimensionável** que guarda elementos contíguos na heap. É a coleção padrão.

```rust
fn main() {
    let mut v: Vec<i32> = Vec::new();
    v.push(1);
    v.push(2);
    v.extend([3, 4, 5]);

    let mut w = vec![10, 20, 30];     // macro vec!
    let zeros = vec![0u8; 4];         // [0, 0, 0, 0]

    // Acesso: [] causa panic fora do limite; get devolve Option
    println!("{} {:?} {:?}", v[0], v.get(2), v.get(99));

    // Remoção e inserção
    v.pop();            // remove o último
    v.insert(0, 99);    // insere no índice 0 (O(n))
    v.remove(1);        // remove o índice 1 (O(n))
    v.retain(|x| x % 2 == 1); // mantém só os ímpares
    println!("{:?}", v);

    // Mutação por iteração
    for x in &mut w {
        *x += 1;
    }
    println!("{:?} {:?}", w, zeros);

    // Capacidade
    let mut grande = Vec::with_capacity(100);
    grande.push(1u8);
    println!("len={} cap>=100: {}", grande.len(), grande.capacity() >= 100);

    // Vetores "heterogêneos" com enum
    #[derive(Debug)]
    enum Celula {
        Inteiro(i32),
        Texto(String),
    }
    let linha = vec![Celula::Inteiro(1), Celula::Texto("a".to_string())];
    println!("{:?}", linha);
}
```

## Métodos úteis

| Método | Uso |
|---|---|
| `len`, `is_empty` | tamanho |
| `first`, `last` | `Option<&T>` |
| `contains(&x)` | busca linear |
| `sort`, `dedup`, `reverse` | ordenação e limpeza |
| `drain(a..b)` | remove e itera um intervalo |
| `windows(n)`, `chunks(n)` | janelas e blocos sobre slices |
| `split_at(i)` | divide em dois slices |
| `truncate`, `clear` | encurtar/esvaziar |
| `extend_from_slice` | acrescenta cópia de um slice |

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5];
    for janela in v.windows(2) {
        print!("{} ", janela[1] - janela[0]);
    }
    println!();
    for bloco in v.chunks(2) {
        print!("{:?} ", bloco);
    }
    println!();
}
```

> [!warning] Referências e realocação
> Guardar `&v[0]` e depois fazer `v.push(...)` não compila: o push pode realocar. Veja [[Regras do borrow checker]].

## Exercício

Dado `vec![5, 3, 8, 1]`, remova os números pares e ordene o resultado.

## Veja também

- [[Escolhendo uma coleção]]
- [[Iteradores]]
- [[Arrays]]
- [[Slices]]
- [[Ordenação e busca]]
