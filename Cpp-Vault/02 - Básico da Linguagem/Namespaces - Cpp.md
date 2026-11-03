---
titulo: "Namespaces - Cpp"
tags: [cpp, basico, modulos-e-pacotes]
aliases: ["Namespace", "using namespace", "using declaration", "Namespace alias", "inline namespace"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Escopo e Duração de Armazenamento]]", "[[Entrada e Saída Básica]]", "[[Funções - Cpp]]"]
---

# Namespaces - Cpp

Um **namespace** agrupa nomes para evitar colisões. Toda a biblioteca padrão vive em `std`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

namespace geometria {
    constexpr double pi = 3.14159265358979;
    double area_circulo(double r) { return pi * r * r; }

    namespace detalhes {                // aninhado
        int auxiliar() { return 1; }
    }
}

namespace audio::efeitos {              // namespaces aninhados em uma linha (C++17)
    inline int volume() { return 11; }
}

namespace g = geometria;                // alias de namespace

int area_circulo(int) { return 0; }     // função global com mesmo nome: sem conflito

int main() {
    std::cout << geometria::area_circulo(2.0) << '\n';
    std::cout << g::detalhes::auxiliar() << '\n';
    std::cout << audio::efeitos::volume() << '\n';
    std::cout << ::area_circulo(1) << '\n';       // '::' sozinho = escopo global
}
```

## `using`

| Forma | Efeito | Recomendação |
|---|---|---|
| `using std::cout;` | Traz **um** nome para o escopo atual | Aceitável em `.cpp` e dentro de funções |
| `using namespace std;` | Traz **todos** os nomes | Evite; **nunca** em cabeçalhos |
| `using Alias = Tipo;` | Alias de tipo (substitui `typedef`) | Preferido |
| `namespace curto = nome::longo;` | Alias de namespace | Bom para nomes longos |

> [!bug] Por que evitar `using namespace std;` em cabeçalhos
> Ele contamina **todo arquivo que incluir o cabeçalho**. Se você define `count` ou `distance` e outro código inclui `<algorithm>`, surgem ambiguidades difíceis de rastrear (`std::count` vs `::count`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

int main() {
    using std::vector;                       // escopo de função: seguro
    using Matriz = vector<vector<double>>;   // alias de tipo

    Matriz m(2, vector<double>(2, 1.0));
    std::cout << m[1][1] << '\n';            // 1
}
```

## Namespaces anônimos e `inline`

- `namespace { ... }`: nomes com **ligação interna** (visíveis só na unidade de tradução).
- `inline namespace v2 { ... }`: membros acessíveis como se estivessem no namespace pai; útil para **versionar** APIs e ABI.

## Pesquisa dependente de argumentos (ADL)

Quando uma função é chamada sem qualificação, o compilador também procura no namespace dos **argumentos**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

namespace loja {
    struct Produto { int id; };
    void mostra(const Produto& p) { std::cout << "produto " << p.id << '\n'; }
}

int main() {
    loja::Produto p{7};
    mostra(p);            // ADL encontra loja::mostra por causa do tipo do argumento
}
```

> [!info] ADL e `std::swap`
> O idioma `using std::swap; swap(a, b);` permite que uma sobrecarga específica do tipo (achada por ADL) seja usada, com `std::swap` como padrão.

## Boas práticas

- Use o **nome do projeto** como namespace de nível superior.
- Não coloque nada no namespace `std` (comportamento indefinido, com poucas exceções para especializações).
- Evite namespaces profundos (mais de 2 a 3 níveis).

## Veja também

- [[Escopo e Duração de Armazenamento]]
- [[Entrada e Saída Básica]]
- [[Funções - Cpp]]
- [[Sobrecarga de Funções]]

## Exercício

1. Crie dois namespaces com uma função `saudacao()` cada e chame as duas em `main`.
2. Por que `using namespace std;` em um `.hpp` é considerado má prática?
