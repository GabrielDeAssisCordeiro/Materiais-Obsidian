---
titulo: "Construtores e destrutores"
tags: [cpp, poo, construtores, destrutores, ciclo-de-vida]
aliases: ["Construtores", "Destrutores", "Ciclo de vida de objetos", "Construtor delegante"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Lista de Inicialização]]", "[[Classes e Structs]]", "[[default e delete]]"]
---

# Construtores e destrutores

- **Construtor**: função especial chamada **quando o objeto nasce**; garante que ele comece em estado válido (invariantes).
- **Destrutor** (`~Classe()`): chamado **quando o objeto morre**; libera recursos.

## Ciclo de vida

```mermaid
stateDiagram-v2
    [*] --> Construído: construtor
    Construído --> Construído: uso
    Construído --> Movido: std::move
    Movido --> Destruído: destrutor
    Construído --> Destruído: fim do escopo / delete / exceção
    Destruído --> [*]
```

## Tipos de construtores

| Tipo | Assinatura típica | Quando é usado |
|---|---|---|
| Padrão | `T()` | `T t;`, `T t{};`, elementos de `vector<T>(n)` |
| Parametrizado | `T(int, std::string)` | `T t{1, "a"};` |
| Cópia | `T(const T&)` | `T b = a;`, passagem por valor |
| Movimento (C++11) | `T(T&&) noexcept` | `T b = std::move(a);`, retorno temporário |
| Conversão | `T(int)` (sem `explicit`) | Conversão implícita — veja [[Conversões Implícitas e explicit]] |
| Delegante (C++11) | `T() : T(0) {}` | Um construtor chama outro |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

class Pessoa {
public:
    Pessoa() : Pessoa("anônimo", 0) { std::cout << "padrão\n"; }          // delegante
    Pessoa(std::string nome, int idade)
        : nome_(std::move(nome)), idade_(idade) { std::cout << "param: " << nome_ << '\n'; }
    Pessoa(const Pessoa& o) : nome_(o.nome_), idade_(o.idade_) { std::cout << "cópia\n"; }
    Pessoa(Pessoa&& o) noexcept : nome_(std::move(o.nome_)), idade_(o.idade_) { std::cout << "move\n"; }
    ~Pessoa() { std::cout << "~" << nome_ << '\n'; }

private:
    std::string nome_;
    int idade_;
};

int main() {
    Pessoa a;                       // padrão
    Pessoa b{"Bia", 20};            // param
    Pessoa c = b;                   // cópia
    Pessoa d = std::move(b);        // move (b fica "movido")
    std::cout << "fim de main\n";
}   // destrutores em ordem INVERSA da construção: d, c, b, a
```

## Ordem de construção e destruição

1. **Classes base**, na ordem em que aparecem na lista de bases.
2. **Membros**, na **ordem de declaração** na classe (não na lista de inicialização — [[Lista de Inicialização]]).
3. Corpo do construtor.

A destruição acontece na ordem **inversa**. Objetos locais são destruídos em ordem inversa à criação.

## O construtor padrão implícito

O compilador gera `T()` **somente se você não declarar nenhum construtor**. Se declarar qualquer um, peça o padrão explicitamente com `T() = default;` ([[default e delete]]).

> [!bug] *Most vexing parse*
> ```cpp
> Pessoa p();        // NÃO cria objeto: declara uma função p que retorna Pessoa
> Pessoa q;          // correto
> Pessoa r{};        // correto (preferido)
> ```

## Destrutores

- Liberam recursos (memória, arquivos, locks). É a base do **RAII** (seção de RAII e Move).
- São `noexcept` por padrão: **não deixe exceções escaparem**.
- Em classes com **herança polimórfica**, o destrutor da base deve ser `virtual` ([[Polimorfismo e Funções Virtuais]]).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdio>

class Arquivo {
public:
    explicit Arquivo(const char* caminho) : f_(std::fopen(caminho, "w")) {}
    ~Arquivo() { if (f_) std::fclose(f_); }                // sempre fecha, mesmo com exceção
    Arquivo(const Arquivo&) = delete;                      // evita dois donos do mesmo FILE*
    Arquivo& operator=(const Arquivo&) = delete;
    bool aberto() const { return f_ != nullptr; }
private:
    std::FILE* f_;
};

int main() {
    Arquivo a{"/tmp/saida.txt"};
    return a.aberto() ? 0 : 1;
}
```

> [!danger] Destruir polimorficamente sem destrutor virtual é UB
> ```cpp
> struct Base { ~Base() {} };                 // não virtual
> struct Derivada : Base { int* p = new int; ~Derivada() { delete p; } };
> Base* b = new Derivada;
> delete b;                                   // UB: só ~Base roda; vaza p
> ```
> **Correção:** `virtual ~Base() = default;`.

## Veja também

- [[Lista de Inicialização]]
- [[Classes e Structs]]
- [[default e delete]]
- [[Conversões Implícitas e explicit]]
- [[Polimorfismo e Funções Virtuais]]

## Exercício

1. Escreva uma classe `Rastreador` que imprime em cada construtor, cópia, movimento e destrutor, e passe-a por valor a uma função para ver a sequência.
2. Em qual ordem os destrutores serão chamados para três objetos locais `a`, `b`, `c` criados nessa ordem?
