---
tags: [rust, crates]
aliases: []
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Strings String vs str]]", "[[LazyLock e OnceLock]]"]
---

# regex

O crate **regex** implementa expressões regulares com **tempo linear** (sem backtracking catastrófico).

```toml
[dependencies]
regex = "1"
```

```rust
// requer crate: regex
use regex::Regex;

fn main() {
    // r"..." (raw string) evita escapar barras
    let re = Regex::new(r"(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})").unwrap();
    let texto = "Entrega em 2026-10-24 e revisão em 2026-11-02.";

    println!("{}", re.is_match(texto));

    // Primeira ocorrência com grupos nomeados
    if let Some(c) = re.captures(texto) {
        println!("{} / {} / {}", &c["dia"], &c["mes"], &c["ano"]);
    }

    // Todas as ocorrências
    for m in re.find_iter(texto) {
        println!("{} em {}..{}", m.as_str(), m.start(), m.end());
    }

    // Substituição com referências aos grupos
    println!("{}", re.replace_all(texto, "$dia/$mes/$ano"));
}
```

> [!warning] Compile uma vez
> `Regex::new` é custoso. Não o chame dentro de laços; guarde em `static` com [[LazyLock e OnceLock]].

> [!info] Limitações
> Não há *backreferences* nem *lookaround* no crate `regex` (para isso existe `fancy-regex`).

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/regex antes de copiar para um projeto.

## Veja também

- [[Strings String vs str]]
- [[LazyLock e OnceLock]]
