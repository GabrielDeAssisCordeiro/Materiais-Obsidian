---
titulo: "Exceções: try, catch, throw"
tags: [cpp, erros, excecoes]
aliases: ["Exceções", "try catch", "throw", "Stack unwinding", "Relançar exceção", "catch (...)"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Hierarquia de Exceções]]", "[[Segurança de Exceções]]", "[[RAII]]"]
---

# Exceções: `try`, `catch`, `throw`

Exceções são o mecanismo da linguagem para **sinalizar e propagar falhas** sem poluir o fluxo normal. Quando um erro ocorre, `throw` **desenrola a pilha** (*stack unwinding*) até encontrar um `catch` compatível, destruindo objetos automáticos no caminho (por isso [[RAII]] é essencial).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <stdexcept>
#include <string>

double divide(double a, double b) {
    if (b == 0) throw std::invalid_argument("divisão por zero");   // lança um objeto
    return a / b;
}

struct Guarda {
    ~Guarda() { std::cout << "limpando\n"; }                        // roda durante o desenrolamento
};

void processa() {
    Guarda g;
    std::cout << divide(1, 0) << '\n';                              // lança: g é destruído
}

int main() {
    try {
        processa();
    } catch (const std::invalid_argument& e) {                      // CAPTURE POR REFERÊNCIA CONST
        std::cout << "argumento inválido: " << e.what() << '\n';
    } catch (const std::exception& e) {                             // base: pega o resto da hierarquia padrão
        std::cout << "erro: " << e.what() << '\n';
    } catch (...) {                                                 // qualquer coisa (inclusive não-std)
        std::cout << "erro desconhecido\n";
    }
}
```

## Regras essenciais

| Regra | Motivo |
|---|---|
| **Lance por valor**, capture **por referência `const`** | Evita *slicing* e cópias; `catch (std::exception e)` fatiaria |
| Ordem dos `catch`: **do mais específico ao mais geral** | O primeiro compatível vence |
| Lance **tipos de `std::exception`** (ou derivados) | Interoperabilidade; `what()` |
| Nunca lance ponteiros nem tipos primitivos | Dificultam captura e posse |
| Relance com `throw;` (sem argumento) | Preserva o objeto original e o tipo dinâmico |
| **Não** deixe exceções escaparem de **destrutores** | Duas exceções ativas → `std::terminate` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <exception>
#include <iostream>
#include <stdexcept>

void camada_baixa() { throw std::runtime_error("falha de I/O"); }

void camada_media() {
    try {
        camada_baixa();
    } catch (const std::exception& e) {
        std::cout << "log: " << e.what() << '\n';
        throw;                                                       // relança A MESMA exceção
    }
}

void camada_alta() {
    try {
        camada_media();
    } catch (...) {
        // Encapsular com contexto adicional
        std::throw_with_nested(std::runtime_error("operação X falhou"));
    }
}

void imprime(const std::exception& e, int nivel = 0) {
    std::cout << std::string(nivel * 2, ' ') << e.what() << '\n';
    try { std::rethrow_if_nested(e); }
    catch (const std::exception& interna) { imprime(interna, nivel + 1); }
}

int main() {
    try { camada_alta(); }
    catch (const std::exception& e) { imprime(e); }
}
```

## `noexcept`, `terminate` e exceções não capturadas

- Exceção **não capturada** → `std::terminate()` → `abort()`.
- Função `noexcept` que lança → `std::terminate()` ([[noexcept e Movimento]]).
- `std::current_exception()`/`std::exception_ptr` transportam exceções entre threads.

> [!bug] Exemplo inválido proposital: *slicing* e ordem de `catch`
> ```cpp
> try { throw std::out_of_range("x"); }
> catch (std::exception e) { }              // captura por VALOR: fatia, perde o tipo dinâmico
> catch (const std::out_of_range&) { }      // inalcançável: o catch de cima já pegou (aviso do compilador)
> ```
> **Correção:** `catch (const std::out_of_range&)` primeiro e `catch (const std::exception&)` depois.

> [!danger] Lançar de um destrutor
> ```cpp
> struct Ruim { ~Ruim() noexcept(false) { throw 1; } };   // se já houver outra exceção ativa: terminate
> ```
> Destrutores devem ser `noexcept`; trate/registre erros dentro deles.

## Veja também

- [[Hierarquia de Exceções]]
- [[Segurança de Exceções]]
- [[Boas Práticas e Custo das Exceções]]
- [[RAII]]
- [[noexcept e Movimento]]

## Exercício

1. Escreva `int para_int(const std::string&)` que lance `std::invalid_argument` com mensagem útil; capture-a em `main` e imprima a cadeia de exceções aninhadas.
2. Teste o que acontece com uma exceção não capturada em `main` e como `std::set_terminate` pode registrá-la.
