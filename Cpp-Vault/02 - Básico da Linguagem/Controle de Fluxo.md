---
titulo: "Controle de fluxo"
tags: [cpp, basico, controle-de-fluxo]
aliases: ["if/else", "switch", "break e continue", "Estruturas de controle"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Operadores - Cpp]]", "[[Range-for e Inicializadores]]", "[[Funções - Cpp]]"]
---

# Controle de fluxo

## `if` / `else`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    int nota = 7;
    if (nota >= 9)      std::cout << "A\n";
    else if (nota >= 7) std::cout << "B\n";
    else                std::cout << "C\n";
}
```

> [!tip] Use sempre chaves
> `if (x) a(); b();` executa `b()` sempre. Mesmo com uma única instrução, prefira `{ }`.

## `switch`

`switch` escolhe entre valores **inteiros ou enumerações** (constantes de compilação).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

enum class Dia { Seg, Ter, Sab, Dom };

std::string tipo(Dia d) {
    switch (d) {
        case Dia::Sab:
        case Dia::Dom:
            return "fim de semana";
        default:
            return "dia útil";
    }
}

int pontos(char nota) {
    int p = 0;
    switch (nota) {
        case 'A': p += 10; [[fallthrough]];   // atravessa intencionalmente (C++17)
        case 'B': p += 5;  [[fallthrough]];
        case 'C': p += 1;  break;
        default:  break;
    }
    return p;
}

int main() {
    std::cout << tipo(Dia::Dom) << ", " << tipo(Dia::Ter) << '\n';
    std::cout << pontos('A') << ' ' << pontos('B') << ' ' << pontos('Z') << '\n';   // 16 6 0
}
```

> [!warning] *Fallthrough* acidental
> Sem `break`, a execução "cai" no próximo `case`. O atributo `[[fallthrough]]` (C++17) marca a intenção; com `-Wextra` o compilador avisa quando falta.

> [!tip] `switch` sobre `enum class`
> Evite `default` quando todos os enumeradores são tratados: assim o compilador avisa (`-Wswitch`) se um valor novo for adicionado e esquecido.

## Laços

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    // for clássico
    for (int i = 0; i < 3; ++i) std::cout << i << ' ';
    std::cout << '\n';                                  // 0 1 2

    // while: testa antes
    int n = 3;
    while (n > 0) { std::cout << n-- << ' '; }
    std::cout << '\n';                                  // 3 2 1

    // do-while: executa ao menos uma vez
    int k = 0;
    do { std::cout << "k=" << k << '\n'; } while (k > 0);

    // break e continue
    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) continue;     // pula pares
        if (i > 6) break;             // encerra o laço
        std::cout << i << ' ';
    }
    std::cout << '\n';                // 1 3 5
}
```

### Quebrando laços aninhados

`break` sai só do laço mais interno. Opções: *flag*, extrair para uma função com `return`, ou (raramente) `goto`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <utility>

// Extrair para função resolve limpo
std::pair<int, int> procura(int alvo) {
    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            if (i * j == alvo) return {i, j};
    return {-1, -1};
}

int main() {
    auto [i, j] = procura(12);
    std::cout << i << ',' << j << '\n';   // 3,4
}
```

## Laços infinitos e condições

```cpp
for (;;) { /* laço infinito */ }
while (true) { /* idem */ }
```

> [!bug] Erro clássico: atribuição no lugar de comparação
> ```cpp
> if (x = 5) { }   // atribui 5 a x e testa se é diferente de zero: sempre verdadeiro
> ```
> `-Wall` avisa (*suggest parentheses around assignment*). **Correção:** `if (x == 5)`.

## Veja também

- [[Operadores - Cpp]]
- [[Range-for e Inicializadores]]
- [[Funções - Cpp]]
- [[Sobrecarga de Funções]]

## Exercício

1. Escreva FizzBuzz de 1 a 30 usando `for` e `if`.
2. Reescreva o `switch` de `pontos` sem `[[fallthrough]]` e compare a legibilidade.
