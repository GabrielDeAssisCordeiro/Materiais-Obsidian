---
tags: [rust, colecoes]
aliases: ["HashMap<K, V>", "dicionário", "mapa hash"]
tipo: tipo-de-dado
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Escolhendo uma coleção]]", "[[BTreeMap]]", "[[HashSet]]", "[[Iteradores]]"]
---

# HashMap

`HashMap<K, V>` associa chaves a valores usando uma tabela hash. A ordem de iteração **não é garantida**. A chave precisa implementar `Eq + Hash`.

```rust
use std::collections::HashMap;

fn main() {
    let mut notas: HashMap<String, u32> = HashMap::new();
    notas.insert("Ana".to_string(), 9);
    notas.insert("Bia".into(), 7);

    // Consulta (aceita &str porque String: Borrow<str>)
    if let Some(n) = notas.get("Ana") {
        println!("Ana: {n}");
    }

    // API entry: insere se não existir / atualiza se existir
    *notas.entry("Ana".to_string()).or_insert(0) += 1;
    notas.entry("Caio".to_string()).or_insert(5);

    // Contagem de palavras (idioma clássico)
    let texto = "a b a c b a";
    let mut contagem: HashMap<&str, usize> = HashMap::new();
    for palavra in texto.split_whitespace() {
        *contagem.entry(palavra).or_insert(0) += 1;
    }
    let mut pares: Vec<_> = contagem.iter().collect();
    pares.sort(); // ordena para saída determinística
    println!("{:?}", pares);

    notas.remove("Bia");
    println!("{}", notas.contains_key("Bia")); // false

    // Construção a partir de um array
    let m = HashMap::from([("a", 1), ("b", 2)]);
    println!("{}", m["a"]); // [] causa panic se a chave não existir
}
```

> [!info] Ownership
> Inserir move chaves e valores para o mapa (tipos `Copy` são copiados). Para guardar referências, os dados precisam viver mais que o mapa.

> [!tip] Hasher
> O hasher padrão (SipHash) resiste a ataques de colisão, mas é mais lento que alternativas como `ahash`/`rustc-hash`, úteis em código crítico.

## Exercício

Conte a frequência de cada letra em "abracadabra" e imprima em ordem alfabética.

## Veja também

- [[Escolhendo uma coleção]]
- [[BTreeMap]]
- [[HashSet]]
- [[Iteradores]]
