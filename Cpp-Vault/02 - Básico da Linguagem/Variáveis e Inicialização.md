---
titulo: "Variáveis e inicialização"
tags: [cpp, basico, variaveis, inicializacao]
aliases: ["Variáveis", "Inicialização", "Brace initialization", "Inicialização uniforme"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Tipos Fundamentais]]", "[[auto e decltype]]", "[[const e constexpr]]"]
---

# Variáveis e inicialização

Uma **variável** é um objeto nomeado com tipo e valor. Em C++ existem várias sintaxes de inicialização; entender as diferenças evita bugs.

## As formas de inicializar

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

int main() {
    int a = 1;       // inicialização por cópia (herdada do C)
    int b(2);        // inicialização direta (parênteses)
    int c{3};        // inicialização com chaves (lista) — C++11
    int d = {4};     // cópia com lista
    int e{};         // inicialização por valor: zero
    auto f = 5;      // tipo deduzido: int
    auto g{6};       // C++17: int (em C++11/14 seria initializer_list<int>)

    std::string s1{"abc"};
    std::string s2(3, 'x');   // "xxx" (construtor com contagem)

    std::cout << a << b << c << d << e << f << g << ' ' << s1 << ' ' << s2 << '\n';
}
```

## Por que preferir chaves `{}`

1. **Proíbem conversões que perdem informação (*narrowing*)**.
2. Funcionam para quase tudo (tipos básicos, classes, agregados, contêineres).
3. Evitam a *vexing parse* (`T x();` declara uma função!).

> [!bug] Exemplo inválido proposital: narrowing
> ```cpp
> int i{3.5};          // erro: conversão double -> int por chaves é narrowing
> char c{300};         // erro: 300 não cabe em char
> ```
> **Correção:** `int i = static_cast<int>(3.5);` quando a conversão for intencional.

## Inicialização padrão vs por valor

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int global;               // variáveis globais/estáticas são zeradas automaticamente

int main() {
    int a{};              // por valor: 0 (seguro)
    int b = int();        // também 0
    // int c;             // por padrão: valor INDETERMINADO (não leia!)
    std::cout << global << a << b << '\n';   // 000
}
```

> [!danger] Ler variável local não inicializada é UB (até C++23)
> ```cpp
> int x;
> std::cout << x;   // COMPORTAMENTO INDEFINIDO em C++23 e anteriores
> ```
> Compiladores avisam com `-Wall -Wextra` (`-Wmaybe-uninitialized`). **Correção:** sempre inicialize (`int x{};`). No C++26, a leitura passa a ser *erroneous behavior* — veja [[Cpp26 Visão Geral]].

## Armadilha: parênteses vs chaves em contêineres

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v1(3, 1);   // parênteses: 3 elementos com valor 1  -> {1, 1, 1}
    std::vector<int> v2{3, 1};   // chaves: lista de inicialização         -> {3, 1}

    std::cout << v1.size() << ' ' << v2.size() << '\n';   // 3 2
}
```

> [!warning] `initializer_list` tem prioridade
> Com chaves, construtores que aceitam `std::initializer_list` são preferidos. Use parênteses quando quiser o construtor "de contagem".

## Declarações múltiplas e nomes

- `int a = 1, b = 2;` é válido, mas prefira **uma declaração por linha**.
- Nomes: letras, dígitos e `_`; não podem começar com dígito; evite nomes que começam com `_` seguido de maiúscula ou com `__` (reservados).
- Declare a variável **perto do primeiro uso**, já inicializada.

## Veja também

- [[Tipos Fundamentais]]
- [[auto e decltype]]
- [[const e constexpr]]
- [[Conversões e Casts]]

## Exercício

1. Qual a diferença entre `std::vector<int> v(2, 5)` e `std::vector<int> v{2, 5}`?
2. Por que `int x{2.0};` é um erro, mas `int x = 2.0;` apenas compila (possivelmente com aviso)?
