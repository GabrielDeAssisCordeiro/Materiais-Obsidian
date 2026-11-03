---
titulo: "Conversões e casts"
tags: [cpp, basico, conversoes]
aliases: ["Casts", "static_cast", "dynamic_cast", "const_cast", "reinterpret_cast", "Conversões implícitas"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Tipos Fundamentais]]", "[[Operadores - Cpp]]", "[[const e constexpr]]"]
---

# Conversões e casts

## Conversões implícitas

O compilador converte tipos automaticamente em vários contextos:

| Tipo de conversão | Exemplo |
|---|---|
| **Promoção integral** | `char`/`short` → `int` em expressões |
| **Conversão aritmética usual** | `int + double` → `double`; `int + unsigned` → `unsigned` |
| **Narrowing (estreitamento)** | `double` → `int`, `long` → `short` (perda de informação) |
| **Para `bool`** | Qualquer escalar não nulo → `true` |
| **Ponteiro** | `T*` → `void*`, `Derivada*` → `Base*`, array → ponteiro (*decay*) |

> [!bug] Armadilha: signed vs unsigned
> Em `-1 < 1u` o `-1` é convertido para `unsigned` (vira um número enorme), então o resultado é **falso**. `-Wall -Wextra` emite `-Wsign-compare`. Em C++20, use `std::cmp_less` e afins (`<utility>`).

## Os quatro casts do C++ (e o cast de C)

| Cast | Uso | Verificação |
|---|---|---|
| `static_cast<T>(x)` | Conversões "razoáveis" entre tipos relacionados (numéricos, `void*`, base↔derivada sem checagem) | Em compilação |
| `dynamic_cast<T>(x)` | Descida/lateral em hierarquias **polimórficas** (com `virtual`) | Em execução (RTTI); `nullptr`/`std::bad_cast` em falha |
| `const_cast<T>(x)` | Adiciona/remove `const`/`volatile` | Nenhuma |
| `reinterpret_cast<T>(x)` | Reinterpreta bits (ponteiro↔inteiro, ponteiros de tipos não relacionados) | Nenhuma |
| `(T)x` (estilo C) | Tenta `const_cast`, `static_cast`, `reinterpret_cast`... | Evite |
| `std::bit_cast<T>(x)` (C++20, `<bit>`) | Reinterpretar representação de bits de forma **definida** (mesmo tamanho, trivialmente copiável) | Em compilação |

> [!tip] Regra de ouro
> Se precisar de um cast, procure antes uma solução de projeto melhor. Quando for inevitável, use o **mais específico** (e fácil de achar com busca) — nunca o cast de estilo C.

## `static_cast`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <utility>

int main() {
    double d = 3.99;
    int i = static_cast<int>(d);               // trunca em direção a zero: 3
    std::cout << i << '\n';

    int a = 7, b = 2;
    double media = static_cast<double>(a) / b; // sem o cast: divisão inteira (3)
    std::cout << media << '\n';                // 3.5

    int neg = -1;
    unsigned pos = 1;
    std::cout << std::cmp_less(neg, pos) << '\n';   // 1: comparação segura (C++20)
}
```

## `dynamic_cast`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Base { virtual ~Base() = default; };          // virtual => tipo polimórfico
struct Derivada : Base { void oi() const { std::cout << "oi da Derivada\n"; } };
struct Outra : Base {};

int main() {
    Derivada d;
    Outra o;
    Base* p1 = &d;
    Base* p2 = &o;

    if (auto* pd = dynamic_cast<Derivada*>(p1)) pd->oi();         // sucesso
    if (auto* pd = dynamic_cast<Derivada*>(p2)) pd->oi();         // falha: nullptr, não entra
    else std::cout << "p2 não é Derivada\n";
}
```

## `const_cast` e `reinterpret_cast`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <iostream>

void imprime_legado(char* s) { std::cout << s << '\n'; }   // API antiga que não usa const, mas só lê

int main() {
    const char* msg = "olá";
    imprime_legado(const_cast<char*>(msg));   // OK somente porque a função NÃO modifica

    int x = 42;
    auto endereco = reinterpret_cast<std::uintptr_t>(&x);   // ponteiro -> inteiro
    std::cout << (endereco != 0) << '\n';                    // 1
}
```

> [!danger] Modificar um objeto originalmente `const` via `const_cast` é UB
> ```cpp
> const int k = 10;
> *const_cast<int*>(&k) = 20;   // COMPORTAMENTO INDEFINIDO
> ```
> `const_cast` serve para chamar APIs mal declaradas, **não** para burlar constância.

## `std::bit_cast` (C++20)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <bit>
#include <cstdint>
#include <iostream>

int main() {
    static_assert(sizeof(float) == sizeof(std::uint32_t));
    float f = 1.0f;
    auto bits = std::bit_cast<std::uint32_t>(f);          // bits IEEE 754 de 1.0f
    std::cout << std::hex << bits << '\n';                // 3f800000
}
```

> [!bug] "Type punning" com `reinterpret_cast` viola *strict aliasing*
> ```cpp
> float f = 1.0f;
> std::uint32_t u = *reinterpret_cast<std::uint32_t*>(&f);   // UB (aliasing)
> ```
> **Correção:** `std::bit_cast` (C++20) ou `std::memcpy`.

## Veja também

- [[Tipos Fundamentais]]
- [[Operadores - Cpp]]
- [[const e constexpr]]
- [[auto e decltype]]

## Exercício

1. Explique por que `int r = 7 / 2 * 2.0;` vale 6 e não 7, e reescreva com `static_cast` para obter 7.
2. Quando `dynamic_cast<Derivada*>` retorna `nullptr` e quando lança exceção?
