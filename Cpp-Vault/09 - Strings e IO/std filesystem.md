---
titulo: "std::filesystem"
tags: [cpp, io, filesystem, cpp17]
aliases: ["std::filesystem", "filesystem", "path", "directory_iterator", "fs::path"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Arquivos fstream]]", "[[Códigos de Erro e error_code]]", "[[Unicode e Codificações]]"]
---

# `std::filesystem`

> [!info] Introdução
> **C++17**, cabeçalho `<filesystem>`. GCC 9+ (em GCC 8 exigia `-lstdc++fs`), Clang 9+ com libc++ 9+, MSVC 2017 15.7+.

Manipula **caminhos** e o **sistema de arquivos**: criar/remover diretórios, listar, copiar, consultar tamanho e permissões.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <filesystem>
#include <fstream>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path base = fs::temp_directory_path() / "cpp_vault_demo";   // operador / junta caminhos
    fs::create_directories(base / "sub");

    std::ofstream{base / "a.txt"} << "abc";
    std::ofstream{base / "sub" / "b.log"} << "12345";

    fs::path p = base / "sub" / "b.log";
    std::cout << p.filename() << ' ' << p.stem() << ' ' << p.extension() << '\n';
    std::cout << p.parent_path().filename() << '\n';
    std::cout << fs::exists(p) << ' ' << fs::is_regular_file(p) << ' ' << fs::file_size(p) << '\n';

    for (const auto& entrada : fs::recursive_directory_iterator(base))
        std::cout << (entrada.is_directory() ? "[D] " : "[F] ")
                  << fs::relative(entrada.path(), base).string() << '\n';

    fs::copy_file(base / "a.txt", base / "copia.txt", fs::copy_options::overwrite_existing);
    fs::rename(base / "copia.txt", base / "renomeado.txt");
    auto removidos = fs::remove_all(base);                          // remove tudo, retorna a contagem
    std::cout << "removidos: " << removidos << '\n';
}
```

## Tratamento de erros: exceção ou `error_code`

Quase todas as funções têm **duas sobrecargas**: lançam `fs::filesystem_error`, ou preenchem um `std::error_code` (sem exceção). Veja [[Códigos de Erro e error_code]].

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <filesystem>
#include <iostream>
#include <system_error>

namespace fs = std::filesystem;

int main() {
    std::error_code ec;
    auto tamanho = fs::file_size("nao_existe.bin", ec);              // não lança
    if (ec) std::cout << "erro: " << ec.message() << '\n';
    else std::cout << tamanho << '\n';

    try {
        fs::file_size("nao_existe.bin");                             // lança
    } catch (const fs::filesystem_error& e) {
        std::cout << "exceção: " << e.what() << '\n';
    }
}
```

## Pontos importantes

| Tema | Detalhe |
|---|---|
| `fs::path` | Armazena no formato nativo (`char` no POSIX, `wchar_t` no Windows). `.string()` pode perder informação no Windows; prefira `.u8string()` ou manter como `path` |
| Operador `/` | Junta; se o lado direito for **absoluto**, ele **substitui** o esquerdo |
| `canonical` vs `absolute` | `canonical` resolve `..`, links e **exige existência**; `absolute` não |
| *Race conditions* | Verificar `exists()` e depois usar é **TOCTOU**: tente a operação e trate o erro |
| Links simbólicos | `symlink_status`, `read_symlink`; `recursive_directory_iterator` não segue links por padrão |

> [!warning] Cuidado com `operator/` e caminhos absolutos
> `fs::path("/tmp") / "/etc"` resulta em `"/etc"`, não `"/tmp/etc"`. Em código que combina entrada do usuário, valide para evitar **path traversal** (`../`).

## Veja também

- [[Arquivos fstream]]
- [[Códigos de Erro e error_code]]
- [[Unicode e Codificações]]
- [[Estrutura de Projetos]]

## Exercício

1. Liste recursivamente os 5 maiores arquivos de um diretório.
2. Escreva uma função que organize arquivos em subpastas por extensão.
