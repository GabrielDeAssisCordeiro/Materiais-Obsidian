---
titulo: "Pimpl (*Pointer to Implementation*)"
tags: [cpp, avancado, pimpl, abi, encapsulamento, compilacao]
aliases: ["Pimpl", "Pointer to Implementation", "Compilation firewall", "propagate_const"]
tipo: padrao
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Forward Declarations]]", "[[ABI]]", "[[unique_ptr]]"]
---

# Pimpl (*Pointer to Implementation*)

Esconde os **detalhes privados** de uma classe atrás de um ponteiro para uma `struct Impl` definida apenas no `.cpp`. A interface pública (header) não menciona membros nem inclui dependências pesadas.

**Benefícios:**
- **Compilação mais rápida**: mudar a implementação não recompila os clientes ([[Headers vs Sources]], [[ccache]]).
- **ABI estável**: o *layout* da classe pública (um ponteiro) não muda ([[ABI]]).
- **Isolamento de dependências**: headers de terceiros ficam só no `.cpp`.

**Custos:** uma alocação extra e uma indireção por objeto; código a mais.

```cpp
// arquivo: widget.hpp
#pragma once
#include <memory>
#include <string>

class Widget {
public:
    explicit Widget(std::string nome);
    ~Widget();                                   // declarado aqui, DEFINIDO no .cpp (Impl completo lá)
    Widget(Widget&&) noexcept;                   // movimentos também no .cpp
    Widget& operator=(Widget&&) noexcept;
    Widget(const Widget&);                       // cópia profunda (se desejada)
    Widget& operator=(const Widget&);

    void rotular(const std::string& texto);
    std::string descricao() const;

private:
    struct Impl;                                 // declaração antecipada
    std::unique_ptr<Impl> pimpl_;
};
```

```cpp
// arquivo: widget.cpp
#include "widget.hpp"
#include <vector>                                 // dependências "escondidas" ficam aqui

struct Widget::Impl {
    std::string nome;
    std::vector<std::string> rotulos;
};

Widget::Widget(std::string nome) : pimpl_{std::make_unique<Impl>(Impl{std::move(nome), {}})} {}
Widget::~Widget() = default;
Widget::Widget(Widget&&) noexcept = default;
Widget& Widget::operator=(Widget&&) noexcept = default;
Widget::Widget(const Widget& o) : pimpl_{std::make_unique<Impl>(*o.pimpl_)} {}
Widget& Widget::operator=(const Widget& o) { if (this != &o) *pimpl_ = *o.pimpl_; return *this; }

void Widget::rotular(const std::string& t) { pimpl_->rotulos.push_back(t); }
std::string Widget::descricao() const { return pimpl_->nome + " (" + std::to_string(pimpl_->rotulos.size()) + " rótulos)"; }
```

## Versão autocontida (compilável em um único arquivo)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

// ===== "widget.hpp" =====
class Widget {
public:
    explicit Widget(std::string nome);
    ~Widget();
    Widget(Widget&&) noexcept;
    Widget& operator=(Widget&&) noexcept;
    void rotular(const std::string& texto);
    std::string descricao() const;
private:
    struct Impl;
    std::unique_ptr<Impl> pimpl_;
};

// ===== "widget.cpp" =====
struct Widget::Impl { std::string nome; std::vector<std::string> rotulos; };

Widget::Widget(std::string nome) : pimpl_{std::make_unique<Impl>(Impl{std::move(nome), {}})} {}
Widget::~Widget() = default;
Widget::Widget(Widget&&) noexcept = default;
Widget& Widget::operator=(Widget&&) noexcept = default;
void Widget::rotular(const std::string& t) { pimpl_->rotulos.push_back(t); }
std::string Widget::descricao() const { return pimpl_->nome + " (" + std::to_string(pimpl_->rotulos.size()) + ")"; }

// ===== uso =====
int main() {
    Widget w{"botão"};
    w.rotular("ok");
    std::cout << w.descricao() << '\n';                          // botão (1)
}
```

> [!bug] Erro típico
> `error: invalid application of 'sizeof' to incomplete type 'Widget::Impl'`: o destrutor/movimentos foram gerados implicitamente no header, onde `Impl` é incompleto. Declare-os no header e defina `= default` no `.cpp` ([[Forward Declarations]]).

> [!warning] Constância "rasa"
> Em um método `const`, `pimpl_->` ainda permite **modificar** `Impl` (o ponteiro é const, o apontado não). Use `std::experimental::propagate_const` (Library Fundamentals TS) ou um wrapper próprio para propagar a constância ([[const em Métodos]]).

> [!tip] Alternativas
> Interface abstrata + fábrica (custo virtual), módulos C++20 ([[Módulos Cpp20]]) e *header-only* leve para reduzir dependências.

## Veja também

- [[Forward Declarations]]
- [[ABI]]
- [[unique_ptr]]
- [[const em Métodos]]
- [[Regra do 0, 3 e 5]]

## Exercício

1. Aplique Pimpl a uma classe `Logger` que inclui `<fstream>` e `<mutex>` e meça o tempo de recompilação dos clientes.
2. Implemente `propagate_const` simplificado e use-o em `Widget`.
