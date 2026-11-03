---
titulo: "Sobrecarga de funções"
tags: [cpp, basico, sobrecarga]
aliases: ["Sobrecarga", "Overloading", "Resolução de sobrecarga", "Overload resolution"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Funções - Cpp]]", "[[Argumentos Padrão e inline]]", "[[Conversões e Casts]]"]
---

# Sobrecarga de funções

**Sobrecarga** (*overloading*) permite várias funções com o **mesmo nome** e **parâmetros diferentes** (número ou tipos).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

void mostra(int x)                { std::cout << "int " << x << '\n'; }
void mostra(double x)             { std::cout << "double " << x << '\n'; }
void mostra(const std::string& s) { std::cout << "string " << s << '\n'; }
void mostra(const char* s)        { std::cout << "const char* " << s << '\n'; }
void mostra(int a, int b)         { std::cout << "dois ints " << a << ',' << b << '\n'; }

int main() {
    mostra(1);                      // int           (correspondência exata)
    mostra(2.5);                    // double        (exata)
    mostra(2.5f);                   // double        (promoção float -> double)
    mostra('a');                    // int 97        (promoção char -> int)
    mostra("literal");              // const char*   (array-to-pointer: exata)
    mostra(std::string("abc"));     // string
    mostra(1, 2);                   // dois ints
}
```

## O que diferencia uma sobrecarga

| Diferença válida | Exemplo |
|---|---|
| Número de parâmetros | `f(int)` e `f(int, int)` |
| Tipos dos parâmetros | `f(int)` e `f(double)` |
| `const`/`volatile` de referências ou ponteiros apontados | `f(int&)` e `f(const int&)` |
| `const` em métodos de classe | `T& get()` e `const T& get() const` |

> [!bug] **Não** diferenciam
> - O **tipo de retorno** (`int f()` e `double f()` conflitam).
> - `const` **de nível superior** em parâmetros por valor (`f(int)` e `f(const int)` são a mesma função).
> - Argumentos padrão.

## Como o compilador escolhe (resumo)

1. Reúne as funções candidatas pelo nome.
2. Mantém as **viáveis** (aceitam os argumentos).
3. Escolhe a **melhor** por ranking de conversões:
   1. Correspondência exata (inclui `T` → `const T&`, array → ponteiro)
   2. Promoção (`char`/`short` → `int`, `float` → `double`)
   3. Conversão padrão (`int` → `double`, `double` → `long`, ponteiro → `bool`)
   4. Conversão definida pelo usuário (construtores e operadores de conversão)
   5. Reticências (`...`)
4. Se nenhuma for estritamente melhor: **erro de ambiguidade**.

> [!bug] Exemplo inválido proposital: chamada ambígua
> ```cpp
> void f(long x);
> void f(double x);
>
> f(1);   // erro: call of overloaded 'f(int)' is ambiguous
>         // int -> long e int -> double são ambos "conversão"; nenhuma é melhor
> ```
> **Correção:** passe o tipo exato (`f(1L)` ou `f(1.0)`) ou adicione uma sobrecarga `f(int)`.

> [!warning] `nullptr` vs `0`
> `f(int)` e `f(char*)` com a chamada `f(NULL)` pode ser ambígua ou chamar `f(int)`. Use `nullptr`, que só converte para ponteiros.

## Bloqueando sobrecargas indesejadas com `= delete`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void imprime(int x) { std::cout << x << '\n'; }
void imprime(double) = delete;      // proíbe chamadas com double (e float por promoção)

int main() {
    imprime(7);
    // imprime(7.5);   // erro de compilação: uso de função deletada
}
```

Em C++26 é possível documentar o motivo: `void imprime(double) = delete("use int");`.
> [!question] Verificar na documentação oficial
> Disponibilidade de `= delete("motivo")` no seu compilador (C++26).

## Sobrecarga vs templates vs argumentos padrão

| Situação | Ferramenta |
|---|---|
| Comportamentos diferentes para tipos diferentes | Sobrecarga |
| Mesmo algoritmo para muitos tipos | Template de função |
| Mesmo comportamento com parâmetros opcionais | [[Argumentos Padrão e inline\|Argumentos padrão]] |

## Veja também

- [[Funções - Cpp]]
- [[Argumentos Padrão e inline]]
- [[Conversões e Casts]]
- [[auto e decltype]]

## Exercício

1. Implemente `abs_valor` com sobrecargas para `int`, `double` e `long long` e teste com `short` e `float`. Qual sobrecarga é chamada?
2. Por que `std::cout << 'a'` imprime um caractere, mas `mostra('a')` acima imprimiu `int 97`?
