---
titulo: "Referências universais e *perfect forwarding*"
tags: [cpp, move, templates]
aliases: ["Referências universais", "Forwarding references", "Perfect forwarding", "Reference collapsing", "emplace"]
tipo: conceito
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[std move e std forward]]", "[[Lvalue e Rvalue]]", "[[auto e decltype]]"]
---

# Referências universais e *perfect forwarding*

## Referência universal (*forwarding reference*)

`T&&` é uma **referência universal** apenas quando `T` é **deduzido** pelo compilador (parâmetro de template ou `auto&&`). Ela se liga a **lvalues e rvalues**.

```cpp
template <typename T> void f(T&& x);   // universal: T deduzido
void g(std::string&& x);               // NÃO universal: só rvalue
template <typename T> void h(std::vector<T>&& x);   // NÃO universal: forma diferente de T&&
auto&& r = expr;                       // universal
```

### Dedução

| Argumento | `T` deduzido | Tipo do parâmetro `T&&` |
|---|---|---|
| lvalue `int x` | `int&` | `int&` |
| lvalue `const int x` | `const int&` | `const int&` |
| rvalue `int{}`/`42` | `int` | `int&&` |

## Colapso de referências

Referência a referência é colapsada: **`&` sempre vence**.

| Combinação | Resultado |
|---|---|
| `T& &` | `T&` |
| `T& &&` | `T&` |
| `T&& &` | `T&` |
| `T&& &&` | `T&&` |

## *Perfect forwarding*

Encaminhar argumentos preservando categoria **e** `const`, sem sobrecargas para cada combinação.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <string>
#include <utility>

struct Pessoa {
    Pessoa(std::string nome, int idade) : nome(std::move(nome)), idade(idade) {
        std::cout << "construída: " << this->nome << '\n';
    }
    std::string nome;
    int idade;
};

// Fábrica genérica: repassa os argumentos exatamente como recebeu
template <typename T, typename... Args>
std::unique_ptr<T> fabrica(Args&&... args) {
    return std::unique_ptr<T>(new T(std::forward<Args>(args)...));   // forward em cada elemento do pacote
}

int main() {
    std::string nome = "Ana";
    auto p1 = fabrica<Pessoa>(nome, 30);                    // nome: lvalue -> copiado
    auto p2 = fabrica<Pessoa>(std::string("Bia"), 25);      // rvalue -> movido
    std::cout << p1->idade + p2->idade << '\n';             // 55
}
```

É exatamente o que fazem `std::make_unique`, `std::make_shared`, `emplace_back` e `std::construct_at`.

## Armadilhas

> [!bug] Sobrecarga com referência universal "engole" tudo
> ```cpp
> template <typename T> void log(T&&);      // universal: match perfeito para quase qualquer tipo
> void log(int);                            // preferida para int rvalue, mas para 'int&' ou 'long', a template vence!
> ```
> Restrinja com **concepts** (`requires`) ou `std::enable_if` — seção de templates.

> [!warning] Construtor universal em classes
> `template<class T> Classe(T&&)` pode ser escolhido no lugar do construtor de cópia ao copiar um objeto não-`const` (match melhor com `Classe&`). Restrinja o template.

> [!info] `auto&&` e `decltype(auto)` em lambdas genéricas
> `[](auto&&... args) { return f(std::forward<decltype(args)>(args)...); }` é o idioma para *forwarding* em lambdas. C++23 oferece `std::forward_like` para casos relacionados.

## Resumo de uso

| Quer... | Use |
|---|---|
| Aceitar qualquer categoria e **repassar** | `template<class T> void f(T&& x) { g(std::forward<T>(x)); }` |
| Aceitar qualquer categoria e **só ler** | `const T&` |
| Tomar posse de uma cópia ou movimento | Parâmetro por valor + `std::move` |
| Apenas rvalues | `T&&` com `T` concreto |

## Veja também

- [[std move e std forward]]
- [[Lvalue e Rvalue]]
- [[make_unique e make_shared]]
- [[Semântica de Movimento]]

## Exercício

1. Implemente `template<class F, class... A> decltype(auto) chama(F&& f, A&&... a)` com *perfect forwarding* e teste com uma função que recebe `std::string&&`.
2. Explique por que `void f(std::vector<T>&&)` não é uma referência universal.
