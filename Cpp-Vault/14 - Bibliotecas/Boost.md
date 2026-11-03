---
titulo: "Boost"
tags: [cpp, bibliotecas]
aliases: ["Boost", "Boost C++ Libraries", "Boost.Beast", "Boost.Program_options", "Boost.Spirit", "Boost.Graph"]
tipo: biblioteca
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Visão Geral das Bibliotecas]]", "[[Asio e Rede]]", "[[vcpkg e Conan]]"]
---

# Boost

Coleção revisada por pares (licença **Boost Software License**, permissiva) de dezenas de bibliotecas. Várias viraram parte do padrão: `shared_ptr`, `thread`, `regex`, `filesystem`, `optional`, `variant`, `any`, `chrono`, `function`, `tuple`, `array`, `unordered`...

| Biblioteca | Para quê |
|---|---|
| **Asio** / **Beast** | Rede assíncrona; HTTP/WebSocket ([[Asio e Rede]]) |
| **Program_options** | Parsing de linha de comando |
| **Container** | `flat_map`, `small_vector`, `static_vector`, `stable_vector` |
| **Graph** | Algoritmos em grafos |
| **Spirit / X3** | Parsers em DSL embutido |
| **Hana / MP11** | Metaprogramação |
| **Multiprecision** | Inteiros e decimais grandes |
| **Math / Geometry / Numeric** | Funções especiais, geometria computacional |
| **Interprocess** | Memória compartilhada, filas entre processos |
| **Lockfree** | Estruturas lock-free |
| **Test** | Framework de testes |
| **Describe / PFR** | Reflexão leve de estruturas |
| **Unordered** | Hash maps de alto desempenho (open addressing) |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lboost_program_options   (requer Boost instalado; indisponível no ambiente de teste do vault)
#include <boost/program_options.hpp>
#include <iostream>

namespace po = boost::program_options;

int main(int argc, char** argv) {
    po::options_description desc("Opções");
    desc.add_options()
        ("ajuda,h", "mostra a ajuda")
        ("nome,n", po::value<std::string>()->default_value("mundo"), "nome a saudar");

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    if (vm.count("ajuda")) { std::cout << desc << '\n'; return 0; }
    std::cout << "Olá, " << vm["nome"].as<std::string>() << "!\n";
}
```

```cmake
find_package(Boost 1.83 REQUIRED COMPONENTS program_options)
target_link_libraries(app PRIVATE Boost::program_options)
```

> [!info] Header-only vs compilado
> A maioria é *header-only*; algumas precisam ser compiladas (`filesystem`, `program_options`, `regex`, `thread` em certos casos, `json`, `log`...). Instale via vcpkg/Conan ([[vcpkg e Conan]]) para evitar compilar tudo à mão.

> [!tip] Quando preferir a STL
> Se o padrão já oferece (`std::optional`, `std::filesystem`, `std::thread`), use-o. Escolha Boost para o que **não** existe no padrão.

> [!question] Verificar na documentação oficial
> Versão mais recente, lista de bibliotecas e requisitos de compilador em boost.org.

## Veja também

- [[Visão Geral das Bibliotecas]]
- [[Asio e Rede]]
- [[std filesystem]]
- [[optional]]
- [[vcpkg e Conan]]

## Exercício

1. Implemente uma CLI com `Boost.Program_options` e três opções.
2. Use `boost::container::small_vector` e compare alocações com `std::vector`.
