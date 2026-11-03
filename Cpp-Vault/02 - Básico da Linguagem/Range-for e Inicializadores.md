---
titulo: "Range-for e inicializadores em if/switch"
tags: [cpp, basico, controle-de-fluxo]
aliases: ["Range-based for", "if com inicializador", "switch com inicializador", "for com inicializador"]
tipo: conceito
nivel: iniciante
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Controle de Fluxo]]", "[[auto e decltype]]", "[[Variáveis e Inicialização]]"]
---

# Range-for e inicializadores em `if`/`switch`

> [!info] Introdução
> - **Range-based for**: C++11.
> - **`if`/`switch` com inicializador**: C++17.
> - **`for` com inicializador (range-for)**: C++20.
> - Suporte: GCC 9+, Clang 8+ e MSVC 2019+ cobrem o C++20 dessa lista.

## Range-for

Percorre qualquer intervalo que tenha `begin()`/`end()`: contêineres, arrays, listas de inicialização.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> nomes{"Ana", "Bia", "Caio"};

    for (const auto& n : nomes)            // leitura sem cópia
        std::cout << n << ' ';
    std::cout << '\n';

    for (auto& n : nomes) n += "!";        // modifica os elementos originais
    for (auto n : nomes) n += "?";         // 'n' é CÓPIA: o vetor não muda

    int arr[] = {1, 2, 3};
    for (int x : arr) std::cout << x << ' ';   // arrays também funcionam
    for (int x : {10, 20, 30}) std::cout << x << ' ';
    std::cout << '\n';

    for (const auto& n : nomes) std::cout << n << ' ';   // Ana! Bia! Caio!
    std::cout << '\n';
}
```

| Forma | Quando usar |
|---|---|
| `for (const auto& x : c)` | Leitura de elementos possivelmente grandes (padrão) |
| `for (auto& x : c)` | Modificar elementos no lugar |
| `for (auto x : c)` | Tipos pequenos e baratos de copiar (`int`, `double`) |
| `for (auto&& x : c)` | Código genérico, inclusive com proxies (`vector<bool>`) |

> [!danger] Não modifique o tamanho do contêiner dentro do range-for
> `push_back`/`erase` durante o laço pode invalidar iteradores — comportamento indefinido.

> [!warning] Temporários (antes do C++23)
> `for (auto x : funcao().membro())` pode usar um objeto temporário já destruído. O C++23 estendeu a vida dos temporários no cabeçalho do range-for, mas para código portável guarde o resultado em uma variável.

## `if` com inicializador (C++17)

Mantém a variável **somente no escopo do `if`**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> idades{{"Ana", 30}, {"Bia", 25}};

    // 'it' existe só dentro do if/else
    if (auto it = idades.find("Ana"); it != idades.end()) {
        std::cout << "Ana tem " << it->second << " anos\n";
    } else {
        std::cout << "Ana não encontrada\n";
    }

    // switch com inicializador
    switch (auto n = idades.size(); n) {
        case 0:  std::cout << "vazio\n"; break;
        case 2:  std::cout << "dois itens\n"; break;
        default: std::cout << "outro tamanho\n"; break;
    }
}
```

## Range-for com inicializador (C++20)

Útil para um contador sem poluir o escopo externo.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> idades{{"Ana", 30}, {"Bia", 25}};

    for (int i = 1; const auto& [nome, idade] : idades)   // structured binding no range-for
        std::cout << i++ << ". " << nome << " (" << idade << ")\n";
}
```

> [!info] Structured bindings
> A sintaxe `const auto& [nome, idade]` (C++17) decompõe pares e structs; ela é explicada na seção de structured bindings deste vault.

## Veja também

- [[Controle de Fluxo]]
- [[auto e decltype]]
- [[Variáveis e Inicialização]]
- [[Funções - Cpp]]

## Exercício

1. Percorra um `std::vector<double>` e imprima só os maiores que a média, usando `if` com inicializador para calcular a média.
2. Por que `for (auto n : nomes) n += "?";` não altera `nomes`?
