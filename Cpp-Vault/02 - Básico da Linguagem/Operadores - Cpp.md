---
titulo: "Operadores - Cpp"
tags: [cpp, basico, operadores]
aliases: ["Precedência de operadores", "Operador spaceship", "Short-circuit"]
tipo: referencia
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Tipos Fundamentais]]", "[[Conversões e Casts]]", "[[Controle de Fluxo]]"]
---

# Operadores - Cpp

## Visão geral

| Categoria | Operadores | Observações |
|---|---|---|
| Aritméticos | `+ - * / %` | `/` entre inteiros trunca; `%` só para inteiros |
| Incremento/decremento | `++ --` (pré e pós) | Prefira o prefixo (`++i`) quando o valor não é usado |
| Relacionais | `< <= > >= == !=` | Comparar `double` com `==` é arriscado |
| Three-way (C++20) | `<=>` | "Spaceship": retorna ordenação (`<compare>`) |
| Lógicos | `&&`, `\|\|`, `!` | `&&` e `\|\|` fazem **curto-circuito** |
| Bit a bit | `&`, `\|`, `^`, `~`, `<<`, `>>` | Para flags e máscaras |
| Atribuição | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `\|=`, `^=`, `<<=`, `>>=` | |
| Ternário | `cond ? a : b` | Os dois ramos devem ter tipo comum |
| Membro | `. -> .* ->*` | |
| Outros | `sizeof`, `alignof`, `typeid`, `new`, `delete`, `,`, `()` , `[]` | |

## Divisão e resto

A divisão inteira **trunca em direção a zero** (garantido desde o C++11). O resto tem o sinal do dividendo.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <compare>
#include <iostream>

bool verdade() { std::cout << "V "; return true; }
bool falso() { std::cout << "F "; return false; }

int main() {
    std::cout << 7 / 2 << ' ' << -7 / 2 << ' ' << 7 % 3 << ' ' << -7 % 3 << '\n';   // 3 -3 1 -1
    std::cout << 7 / 2.0 << '\n';                                                     // 3.5

    // Flags com operadores bit a bit
    constexpr unsigned LER = 1u << 0, ESCREVER = 1u << 1, EXEC = 1u << 2;
    unsigned permissoes = 0;
    permissoes |= LER | ESCREVER;      // liga bits
    permissoes &= ~ESCREVER;           // desliga ESCREVER
    permissoes ^= EXEC;                // alterna EXEC
    std::cout << permissoes << ' ' << ((permissoes & LER) != 0) << '\n';          // 5 1

    // Curto-circuito: o segundo operando só é avaliado se necessário
    bool r1 = falso() && verdade();    // imprime "F " (verdade() não é chamada)
    bool r2 = verdade() || falso();    // imprime "V " (falso() não é chamada)
    std::cout << r1 << r2 << '\n';     // 01

    // Operador <=> (C++20)
    auto cmp = 3 <=> 5;
    std::cout << (cmp < 0) << '\n';    // 1: 3 é menor que 5
}
```

## Precedência (resumo, do mais forte ao mais fraco)

1. `::` (escopo), `()`/`[]`/`.`/`->`/`++ --` pós-fixados
2. Unários: `! ~ + - ++ -- * & sizeof new delete` e casts
3. `* / %`
4. `+ -`
5. `<< >>`
6. `<=>`
7. `< <= > >=`
8. `== !=`
9. `&`, depois `^`, depois `|`
10. `&&`, depois `||`
11. `?:` e atribuições (da direita para a esquerda)
12. `,`

> [!warning] Armadilha clássica
> `a & b == c` é lido como `a & (b == c)`, porque `==` tem precedência maior que `&`. Use parênteses: `(a & b) == c`.

> [!tip] Na dúvida, use parênteses
> Parênteses não custam nada e eliminam leituras erradas.

## Ordem de avaliação

Precedência não define **qual operando é avaliado primeiro**. Exemplos:

- Em `f(a(), b())`, a ordem de avaliação de `a()` e `b()` é **não especificada**.
- Modificar e ler a mesma variável sem sequenciamento (por exemplo, `i + i++`) é problemático; o C++17 definiu a ordem para alguns operadores (`<<`, `>>`, atribuição, `.`, `->`), mas **não** para argumentos de função.

> [!danger] Evite expressões com efeitos colaterais múltiplos na mesma variável
> ```cpp
> int i = 1;
> int r = i++ + ++i;   // não escreva isso: UB (versões antigas) / resultado confuso
> ```

## Veja também

- [[Tipos Fundamentais]]
- [[Conversões e Casts]]
- [[Controle de Fluxo]]
- [[Funções - Cpp]]

## Exercício

1. Calcule à mão `-9 / 4` e `-9 % 4` em C++ e confirme compilando.
2. Escreva uma função `bool tem_bit(unsigned valor, int pos)` usando operadores bit a bit.
