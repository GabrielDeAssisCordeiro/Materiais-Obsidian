---
titulo: "Classes abstratas e interfaces"
tags: [cpp, poo, interface]
aliases: ["Classe abstrata", "Função virtual pura", "= 0"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Polimorfismo e Funções Virtuais]]", "[[override e final]]", "[[Herança]]"]
---

# Classes abstratas e interfaces

Uma classe com **ao menos uma função virtual pura** (`= 0`) é **abstrata**: não pode ser instanciada, só serve como contrato para classes derivadas.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <string>

class Logger {                                     // "interface": só virtuais puras e destrutor virtual
public:
    virtual ~Logger() = default;
    virtual void log(const std::string& msg) = 0;
};

class LoggerConsole : public Logger {
public:
    void log(const std::string& msg) override { std::cout << "[console] " << msg << '\n'; }
};

class LoggerNulo : public Logger {                 // útil em testes
public:
    void log(const std::string&) override {}
};

class Servico {
public:
    explicit Servico(std::unique_ptr<Logger> l) : logger_(std::move(l)) {}   // injeção de dependência
    void executar() { logger_->log("executando"); }
private:
    std::unique_ptr<Logger> logger_;
};

int main() {
    Servico s{std::make_unique<LoggerConsole>()};
    s.executar();                                  // [console] executando
    // Logger l;                                   // erro: Logger é abstrata
}
```

## Pontos importantes

- Uma classe é abstrata enquanto **qualquer** virtual pura não tiver sido sobrescrita.
- Uma virtual pura **pode ter definição** (útil para destrutor puro ou implementação padrão chamável por `Base::f()`).
- C++ **não tem** a palavra-chave `interface`; usa-se uma classe abstrata sem dados.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Base {
    virtual ~Base() = 0;                           // destrutor puro: exige definição
};
Base::~Base() { std::cout << "~Base\n"; }          // definição obrigatória

struct D : Base {};

int main() { D d; }                                // imprime ~Base
```

> [!bug] Exemplo inválido proposital
> ```cpp
> struct Forma { virtual double area() const = 0; };
> Forma f;                    // erro: cannot declare variable 'f' to be of abstract type
> void usa(Forma f);          // erro: passagem por valor de tipo abstrato
> ```
> **Correção:** use ponteiros/referências (`Forma&`, `std::unique_ptr<Forma>`).

## NVI: *Non-Virtual Interface*

A interface **pública** é não virtual; a personalização está em virtuais **privadas**. Isso permite à base impor pré/pós-condições, *logging* e travamento em um ponto único.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Relatorio {
public:
    virtual ~Relatorio() = default;
    void gerar() const {                           // público, não virtual
        std::cout << "--- início ---\n";
        corpo();                                   // ponto de personalização
        std::cout << "--- fim ---\n";
    }
private:
    virtual void corpo() const = 0;                // privada e virtual
};

class RelatorioVendas : public Relatorio {
private:
    void corpo() const override { std::cout << "vendas: 100\n"; }
};

int main() { RelatorioVendas{}.gerar(); }
```

> [!tip] Interfaces sem custo de herança
> Para polimorfismo estático, use **concepts** (seção de templates). Para polimorfismo dinâmico sem hierarquia, veja *type erasure* na seção de avançado.

## Veja também

- [[Polimorfismo e Funções Virtuais]]
- [[override e final]]
- [[Herança]]
- [[vtable]]

## Exercício

1. Crie a interface `Repositorio` com `salvar` e `buscar` e duas implementações (em memória e em arquivo).
2. Por que uma virtual pura ainda pode ter corpo? Dê um caso de uso.
