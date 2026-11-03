---
tags: [rust, ownership, erros]
aliases: ["Erros do compilador sobre ownership", "E0499", "E0502", "E0505"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Regras do borrow checker]]", "[[Move, Copy e Clone]]", "[[Lifetimes]]"]
---

# Erros comuns do borrow checker

| Código | Mensagem (resumida) | Causa | Correção típica |
|---|---|---|---|
| E0382 | borrow of moved value | usou valor depois de movê-lo | `clone()`, emprestar `&`, ou devolver o valor |
| E0499 | cannot borrow as mutable more than once | duas `&mut` simultâneas | restringir o escopo ou reorganizar |
| E0502 | cannot borrow as mutable because also borrowed as immutable | `&` ainda em uso durante `&mut` | terminar o uso antes de mutar |
| E0505 | cannot move out of `x` because it is borrowed | moveu enquanto emprestado | encerrar o empréstimo antes |
| E0506 | cannot assign to `x` because it is borrowed | atribuiu com empréstimo ativo | idem |
| E0597 | `x` does not live long enough | referência sobrevive ao dado | ampliar o escopo do dono |
| E0515 | cannot return reference to local variable | retornou `&` para dado local | retornar o valor (owned) |
| E0106 | missing lifetime specifier | retorno ambíguo | anotar `'a` |
| E0507 | cannot move out of borrowed content | tentou mover de `&T` | `clone()` ou `Option::take()` |
| E0373 | closure may outlive the current function | closure em thread usa referência local | usar `move` |

## Exemplo E0505

```rust
// ❌ NÃO COMPILA
fn main() {
    let s = String::from("a");
    let r = &s;
    let t = s;        // move enquanto r existe
    println!("{r} {t}");
}
```

**Correção:**

```rust
fn main() {
    let s = String::from("a");
    let r = &s;
    println!("{r}"); // r termina aqui
    let t = s;
    println!("{t}");
}
```

## Exemplo E0507

```rust
// ❌ NÃO COMPILA
struct Caixa {
    nome: String,
}

fn main() {
    let c = Caixa { nome: String::from("x") };
    let r = &c;
    let n = r.nome; // não pode mover de trás de uma referência
    println!("{n}");
}
```

**Correção:** `let n = r.nome.clone();` ou `let n = &r.nome;`.

> [!tip] Leia a mensagem inteira
> O compilador mostra onde o valor foi movido, onde foi emprestado e frequentemente sugere a correção em `help:`.

## Veja também

- [[Regras do borrow checker]]
- [[Move, Copy e Clone]]
- [[Lifetimes]]
