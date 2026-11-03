---
titulo: "Forward declarations"
tags: [cpp, organizacao, dependencias, pimpl]
aliases: ["Forward declaration", "Declaração antecipada", "Tipo incompleto", "Dependência circular"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Headers vs Sources]]", "[[Include Guards e pragma once]]", "[[unique_ptr]]"]
---

# Forward declarations

Uma **forward declaration** (`class Motor;`) apresenta o nome sem a definição: o tipo fica **incompleto**. Isso reduz `#include`s, acelera a compilação e quebra dependências circulares.

## O que se pode fazer com tipo incompleto

| Permitido | Não permitido |
|---|---|
| Declarar ponteiros e referências (`Motor*`, `Motor&`) | Criar objetos (`Motor m;`) |
| Declarar parâmetros/retorno **em declarações de função** | Usar membros (`m->ligar()`), `sizeof`, herdar |
| `std::unique_ptr<Motor>` como membro* | Definir função que desreferencia sem ver a classe |

\* desde que o destrutor/construtores sejam definidos **onde o tipo é completo** (no `.cpp`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>

class Motor;                                   // forward declaration

class Carro {
public:
    Carro();
    ~Carro();                                   // definido DEPOIS, onde Motor é completo
    void ligar();
private:
    std::unique_ptr<Motor> motor_;              // OK com tipo incompleto
};

class Motor {
public:
    void ligar() { std::cout << "vruum\n"; }
};

Carro::Carro() : motor_{std::make_unique<Motor>()} {}
Carro::~Carro() = default;
void Carro::ligar() { motor_->ligar(); }

int main() { Carro c; c.ligar(); }
```

> [!bug] Erro típico com `unique_ptr`
> Se o destrutor for gerado implicitamente num header onde `Motor` é incompleto: `error: invalid application of 'sizeof' to incomplete type`. Declare `~Carro();` no header e defina `= default` no `.cpp` — é o idioma **pimpl** ([[Pimpl]]).

## Dependência circular

```cpp
// arquivo: a.hpp
#pragma once
class B;                                       // em vez de #include "b.hpp"
class A { B* b_ = nullptr; };
```

```cpp
// arquivo: b.hpp
#pragma once
#include "a.hpp"
class B { A a_; };
```

> [!warning] Exceções à regra
> Enums com tipo subjacente fixo podem ser declarados antecipadamente (`enum class Cor : int;`). Tipos da biblioteca padrão (`std::string`, `std::vector`) **não** devem ser declarados por você (comportamento indefinido); inclua `<iosfwd>` para streams.

## Veja também

- [[Headers vs Sources]]
- [[Include Guards e pragma once]]
- [[unique_ptr]]
- [[Declaração vs Definição e ODR]]

## Exercício

1. Quebre um ciclo `Pessoa` ↔ `Empresa` com forward declarations e `shared_ptr`/`weak_ptr` ([[weak_ptr]]).
2. Meça o tempo de compilação antes/depois de trocar `#include` por forward declaration em um header grande.
