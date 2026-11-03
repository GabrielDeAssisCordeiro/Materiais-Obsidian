---
titulo: "std::map e std::set"
tags: [cpp, stl, conteineres]
aliases: ["std::map", "std::set", "multimap", "multiset", "Contêineres ordenados", "Árvore rubro-negra"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[unordered_map e unordered_set]]", "[[Complexidade e Invalidação de Iteradores]]", "[[Escolhendo um Contêiner]]"]
---

# `std::map` e `std::set`

Contêineres **ordenados por chave**, tipicamente implementados como **árvores balanceadas** (rubro-negras). Busca, inserção e remoção: **O(log n)**. A iteração percorre na ordem das chaves.

| Tipo | Guarda | Chaves duplicadas? |
|---|---|---|
| `std::set<K>` | só chaves | Não |
| `std::multiset<K>` | só chaves | Sim |
| `std::map<K, V>` | pares chave → valor | Não |
| `std::multimap<K, V>` | pares chave → valor | Sim |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <map>
#include <set>
#include <string>

int main() {
    std::map<std::string, int> idades;
    idades["Ana"] = 30;                          // operator[]: insere com valor padrão se não existir
    idades.insert({"Bia", 25});
    idades.emplace("Caio", 41);
    auto [it, inseriu] = idades.insert({"Ana", 99});   // não sobrescreve: inseriu == false
    std::cout << inseriu << it->second << '\n';        // 030

    idades.insert_or_assign("Ana", 31);          // C++17: insere ou atualiza
    idades.try_emplace("Dani", 22);              // C++17: não constrói se a chave já existe

    if (auto f = idades.find("Bia"); f != idades.end())
        std::cout << f->first << " tem " << f->second << '\n';

    std::cout << idades.count("Zé") << idades.contains("Ana") << '\n';   // 01 (contains: C++20)

    for (const auto& [nome, idade] : idades)     // ordem alfabética
        std::cout << nome << '=' << idade << ' ';
    std::cout << '\n';

    idades.erase("Bia");                         // por chave

    std::set<int> s{5, 1, 3, 3, 1};              // {1, 3, 5}: sem duplicatas
    s.insert(4);
    auto lb = s.lower_bound(3);                  // primeiro >= 3
    auto ub = s.upper_bound(3);                  // primeiro > 3
    std::cout << *lb << *ub << '\n';             // 34
}
```

## Cuidado com `operator[]`

> [!warning] `m[chave]` **insere** se não existir
> Ler com `operator[]` cria uma entrada com valor padrão. Para só consultar use `find`, `at` (lança se ausente) ou `contains`. `operator[]` não existe em `const map`.

## Comparador personalizado

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <cctype>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <string>

struct SemCaso {                                  // compara strings ignorando maiúsculas (simplificado)
    bool operator()(const std::string& a, const std::string& b) const {
        auto low = [](unsigned char c) { return std::tolower(c); };
        return std::lexicographical_compare(a.begin(), a.end(), b.begin(), b.end(),
                                            [&](char x, char y) { return low(x) < low(y); });
    }
};

int main() {
    std::set<int, std::greater<>> decrescente{3, 1, 2};    // ordem decrescente
    for (int x : decrescente) std::cout << x;               // 321
    std::cout << '\n';

    std::map<std::string, int, SemCaso> m;
    m["Ana"] = 1;
    m["ana"] = 2;                                           // mesma chave para o comparador
    std::cout << m.size() << '\n';                          // 1
}
```

O comparador deve definir uma **ordem fraca estrita** (irreflexiva, transitiva); caso contrário, comportamento indefinido.

## Busca heterogênea (C++14/20)

Com comparador transparente (`std::less<>`), `m.find("texto")` evita criar um `std::string` temporário.

## Complexidade e propriedades

| Operação | Custo |
|---|---|
| `find`, `insert`, `erase`, `count` | O(log n) |
| Iteração completa | O(n), em ordem |
| `lower_bound`/`upper_bound`/`equal_range` | O(log n) |
| Invalidação | Iteradores/referências **só** do elemento apagado |

> [!tip] Extração de nós (C++17)
> `auto nh = m.extract("Ana");` remove o nó **sem realocar**, permite mudar a chave (`nh.key() = ...`) e reinserir em outro contêiner (`m2.insert(std::move(nh))`).

## Veja também

- [[unordered_map e unordered_set]]
- [[flat_map e flat_set]]
- [[Complexidade e Invalidação de Iteradores]]
- [[Escolhendo um Contêiner]]
- [[Structured Bindings]]

## Exercício

1. Leia nomes e telefones e, com `std::map`, imprima-os em ordem alfabética; use `find` para consultas.
2. Use `lower_bound` em um `std::set<int>` para achar o menor elemento maior ou igual a x.
