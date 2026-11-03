---
titulo: "Copy elision* e RVO"
tags: [cpp, move, cpp17]
aliases: ["Copy elision", "RVO", "NRVO", "Return value optimization", "Elisão de cópia"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Semântica de Movimento]]", "[[std move e std forward]]", "[[Funções - Cpp]]"]
---

# *Copy elision* e RVO

**Elisão de cópia** é a omissão de uma cópia/movimento: o objeto é construído **diretamente** onde será usado.

## Duas formas

| Forma | Quando | Garantida? |
|---|---|---|
| **RVO** (*Return Value Optimization*) | Retornar um **prvalue** (temporário): `return T{...};` | **Sim, desde o C++17** (nem exige construtor de cópia/movimento) |
| **NRVO** (*Named RVO*) | Retornar uma **variável local nomeada**: `T r; ... return r;` | **Não** (permitida; compiladores a aplicam com frequência) |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Rastreia {
    Rastreia()                  { std::cout << "ctor\n"; }
    Rastreia(const Rastreia&)   { std::cout << "cópia\n"; }
    Rastreia(Rastreia&&) noexcept { std::cout << "move\n"; }
    ~Rastreia()                 { std::cout << "dtor\n"; }
};

Rastreia rvo()  { return Rastreia{}; }          // C++17: construído direto no chamador: só "ctor"

Rastreia nrvo() {
    Rastreia r;                                 // variável nomeada
    return r;                                   // NRVO (típico): só "ctor"; se não elidir, move automático
}

Rastreia talvez(bool b) {
    Rastreia x, y;
    return b ? x : y;                           // dois candidatos: NRVO inviável; usa cópia/move
}

int main() {
    std::cout << "-- rvo\n";    Rastreia a = rvo();
    std::cout << "-- nrvo\n";   Rastreia b = nrvo();
    std::cout << "-- talvez\n"; Rastreia c = talvez(true);
    std::cout << "-- fim\n";
}
```

Em `-O0` GCC/Clang ainda aplicam RVO/NRVO (desative com `-fno-elide-constructors` para observar as cópias/movimentos; a elisão obrigatória do C++17 continua).

## Regras práticas

> [!tip] Retorne por valor
> `std::vector<int> cria() { std::vector<int> v; ...; return v; }` é **barato**: NRVO ou movimento. Não use parâmetros de saída (`void f(std::vector<int>& out)`) por desempenho em código moderno.

> [!bug] Anti-padrão: `return std::move(local);`
> ```cpp
> std::vector<int> f() {
>     std::vector<int> v(1000);
>     return std::move(v);     // IMPEDE NRVO: força um movimento (pior que a elisão)
> }
> ```
> `-Wpessimizing-move` e `-Wredundant-move` (GCC/Clang) detectam.

> [!warning] Quando o retorno vira cópia/movimento
> - Retornar **membro** (`return this->dados_;`) copia (não é local).
> - Retornar **parâmetro por valor**: `return param;` move automaticamente.
> - Retornar **dois objetos distintos** conforme condição: sem NRVO.
> - Retornar com `std::move` explícito.

## Elisão em outros contextos (C++17)

```cpp
Rastreia t = Rastreia{};            // C++17: sem cópia/move, mesmo em inicialização
void f(Rastreia);
f(Rastreia{});                      // o temporário é construído direto no parâmetro
```

## Veja também

- [[Semântica de Movimento]]
- [[std move e std forward]]
- [[Construtores de Cópia e Atribuição]]
- [[Funções - Cpp]]

## Exercício

1. Compile o programa com e sem `-fno-elide-constructors` em `-std=c++14` e `-std=c++17` e compare as saídas.
2. Reescreva uma função com parâmetro de saída para retornar por valor e meça.
