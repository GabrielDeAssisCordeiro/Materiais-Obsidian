---
titulo: "std::string_view"
tags: [cpp, basico, strings, cpp17]
aliases: ["std::string_view", "string_view", "Visão de string", "View de string"]
tipo: conceito
nivel: iniciante
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Strings C e std string]]", "[[Arrays e std array]]", "[[Funções - Cpp]]"]
---

# `std::string_view`

> [!info] Introdução
> `std::string_view` (`<string_view>`) existe desde o **C++17**. Suporte: GCC 7+, Clang 4+, MSVC 2017 15.3+.

Uma `string_view` é uma **visão não proprietária** de uma sequência de caracteres: guarda apenas um **ponteiro** e um **tamanho**. Não aloca, não copia e é barata de passar por valor.

## Para que serve

Aceitar qualquer origem de texto (literal, `std::string`, `char[]`, parte de outra string) em parâmetros de funções **somente leitura**, sem cópias nem sobrecargas.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <string_view>

// Uma única função aceita literal, std::string e fatias
bool eh_comando(std::string_view s) {
    return s.starts_with("cmd:");              // starts_with: C++20
}

int main() {
    std::string dono = "cmd:abrir";
    std::string_view v = dono;                 // sem cópia

    std::cout << eh_comando("cmd:sair") << eh_comando(dono) << eh_comando(v.substr(4)) << '\n';   // 110

    v.remove_prefix(4);                        // "avança" o início: O(1), não altera 'dono'
    std::cout << v << ' ' << v.size() << '\n'; // abrir 5

    using namespace std::string_view_literals;
    constexpr auto sv = "texto"sv;             // literal string_view (constexpr)
    static_assert(sv.size() == 5);
}
```

## Comparação

| | `const std::string&` | `std::string_view` |
|---|---|---|
| Aceita literal sem criar `std::string` temporária | Não (aloca) | **Sim** |
| Sub-strings baratas | `substr` copia | `substr` é O(1) |
| Possui os dados | Não (referência) | Não |
| Garante `'\0'` no final | Sim (`c_str`) | **Não** |
| Seguro contra dangling | Também não | Também não |

> [!danger] Armadilha: `string_view` pendente (*dangling*)
> A `string_view` **não mantém vivos** os dados. Se a string de origem for destruída ou realocada, a visão fica inválida (UB ao usar).
> ```cpp
> std::string_view ruim() {
>     std::string s = "temporária";
>     return s;                       // dangling: 's' morre ao sair da função
> }
>
> std::string_view sv = std::string("abc");   // dangling: temporário destruído no fim da linha
> ```
> **Correção:** guarde a `std::string` (ou retorne `std::string`) e crie a visão só enquanto o dono estiver vivo.

> [!warning] `data()` não é uma C-string
> Não passe `sv.data()` para funções C que esperam `'\0'` no final, a menos que tenha certeza de que a visão vai até o fim de uma string terminada em zero. Converta com `std::string(sv)`.

## Quando usar

- **Use** como parâmetro de funções que apenas **leem** texto.
- **Não use** como membro de classe ou valor de retorno sem pensar no tempo de vida do dono.
- Existe análogo para sequências genéricas: `std::span` (C++20), tratado na seção de contêineres.

## Veja também

- [[Strings C e std string]]
- [[Arrays e std array]]
- [[Funções - Cpp]]
- [[Comportamento Indefinido e Não Especificado]]

## Exercício

1. Escreva `int contar_vogais(std::string_view s)` e chame com literal, `std::string` e `char[]`.
2. Descreva uma situação concreta em que retornar `std::string_view` de uma função causa UB.
