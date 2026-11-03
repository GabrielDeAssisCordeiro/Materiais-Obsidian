---
titulo: "Tabela de erros de compilador e linker"
tags: [cpp, referencia, erros, compilador, linker]
aliases: ["Erros comuns do compilador", "Erros de linker", "Mensagens de erro", "Tabela de erros"]
tipo: referencia
nivel: iniciante
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Declaração vs Definição e ODR]]", "[[Headers vs Sources]]", "[[Flags Essenciais do Compilador]]"]
---

# Tabela de erros de compilador e linker

> [!info] Como ler uma mensagem
> 1. Comece pela **primeira** linha `error:` (as demais costumam ser consequência).
> 2. Veja arquivo:linha. 3. Leia as linhas `note:` (candidatos, locais de declaração).
> 4. Em templates, procure a linha com `required from here` (onde **você** causou a instanciação).
> As mensagens abaixo são típicas de GCC/Clang e variam por versão.

## Erros de compilação

| Mensagem (resumo) | Causa provável | Solução |
|---|---|---|
| `'X' was not declared in this scope` / `use of undeclared identifier` | Faltou `#include`, `std::`, ou nome digitado errado | Incluir o header correto; `std::vector` |
| `expected ';' before ...` | Faltou `;` na linha anterior (ou depois de `class {}`) | Procure na linha **acima** |
| `no matching function for call to 'f(...)'` | Tipos/quantidade de argumentos não batem; nenhum *overload* serve | Leia as `note: candidate:`; converta/ajuste |
| `invalid conversion from 'const char*' to 'int'` | Conversão implícita inválida | `static_cast`, tipo correto |
| `cannot bind non-const lvalue reference to an rvalue` | `f(int&)` chamado com temporário | Use `const int&` ou passe uma variável |
| `passing 'const X' as 'this' argument discards qualifiers` | Chamou método **não-const** em objeto `const` | Marque o método como `const` |
| `use of deleted function` | Cópia de `unique_ptr`/tipo não copiável; função `= delete` | `std::move`, ou mude o design |
| `call of overloaded 'f(int)' is ambiguous` | Dois *overloads* igualmente bons | Cast explícito ou remova ambiguidade |
| `invalid use of incomplete type` / `forward declaration of 'X'` | Usou membros/`sizeof` de tipo só declarado | `#include` completo no `.cpp` |
| `'X' does not name a type` | Header faltando ou ciclo de includes | Include correto / forward declaration |
| `redefinition of 'struct X'` | Header incluído duas vezes sem guarda | `#pragma once` / include guard |
| `jump to case label crosses initialization` | Variável inicializada dentro de `case` | Envolva o `case` em `{ }` |
| `narrowing conversion of 'x' from 'double' to 'int' inside { }` | Inicialização com chaves proíbe perda | `static_cast` ou `=` |
| `cannot convert 'X*' to 'Y*'` entre classes não relacionadas | Ponteiros incompatíveis | `dynamic_cast`/design |
| `static assertion failed: ...` | `static_assert` ou concept violado | Leia a mensagem; ajuste tipos |
| `the value of 'x' is not usable in a constant expression` | Usou valor de execução em contexto `constexpr` | Torne a origem `constexpr` |
| `template argument deduction/substitution failed` | Argumentos incompatíveis com o template | Veja `required from here` e as `note:` |
| `no type named 'type' in 'struct std::enable_if<false,...>'` | SFINAE removeu o candidato | Verifique restrições/concepts |
| `'xyz' is not a member of 'std'` | Header/padrão errado (`-std`) ou nome de versão mais nova | Inclua o header; `-std=c++20/23` |
| `missing 'typename' prior to dependent type name` | Tipo dependente em template | `typename T::tipo` |
| `unused variable` / `-Wunused` | Aviso | Remova ou `[[maybe_unused]]` |
| `control reaches end of non-void function` | Faltou `return` em algum caminho (UB se alcançado) | Retorne em todos os caminhos |
| `comparison of integers of different signs` | `-Wsign-compare`: `int` com `size_t` | Mesmos tipos / `std::cmp_less` |
| `variable 'x' set but not used` / `may be used uninitialized` | Aviso de possível UB | Inicialize `T x{};` |

## Erros de linker

| Mensagem | Causa | Solução |
|---|---|---|
| `undefined reference to 'f(int)'` | Declarado mas **nunca definido**, ou o `.cpp`/biblioteca não foi ligado | Adicione o `.cpp` ao build; `-lbiblioteca` na **ordem** certa |
| `undefined reference to 'vtable for X'` | Método virtual declarado sem definição (ou destrutor virtual não definido) | Defina todos os virtuais não puros |
| `undefined reference to 'X::estatico'` | Membro `static` declarado, não definido | Defina em um `.cpp` ou use `inline static` (C++17) |
| `multiple definition of 'x'` | Definição não-`inline` em header incluído em várias TUs | `inline`/`constexpr`, ou mova para `.cpp` |
| `undefined reference to 'main'` | Sem função `main` (ou `main` em namespace) | Defina `int main()` global |
| `undefined reference to 'pthread_create'` / `std::thread` | Faltou `-pthread` (libs antigas) | `-pthread` / `Threads::Threads` |
| `cannot find -lxyz` | Biblioteca não instalada / caminho ausente | `-L` e pacote `-dev` |
| `error while loading shared libraries: libxyz.so` | Em execução: não achou a `.so` | `LD_LIBRARY_PATH`, `rpath`, instalar |
| `relocation R_X86_64_32 ... recompile with -fPIC` | Objeto não-PIC em biblioteca compartilhada | Compile com `-fPIC` |
| `undefined reference to 'std::filesystem::...'` | GCC < 9 | `-lstdc++fs` ou atualize |
| `undefined symbol ... _GLIBCXX_USE_CXX11_ABI` | Mistura de ABIs de `std::string` | Mesma flag/compilador em tudo ([[ABI]]) |

## Exemplo comentado

```cpp
// ERRO PROPOSITAL (não compila): ilustra "no matching function" e "const".
// Correção indicada nos comentários.
#include <iostream>
#include <string>

struct Conta {
    int saldo() { return 100; }             // BUG: deveria ser `const`
};

void mostra(const Conta& c) {
    std::cout << c.saldo();                 // ERRO: passing 'const Conta' as 'this' argument discards qualifiers
}                                           // CORREÇÃO: int saldo() const { ... }

int main() {
    std::string s = "a";
    // std::cout << s.append(1);            // ERRO: nenhum append(int) — CORREÇÃO: s.append(1, 'x')
    mostra(Conta{});
}
```

> [!tip] Ferramentas
> Use `-Wall -Wextra -Wpedantic`, o **Compiler Explorer** ([[Compiler Explorer]]) para reproduzir em outro compilador e `clang++` quando a mensagem do GCC estiver confusa (ou vice-versa).

## Veja também

- [[Declaração vs Definição e ODR]]
- [[Headers vs Sources]]
- [[Flags Essenciais do Compilador]]
- [[Catálogo de Armadilhas e UB]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Provoque cada um dos erros de linker da tabela em um mini-projeto de 2 arquivos e corrija.
2. Cole uma mensagem de erro de template longa e identifique a linha `required from here`.
