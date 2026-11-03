---
titulo: "std::function e functors"
tags: [cpp, stl, std-function]
aliases: ["std::function", "Functors", "Objetos função", "std::bind", "std::invoke", "std::move_only_function", "function_ref"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Lambdas e Captura]]", "[[Algoritmos da STL]]", "[[Sobrecarga de Operadores - Cpp]]"]
---

# `std::function` e functors

## Functor (objeto-função)

Qualquer objeto que define `operator()` pode ser chamado como uma função — e **carregar estado**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

struct MaiorQue {
    int limite;
    bool operator()(int x) const { return x > limite; }      // functor com estado
};

int main() {
    std::vector<int> v{1, 5, 8, 3};
    std::cout << std::count_if(v.begin(), v.end(), MaiorQue{4}) << '\n';   // 2

    // Functors prontos de <functional>
    std::sort(v.begin(), v.end(), std::greater<>{});          // decrescente
    std::cout << std::plus<>{}(2, 3) << std::multiplies<>{}(2, 3) << '\n';   // 56
}
```

## `std::function` (C++11)

Um **invólucro polimórfico** que guarda **qualquer chamável** com uma assinatura fixa (função livre, lambda, functor, método via `std::bind`/lambda) — *type erasure*.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <functional>
#include <iostream>
#include <map>
#include <string>
#include <vector>

int dobro(int x) { return 2 * x; }

struct Triplo { int operator()(int x) const { return 3 * x; } };

class Botao {
public:
    using Callback = std::function<void(const std::string&)>;
    void ao_clicar(Callback cb) { callback_ = std::move(cb); }
    void clicar() { if (callback_) callback_("botão clicado"); }
private:
    Callback callback_;
};

int main() {
    std::function<int(int)> f;
    f = dobro;                        std::cout << f(5) << ' ';          // função livre
    f = Triplo{};                     std::cout << f(5) << ' ';          // functor
    f = [](int x) { return x + 1; };  std::cout << f(5) << '\n';         // lambda -> 10 15 6

    Botao b;
    int cliques = 0;
    b.ao_clicar([&cliques](const std::string& msg) { ++cliques; std::cout << msg << '\n'; });
    b.clicar(); b.clicar();
    std::cout << cliques << '\n';     // 2

    std::map<std::string, std::function<double(double, double)>> ops{
        {"+", std::plus<double>{}}, {"*", std::multiplies<double>{}}};
    std::cout << ops["*"](3, 4) << '\n';   // 12
}
```

## Custos e alternativas

| Característica | `std::function` | Lambda/template (`F&&`) | `std::move_only_function` (C++23) | `std::function_ref` (C++26) |
|---|---|---|---|---|
| Tipo fixo (armazenável em membros/contêineres) | **Sim** | Não | Sim | Sim |
| Chamada | Indireta (sem inline) | **Inline** | Indireta | Indireta |
| Alocação | Possível (se o objeto for grande) | Nenhuma | Possível | **Nenhuma** (não possui) |
| Copiável | Exige chamável copiável | — | Aceita *move-only* | Não possui (view) |
| Vazia → chamar | `std::bad_function_call` | — | UB | — |

> [!tip] Como escolher
> - Recebe um chamável **só durante a chamada**? Use **template** (`template<class F> void f(F&& fn)`) ou `std::function_ref` (C++26).
> - Precisa **guardar** (callbacks, tabelas de comandos)? `std::function` (ou `move_only_function` se o chamável for *move-only*).
> - Em *hot paths*, evite `std::function`.

## `std::invoke` (C++17)

Chama qualquer coisa "chamável" de forma uniforme, inclusive **ponteiros para membro**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <functional>
#include <iostream>
#include <string>

struct Pessoa {
    std::string nome;
    std::size_t tamanho() const { return nome.size(); }
};

int main() {
    Pessoa p{"Ana Maria"};
    std::cout << std::invoke(&Pessoa::tamanho, p) << std::invoke(&Pessoa::nome, p) << '\n';   // 9Ana Maria
    std::cout << std::invoke([](int a, int b) { return a * b; }, 6, 7) << '\n';              // 42
}
```

> [!info] `std::bind`
> `std::bind` (C++11) liga argumentos, mas **lambdas são mais claras** e geralmente mais rápidas. `std::bind_front` (C++20) cobre bem o caso comum.

> [!warning] `std::function` copia o chamável
> Capturas pesadas são copiadas ao copiar a `std::function`. Capture ponteiros/`shared_ptr` ou use `std::ref`.

## Veja também

- [[Lambdas e Captura]]
- [[Algoritmos da STL]]
- [[Sobrecarga de Operadores - Cpp]]
- [[Funções - Cpp]]

## Exercício

1. Implemente uma calculadora com `std::map<std::string, std::function<double(double,double)>>` para `+ - * /`.
2. Compare o tempo de chamar 100 milhões de vezes uma lambda direta e a mesma lambda dentro de uma `std::function`.
