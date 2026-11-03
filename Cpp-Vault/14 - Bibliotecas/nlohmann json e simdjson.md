---
titulo: "nlohmann/json e simdjson"
tags: [cpp, bibliotecas, json, serializacao]
aliases: ["nlohmann/json", "nlohmann json", "simdjson", "RapidJSON", "Glaze", "JSON em C++"]
tipo: biblioteca
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Serialização]]", "[[Visão Geral das Bibliotecas]]", "[[optional]]"]
---

# nlohmann/json e simdjson

| Biblioteca | Foco |
|---|---|
| **nlohmann/json** | **Ergonomia**: API que parece JSON nativo; *header-only* |
| **simdjson** | **Velocidade** de parsing (GB/s) com SIMD; API *on-demand* |
| **RapidJSON** | Rápida, API clássica DOM/SAX |
| **Glaze** | Serialização com reflexão de compilação, muito rápida |
| **Boost.JSON** | Integrada ao ecossistema Boost |

## nlohmann/json

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra   (requer nlohmann/json; indisponível no ambiente de teste do vault)
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <vector>

using json = nlohmann::json;

struct Pessoa {
    std::string nome;
    int idade;
    std::vector<std::string> hobbies;
};
NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Pessoa, nome, idade, hobbies)   // gera to_json/from_json

int main() {
    json j = json::parse(R"({"nome":"Ana","idade":30,"hobbies":["xadrez","corrida"]})");
    std::cout << j["nome"] << ' ' << j.at("idade") << '\n';

    Pessoa p = j.get<Pessoa>();                                     // JSON → struct
    p.idade++;
    json saida = p;                                                  // struct → JSON
    std::cout << saida.dump(2) << '\n';                              // indentado

    j["extra"] = {{"ativo", true}, {"pontos", 12.5}};
    if (auto it = j.find("faltando"); it == j.end()) std::cout << "sem 'faltando'\n";

    try { json::parse("{inválido"); }
    catch (const json::parse_error& e) { std::cout << "erro: " << e.what() << '\n'; }
}
```

```cmake
find_package(nlohmann_json CONFIG REQUIRED)
target_link_libraries(app PRIVATE nlohmann_json::nlohmann_json)
```

> [!warning] Armadilhas
> - `j["chave"]` em objeto **não const** **cria** a chave se não existir; use `at()` (lança) ou `find`/`contains` para leitura.
> - Tipos numéricos: inteiros vs ponto flutuante são distinguidos; conversões erradas lançam exceção (`type_error`).
> - Desempenho: para grandes volumes use **simdjson**/**Glaze**.

## simdjson (leitura rápida)

```cpp
// [nv] g++ -std=c++20 -O2 -lsimdjson   (requer simdjson; indisponível no ambiente de teste do vault)
#include <iostream>
#include <simdjson.h>

int main() {
    simdjson::ondemand::parser parser;
    auto json = simdjson::padded_string(std::string_view(R"({"x": 1.5, "lista": [1,2,3]})"));
    auto doc = parser.iterate(json);
    double x = doc["x"].get_double();
    int64_t soma = 0;
    for (auto v : doc["lista"].get_array()) soma += v.get_int64();
    std::cout << x << ' ' << soma << '\n';                           // 1.5 6
}
```

## Veja também

- [[Serialização]]
- [[Visão Geral das Bibliotecas]]
- [[Exceções try catch throw]]
- [[Locale]]

## Exercício

1. Leia um arquivo de configuração JSON em uma `struct` com valores padrão para chaves ausentes.
2. Compare o tempo de parse de um arquivo de 100 MB com nlohmann e simdjson.
