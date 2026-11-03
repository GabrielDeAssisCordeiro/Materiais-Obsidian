---
titulo: "nullptr"
tags: [cpp, memoria, ponteiros]
aliases: ["nullptr", "NULL", "Ponteiro nulo", "std::nullptr_t"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Ponteiros]]", "[[Sobrecarga de Funções]]", "[[Vazamentos e Dangling Pointers]]"]
---

# `nullptr`

> [!info] Introdução
> **C++11.** Substitui `NULL` e o literal `0` como ponteiro nulo. Seu tipo é `std::nullptr_t` (em `<cstddef>`).

## Por que `NULL` e `0` são problemáticos

`NULL` é uma macro que expande para `0` (ou `0L`, `__null`...): um **inteiro**. Isso atrapalha a sobrecarga.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>

void f(int)   { std::cout << "f(int)\n"; }
void f(char*) { std::cout << "f(char*)\n"; }

int main() {
    f(0);          // f(int): 0 é int
    f(nullptr);    // f(char*): nullptr só converte para ponteiros
    // f(NULL);    // ambíguo ou f(int), conforme o compilador: evite

    char* p = nullptr;
    int* q = nullptr;
    std::nullptr_t n = nullptr;     // tipo próprio
    std::cout << (p == nullptr) << (q == n) << '\n';   // 11
}
```

## Propriedades

| Característica | Detalhe |
|---|---|
| Converte para qualquer tipo de ponteiro ou ponteiro para membro | Sim |
| Converte para `bool` | Apenas explicitamente (`bool b = (p == nullptr)`); em contexto de condição (`if (p)`) funciona |
| Converte para inteiro | **Não** (exceto `std::nullptr_t` → `bool` em inicialização direta) |
| Comparável com ponteiros | Sim |

## Testando ponteiros

```cpp
if (p)               // verdadeiro se p != nullptr
if (p == nullptr)    // equivalente, mais explícito
if (!p)              // verdadeiro se p é nulo
```

> [!danger] Desreferenciar `nullptr` é UB
> O resultado habitual é *segmentation fault*, mas o padrão não garante nada — o compilador pode até remover verificações posteriores, assumindo que o ponteiro era válido.
> ```cpp
> int* p = nullptr;
> int x = *p;   // COMPORTAMENTO INDEFINIDO
> ```

## `delete nullptr` é seguro

Aplicar `delete` a um ponteiro nulo **não faz nada**. Por isso, não é necessário `if (p) delete p;`. Em C++ moderno, evite `delete` manual: use smart pointers ([[new e delete]]).

## Boas práticas

- Inicialize ponteiros com `nullptr` quando ainda não houver destino.
- Em C++ moderno, ponteiros brutos são **observadores**; documente se podem ser nulos (ou use `std::optional`/referência quando não podem).
- Após `delete` manual, atribuir `nullptr` ajuda a detectar uso depois de liberado, mas **não resolve cópias** do ponteiro (veja [[Vazamentos e Dangling Pointers]]).

## Veja também

- [[Ponteiros]]
- [[Sobrecarga de Funções]]
- [[new e delete]]
- [[Vazamentos e Dangling Pointers]]

## Exercício

1. Explique por que `f(NULL)` pode chamar `f(int)` quando você esperava `f(char*)`.
2. Escreva uma função que receba `const char*` e retorne o comprimento, tratando `nullptr` como string vazia.
