---
titulo: "Exercícios de Ponteiros e Memória"
tags: [cpp, exercicios, ponteiros, memoria]
aliases: ["Exercícios de ponteiros"]
tipo: exercicio
nivel: iniciante
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Ponteiros e Memória]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de Ponteiros e Memória

Teoria: [[Ponteiros]], [[Referências - Cpp]], [[Aritmética de Ponteiros]], [[new e delete]], [[Vazamentos e Dangling Pointers]].

## 1. Troca de valores

Implemente `trocar` de duas formas: com ponteiros e com referências.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void trocar_ptr(int* a, int* b) { int t = *a; *a = *b; *b = t; }
void trocar_ref(int& a, int& b) { int t = a; a = b; b = t; }

int main() {
    int x = 1, y = 2;
    trocar_ptr(&x, &y);
    std::cout << x << y << ' ';
    trocar_ref(x, y);
    std::cout << x << y << '\n';   // 21 12
}
```

## 2. Corrija o dangling

```cpp
// ERRO (UB): retorna referência para variável local
// const std::string& saudacao() { std::string s = "oi"; return s; }
```

Explique o bug e corrija.

> [!danger] Referência pendente
> `s` é destruída ao sair da função; a referência devolvida aponta para memória inválida.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

std::string saudacao() { return "oi"; }   // por valor (RVO/move, sem custo)

int main() { std::cout << saudacao() << '\n'; }
```

## 3. `meu_strlen` com aritmética de ponteiros

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>

std::size_t meu_strlen(const char* s) {
    const char* p = s;
    while (*p != '\0') ++p;
    return static_cast<std::size_t>(p - s);
}

int main() { std::cout << meu_strlen("ponteiro") << '\n'; }   // 8
```

## 4. Do `new[]` ao RAII

Escreva um programa que aloca `n` inteiros com `new int[n]`, preenche com quadrados e libera. Depois reescreva sem `delete`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>

int main() {
    const int n = 5;
    int* cru = new int[n];
    for (int i = 0; i < n; ++i) cru[i] = i * i;
    std::cout << cru[n - 1] << ' ';
    delete[] cru;                              // delete[] (não delete!)

    auto seguro = std::make_unique<int[]>(n);  // libera sozinho
    for (int i = 0; i < n; ++i) seguro[i] = i * i;
    std::cout << seguro[n - 1] << '\n';        // 16 16
}
```

## Veja também

- [[Ponteiros]]
- [[Referências - Cpp]]
- [[unique_ptr]]
- [[Stack vs Heap]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Rode o exercício 4 (versão crua, sem `delete[]`) com `-fsanitize=address` e leia o relatório de vazamento ([[Sanitizers]]).
