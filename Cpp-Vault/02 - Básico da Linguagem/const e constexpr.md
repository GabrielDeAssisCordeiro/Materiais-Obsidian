---
titulo: "const e constexpr"
tags: [cpp, basico, const, constexpr]
aliases: ["const", "Constantes"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Variáveis e Inicialização]]", "[[auto e decltype]]", "[[Funções - Cpp]]"]
---

# `const` e `constexpr`

> [!info] Introdução
> `const` existe desde o C++98. `constexpr` surgiu no **C++11** (funções limitadas), foi ampliado no **C++14** (laços e variáveis locais) e continua evoluindo (C++20: `constexpr` em mais partes da biblioteca; C++23/26 ampliam ainda mais).

## `const`: "não modifique"

`const` impede modificações **por aquele nome**. O valor pode ser conhecido apenas em tempo de execução.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    const int idade = 30;        // inicialização obrigatória
    // idade = 31;               // erro: atribuição a variável const

    int x = 1, y = 2;
    const int* p1 = &x;          // ponteiro para const int: não altera *p1; pode apontar para outro
    int* const p2 = &x;          // ponteiro const: não muda o destino; pode alterar *p2
    const int* const p3 = &x;    // nenhum dos dois

    p1 = &y;                     // ok
    *p2 = 10;                    // ok
    std::cout << idade << ' ' << *p1 << ' ' << *p2 << ' ' << *p3 << '\n';   // 30 2 10 10
}
```

> [!tip] Leia da direita para a esquerda
> `const int* p` → "p é ponteiro para int const". `int* const p` → "p é const ponteiro para int". `const` aplica-se ao que está imediatamente à sua esquerda (ou à direita, se nada estiver à esquerda).

### *const correctness*

Marque como `const` tudo que não deve mudar: variáveis, parâmetros por referência e métodos de classes que não modificam o objeto. Isso documenta a intenção e permite otimizações.

## `constexpr`: "pode ser calculado em tempo de compilação"

- **Variável `constexpr`**: valor conhecido em tempo de compilação (implica `const`).
- **Função `constexpr`**: *pode* ser avaliada em compilação (se os argumentos forem constantes) **ou** em execução.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>

constexpr int fatorial(int n) {          // C++14: laços permitidos
    int r = 1;
    for (int i = 2; i <= n; ++i) r *= i;
    return r;
}

constexpr int f5 = fatorial(5);          // calculado na compilação
static_assert(f5 == 120, "fatorial errado");

int main() {
    std::array<int, fatorial(4)> arr{};  // tamanho 24 precisa ser constante de compilação
    std::cout << f5 << ' ' << arr.size() << '\n';   // 120 24

    int n = 6;
    std::cout << fatorial(n) << '\n';    // 720: argumento em runtime, avaliado em execução
}
```

## `const` vs `constexpr`

| | `const` | `constexpr` |
|---|---|---|
| Valor conhecido na compilação? | Não necessariamente | **Sim** |
| Pode ser usado como tamanho de array / argumento de template | Só se inicializado com constante | Sim |
| Funções | Não se aplica (usa-se em métodos para marcar *this* como const) | Função avaliável em compilação |
| Inicialização | Obrigatória | Obrigatória, com expressão constante |

## Parentes próximos

| Palavra-chave | Padrão | Significado |
|---|---|---|
| `consteval` | C++20 | Função que **deve** ser avaliada em compilação ("função imediata") |
| `constinit` | C++20 | Garante inicialização constante de variável estática, mas ela continua mutável |
| `if constexpr` | C++17 | `if` decidido em compilação (muito usado com templates) |
| `static_assert` | C++11 | Verificação em tempo de compilação |

> [!info] Mais detalhes
> `consteval`, `constinit` e `if constexpr` são aprofundados na seção de templates e metaprogramação deste vault.

## Boas práticas

- Padrão: declare variáveis como `const` e só remova o `const` se precisar modificar.
- Use `constexpr` para constantes numéricas em vez de `#define`.
- Em cabeçalhos, use `inline constexpr` (C++17) para constantes compartilhadas ([[Argumentos Padrão e inline]]).

> [!bug] Exemplo inválido proposital
> ```cpp
> int n = 5;
> constexpr int dobro = n * 2;   // erro: n não é constante de compilação
> ```
> **Correção:** declare `constexpr int n = 5;`.

## Veja também

- [[Variáveis e Inicialização]]
- [[auto e decltype]]
- [[Funções - Cpp]]
- [[Argumentos Padrão e inline]]

## Exercício

1. Escreva uma função `constexpr` que calcula o n-ésimo número de Fibonacci e valide `fib(10) == 55` com `static_assert`.
2. Explique a diferença entre `const int* p` e `int* const p`.
