---
titulo: "C++ vs C"
tags: [cpp, fundamentos, comparacao]
aliases: ["C++ vs C", "Diferenças entre C e C++"]
tipo: comparacao
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[O que é Cpp]]", "[[Filosofia do Cpp]]", "[[Cpp vs Rust, Java, Go e Python]]"]
---

# C++ vs C

C++ nasceu como extensão do C e mantém grande compatibilidade, mas **não é um superconjunto estrito**: há código C válido que não compila (ou significa outra coisa) em C++.

## Quadro comparativo

| Aspecto | C | C++ |
|---|---|---|
| Paradigma | Procedural | Multiparadigma |
| Tipo booleano | `_Bool`/`bool` (`<stdbool.h>`; palavra-chave em C23) | `bool` nativo |
| Strings | Arrays de `char` terminados em `\0` | `std::string`, `std::string_view` |
| Memória dinâmica | `malloc`/`free` | `new`/`delete` (evitar) → smart pointers e contêineres |
| Conversão de `void*` | Implícita | Exige cast explícito |
| Sobrecarga de funções | Não | Sim |
| Referências | Não | Sim (`T&`, `T&&`) |
| Namespaces | Não | Sim |
| Classes / herança / virtual | Não | Sim |
| Templates / genéricos | Macros | Templates e concepts |
| Exceções | Não (usa códigos de erro) | Sim |
| Biblioteca padrão | Pequena | STL, `<string>`, `<thread>`, `<filesystem>`... |
| Tipo de `'a'` | `int` (`sizeof('a') == 4` típico) | `char` (`sizeof('a') == 1`) |
| Linkagem de nomes | Sem *mangling* | *Name mangling* por causa da sobrecarga |

## Exemplo: o mesmo problema nas duas linguagens

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

int main() {
    // C++: tamanho dinâmico sem malloc/free; memória liberada automaticamente.
    std::vector<int> v(5, 7);   // cinco elementos com valor 7
    v.push_back(9);

    static_assert(sizeof('a') == 1);   // em C seria sizeof(int)

    for (int x : v) std::cout << x << ' ';
    std::cout << '\n';
}
```

> [!bug] Código C válido que **não** compila em C++ (exemplo inválido proposital)
> ```c
> #include <stdlib.h>
> int main(void) {
>     int *p = malloc(10 * sizeof *p);   // C: ok. C++: erro, void* não converte implicitamente
>     free(p);
> }
> ```
> **Correção em C++ moderno:** use `std::vector<int> p(10);` ou `std::make_unique<int[]>(10)`.

## Usando as duas linguagens juntas

Cabeçalhos C devem ser envolvidos em `extern "C"` quando incluídos em C++ para evitar *name mangling* (veja a nota de interoperabilidade na seção de áreas de aplicação deste vault).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdio>   // versão C++ de <stdio.h>: funções em std:: (e geralmente no global)

int main() {
    std::printf("printf ainda funciona em C++\n");
}
```

> [!tip] Cabeçalhos C
> Em C++ prefira `<cstdio>`, `<cstdlib>`, `<cstring>`, `<cmath>` aos equivalentes `.h`.

> [!warning] Não escreva "C com `cout`"
> Usar C++ apenas como "C melhorado" perde segurança e produtividade. Aprenda os idiomas modernos.

## Veja também

- [[O que é Cpp]]
- [[Filosofia do Cpp]]
- [[Primeiro Programa]]
- [[Pipeline de Compilação - Cpp]]

## Exercício

1. Cite três diferenças entre `malloc` e um `std::vector`.
2. Por que `sizeof('a')` difere entre C e C++?
