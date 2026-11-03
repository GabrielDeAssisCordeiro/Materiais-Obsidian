---
titulo: "Lista de inicialização de membros"
tags: [cpp, poo, construtores, inicializacao]
aliases: ["Lista de inicialização", "Member initializer list", "NSDMI", "Inicializadores de membro"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Construtores e Destrutores]]", "[[Classes e Structs]]", "[[Variáveis e Inicialização]]"]
---

# Lista de inicialização de membros

É a seção entre `:` e `{` do construtor, onde os membros são **inicializados** (não atribuídos).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

class Aluno {
public:
    Aluno(std::string nome, int ra)
        : nome_(std::move(nome)),      // inicializa direto, sem criar string vazia antes
          ra_(ra),
          notas_{} {}                  // vetor vazio explícito

    void add(double n) { notas_.push_back(n); }
    std::size_t qtd() const { return notas_.size(); }

private:
    std::string nome_;
    int ra_;
    std::vector<double> notas_;
    int turma_ = 1;                    // NSDMI (C++11): valor padrão, usado se o construtor não inicializar
};

int main() {
    Aluno a{"Ana", 123};
    a.add(9.5);
    std::cout << a.qtd() << '\n';      // 1
}
```

## Por que usar a lista (e não atribuir no corpo)

| Motivo | Explicação |
|---|---|
| **Obrigatória** para `const` e referências | Membros `const T` e `T&` precisam ser inicializados na criação |
| **Obrigatória** para membros sem construtor padrão | Não há como "atribuir" a algo que não pôde ser criado |
| **Obrigatória** para bases sem construtor padrão | `Derivada(int x) : Base(x) {}` |
| **Eficiência** | Evita construir um valor padrão e depois atribuir |

> [!bug] Exemplo inválido proposital
> ```cpp
> class A {
>     const int id_;
>     int& ref_;
> public:
>     A(int id, int& r) {          // erro: 'id_' e 'ref_' não inicializados
>         id_ = id;                // erro: atribuição a const
>         ref_ = r;
>     }
> };
> ```
> **Correção:** `A(int id, int& r) : id_(id), ref_(r) {}`.

## A ordem é a da **declaração**

Os membros são inicializados na ordem em que são **declarados na classe**, **não** na ordem da lista. `-Wall` avisa (`-Wreorder`).

> [!danger] Dependência de ordem
> ```cpp
> class B {
>     int b_;
>     int a_;
> public:
>     B(int x) : a_(x), b_(a_ * 2) {}   // ERRO LÓGICO: b_ é inicializado ANTES de a_ (lê a_ indeterminado)
> };
> ```
> **Correção:** declare `a_` antes de `b_`, ou use `x` diretamente: `b_(x * 2)`.

## NSDMI (*non-static data member initializers*)

Valores padrão na declaração reduzem repetição quando há vários construtores.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Janela {
public:
    Janela() = default;                         // usa todos os padrões
    explicit Janela(int largura) : largura_(largura) {}   // sobrescreve só um
    int largura() const { return largura_; }
    int altura() const { return altura_; }
private:
    int largura_ = 800;
    int altura_ = 600;
    bool visivel_ = true;
};

int main() {
    std::cout << Janela{}.largura() << ' ' << Janela{1024}.altura() << '\n';   // 800 600
}
```

## Inicializando bases e delegando

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Base {
    explicit Base(int v) : valor(v) {}
    int valor;
};

struct Derivada : Base {
    Derivada() : Derivada(7) {}                 // construtor delegante
    explicit Derivada(int v) : Base(v * 2), extra(v) {}   // inicializa a base primeiro
    int extra;
};

int main() {
    Derivada d;
    std::cout << d.valor << ' ' << d.extra << '\n';   // 14 7
}
```

> [!tip] Resumo
> Inicialize **tudo** na lista (ou com NSDMI), na ordem de declaração, e deixe o corpo do construtor para lógica adicional.

## Veja também

- [[Construtores e Destrutores]]
- [[Classes e Structs]]
- [[Variáveis e Inicialização]]
- [[Herança]]

## Exercício

1. Corrija a classe `B` acima e confirme o aviso `-Wreorder` antes da correção.
2. Crie uma classe com um membro `const std::string` e uma referência e inicialize ambos corretamente.
