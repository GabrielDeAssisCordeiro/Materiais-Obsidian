---
titulo: "{fmt} e spdlog"
tags: [cpp, bibliotecas, formatacao]
aliases: ["fmt", "{fmt}", "spdlog", "Log em C++", "glog", "quill"]
tipo: biblioteca
nivel: iniciante
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Formatação std format e std print]]", "[[Visão Geral das Bibliotecas]]", "[[Streams e iostream]]"]
---

# `{fmt}` e spdlog

## fmt

Biblioteca que originou `std::format`/`std::print` ([[Formatação std format e std print]]). Mais recursos que o padrão e compatível com compiladores sem `<format>`.

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lfmt   (requer {fmt}; indisponível no ambiente de teste do vault)
#include <fmt/core.h>
#include <fmt/ranges.h>
#include <fmt/color.h>
#include <vector>

int main() {
    fmt::print("Olá, {}!\n", "mundo");
    std::vector<int> v{1, 2, 3};
    fmt::print("{}\n", v);                                          // imprime [1, 2, 3] (ranges)
    fmt::print(fg(fmt::color::green), "{:>8.2f}\n", 3.14159);       // cores
    fmt::print("{:#x} {:08b}\n", 255, 5);
}
```

## spdlog

Logger rápido (síncrono/assíncrono), com formatação `{fmt}`, vários *sinks* (console colorido, arquivo, rotativo, syslog), níveis e padrões.

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lspdlog -lfmt   (requer spdlog; indisponível no ambiente de teste do vault)
#include <spdlog/spdlog.h>
#include <spdlog/sinks/rotating_file_sink.h>

int main() {
    spdlog::set_level(spdlog::level::debug);
    spdlog::info("Servidor iniciado na porta {}", 8080);
    spdlog::warn("Uso de memória: {:.1f}%", 87.3);
    spdlog::error("Falha ao abrir {}", "config.json");

    auto arquivo = spdlog::rotating_logger_mt("app", "logs/app.log", 5 * 1024 * 1024, 3);   // 5 MB, 3 arquivos
    arquivo->info("Mensagem no arquivo");
    arquivo->flush_on(spdlog::level::warn);
}
```

```cmake
find_package(spdlog CONFIG REQUIRED)
target_link_libraries(app PRIVATE spdlog::spdlog)    # inclui fmt
```

| Boa prática de log | |
|---|---|
| Níveis: `trace` < `debug` < `info` < `warn` < `error` < `critical` | Ajuste por ambiente |
| Logging **assíncrono** (`spdlog::async_logger`) | Não bloqueia a thread de trabalho |
| Não logar dados sensíveis | Senhas, tokens, dados pessoais |
| Mensagens estruturadas | Facilita busca (JSON, chave=valor) |

> [!info] Alternativas
> **quill** (latência muito baixa para HFT), **glog**, **Boost.Log**, **Easylogging++**, `std::print` + sua camada.

## Veja também

- [[Formatação std format e std print]]
- [[Streams e iostream]]
- [[Visão Geral das Bibliotecas]]
- [[Cpp em Finanças e Baixa Latência]]

## Exercício

1. Configure spdlog com saída em console e arquivo rotativo.
2. Meça o custo de `spdlog::debug` com e sem o nível ativo.
