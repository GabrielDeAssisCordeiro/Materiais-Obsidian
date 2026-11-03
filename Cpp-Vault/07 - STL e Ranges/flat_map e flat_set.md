---
titulo: "std::flat_map e std::flat_set (C++23)"
tags: [cpp, stl, cpp23, conteineres]
aliases: ["std::flat_map", "std::flat_set", "flat_multimap", "Mapa plano", "Contêiner associativo plano"]
tipo: conceito
nivel: avancado
padrao: C++23
criado: 2026-10-24
relacionados: ["[[map e set]]", "[[vector]]", "[[Escolhendo um Contêiner]]"]
---

# `std::flat_map` e `std::flat_set` (C++23)

> [!info] Introdução
> **C++23** (`<flat_map>`, `<flat_set>`). Suporte: MSVC 2022 17.x, libstdc++ (GCC 15+), libc++ (versões recentes).
> [!question] Verificar na documentação oficial
> Confirme o suporte no seu compilador e biblioteca padrão (cppreference, *compiler support*). Os exemplos abaixo estão marcados como não verificados porque o ambiente de teste do vault usa GCC 13.

São **adaptadores** que mantêm as chaves (e valores) em **vetores ordenados** (por padrão `std::vector`) em vez de nós de uma árvore.

| Aspecto | `std::map` | `std::flat_map` |
|---|---|---|
| Estrutura | Árvore (nós separados) | Dois vetores contíguos (chaves, valores) |
| Busca | O(log n) | O(log n), com **muito melhor localidade de cache** |
| Iteração | Mais lenta (ponteiros) | **Rápida** (varredura linear) |
| Inserção/remoção | O(log n) | **O(n)** (desloca elementos) |
| Memória | Maior (nós) | Menor |
| Invalidação | Só o apagado | **Qualquer inserção/remoção** pode invalidar tudo |
| Tipo de referência | `pair<const K, V>&` | Referência *proxy* (`pair<const K&, V&>`) |

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra   (requer libstdc++ 15+, MSVC 17.x ou libc++ recente)
#include <flat_map>
#include <iostream>
#include <string>

int main() {
    std::flat_map<std::string, int> m;
    m["c"] = 3;
    m["a"] = 1;
    m.emplace("b", 2);

    for (const auto& [chave, valor] : m)           // ordem das chaves, varredura contígua
        std::cout << chave << '=' << valor << ' ';
    std::cout << '\n';                             // a=1 b=2 c=3

    // Construção em lote: ordenada e sem duplicatas é muito mais barata
    std::vector<std::string> ks{"x", "y"};
    std::vector<int> vs{10, 20};
    std::flat_map<std::string, int> n{std::sorted_unique, ks, vs};   // pré-ordenado: O(1) para montar
    std::cout << n.at("y") << '\n';
}
```

## Quando usar

- Conjunto de dados **carregado uma vez** (ou raramente alterado) e **consultado muito**.
- Mapas **pequenos/médios** onde localidade de cache supera o custo O(n) de inserção.
- Quando a memória importa.

## Quando evitar

- Muitas inserções/remoções aleatórias em contêineres grandes.
- Quando precisa de iteradores/referências **estáveis**.
- Se depende de `node extraction`/`splice` (não existe).

> [!tip] Alternativas anteriores ao C++23
> `boost::container::flat_map` e `abseil::flat_hash_map` (hash) oferecem o mesmo conceito. Em qualquer versão você pode usar `std::vector<std::pair<K,V>>` ordenado + `std::lower_bound`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

// "Flat map" artesanal: vetor ordenado + busca binária
int main() {
    std::vector<std::pair<std::string, int>> v{{"a", 1}, {"b", 2}, {"d", 4}};
    auto cmp = [](const auto& par, const std::string& k) { return par.first < k; };
    auto it = std::lower_bound(v.begin(), v.end(), std::string("b"), cmp);
    if (it != v.end() && it->first == "b") std::cout << it->second << '\n';   // 2
}
```

## Veja também

- [[map e set]]
- [[vector]]
- [[Escolhendo um Contêiner]]
- [[Complexidade e Invalidação de Iteradores]]

## Exercício

1. Compare o tempo de 1 milhão de buscas em `std::map` e no *flat map* artesanal acima para 100 mil chaves.
2. Quais operações de `std::map` não têm equivalente barato em `flat_map` e por quê?
