---
titulo: "Códigos de erro e std::error_code"
tags: [cpp, erros]
aliases: ["error_code", "std::error_code", "error_category", "errc", "Códigos de erro", "errno", "system_error"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[expected]]", "[[Exceções try catch throw]]", "[[Hierarquia de Exceções]]"]
---

# Códigos de erro e `std::error_code`

## Códigos de retorno clássicos

Estilo C: a função devolve um inteiro/`bool` e/ou define `errno`. Simples, mas fácil de **ignorar** e sem contexto.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cerrno>
#include <cstdio>
#include <cstring>
#include <iostream>

int main() {
    std::FILE* f = std::fopen("/caminho/inexistente.txt", "r");
    if (!f) std::cout << "erro " << errno << ": " << std::strerror(errno) << '\n';
    else std::fclose(f);
}
```

## `std::error_code` (C++11, `<system_error>`)

Um **valor de erro + categoria**: portável e extensível, sem alocação e sem exceção. É a base de `std::filesystem` (sobrecargas sem exceção) e de `Asio`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <filesystem>
#include <iostream>
#include <system_error>

namespace fs = std::filesystem;

int main() {
    std::error_code ec;
    auto tamanho = fs::file_size("/caminho/inexistente", ec);   // sobrecarga que NÃO lança
    if (ec) {
        std::cout << ec.value() << ' ' << ec.message() << ' ' << ec.category().name() << '\n';
        if (ec == std::errc::no_such_file_or_directory) std::cout << "arquivo ausente\n";   // comparação portável
    } else {
        std::cout << tamanho << '\n';
    }

    try {
        fs::file_size("/caminho/inexistente");                  // sobrecarga que LANÇA fs::filesystem_error
    } catch (const fs::filesystem_error& e) {
        std::cout << e.what() << " | " << e.code().message() << '\n';
    }
}
```

## Categorias e `std::errc`

| Conceito | Papel |
|---|---|
| `std::error_code` | Valor concreto de **uma plataforma/biblioteca** (`value()` + `category()`) |
| `std::error_condition` | Valor **portável** para comparar (`std::errc::*`) |
| `std::error_category` | Define nomes e mensagens (`std::generic_category()`, `std::system_category()`) |
| `std::system_error` | Exceção que carrega um `error_code` |

## Criando sua própria categoria

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <system_error>

enum class ErroApp { ok = 0, config_invalida, rede_fora };

class CategoriaApp final : public std::error_category {
public:
    const char* name() const noexcept override { return "app"; }
    std::string message(int c) const override {
        switch (static_cast<ErroApp>(c)) {
            case ErroApp::ok:               return "sucesso";
            case ErroApp::config_invalida:  return "configuração inválida";
            case ErroApp::rede_fora:        return "rede indisponível";
        }
        return "erro desconhecido";
    }
};

const std::error_category& categoria_app() { static CategoriaApp c; return c; }

// Habilita a conversão implícita ErroApp -> error_code
namespace std { template <> struct is_error_code_enum<ErroApp> : true_type {}; }
std::error_code make_error_code(ErroApp e) { return {static_cast<int>(e), categoria_app()}; }

std::error_code conecta(bool ok) { return ok ? std::error_code{} : ErroApp::rede_fora; }

int main() {
    if (auto ec = conecta(false)) std::cout << ec.category().name() << ": " << ec.message() << '\n';
}
```

## Quando escolher cada estilo

| Estilo | Quando |
|---|---|
| **Exceções** | Falhas excepcionais, difíceis de tratar localmente |
| **`error_code` (parâmetro de saída)** | APIs de sistema/E-S onde falhas são **esperadas** (padrão em `<filesystem>`, Asio) |
| **`std::expected<T, std::error_code>`** | Código novo (C++23): valor **ou** erro, composável ([[expected]]) |
| Códigos inteiros/`errno` | Interoperar com C |

> [!tip] Misture com critério
> Muitas bibliotecas oferecem **as duas** sobrecargas (com e sem `error_code`); escolha conforme o contexto: laço quente com falha comum → `error_code`; falha rara → exceção.

## Veja também

- [[expected]]
- [[Tratamento de Erros com expected]]
- [[Exceções try catch throw]]
- [[Hierarquia de Exceções]]

## Exercício

1. Use `std::filesystem::exists`, `copy_file` com `error_code` e imprima a mensagem de falha ao copiar para um diretório inexistente.
2. Defina um `enum class ErroParser` com categoria própria e retorne `std::expected<int, std::error_code>` de uma função de parsing.
