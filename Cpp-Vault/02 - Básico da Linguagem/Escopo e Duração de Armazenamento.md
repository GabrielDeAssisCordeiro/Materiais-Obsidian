---
titulo: "Escopo e duração de armazenamento"
tags: [cpp, basico, escopo, static]
aliases: ["Escopo", "Duração de armazenamento", "Storage duration"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Namespaces - Cpp]]", "[[Funções - Cpp]]", "[[Stack vs Heap]]"]
---

# Escopo e duração de armazenamento

Dois conceitos distintos:

- **Escopo**: a região do código onde um **nome** é visível.
- **Duração de armazenamento**: por quanto tempo o **objeto** existe na memória.

## Tipos de escopo

| Escopo | Onde | Visível |
|---|---|---|
| Bloco | Dentro de `{ }` (função, `if`, `for`...) | Do ponto da declaração até o `}` |
| Função | Rótulos de `goto` | Função inteira |
| Namespace / global | Fora de funções e classes | Da declaração em diante (e nas unidades que a declararem) |
| Classe | Membros | Dentro da classe e via acesso ao objeto |
| Enumeração | `enum class` | Só com qualificação (`Cor::Verde`) |

## Duração de armazenamento

| Duração | Como obter | Início → Fim |
|---|---|---|
| **Automática** | Variável local (sem `static`) | Entrada do bloco → saída do bloco (pilha) |
| **Estática** | Globais, `static` locais, membros `static` | Início (ou 1º uso, se local) → fim do programa |
| **Dinâmica** | `new`/`malloc`, `std::make_unique` | Até `delete`/`free` (heap) |
| **Thread** | `thread_local` | Criação da thread → fim da thread |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int global = 10;                 // estática (zero/constante inicializada)

int contador() {
    static int n = 0;            // estática: inicializada uma vez, na 1ª chamada
    return ++n;
}

int main() {
    int x = 1;                   // automática
    {
        int x = 2;               // sombreia (shadowing) o x externo
        std::cout << x << '\n';  // 2
    }
    std::cout << x << '\n';      // 1

    std::cout << contador() << contador() << contador() << '\n';   // 123

    for (int i = 0; i < 2; ++i) {
        int tmp = i * 10;        // criada e destruída a cada iteração
        std::cout << tmp << ' ';
    }
    std::cout << global << '\n';
}
```

> [!tip] Reduza o escopo
> Declare variáveis o mais perto possível do uso e no menor escopo. Use `-Wshadow` para detectar sombreamento acidental.

## `static` tem três sentidos

| Contexto | Significado |
|---|---|
| Variável local | Duração estática |
| Global/função em `.cpp` | **Ligação interna**: nome visível só naquele arquivo (prefira *namespace anônimo*) |
| Membro de classe | Pertence à classe, não ao objeto |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

namespace {                       // namespace anônimo: ligação interna (preferido a 'static' global)
    int segredo = 42;
    int ajuda() { return segredo + 1; }
}

int main() {
    std::cout << ajuda() << '\n';   // 43
}
```

## Ordem de inicialização de globais

Entre **unidades de tradução diferentes**, a ordem de inicialização de variáveis globais é **não especificada** (*static initialization order fiasco*).

> [!danger] Fiasco da ordem de inicialização
> Se `a.cpp` define `std::string nome = "x";` e `b.cpp` usa `nome` ao inicializar outro global, `nome` pode ainda não estar construído. **Correção:** use a *Meyers singleton* (variável `static` local dentro de função, inicializada no primeiro uso, e thread-safe desde o C++11) ou `constinit` (C++20).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

const std::string& nome() {
    static const std::string valor = "inicializado no primeiro uso";   // seguro
    return valor;
}

int main() { std::cout << nome() << '\n'; }
```

## Veja também

- [[Namespaces - Cpp]]
- [[Funções - Cpp]]
- [[Stack vs Heap]]
- [[const e constexpr]]

## Exercício

1. O que o programa imprime se você trocar `static int n = 0;` por `int n = 0;` em `contador()`?
2. Explique por que o namespace anônimo é preferido a `static` para esconder funções em um `.cpp`.
