---
titulo: "Strings C vs std::string"
tags: [cpp, basico, strings, std-string]
aliases: ["Strings C", "char*", "C-strings", "Strings em C++"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[string_view]]", "[[Arrays e std array]]", "[[Entrada e Saída Básica]]"]
---

# Strings C vs `std::string`

## Strings C (`char[]` / `const char*`)

Uma *C-string* é um array de `char` terminado por `'\0'`. O comprimento é desconhecido sem varrer o array (`std::strlen`), e **nada** protege contra estouro.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstring>
#include <iostream>

int main() {
    const char* literal = "olá";            // literal: const char[N], armazenado em memória somente leitura
    char buf[16] = "abc";                   // array modificável (copiado do literal)

    std::cout << std::strlen(literal) << '\n';   // conta bytes até '\0' (acentos UTF-8 ocupam 2 bytes)
    std::strncat(buf, "def", sizeof buf - std::strlen(buf) - 1);   // concatenação "limitada"
    std::cout << buf << '\n';                // abcdef
    std::cout << std::strcmp("a", "b") << '\n';   // <0: comparação lexicográfica (valor negativo)
}
```

> [!danger] Estouro de buffer (*buffer overflow*) — UB
> ```cpp
> char pequeno[4];
> std::strcpy(pequeno, "texto longo");   // escreve além do array: COMPORTAMENTO INDEFINIDO
> ```
> `strcpy`, `strcat`, `gets` e `sprintf` não verificam limites. É a origem de inúmeras falhas de segurança. **Correção:** use `std::string`.

## `std::string` (`<string>`)

Contêiner de caracteres que **gerencia a própria memória**, sabe seu tamanho e cresce conforme necessário.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

int main() {
    std::string s = "C++";
    s += " moderno";                          // concatenação
    s.push_back('!');
    s.append(" ok");

    std::cout << s << ' ' << s.size() << '\n';              // C++ moderno! ok 15
    std::cout << s.substr(4, 7) << '\n';                    // moderno
    std::cout << s.find("mod") << '\n';                     // 4 (posição) ; std::string::npos se não achar
    std::cout << (s == "C++ moderno! ok") << '\n';          // 1: comparação por valor
    std::cout << s.starts_with("C++") << '\n';              // 1 (C++20)

    if (s.find("xyz") == std::string::npos) std::cout << "não achou\n";

    std::string n = std::to_string(42) + "!";               // número -> string
    int v = std::stoi("123");                               // string -> int (lança exceção em erro)
    std::cout << n << ' ' << v + 1 << '\n';                 // 42! 124

    const char* c = s.c_str();                              // ponteiro C terminado em '\0' (válido enquanto s não mudar)
    std::cout << c << '\n';

    for (char& ch : s) if (ch == ' ') ch = '_';             // percorre e modifica
    std::cout << s << '\n';
}
```

## Comparação

| | C-string | `std::string` |
|---|---|---|
| Tamanho | `strlen` (O(n)) | `size()` (O(1)) |
| Concatenação | `strcat` (manual, perigosa) | `+`, `+=`, `append` |
| Comparação | `strcmp` | `==`, `<`, `compare` |
| Memória | Você cuida | Automática (RAII) |
| Cópia | `strcpy` | `=` |
| Interoperar com APIs C | Direto | `c_str()`, `data()` |
| Texto com `'\0'` no meio | Impossível | Possível |

> [!info] SSO (*small string optimization*)
> Implementações guardam strings curtas (≈15 a 22 caracteres) dentro do próprio objeto, sem alocação no heap. Isso é detalhe de implementação, não garantia do padrão.

> [!warning] `std::string` é bytes, não "letras"
> `size()` conta **bytes** (`char`). Em UTF-8, `"ç"` ocupa 2 bytes. Para texto Unicode, veja as notas de Unicode na seção de strings e I/O.

> [!bug] Armadilha: somar literais
> ```cpp
> std::string s = "a" + "b";   // erro: não há operador + entre dois const char*
> ```
> **Correção:** `std::string s = std::string("a") + "b";` ou `using namespace std::string_literals; auto s = "a"s + "b";`.

## Veja também

- [[string_view]]
- [[Arrays e std array]]
- [[Entrada e Saída Básica]]
- [[Comportamento Indefinido e Não Especificado]]

## Exercício

1. Escreva uma função que inverte uma `std::string` sem usar `std::reverse`.
2. Mostre, com `sizeof` e `size()`, a diferença entre `char arr[] = "abc";` e `std::string s = "abc";`.
