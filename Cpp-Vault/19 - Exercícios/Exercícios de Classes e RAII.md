---
titulo: "Exercícios de Classes e RAII"
tags: [cpp, exercicios, classes, raii, poo]
aliases: ["Exercícios de classes"]
tipo: exercicio
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Classes e POO]]", "[[MOC - RAII e Move]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de Classes e RAII

Teoria: [[Classes e Structs]], [[Sobrecarga de Operadores - Cpp]], [[Polimorfismo e Funções Virtuais]], [[RAII]], [[Regra do 0, 3 e 5]].

## 1. `Ponto` com operadores

Crie `struct Ponto { double x, y; }` com `operator+` e `operator<<`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Ponto {
    double x{}, y{};
    friend Ponto operator+(Ponto a, Ponto b) { return {a.x + b.x, a.y + b.y}; }
    friend std::ostream& operator<<(std::ostream& os, Ponto p) { return os << '(' << p.x << ", " << p.y << ')'; }
    bool operator==(const Ponto&) const = default;   // C++20
};

int main() { std::cout << Ponto{1, 2} + Ponto{3, 4} << '\n'; }   // (4, 6)
```

## 2. Hierarquia de formas

Crie `Forma` abstrata (`area()`), `Circulo` e `Retangulo`; guarde-os em `std::vector<std::unique_ptr<Forma>>` e some as áreas.

> [!warning] Destrutor virtual
> Sem `virtual ~Forma()`, destruir via ponteiro base é UB.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <numbers>
#include <vector>

struct Forma {
    virtual ~Forma() = default;
    virtual double area() const = 0;
};
struct Circulo final : Forma {
    double r;
    explicit Circulo(double r) : r(r) {}
    double area() const override { return std::numbers::pi * r * r; }
};
struct Retangulo final : Forma {
    double l, a;
    Retangulo(double l, double a) : l(l), a(a) {}
    double area() const override { return l * a; }
};

int main() {
    std::vector<std::unique_ptr<Forma>> v;
    v.push_back(std::make_unique<Circulo>(1.0));
    v.push_back(std::make_unique<Retangulo>(2.0, 3.0));
    double total = 0;
    for (const auto& f : v) total += f->area();
    std::cout << total << '\n';
}
```

## 3. RAII para `FILE*` (move-only)

Escreva `Arquivo` que abre no construtor, fecha no destrutor, é **movível** e **não copiável**.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdio>
#include <iostream>
#include <stdexcept>
#include <utility>

class Arquivo {
    std::FILE* f_ = nullptr;
public:
    Arquivo(const char* caminho, const char* modo) : f_(std::fopen(caminho, modo)) {
        if (!f_) throw std::runtime_error("falha ao abrir arquivo");
    }
    ~Arquivo() { if (f_) std::fclose(f_); }
    Arquivo(const Arquivo&) = delete;
    Arquivo& operator=(const Arquivo&) = delete;
    Arquivo(Arquivo&& o) noexcept : f_(std::exchange(o.f_, nullptr)) {}
    Arquivo& operator=(Arquivo&& o) noexcept {
        if (this != &o) { if (f_) std::fclose(f_); f_ = std::exchange(o.f_, nullptr); }
        return *this;
    }
    void escrever(const char* s) { std::fputs(s, f_); }
};

int main() {
    Arquivo a("/tmp/exercicio_raii.txt", "w");
    a.escrever("ola\n");
    Arquivo b = std::move(a);          // a fica vazio
    b.escrever("mundo\n");
    std::cout << "ok\n";
}                                       // fecha uma única vez
```

## 4. Regra dos 5 em `Buffer`

Implemente `Buffer` com `std::size_t n_` e `int* dados_` (alocado com `new[]`) com cópia profunda e movimento.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <utility>

class Buffer {
    std::size_t n_ = 0;
    int* dados_ = nullptr;
public:
    explicit Buffer(std::size_t n) : n_(n), dados_(new int[n]{}) {}
    ~Buffer() { delete[] dados_; }
    Buffer(const Buffer& o) : n_(o.n_), dados_(new int[o.n_]) { std::copy(o.dados_, o.dados_ + n_, dados_); }
    Buffer& operator=(const Buffer& o) { Buffer t(o); swap(t); return *this; }   // copy-and-swap
    Buffer(Buffer&& o) noexcept : n_(std::exchange(o.n_, 0)), dados_(std::exchange(o.dados_, nullptr)) {}
    Buffer& operator=(Buffer&& o) noexcept { Buffer t(std::move(o)); swap(t); return *this; }
    void swap(Buffer& o) noexcept { std::swap(n_, o.n_); std::swap(dados_, o.dados_); }
    int& operator[](std::size_t i) { return dados_[i]; }
    std::size_t tamanho() const { return n_; }
};

int main() {
    Buffer a(3);
    a[0] = 7;
    Buffer b = a;              // cópia profunda
    b[0] = 9;
    Buffer c = std::move(a);   // movimento
    std::cout << b[0] << ' ' << c[0] << ' ' << c.tamanho() << '\n';   // 9 7 3
}
```

> [!tip] Melhor ainda
> Em código real, use `std::vector<int>` e siga a **Regra do 0**.

## Veja também

- [[Classes e Structs]]
- [[Sobrecarga de Operadores - Cpp]]
- [[RAII]]
- [[Semântica de Movimento]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Reescreva o exercício 4 com `std::vector<int>` e remova todos os membros especiais. O que mudou no comportamento?
