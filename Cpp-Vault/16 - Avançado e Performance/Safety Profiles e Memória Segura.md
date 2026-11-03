---
titulo: "Safety profiles* e memória segura"
tags: [cpp, seguranca, cpp26, contratos]
aliases: ["Safety profiles", "Perfis de segurança", "Rust vs C++", "Contracts", "Lifetime profile", "Segurança de memória em C++"]
tipo: conceito
nivel: avancado
padrao: C++26
criado: 2026-10-24
relacionados: ["[[Segurança e Hardening]]", "[[Core Guidelines]]", "[[Asserts e Contratos]]"]
---

# *Safety profiles* e memória segura

Governos e a indústria pressionam por **linguagens memory-safe**. O C++ responde em várias frentes: **hardening** da biblioteca, **contratos**, **comportamento errôneo** e **perfis de segurança** (*profiles*).

> [!info] Estado em 2026-10-24 (pesquisa do vault)
> - **C++26**: contratos (P2900), biblioteca padrão *hardened* (P3471), leituras não inicializadas como *erroneous behavior* (P2795) — [[Cpp26 Visão Geral]].
> - **Profiles**: proposta (Stroustrup, Sutter e outros) de conjuntos nomeados de regras verificadas por compilador/analisador (tipos, limites, ciclo de vida/ponteiros). Discussão e *design* continuam em andamento no comitê; **não** presuma que fazem parte do C++26.
> [!question] Verificar na documentação oficial
> Confirme o estado atual no site do comitê (isocpp.org / open-std.org WG21) antes de afirmar que um perfil está padronizado.

## Os três grandes objetivos

| Garantia | Problema que ataca | Mecanismo atual |
|---|---|---|
| **Tipos** | Conversões e `reinterpret_cast`, `union` mal usada | Warnings, `std::variant`, `std::bit_cast` |
| **Limites** (*bounds*) | Estouro de buffer | `std::span`, `at()`, hardened library |
| **Ciclo de vida** (*lifetime*) | *Dangling*, use-after-free | Análise estática (clang `-Wdangling`, `[[clang::lifetimebound]]`), RAII |
| **Inicialização** | Leitura de valor indeterminado | `-ftrivial-auto-var-init`, C++26 erroneous behavior |
| **Concorrência** | Data races | TSan, tipos *thread-safe* |

## Ferramentas já utilizáveis hoje

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <string_view>

// Warning útil: retornar view de temporário (GCC 13 detecta algumas formas com -Wdangling-pointer/-Wreturn-local-addr)
std::string_view pior_caso() {
    std::string s = "temporária";
    return s;                       // BUG PROPOSITAL: view aponta para memória destruída (UB ao usar)
}

int main() {
    std::string seguro = "dado";
    std::string_view v = seguro;    // OK enquanto 'seguro' viver
    std::cout << v << '\n';
    // std::cout << pior_caso();    // NÃO descomente: UB (use-after-free)
}
```

> [!bug] Correção
> Retorne `std::string` por valor. Em Clang, `[[clang::lifetimebound]]` ajuda a detectar casos como `std::string_view f(const std::string& s [[clang::lifetimebound]])` usados com temporários.

| Mecanismo | O que oferece |
|---|---|
| **Contratos C++26** | `pre(...)`, `post(...)`, `contract_assert` — verificação semântica configurável ([[Asserts e Contratos]]) |
| **Hardened library** | Pré-condições da biblioteca padrão verificadas (ver [[Segurança e Hardening]]) |
| **Core Guidelines + GSL** | Regras e tipos (`not_null`, `owner`) verificáveis com clang-tidy ([[Core Guidelines]]) |
| **Clang `-fbounds-safety`** (extensão) | Anotações de limites (suporte e estado: verificar) |
| **Rust/C++ interop** (cxx, autocxx) | Migração gradual de componentes críticos |
| **Linguagens seguras para novos módulos** | Estratégia "novo código seguro, legado endurecido" |

## Estratégia pragmática para equipes

1. Habilite warnings e `-Werror` em novos módulos; adote Core Guidelines gradualmente.
2. Compile com **hardening** e **bibliotecas endurecidas** em produção.
3. Rode **sanitizers e fuzzing** em CI.
4. Reduza a superfície: `span`, `string_view` **com cuidado**, RAII, sem `new` cru.
5. Isole parsers e código de entrada não confiável (processo separado, *sandbox*).
6. Acompanhe o comitê (profiles/contratos) e atualize padrões de código.

## Veja também

- [[Segurança e Hardening]]
- [[Core Guidelines]]
- [[Asserts e Contratos]]
- [[Cpp26 Visão Geral]]
- [[Sanitizers]]

## Exercício

1. Habilite `-Wdangling-pointer`/`-Wreturn-local-addr` e provoque um aviso com o exemplo.
2. Liste 3 funções do seu código que recebem `(ptr, n)` e converta para `std::span`.
