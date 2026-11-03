---
titulo: "Comportamento indefinido e não especificado"
tags: [cpp, basico, ub, seguranca, sanitizers]
aliases: ["UB", "Undefined behavior", "Comportamento indefinido", "Unspecified behavior", "Implementation-defined", "Comportamento não especificado"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Tipos Fundamentais]]", "[[Operadores - Cpp]]", "[[Strings C e std string]]"]
---

# Comportamento indefinido e não especificado

O padrão classifica o que o código pode fazer em quatro categorias:

| Categoria | Significado | Exemplo |
|---|---|---|
| **Bem definido** | Resultado determinado pelo padrão | Estouro de `unsigned` (módulo 2ⁿ) |
| **Definido pela implementação** (*implementation-defined*) | O compilador escolhe e **documenta** | `sizeof(int)`, sinal de `char`, `>>` de negativo (até C++20) |
| **Não especificado** (*unspecified*) | Várias possibilidades válidas, sem documentação obrigatória | Ordem de avaliação dos argumentos de função |
| **Indefinido** (*undefined behavior*, **UB**) | **Sem nenhuma garantia** | Acesso fora dos limites, estouro de `int`, desreferenciar `nullptr` |

> [!danger] O que UB realmente significa
> Se o programa executa UB, o padrão **não impõe nenhuma exigência**: pode "funcionar", travar, corromper dados, ou fazer algo aparentemente impossível. Pior: o compilador **assume que UB nunca acontece** e otimiza com base nisso. Um bug pode aparecer só com `-O2`, em outro compilador ou em outra máquina.

## Exemplos clássicos de UB

> [!danger] Lista (exemplos propositalmente inválidos)
> ```cpp
> int a[3]; a[3] = 0;                       // 1. acesso fora dos limites
> int* p = nullptr; *p = 1;                 // 2. desreferenciar ponteiro nulo
> int x = INT_MAX; x + 1;                   // 3. estouro de inteiro com sinal
> int y; int z = y;                         // 4. ler variável não inicializada (até C++23)
> int* q = new int; delete q; *q = 1;       // 5. use-after-free
> int* r = new int[2]; delete r;            // 6. new[] liberado com delete (deve ser delete[])
> int s = 1 / 0;                            // 7. divisão inteira por zero
> 1 << 40;                                  // 8. deslocamento maior ou igual à largura do tipo (int de 32 bits)
> i = i++ + 1;  f(i++, i);                  // 9. modificações não sequenciadas (alguns casos)
> int& ref() { int l = 1; return l; }       // 10. retornar referência para local
> const int k = 1; *const_cast<int*>(&k)=2; // 11. modificar objeto const
> data race entre threads sem sincronização // 12. condição de corrida
> ```

## Um exemplo que "engana" o compilador

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <climits>
#include <iostream>

// Em C++, o compilador pode concluir que 'x + 1 > x' é SEMPRE verdadeiro para int,
// já que estouro com sinal é UB. Com -O2 a função pode virar "return true".
bool sempre_maior(int x) { return x + 1 > x; }

int main() {
    std::cout << sempre_maior(5) << '\n';        // 1
    // sempre_maior(INT_MAX) seria UB: o resultado "esperado" (false) não é garantido
    std::cout << INT_MAX << '\n';
}
```

## Não especificado: duas respostas válidas

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int a() { std::cout << "a "; return 1; }
int b() { std::cout << "b "; return 2; }
int soma(int x, int y) { return x + y; }

int main() {
    // A ordem de avaliação dos argumentos NÃO é especificada: pode imprimir "a b" ou "b a".
    std::cout << soma(a(), b()) << '\n';
}
```

Não é UB (o programa é válido), mas **não dependa** da ordem.

## Como se defender

| Ferramenta | O que detecta |
|---|---|
| `-Wall -Wextra -Wpedantic` | Muitos usos suspeitos em compilação |
| `-fsanitize=address` (ASan) | Estouros de buffer, use-after-free, vazamentos (`detect_leaks`) |
| `-fsanitize=undefined` (UBSan) | Estouro de inteiro com sinal, deslocamentos inválidos, desreferência nula... |
| `-fsanitize=thread` (TSan) | Data races |
| `-fsanitize=memory` (MSan, Clang) | Leitura de memória não inicializada |
| Valgrind | Erros de memória em execução (mais lento) |
| clang-tidy / cppcheck | Análise estática |
| Contêineres e smart pointers | Eliminam classes inteiras de UB (veja as seções de STL e RAII) |

```bash
g++ -std=c++20 -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer programa.cpp -o programa
./programa
```

> [!tip] Mentalidade
> UB não é "erro de execução que o computador avisa": é um **contrato quebrado**. Escreva código que não dependa de nenhum comportamento indefinido, ative avisos e rode sanitizers nos testes.

> [!info] C++26
> O C++26 reclassifica a leitura de variáveis automáticas não inicializadas como *erroneous behavior* (não mais UB) e define uma biblioteca padrão "hardened" com pré-condições verificáveis — veja [[Cpp26 Visão Geral]].

## Veja também

- [[Tipos Fundamentais]]
- [[Operadores - Cpp]]
- [[Strings C e std string]]
- [[Flags Essenciais do Compilador]]
- [[Cpp26 Visão Geral]]

## Exercício

1. Compile um programa com `a[3] = 0;` (array de 3) com `-fsanitize=address` e leia a mensagem de erro.
2. Classifique em "indefinido", "não especificado" ou "definido pela implementação": (a) `sizeof(long)`, (b) `f(g(), h())`, (c) `INT_MAX + 1`.
