---
tags: [rust, exercicios, structs, enums]
aliases: ["Exercícios de enums"]
tipo: exercicio
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Structs]]", "[[Enums]]", "[[Pattern matching avançado]]", "[[Option e Result]]", "[[Exercícios de ownership]]", "[[Exercícios de coleções e iteradores]]"]
---

# Exercícios de tipos e pattern matching

## Exercícios

1. **Retângulo.** Crie `Retangulo` com `novo`, `quadrado` (função associada), `area`, `perimetro` e `cabe_em(&self, outro: &Retangulo)`.
2. **Comandos.** Modele `enum Comando { Mover { dx, dy }, Falar(String), Sair }` e escreva `executar(&mut Estado, Comando)` que atualiza posição, histórico de falas e um flag `ativo`.
3. **Semáforo.** Enum `Semaforo` com `proximo(self)` (ciclo verde → amarelo → vermelho) e `duracao(self)` em segundos.
4. **Quadrantes.** Use `match` com *guards* para classificar um ponto `(i32, i32)` em "origem", "eixo x", "eixo y" ou "1º/2º/3º/4º quadrante".
5. **Option encadeado.** Dada uma lista de usuários com `email: Option<String>`, escreva `dominio_email(usuarios, id) -> Option<&str>` usando `find`, `and_then` e `as_deref`, sem `unwrap`.

Notas relacionadas: [[Structs]], [[Métodos e funções associadas]], [[Enums]], [[Pattern matching avançado]], [[Option e Result]], [[Combinadores de Option e Result]].

## Gabarito

<details>
<summary>Solução 1</summary>

```rust
#[derive(Debug, PartialEq)]
struct Retangulo {
    largura: f64,
    altura: f64,
}

impl Retangulo {
    fn novo(largura: f64, altura: f64) -> Self {
        Retangulo { largura, altura }
    }

    fn quadrado(lado: f64) -> Self {
        Retangulo::novo(lado, lado)
    }

    fn area(&self) -> f64 {
        self.largura * self.altura
    }

    fn perimetro(&self) -> f64 {
        2.0 * (self.largura + self.altura)
    }

    fn cabe_em(&self, outro: &Retangulo) -> bool {
        self.largura <= outro.largura && self.altura <= outro.altura
    }
}

fn main() {
    let r = Retangulo::novo(3.0, 4.0);
    assert_eq!(r.area(), 12.0);
    assert_eq!(r.perimetro(), 14.0);
    assert_eq!(Retangulo::quadrado(2.0), Retangulo::novo(2.0, 2.0));
    assert!(Retangulo::quadrado(2.0).cabe_em(&r));
    assert!(!r.cabe_em(&Retangulo::quadrado(2.0)));
    println!("{r:?}");
}
```

</details>
<details>
<summary>Solução 2</summary>

```rust
#[derive(Debug, Default)]
struct Estado {
    x: i32,
    y: i32,
    falas: Vec<String>,
    ativo: bool,
}

enum Comando {
    Mover { dx: i32, dy: i32 },
    Falar(String),
    Sair,
}

fn executar(e: &mut Estado, c: Comando) {
    match c {
        Comando::Mover { dx, dy } => {
            e.x += dx;
            e.y += dy;
        }
        Comando::Falar(texto) => e.falas.push(texto),
        Comando::Sair => e.ativo = false,
    }
}

fn main() {
    let mut e = Estado { ativo: true, ..Default::default() };
    executar(&mut e, Comando::Mover { dx: 2, dy: -1 });
    executar(&mut e, Comando::Mover { dx: 1, dy: 1 });
    executar(&mut e, Comando::Falar("olá".to_string()));
    assert_eq!((e.x, e.y), (3, 0));
    assert_eq!(e.falas, vec!["olá"]);
    assert!(e.ativo);
    executar(&mut e, Comando::Sair);
    assert!(!e.ativo);
    println!("{e:?}");
}
```

</details>
<details>
<summary>Solução 3</summary>

```rust
#[derive(Debug, Clone, Copy, PartialEq)]
enum Semaforo {
    Verde,
    Amarelo,
    Vermelho,
}

impl Semaforo {
    fn proximo(self) -> Self {
        match self {
            Semaforo::Verde => Semaforo::Amarelo,
            Semaforo::Amarelo => Semaforo::Vermelho,
            Semaforo::Vermelho => Semaforo::Verde,
        }
    }

    fn duracao(self) -> u32 {
        match self {
            Semaforo::Verde => 30,
            Semaforo::Amarelo => 5,
            Semaforo::Vermelho => 25,
        }
    }
}

fn main() {
    let mut s = Semaforo::Verde;
    let mut total = 0;
    for _ in 0..3 {
        total += s.duracao();
        s = s.proximo();
    }
    assert_eq!(s, Semaforo::Verde); // voltou ao início
    assert_eq!(total, 60);
    println!("ciclo completo: {total}s");
}
```

</details>
<details>
<summary>Solução 4</summary>

```rust
fn quadrante(p: (i32, i32)) -> &'static str {
    match p {
        (0, 0) => "origem",
        (_, 0) => "eixo x",
        (0, _) => "eixo y",
        (x, y) if x > 0 && y > 0 => "1º quadrante",
        (x, y) if x < 0 && y > 0 => "2º quadrante",
        (x, y) if x < 0 && y < 0 => "3º quadrante",
        _ => "4º quadrante",
    }
}

fn main() {
    assert_eq!(quadrante((0, 0)), "origem");
    assert_eq!(quadrante((5, 0)), "eixo x");
    assert_eq!(quadrante((0, -2)), "eixo y");
    assert_eq!(quadrante((1, 1)), "1º quadrante");
    assert_eq!(quadrante((-1, 1)), "2º quadrante");
    assert_eq!(quadrante((-1, -1)), "3º quadrante");
    assert_eq!(quadrante((1, -1)), "4º quadrante");
    println!("ok");
}
```

</details>
<details>
<summary>Solução 5</summary>

```rust
struct Usuario {
    id: u32,
    nome: String,
    email: Option<String>,
}

fn buscar(usuarios: &[Usuario], id: u32) -> Option<&Usuario> {
    usuarios.iter().find(|u| u.id == id)
}

fn dominio_email(usuarios: &[Usuario], id: u32) -> Option<&str> {
    buscar(usuarios, id)
        .and_then(|u| u.email.as_deref()) // Option<String> -> Option<&str>
        .and_then(|e| e.split('@').nth(1))
}

fn main() {
    let usuarios = vec![
        Usuario { id: 1, nome: "Ana".into(), email: Some("ana@exemplo.com".into()) },
        Usuario { id: 2, nome: "Bia".into(), email: None },
    ];
    assert_eq!(dominio_email(&usuarios, 1), Some("exemplo.com"));
    assert_eq!(dominio_email(&usuarios, 2), None); // sem e-mail
    assert_eq!(dominio_email(&usuarios, 9), None); // sem usuário
    println!("{} tem domínio {:?}", usuarios[0].nome, dominio_email(&usuarios, 1));
}
```

</details>

## Veja também

- [[Structs]]
- [[Enums]]
- [[Pattern matching avançado]]
- [[Option e Result]]
- [[Exercícios de ownership]]
- [[Exercícios de coleções e iteradores]]
