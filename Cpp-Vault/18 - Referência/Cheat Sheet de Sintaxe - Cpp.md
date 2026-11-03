---
titulo: "Cheat Sheet de Sintaxe - Cpp"
tags: [cpp, referencia, cheat-sheet, sintaxe]
aliases: ["Cheat sheet sintaxe", "Folha de consulta C++"]
tipo: referencia
nivel: iniciante
padrao: C++23
criado: 2026-10-24
relacionados: ["[[Glossário#C++]]", "[[Tipos Fundamentais]]", "[[Funções - Cpp]]"]
---

# Cheat Sheet de Sintaxe - Cpp

Referência rápida (C++11 → C++23). Cada bloco compila com `g++ -std=c++20` salvo indicação.

## Estrutura mínima, tipos e inicialização

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

int main() {
    int a = 1;  int b{2};  auto c = 3.5;  const double pi = 3.14159;    // =, {} (sem narrowing), auto, const
    constexpr int N = 10;                                                 // constante em compilação
    std::int64_t grande = 1LL << 40;  unsigned u = 7u;  char ch = 'x';  bool ok = true;
    std::string s = "texto";  std::vector<int> v{1, 2, 3};
    int* p = &a;  int& r = a;  const int* pc = p;  int* const cp = p;     // ponteiro, referência, const

    if (a < b && ok) { /* ... */ } else if (!ok) { /* ... */ } else { /* ... */ }
    for (int i = 0; i < N; ++i) { if (i == 3) continue; if (i == 8) break; }
    for (const auto& x : v) std::cout << x;                               // range-for
    while (a < 5) ++a;
    do { --a; } while (a > 0);
    switch (b) { case 1: break; case 2: [[fallthrough]]; default: break; }
    auto [x, y] = std::pair{1, 2};                                        // structured binding
    auto t = a > b ? a : b;                                               // ternário
    (void)grande; (void)u; (void)ch; (void)pi; (void)c; (void)s; (void)r; (void)pc; (void)cp; (void)x; (void)y; (void)t;
}
```

## Funções, lambdas e classes

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <utility>

int soma(int a, int b = 0) { return a + b; }                              // argumento padrão
auto dobro(int x) -> int { return 2 * x; }                                 // retorno à direita
template <typename T> T maior(T a, T b) { return a > b ? a : b; }          // template
void incrementa(int& x) { ++x; }                                           // por referência
constexpr int fat(int n) { return n <= 1 ? 1 : n * fat(n - 1); }

class Pessoa {
public:
    Pessoa() = default;
    explicit Pessoa(std::string n, int i = 0) : nome_{std::move(n)}, idade_{i} {}   // lista de inicialização
    virtual ~Pessoa() = default;
    const std::string& nome() const { return nome_; }                      // método const
    static int contagem() { return 0; }
protected:
    std::string nome_;
    int idade_ = 0;                                                         // inicializador de membro
};

class Aluno : public Pessoa {
public:
    using Pessoa::Pessoa;                                                   // herda construtores
    void apresentar() const { std::cout << nome() << '\n'; }
};

int main() {
    auto lam = [&](int x) { return x + soma(1, 2); };                       // lambda com captura por referência
    int n = 0; incrementa(n);
    Aluno a{"Ana"};
    a.apresentar();
    std::cout << lam(1) << dobro(4) << maior(2, 9) << fat(5) << n << '\n';
}
```

## Operadores e precedência (resumo)

| Maior → menor precedência | Operadores |
|---|---|
| 1 | `::` |
| 2 | `a++ a-- () [] . ->` |
| 3 | `++a --a +a -a ! ~ (T) * & sizeof new delete` |
| 4–5 | `* / %` depois `+ -` |
| 6 | `<< >>` |
| 7 | `<=>` (C++20) |
| 8 | `< <= > >=` depois `== !=` |
| 9–11 | `&` depois `^` depois `\|` |
| 12–13 | `&&` depois `\|\|` |
| 14 | `?: = += -= ...` (direita para esquerda) |
| 15 | `,` |

## Categorias de especificadores e palavras-chave úteis

| Palavra | Uso |
|---|---|
| `const` | Imutável |
| `constexpr` / `consteval` / `constinit` | Compilação |
| `static` | Duração estática / membro da classe / linkage interna |
| `extern` | Declaração de entidade definida em outra TU |
| `inline` | Várias definições idênticas permitidas |
| `mutable` | Membro modificável em método `const` |
| `explicit` | Sem conversão implícita |
| `override` / `final` | Controle de virtuais |
| `noexcept` | Não lança exceção |
| `[[nodiscard]]` | Avisa se o retorno é ignorado |
| `[[maybe_unused]]` | Evita aviso de não utilizado |
| `[[likely]]` / `[[unlikely]]` | Dicas de ramo (C++20) |

## Veja também

- [[Tipos Fundamentais]]
- [[Operadores - Cpp]]
- [[Cheat Sheet da STL]]
- [[Cheat Sheet de Templates]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Sem olhar, escreva uma classe `Retangulo` com construtor, método `area() const` e comparação `operator==`.
2. Converta um laço `for` clássico para range-for e depois para `std::ranges::for_each`.
