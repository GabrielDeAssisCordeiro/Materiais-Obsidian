---
titulo: "O que é C++"
tags: [cpp, fundamentos, conceito]
aliases: ["C++", "Linguagem C++", "O que é C++"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[História e Evolução dos Padrões]]", "[[Filosofia do Cpp]]", "[[Pipeline de Compilação - Cpp]]"]
---

# O que é C++

**C++** é uma linguagem de programação **compilada**, de **tipagem estática** e **multiparadigma**, criada por Bjarne Stroustrup nos Bell Labs a partir de 1979 como extensão do C ("C with Classes"). Hoje é padronizada pela ISO/IEC (norma **ISO/IEC 14882**) e evolui em ciclos de três anos pelo comitê **WG21**.

## Características principais

| Característica | Significado prático |
|---|---|
| Compilada para código nativo | O programa vira instruções da CPU; não há máquina virtual obrigatória |
| Tipagem estática e forte | Tipos são verificados em tempo de compilação |
| Multiparadigma | Procedural, orientado a objetos, genérico (templates) e funcional (lambdas, ranges) |
| Acesso de baixo nível | Ponteiros, memória manual, controle de layout, interoperabilidade com C |
| Abstração de alto nível | Classes, templates, concepts, contêineres e algoritmos da biblioteca padrão |
| Sem coleta de lixo | Recursos são gerenciados deterministicamente (RAII) |

## Os três paradigmas em um único arquivo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

// 1) Procedural: função livre
int soma(int a, int b) { return a + b; }

// 2) Orientado a objetos: herança e polimorfismo
class Animal {
public:
    virtual ~Animal() = default;
    virtual std::string fala() const = 0;
};

class Gato : public Animal {
public:
    std::string fala() const override { return "miau"; }
};

// 3) Genérico: template de função
template <typename T>
T maior(T a, T b) { return a > b ? a : b; }

int main() {
    std::cout << soma(2, 3) << '\n';          // 5

    Gato g;
    const Animal& a = g;                      // referência para a base
    std::cout << a.fala() << '\n';            // miau (despacho dinâmico)

    std::cout << maior(3.5, 2.1) << '\n';     // 3.5 (T deduzido como double)

    std::vector<int> v{1, 2, 3};              // contêiner da biblioteca padrão
    std::cout << v.size() << '\n';            // 3
}
```

## C++ é "C com classes"?

Não mais. O C++ moderno (C++11 em diante) é uma linguagem muito diferente do C++ dos anos 1990. Evita-se `new`/`delete` manual, `malloc`, macros e arrays soltos; prefere-se `std::vector`, `std::string`, RAII (veja [[Filosofia do Cpp]]), smart pointers, lambdas e algoritmos.

> [!tip] Estilo moderno
> Ao ler material antigo na internet, desconfie de `char*`, `new[]`, `#define` para constantes e `using namespace std;` em cabeçalhos. Este vault ensina o **C++ moderno** (C++17/20/23, com notas sobre C++26).

> [!info] Quem decide o que é C++?
> O padrão ISO é a especificação oficial. Os compiladores ([[Compiladores GCC Clang e MSVC]]) implementam o padrão e podem acrescentar extensões. A referência pública mais usada é a cppreference.com; as regras de boas práticas estão nas *C++ Core Guidelines* (isocpp.github.io/CppCoreGuidelines).

## Veja também

- [[História e Evolução dos Padrões]]
- [[Filosofia do Cpp]]
- [[Casos de Uso do Cpp]]
- [[Cpp vs C]]
- [[Primeiro Programa]]

## Exercício

1. Cite três paradigmas suportados pelo C++ e um exemplo de recurso da linguagem para cada um.
2. Por que dizer que C++ é "compilado" implica que o mesmo executável não roda em qualquer sistema operacional?
