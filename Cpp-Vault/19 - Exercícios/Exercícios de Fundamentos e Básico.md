---
titulo: "Exercícios de Fundamentos e Básico"
tags: [cpp, exercicios, fundamentos, basico]
aliases: []
tipo: exercicio
nivel: iniciante
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Básico da Linguagem - Cpp]]", "[[MOC - Fundamentos - Cpp]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de Fundamentos e Básico

> [!tip] Como usar
> Tente resolver **antes** de olhar o gabarito. Compile com `g++ -std=c++20 -Wall -Wextra`. Teoria: [[Funções - Cpp]], [[Controle de Fluxo]], [[const e constexpr]], [[Sobrecarga de Funções]].

## 1. FizzBuzz

Escreva `std::string fizzbuzz(int n)`: devolve `"Fizz"` se `n` é múltiplo de 3, `"Buzz"` se de 5, `"FizzBuzz"` se de ambos, senão o número em texto. Imprima de 1 a 15.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

std::string fizzbuzz(int n) {
    if (n % 15 == 0) return "FizzBuzz";
    if (n % 3 == 0) return "Fizz";
    if (n % 5 == 0) return "Buzz";
    return std::to_string(n);
}

int main() {
    for (int i = 1; i <= 15; ++i) std::cout << fizzbuzz(i) << ' ';
    std::cout << '\n';
}
```

## 2. Temperatura em tempo de compilação

Crie `constexpr double celsius_para_f(double c)` e verifique com `static_assert` que 100 °C = 212 °F.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

constexpr double celsius_para_f(double c) { return c * 9.0 / 5.0 + 32.0; }

static_assert(celsius_para_f(100.0) == 212.0);
static_assert(celsius_para_f(0.0) == 32.0);

int main() { std::cout << celsius_para_f(36.5) << '\n'; }
```

## 3. Inverter dígitos

Escreva `long long inverter(long long n)` que inverte os dígitos (`1234 → 4321`) usando `%` e `/`, tratando números negativos.

> [!tip]- Dica
> Trabalhe com o valor absoluto e reaplique o sinal no fim.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

long long inverter(long long n) {
    const bool neg = n < 0;
    if (neg) n = -n;
    long long r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return neg ? -r : r;
}

int main() { std::cout << inverter(1234) << ' ' << inverter(-905) << '\n'; }   // 4321 -509
```

## 4. Sobrecarga e argumento padrão

Crie `area(double raio)` (círculo), `area(double l, double a)` (retângulo) e `area(double l, double a, bool triangulo = false)`. Qual problema surge? Corrija.

> [!bug] Ambiguidade
> `area(2.0, 3.0)` casa com as duas últimas sobrecargas. O compilador recusa (*ambiguous call*). A solução é eliminar a redundância:

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <numbers>

constexpr double area(double raio) { return std::numbers::pi * raio * raio; }
constexpr double area(double l, double a, bool triangulo = false) {
    return triangulo ? l * a / 2.0 : l * a;
}

int main() {
    std::cout << area(1.0) << ' ' << area(2.0, 3.0) << ' ' << area(2.0, 3.0, true) << '\n';
}
```

## Veja também

- [[Funções - Cpp]]
- [[Controle de Fluxo]]
- [[const e constexpr]]
- [[Sobrecarga de Funções]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Reescreva o exercício 1 devolvendo `std::string_view` para os casos fixos. Por que o caso numérico não pode devolver `string_view`? (veja [[string_view]]).
