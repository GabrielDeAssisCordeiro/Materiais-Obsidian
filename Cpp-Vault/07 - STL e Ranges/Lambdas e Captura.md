---
titulo: "Lambdas e captura"
tags: [cpp, stl, captura, closures]
aliases: ["Lambdas", "Expressões lambda", "Captura de lambda", "Lambdas genéricas", "mutable lambda"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Algoritmos da STL]]", "[[std function e Functors]]", "[[auto e decltype]]"]
---

# Lambdas e captura

> [!info] Evolução
> **C++11**: lambdas. **C++14**: genéricas (`auto`), captura com inicialização. **C++17**: `constexpr` implícito. **C++20**: `[=, this]`, templates (`[]<typename T>`), pacote capturado, lambdas sem estado *default-constructible*. **C++23**: `this` explícito (*deducing this*), `static operator()`.

Uma **lambda** é uma expressão que cria um **objeto-função anônimo** (uma *closure*) no ponto de uso.

```
[captura](parâmetros) especificadores -> retorno { corpo }
```

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    auto soma = [](int a, int b) { return a + b; };            // sem captura, retorno deduzido
    std::cout << soma(2, 3) << '\n';

    std::vector<int> v{5, 2, 8, 1};
    std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });   // lambda como comparador

    int limite = 4;
    auto maior_que = [limite](int x) { return x > limite; };    // captura 'limite' por valor
    std::cout << std::count_if(v.begin(), v.end(), maior_que) << '\n';   // 2
}
```

## Captura

| Sintaxe | Significado |
|---|---|
| `[]` | Nada |
| `[x]` | `x` por **valor** (cópia no momento da criação) |
| `[&x]` | `x` por **referência** |
| `[=]` | Tudo que é usado, por valor |
| `[&]` | Tudo que é usado, por referência |
| `[=, &y]` | Padrão por valor, `y` por referência |
| `[this]` | Ponteiro `this` (por referência ao objeto) |
| `[*this]` | **Cópia** do objeto (C++17) |
| `[x = expr]` | **Init capture** (C++14): cria um membro novo; permite **mover** |
| `[...args]` / `[...args = std::move(args)]` | Pacote de parâmetros (C++20 para init) |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <functional>
#include <iostream>
#include <memory>
#include <string>
#include <utility>

int main() {
    int contador = 0;
    auto inc = [&contador] { ++contador; };      // referência: altera o original
    inc(); inc();
    std::cout << contador << '\n';                // 2

    int x = 10;
    auto copia = [x]() mutable { return ++x; };   // 'mutable' permite alterar a CÓPIA
    std::cout << copia() << copia() << x << '\n'; // 111210  (x original continua 10)

    auto p = std::make_unique<std::string>("move-only");
    auto dono = [p = std::move(p)] { return p->size(); };   // init capture move-only (C++14)
    std::cout << dono() << '\n';                  // 9

    auto generica = [](const auto& a, const auto& b) { return a + b; };   // lambda genérica (C++14)
    std::cout << generica(1, 2) << generica(std::string("a"), std::string("b")) << '\n';   // 3ab

    auto modelo = []<typename T>(T a) { return a * 2; };   // template explícito (C++20)
    std::cout << modelo(21) << '\n';

    // Lambda recursiva (C++14 com std::function; ou C++23 com deducing this)
    std::function<int(int)> fat = [&fat](int n) { return n <= 1 ? 1 : n * fat(n - 1); };
    std::cout << fat(5) << '\n';                  // 120
}
```

## O que é uma lambda por dentro

O compilador gera uma classe com `operator()` e um membro por captura:

```cpp
int limite = 4;
auto f = [limite](int x) { return x > limite; };

// equivale aproximadamente a:
struct __Lambda {
    int limite;                                    // membro capturado
    bool operator()(int x) const { return x > limite; }   // const por padrão (por isso 'mutable')
};
```

Sem captura, a lambda converte em **ponteiro de função** (útil com APIs C).

## Armadilhas de captura

> [!danger] Referência pendente em lambda que escapa
> ```cpp
> std::function<int()> cria() {
>     int local = 42;
>     return [&local] { return local; };     // 'local' morre ao sair: UB ao chamar
> }
> ```
> **Correção:** capture **por valor** (`[local]`) quando a lambda sobrevive ao escopo.

> [!warning] `[=]` não captura `this` por valor (C++20: deprecado implicitamente)
> Dentro de um método, `[=]` captura o **ponteiro `this`**, não uma cópia do objeto: se o objeto morrer antes da lambda, é UB. Use `[*this]` para copiar o objeto, ou `[this]` explícito sabendo do risco.

> [!bug] Capturar variável estática/global não é captura
> Variáveis com duração estática são usadas diretamente, não capturadas.

> [!tip] Prefira captura explícita
> `[&]` e `[=]` escondem dependências. Liste o que usa: `[&soma, limite]`.

## Lambdas vs functors vs `std::function`

| | Lambda | Functor (struct com `operator()`) | `std::function` |
|---|---|---|---|
| Tipo | Anônimo, único | Nomeado | Apagado (tipo-erasure) |
| Desempenho | **Inline**, sem custo | Inline | Indireção + possível alocação |
| Armazenar em variável de tipo fixo | Só com `auto`/template | Sim | **Sim** |

## Veja também

- [[std function e Functors]]
- [[Algoritmos da STL]]
- [[auto e decltype]]
- [[Funções - Cpp]]

## Exercício

1. Escreva uma função `auto contador()` que retorna uma lambda com estado (`mutable`) que devolve 1, 2, 3, ... a cada chamada.
2. Reescreva um `std::sort` com comparador de função livre usando lambda com captura de um vetor de prioridades.
