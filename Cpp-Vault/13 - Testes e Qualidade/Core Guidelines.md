---
titulo: "C++ Core Guidelines"
tags: [cpp, qualidade, boas-praticas]
aliases: ["Core Guidelines", "C++ Core Guidelines", "CppCoreGuidelines", "GSL", "Guideline Support Library", "Boas práticas"]
tipo: referencia
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[clang-tidy e cppcheck]]", "[[RAII]]", "[[Regra do 0, 3 e 5]]"]
---

# C++ Core Guidelines

Conjunto de diretrizes editado por **Bjarne Stroustrup e Herb Sutter** (github.com/isocpp/CppCoreGuidelines) para escrever C++ moderno, seguro e eficiente. As regras têm IDs (`R.1`, `C.21`, `ES.20`...) e muitas podem ser verificadas por ferramentas ([[clang-tidy e cppcheck]]: grupo `cppcoreguidelines-*`; analisador do Visual Studio).

| Seção | Prefixo | Exemplos de regras |
|---|---|---|
| Filosofia | P | P.1 Expresse ideias diretamente no código |
| Interfaces | I | I.4 Torne interfaces precisamente e fortemente tipadas |
| Funções | F | F.16 Passe tipos baratos por valor, os demais por `const&` |
| Classes | C | **C.20 Regra do zero**; C.21 se definir um, defina todos (3/5) |
| Enumerações | Enum | Enum.3 Prefira `enum class` |
| Recursos | R | **R.1 Gerencie recursos automaticamente (RAII)**; R.11 evite `new`/`delete` explícitos |
| Expressões e instruções | ES | ES.20 Sempre inicialize um objeto; ES.46 evite conversões com perda |
| Desempenho | Per | Per.1 Não otimize sem motivo; Per.2 Não otimize prematuramente |
| Concorrência | CP | CP.20 Use RAII, nunca `lock()`/`unlock()` simples |
| Erros | E | E.2 Lance exceção para sinalizar que uma função não cumpre sua tarefa |
| Constantes | Con | Con.1 Por padrão, torne objetos imutáveis |
| Templates | T | T.10 Especifique concepts para todos os argumentos |
| Biblioteca padrão | SL | SL.con.1 Prefira `std::array`/`vector` a arrays C |

## Exemplos práticos

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <span>
#include <string>
#include <vector>

// F.16 / F.24: parâmetros baratos por valor; intervalos como span; I.12 ponteiro não nulo → referência
double media(std::span<const double> xs) {                       // em vez de (const double*, int)
    if (xs.empty()) return 0.0;
    double s = 0.0;
    for (double x : xs) s += x;
    return s / static_cast<double>(xs.size());
}

// R.20/R.21: ownership explícito com unique_ptr; C.20: regra do zero (nenhum special member)
struct Aluno {
    std::string nome;
    std::vector<double> notas;
};

// Con.1 / ES.20: const por padrão, sempre inicializar
int main() {
    const std::vector<double> notas{7.5, 8.0, 9.0};
    const auto a = std::make_unique<Aluno>(Aluno{"Ana", notas});
    std::cout << a->nome << ' ' << media(a->notas) << '\n';
}
```

## Guideline Support Library (GSL)

Biblioteca com tipos que ajudam a seguir as regras: `gsl::not_null<T*>`, `gsl::owner<T*>`, `gsl::span` (hoje `std::span`), `gsl::narrow` (conversão checada), `gsl::finally`, `Expects()`/`Ensures()`. Implementações: Microsoft GSL.

> [!info] Perfis de segurança
> As **safety profiles** (tipos, limites, ciclo de vida) propõem checagens estáticas guiadas por essas regras; veja a seção Avançado e Performance e [[Cpp26 Visão Geral]] para o estado atual.

> [!tip] Como adotar
> Não leia tudo de uma vez. Habilite os *checks* `cppcoreguidelines-*` aos poucos, comece por **R** (recursos), **ES.20** (inicialização) e **C.20** (regra do zero) — veja [[Regra do 0, 3 e 5]].

## Veja também

- [[clang-tidy e cppcheck]]
- [[RAII]]
- [[Regra do 0, 3 e 5]]
- [[Segurança e Hardening]]
- [[Filosofia do Cpp]]

## Exercício

1. Escolha 5 regras e procure violações em um projeto seu.
2. Habilite `cppcoreguidelines-*` no clang-tidy e liste os 3 achados mais úteis.
