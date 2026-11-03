---
titulo: "Entrada e saída básica"
tags: [cpp, basico, io, iostream, format, print]
aliases: ["cout e cin", "Entrada e saída"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Primeiro Programa]]", "[[Strings C e std string]]", "[[Namespaces - Cpp]]"]
---

# Entrada e saída básica

> [!info] Versões
> - `iostream`: desde o C++98.
> - `std::format`: **C++20** (GCC 13+, Clang 17+ com libc++ recente, MSVC 2019 16.10+).
> - `std::print`/`std::println`: **C++23** (GCC 14+, MSVC 17.7+, libc++ 18+).
> [!question] Verificar na documentação oficial
> Confirme a versão mínima exata do seu compilador/biblioteca em cppreference.com (compiler support).

## Streams padrão

| Objeto | Cabeçalho | Função |
|---|---|---|
| `std::cout` | `<iostream>` | Saída padrão (buffer) |
| `std::cerr` | `<iostream>` | Erros (sem buffer) |
| `std::clog` | `<iostream>` | Log (com buffer) |
| `std::cin` | `<iostream>` | Entrada padrão |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iomanip>
#include <iostream>
#include <string>

int main() {
    int idade;
    double altura;
    std::string nome;

    std::cout << "Nome: ";
    std::getline(std::cin >> std::ws, nome);        // lê linha inteira (ws descarta espaços iniciais)

    std::cout << "Idade e altura: ";
    if (!(std::cin >> idade >> altura)) {           // sempre valide a leitura
        std::cerr << "entrada inválida\n";
        return 1;
    }

    std::cout << std::fixed << std::setprecision(2);   // 2 casas decimais
    std::cout << nome << ", " << idade << " anos, " << altura << " m\n";
    std::cout << std::setw(8) << std::setfill('.') << 42 << '\n';   // ......42
}
```

> [!warning] `cin >>` deixa o `\n` no buffer
> Misturar `std::cin >> x` com `std::getline` sem descartar o `\n` faz o `getline` ler uma linha vazia. Use `std::cin >> std::ws` ou `std::cin.ignore(...)`.

## Acelerando a E/S

Por padrão, `iostream` está sincronizado com `stdio`. Para programas com muita E/S:

```cpp
std::ios::sync_with_stdio(false);   // antes de qualquer E/S; não misture com printf/scanf depois
std::cin.tie(nullptr);              // desacopla cin de cout
```

E prefira `'\n'` a `std::endl` (que descarrega o buffer).

## `std::format` (C++20)

Formatação segura em tipos, no estilo de `{}` do Python.

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra   (requer GCC 13+; indisponível no ambiente de teste do vault)
#include <format>
#include <iostream>
#include <string>

int main() {
    std::string s = std::format("{} tem {} anos e {:.1f} m", "Ana", 30, 1.68);
    std::cout << s << '\n';                               // Ana tem 30 anos e 1.7 m

    std::cout << std::format("{:>8}|{:<8}|{:^8}\n", "dir", "esq", "meio");
    std::cout << std::format("{:#x} {:08.3f} {:+d}\n", 255, 3.14159, 7);   // 0xff 0003.142 +7
    std::cout << std::format("{1} {0}\n", "mundo", "olá");                 // olá mundo
}
```

## `std::print` e `std::println` (C++23)

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra   (requer GCC 14+; indisponível no ambiente de teste do vault)
#include <print>

int main() {
    std::println("Olá, {}!", "C++23");      // com quebra de linha
    std::print("{} + {} = {}\n", 2, 3, 5);  // sem quebra automática
}
```

Vantagens sobre `iostream`: sintaxe mais legível, verificação da string de formato em tempo de compilação, melhor desempenho e suporte correto a Unicode no terminal.

## Comparação

| Aspecto | `iostream` | `printf` | `std::format`/`std::print` |
|---|---|---|---|
| Segurança de tipos | Sim | **Não** | Sim |
| Tipos definidos pelo usuário | `operator<<` | Não | `std::formatter` |
| Legibilidade | Média (encadeamento) | Boa | Boa |
| Verificação em compilação | Sim | Parcial (avisos) | Sim |

> [!danger] `printf` com tipo errado é UB
> ```cpp
> printf("%d\n", 3.14);   // COMPORTAMENTO INDEFINIDO: %d espera int, recebeu double
> ```
> **Correção:** `std::cout << 3.14;` ou `std::format("{}", 3.14)`.

## Veja também

- [[Primeiro Programa]]
- [[Strings C e std string]]
- [[Namespaces - Cpp]]
- [[Tipos Fundamentais]]

## Exercício

1. Faça um programa que leia números até o EOF (`while (std::cin >> x)`) e imprima a soma.
2. Formate uma tabela de três colunas alinhadas usando `std::setw` (e depois com `std::format`, se disponível).
