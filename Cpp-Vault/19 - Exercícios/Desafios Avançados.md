---
titulo: "Desafios avançados"
tags: [cpp, exercicios, avancado, ub, performance]
aliases: ["Desafios avançados", "Lista 8"]
tipo: exercicio
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Avançado e Performance - Cpp]]", "[[Catálogo de Armadilhas e UB]]", "[[MOC - Exercícios - Cpp]]"]
---

# Desafios avançados

## 1. Caça aos bugs

O trecho abaixo tem **cinco** problemas (UB ou más práticas). Encontre-os e corrija.

```cpp
// ERRO: intencionalmente inválido (não compile como está)
#include <iostream>
#include <vector>
using namespace std;

int* cria() { int x = 42; return &x; }

int main() {
    int* p = new int[3];
    p[3] = 1;
    delete p;
    vector<int> v{1, 2, 3};
    for (auto x : v) if (x == 2) v.push_back(4);
    int y;
    cout << y << *cria() << endl;
}
```

> [!success] Gabarito
> 1. `return &x;` — ponteiro para local (*dangling*); use retorno por valor.
> 2. `p[3] = 1;` — escrita fora dos limites (`new int[3]` tem índices 0–2).
> 3. `delete p;` — deve ser `delete[] p;` (ou use `std::vector`/`unique_ptr<int[]>`).
> 4. `v.push_back` dentro do range-for — invalida iteradores ([[Complexidade e Invalidação de Iteradores]]).
> 5. `int y;` lido sem inicializar — valor indeterminado.
> Extra: `using namespace std;` e `endl` são más práticas, não UB.

Versão corrigida:

```cpp
// g++ -std=c++20 -Wall -Wextra -fsanitize=address,undefined
#include <algorithm>
#include <iostream>
#include <vector>

int cria() { return 42; }

int main() {
    std::vector<int> p(3);
    p.at(2) = 1;
    std::vector<int> v{1, 2, 3};
    const bool tem2 = std::ranges::find(v, 2) != v.end();
    if (tem2) v.push_back(4);
    int y{};
    std::cout << y << cria() << '\n';
}
```

## 2. AoS contra SoA

Escreva dois programas que somam a coordenada `x` de 1 milhão de partículas: um com `std::vector<Particula>` (*array of structs*, 5 campos) e outro com `std::vector<float> xs` (*struct of arrays*). Meça com `std::chrono`. Por que o segundo costuma ser mais rápido? ([[Cache e Localidade de Dados]])

> [!success] Gabarito

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <chrono>
#include <iostream>
#include <vector>

struct Particula { float x, y, z, vx, vy; };

template <typename F>
double medir_ms(F&& f) {
    auto t0 = std::chrono::steady_clock::now();
    f();
    return std::chrono::duration<double, std::milli>(std::chrono::steady_clock::now() - t0).count();
}

int main() {
    constexpr std::size_t N = 1'000'000;
    std::vector<Particula> aos(N, Particula{1, 2, 3, 4, 5});
    std::vector<float> xs(N, 1.0f);
    volatile float sink = 0;                       // evita que o compilador elimine os laços
    double t_aos = medir_ms([&] { float s = 0; for (auto& p : aos) s += p.x; sink = s; });
    double t_soa = medir_ms([&] { float s = 0; for (float x : xs) s += x; sink = s; });
    std::cout << "AoS " << t_aos << " ms | SoA " << t_soa << " ms\n";
}
```

> [!info] Interpretação
> No SoA cada linha de cache (64 B) traz 16 `x` úteis; no AoS traz ~3. Resultado depende do hardware: **meça** ([[Profiling e Benchmarking]]).

## 3. CRTP: contador de instâncias

Crie `Contador<T>` (CRTP) que conta quantas instâncias de cada classe derivada existem.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename T>
struct Contador {
    static inline int vivos = 0;
    Contador() { ++vivos; }
    Contador(const Contador&) { ++vivos; }
    ~Contador() { --vivos; }
};

struct A : Contador<A> {};
struct B : Contador<B> {};

int main() {
    A a1, a2;
    { B b; std::cout << A::vivos << ' ' << B::vivos << ' '; }
    std::cout << B::vivos << '\n';   // 2 1 0
}
```

## 4. Type erasure mínimo

Implemente `Imprimivel` que aceita **qualquer** tipo com `operator<<` sem herança comum e permite guardá-los em um `std::vector`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Imprimivel {
    struct Conceito {
        virtual ~Conceito() = default;
        virtual void imprime(std::ostream&) const = 0;
    };
    template <typename T>
    struct Modelo final : Conceito {
        T v;
        explicit Modelo(T x) : v(std::move(x)) {}
        void imprime(std::ostream& os) const override { os << v; }
    };
    std::shared_ptr<const Conceito> p_;
public:
    template <typename T>
    Imprimivel(T x) : p_(std::make_shared<Modelo<T>>(std::move(x))) {}
    friend std::ostream& operator<<(std::ostream& os, const Imprimivel& i) { i.p_->imprime(os); return os; }
};

int main() {
    std::vector<Imprimivel> v{1, 2.5, std::string("texto")};
    for (const auto& x : v) std::cout << x << ' ';
    std::cout << '\n';
}
```

## Veja também

- [[Catálogo de Armadilhas e UB]]
- [[Cache e Localidade de Dados]]
- [[CRTP e Mixins]]
- [[Type Erasure]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Compile a versão com bugs do desafio 1 (removendo o `using namespace`), rode com `-fsanitize=address,undefined` e relacione cada relatório a um item do gabarito.
