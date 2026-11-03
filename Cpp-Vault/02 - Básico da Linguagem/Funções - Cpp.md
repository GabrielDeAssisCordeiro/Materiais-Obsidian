---
titulo: "Funções - Cpp"
tags: [cpp, basico, funcoes]
aliases: ["Passagem de parâmetros", "Retorno de funções", "nodiscard"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Sobrecarga de Funções]]", "[[Argumentos Padrão e inline]]", "[[const e constexpr]]"]
---

# Funções - Cpp

## Declaração vs definição

- **Declaração** (protótipo): diz que a função existe — `int soma(int, int);`
- **Definição**: o corpo — `int soma(int a, int b) { return a + b; }`

Declarações vão em cabeçalhos (`.hpp`); definições, em `.cpp` (veja [[Pipeline de Compilação - Cpp]]).

## Passagem de parâmetros

| Forma | Sintaxe | Quando |
|---|---|---|
| Por valor | `void f(int x)` | Tipos pequenos e baratos (`int`, `double`, ponteiros); quando a função precisa de uma cópia |
| Por referência constante | `void f(const std::string& s)` | Tipos grandes só lidos (padrão) |
| Por referência | `void f(std::vector<int>& v)` | A função **modifica** o argumento do chamador |
| Por ponteiro | `void f(int* p)` | Quando `nullptr` é um valor válido ("opcional") |
| Por valor + `std::move` | `void f(std::string s)` | Função que "toma posse" do argumento |

Regra prática das C++ Core Guidelines (F.16): tipos baratos de copiar por valor; os demais por `const&`.

## Exemplo completo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

int quadrado(int x) { return x * x; }                                       // por valor

void dobrar(std::vector<int>& v) { for (int& x : v) x *= 2; }               // modifica o original

std::size_t tamanho(const std::string& s) { return s.size(); }              // sem cópia

[[nodiscard]] bool valido(int x) { return x > 0; }                          // aviso se ignorar o retorno (C++17)

struct Divisao { int quociente; int resto; };
Divisao dividir(int a, int b) { return {a / b, a % b}; }                    // retorno múltiplo com struct

int contador() { static int n = 0; return ++n; }                            // 'static' local: persiste entre chamadas

auto soma(int a, int b) -> int { return a + b; }                            // trailing return type

using Op = int (*)(int);                                                    // alias de ponteiro de função
int aplica(Op f, int x) { return f(x); }

int main() {
    std::vector<int> v{1, 2, 3};
    dobrar(v);
    std::cout << v[0] << v[1] << v[2] << '\n';                // 246

    auto [q, r] = dividir(17, 5);                             // structured bindings (C++17)
    std::cout << q << ' ' << r << '\n';                       // 3 2

    std::cout << contador() << contador() << '\n';            // 12
    std::cout << aplica(quadrado, 7) << ' ' << soma(2, 3) << ' ' << tamanho("abc") << '\n';   // 49 5 3

    if (valido(3)) std::cout << "válido\n";
    // valido(3);   // com -Wall: warning: ignoring return value (nodiscard)
}
```

## Retornando valores

- Retorne **por valor**: o compilador aplica *copy elision*/RVO e *move* automaticamente, tornando isso barato.
- Para múltiplos valores: `struct` nomeada, `std::pair`, `std::tuple` (com structured bindings).
- **Nunca** retorne referência ou ponteiro para variável local.

> [!danger] Referência pendente (*dangling reference*)
> ```cpp
> int& ruim() {
>     int x = 42;
>     return x;        // x morre ao fim da função: usar o retorno é COMPORTAMENTO INDEFINIDO
> }
> ```
> **Correção:** retorne por valor (`int ruim() { return 42; }`).

## Outros pontos

- **`noexcept`**: promete que a função não lança exceções (`void f() noexcept;`).
- **Recursão**: cada chamada usa a pilha; profundidade excessiva causa *stack overflow*.
- **`main`**: `int main()` ou `int main(int argc, char* argv[])`; o retorno é opcional.
- **Funções são cidadãs de primeira classe** via ponteiros de função, `std::function` e lambdas (veja a seção de STL).

> [!tip] Funções pequenas e com um propósito
> Prefira funções curtas, nomes descritivos e menos de ~4 parâmetros. Agrupe parâmetros relacionados em `struct`.

## Veja também

- [[Sobrecarga de Funções]]
- [[Argumentos Padrão e inline]]
- [[const e constexpr]]
- [[Controle de Fluxo]]

## Exercício

1. Escreva `std::pair<int,int> min_max(const std::vector<int>&)` e use structured bindings no chamador.
2. Qual é o problema de `const std::string& f() { return std::string("x"); }`?
