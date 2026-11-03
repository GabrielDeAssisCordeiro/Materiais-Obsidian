---
titulo: "Pipeline de Compilação - Cpp"
tags: [cpp, fundamentos, compilacao, linker, preprocessador]
aliases: ["Modelo de compilação", "Pré-processador, compilador e linker", "Build pipeline"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Compiladores GCC Clang e MSVC]]", "[[Flags Essenciais do Compilador]]", "[[Primeiro Programa]]"]
---

# Pipeline de Compilação - Cpp

Transformar `.cpp` em um executável envolve quatro etapas.

```mermaid
flowchart LR
    A["main.cpp<br/>util.cpp"] -->|"1. Pré-processador<br/>(#include, #define)"| B["Unidade de tradução<br/>(.ii)"]
    B -->|"2. Compilador<br/>(parsing, templates, otimização)"| C["Assembly<br/>(.s)"]
    C -->|"3. Assembler"| D["Objeto<br/>(.o / .obj)"]
    D -->|"4. Linker<br/>+ bibliotecas"| E["Executável<br/>ou biblioteca"]
```

## 1. Pré-processamento

Trata diretivas que começam com `#`: `#include` copia o conteúdo de um cabeçalho, `#define` define macros, `#if`/`#ifdef` compila condicionalmente. O resultado é uma **unidade de tradução** (*translation unit*): um `.cpp` com todos os cabeçalhos expandidos.

## 2. Compilação

O compilador analisa a sintaxe, verifica tipos, instancia templates, otimiza e gera código de montagem (assembly). **Cada `.cpp` é compilado de forma independente.**

## 3. Montagem

O *assembler* converte assembly em código de máquina relocável: um arquivo objeto (`.o` no Unix, `.obj` no Windows).

## 4. Linkedição

O *linker* junta objetos e bibliotecas, resolve símbolos (uma função declarada em um arquivo e definida em outro) e produz o executável.

## Vendo cada etapa

```bash
# Etapa 1: apenas pré-processar (saída no terminal ou -o arquivo)
g++ -std=c++20 -E main.cpp -o main.ii

# Etapa 2: gerar assembly
g++ -std=c++20 -S main.cpp -o main.s

# Etapa 3: gerar objeto (sem linkar)
g++ -std=c++20 -c main.cpp -o main.o

# Etapa 4: linkar objetos em executável
g++ main.o util.o -o programa
```

## Exemplo com dois arquivos

```cpp
// util.hpp — declaração (o que existe)
#pragma once
int dobro(int x);
```

```cpp
// util.cpp — definição (como funciona)
#include "util.hpp"
int dobro(int x) { return 2 * x; }
```

```cpp
// main.cpp — uso
#include <iostream>
#include "util.hpp"

int main() {
    std::cout << dobro(21) << '\n';   // 42
}
```

```bash
g++ -std=c++20 -Wall -Wextra -c util.cpp
g++ -std=c++20 -Wall -Wextra -c main.cpp
g++ main.o util.o -o programa && ./programa
```

## Erros por etapa

| Etapa | Exemplo de erro | Causa típica |
|---|---|---|
| Pré-processador | `fatal error: foo.h: No such file or directory` | Caminho de include errado (`-I`) |
| Compilação | `error: 'x' was not declared in this scope` | Nome não declarado, erro de tipo, sintaxe |
| Linkedição | `undefined reference to 'dobro(int)'` | Função declarada mas nunca definida/linkada |
| Linkedição | `multiple definition of ...` | Mesma definição em duas unidades (violação da ODR) |

> [!bug] Exemplo inválido proposital: erro de linkedição
> Se compilar apenas `main.cpp` sem `util.cpp`:
> ```bash
> g++ -std=c++20 main.cpp -o programa
> # undefined reference to `dobro(int)'
> ```
> **Correção:** compile e linke também `util.cpp` (`g++ main.cpp util.cpp -o programa`).

> [!info] Módulos (C++20)
> Módulos substituem parte do modelo "copiar cabeçalhos" por interfaces compiladas. O pipeline muda, mas a ideia de unidades compiladas separadamente continua.

## Veja também

- [[Compiladores GCC Clang e MSVC]]
- [[Flags Essenciais do Compilador]]
- [[Primeiro Programa]]
- [[Cpp vs C]]

## Exercício

1. Rode `g++ -E` num programa que inclui `<iostream>` e conte as linhas da saída (`| wc -l`). O que isso diz sobre `#include`?
2. Provoque deliberadamente um erro de linkedição e outro de compilação. Como distingui-los?
