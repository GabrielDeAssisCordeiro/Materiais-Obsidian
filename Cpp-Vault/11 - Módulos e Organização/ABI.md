---
titulo: "ABI (Application Binary Interface)"
tags: [cpp, organizacao, abi, extern-c]
aliases: ["Application Binary Interface", "Name mangling", "Itanium ABI", "_GLIBCXX_USE_CXX11_ABI"]
tipo: conceito
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Bibliotecas Estáticas e Dinâmicas]]", "[[Linkage]]", "[[vtable]]"]
---

# ABI (Application Binary Interface)

A **API** é o contrato em *código-fonte*; a **ABI** é o contrato em *binário*: layout de objetos, convenção de chamada, *name mangling*, tamanho de tipos, tratamento de exceções, layout de `vtable`. Dois binários só interoperam se concordarem na ABI.

| Aspecto da ABI | Exemplo |
|---|---|
| Convenção de chamada | Quais registradores levam argumentos |
| Layout de classes | Ordem/padding de membros, ponteiro de vtable ([[vtable]]) |
| *Name mangling* | `_Z4somaii` para `soma(int,int)` |
| Biblioteca padrão | Layout de `std::string`, `std::list`... |
| Exceções / RTTI | Formato das tabelas de desenrolamento |

Principais ABIs: **Itanium C++ ABI** (GCC, Clang em Linux/macOS), **Microsoft** (MSVC).

## Name mangling e `extern "C"`

O C++ codifica tipos no nome do símbolo para suportar [[Sobrecarga de Funções]]. C não faz isso. `extern "C"` desliga o *mangling* → permite chamar de C, Python (`ctypes`), Rust, etc.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

extern "C" int soma_c(int a, int b) { return a + b; }   // símbolo "soma_c", sem mangling
int soma(int a, int b) { return a + b; }                  // símbolo mangled (_Z4somaii)

int main() { std::cout << soma_c(1, 2) + soma(3, 4) << '\n'; }   // 10
```

```bash
g++ -c exemplo.cpp -o exemplo.o && nm exemplo.o | grep soma    # compare os símbolos
nm -C exemplo.o | grep soma                                     # -C demangle
```

## O que quebra a ABI

- Mudar membros de uma classe pública, adicionar métodos virtuais ou mudar a ordem deles.
- Mudar a assinatura de funções exportadas ou `inline` que mudam o código gerado.
- Compilar com versões diferentes da libstdc++ (a mudança de `std::string` em GCC 5, flag `_GLIBCXX_USE_CXX11_ABI`).
- Misturar *runtimes* MSVC diferentes (Debug/Release, `/MD` vs `/MT`).

> [!tip] Estratégias para API estável
> 1. Interface `extern "C"` com tipos simples e *handles* opacos.
> 2. **Pimpl**: esconde o layout dos dados ([[Pimpl]]).
> 3. Versionamento de símbolos / `inline namespace` versionados.
> 4. Distribuir fontes (header-only) para evitar o problema.

> [!warning] A ABI do C++ não é padronizada
> O padrão ISO **não** especifica ABI. Cada plataforma/compilador define a sua. Confirme a compatibilidade na documentação do toolchain.

## Veja também

- [[Bibliotecas Estáticas e Dinâmicas]]
- [[Linkage]]
- [[vtable]]
- [[Sobrecarga de Funções]]

## Exercício

1. Use `nm -C` para comparar símbolos de uma função com e sem `extern "C"`.
2. Escreva uma pequena lib `extern "C"` e chame-a de Python com `ctypes`.
