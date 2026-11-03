---
titulo: "std::unordered_map e std::unordered_set"
tags: [cpp, stl, conteineres]
aliases: ["std::unordered_map", "std::unordered_set", "Tabela hash", "std::hash", "Hash map"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[map e set]]", "[[Complexidade e Invalidação de Iteradores]]", "[[Escolhendo um Contêiner]]"]
---

# `std::unordered_map` e `std::unordered_set`

> [!info] Introdução
> **C++11.** Implementados como **tabelas hash** com encadeamento por *buckets*. Busca/inserção/remoção em **O(1) médio** e O(n) no pior caso. **Sem ordem** definida.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>

int main() {
    std::unordered_map<std::string, int> estoque;
    estoque["maçã"] = 10;
    estoque.emplace("pera", 4);
    estoque.try_emplace("uva", 7);

    if (auto it = estoque.find("pera"); it != estoque.end())
        std::cout << it->first << ' ' << it->second << '\n';

    std::cout << estoque.contains("kiwi") << '\n';        // 0 (C++20)
    std::cout << estoque.size() << ' ' << estoque.bucket_count() << ' ' << estoque.load_factor() << '\n';

    std::unordered_set<int> vistos;
    for (int x : {3, 1, 3, 2, 1})
        if (!vistos.insert(x).second)                      // insert devolve {iterador, inseriu?}
            std::cout << "duplicado: " << x << '\n';

    estoque.reserve(1000);                                 // evita rehash durante inserções
}
```

## Quando preferir `unordered_*` a `map/set`

| Critério | `unordered_*` | `map`/`set` |
|---|---|---|
| Busca média | **O(1)** | O(log n) |
| Ordem de iteração | Arbitrária | Por chave |
| Consultas por intervalo (`lower_bound`) | Não | **Sim** |
| Chave | Precisa de `hash` e `==` | Precisa de `<` |
| Pior caso | O(n) (colisões) | O(log n) garantido |
| Memória | Alta (buckets + nós) | Alta (nós) |

## Hash e igualdade para tipos próprios

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <functional>
#include <iostream>
#include <unordered_set>

struct Ponto {
    int x, y;
    bool operator==(const Ponto&) const = default;        // igualdade
};

template <>
struct std::hash<Ponto> {                                 // especialização de std::hash
    std::size_t operator()(const Ponto& p) const noexcept {
        std::size_t h1 = std::hash<int>{}(p.x);
        std::size_t h2 = std::hash<int>{}(p.y);
        return h1 ^ (h2 + 0x9e3779b97f4a7c15ULL + (h1 << 6) + (h1 >> 2));   // combinação de hashes
    }
};

int main() {
    std::unordered_set<Ponto> s{{1, 2}, {3, 4}, {1, 2}};
    std::cout << s.size() << '\n';                        // 2
}
```

> [!danger] Contrato de hash
> Dois objetos **iguais** (`==`) **devem** produzir o **mesmo hash**. Violar isso quebra o contêiner (UB). O inverso não vale: hashes iguais para objetos diferentes são colisões (permitidas).

## Desempenho e armadilhas

- **Rehash**: quando `load_factor` excede `max_load_factor` (padrão 1.0), a tabela cresce e **todos os iteradores são invalidados** (referências/ponteiros a elementos continuam válidos).
- **Chaves maliciosas** podem causar colisões em massa (ataque de complexidade): em serviços expostos considere hashes com sementes aleatórias (bibliotecas como abseil).
- `std::unordered_map` da biblioteca padrão é **lento** comparado a *flat hash maps* de terceiros (abseil `flat_hash_map`, `boost::unordered_flat_map`) por usar nós separados.

> [!tip] Use `reserve`
> `m.reserve(n)` antes de inserir `n` elementos evita *rehashes* repetidos.

## Veja também

- [[map e set]]
- [[Complexidade e Invalidação de Iteradores]]
- [[Escolhendo um Contêiner]]
- [[Especialização de Templates]]

## Exercício

1. Implemente `std::hash` para `struct Pessoa { std::string nome; int idade; }` e use-a em um `unordered_map`.
2. Meça inserção de 1 milhão de inteiros aleatórios em `map` vs `unordered_map`, com e sem `reserve`.
