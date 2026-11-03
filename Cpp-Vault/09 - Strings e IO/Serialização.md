---
titulo: "Serialização"
tags: [cpp, io, serializacao, json, protobuf, binario]
aliases: ["Serialização", "serialization", "endianness"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Arquivos fstream]]", "[[Locale]]", "[[sizeof e alignof]]"]
---

# Serialização

**Serializar** é converter objetos em bytes/texto para armazenar ou transmitir; **desserializar** é o inverso. O C++ **não tem reflexão em runtime** (C++26 traz reflexão estática, que facilitará bibliotecas), então a serialização é manual ou via bibliotecas.

## Por que `fwrite(struct)` é mau

- **Padding** e `sizeof` variam entre compiladores/plataformas ([[sizeof e alignof]]).
- **Endianness** (little vs big endian).
- Ponteiros e `std::string` não são "dados" copiáveis em bytes (UB se tipos não triviais).
- Evolução de versões do formato.

## Formatos

| Formato | Tipo | Bibliotecas | Quando |
|---|---|---|---|
| JSON | Texto | nlohmann/json, simdjson, RapidJSON, Glaze | APIs, configuração |
| Protocol Buffers | Binário com schema | protobuf | RPC, evolução de formatos |
| FlatBuffers / Cap'n Proto | Binário *zero-copy* | flatbuffers, capnproto | Jogos, baixa latência |
| MessagePack / CBOR | Binário auto-descritivo | msgpack-c, jsoncons | JSON compacto |
| Boost.Serialization / cereal | Binário/texto/JSON | cereal | Persistência de objetos C++ |

## Serialização binária manual e portátil

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <bit>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

// Escreve inteiros sempre em little endian, independente da máquina
void escrever_u32(std::vector<std::uint8_t>& buf, std::uint32_t v) {
    for (int i = 0; i < 4; ++i) buf.push_back(static_cast<std::uint8_t>(v >> (8 * i)));
}

std::uint32_t ler_u32(const std::uint8_t* p) {
    return static_cast<std::uint32_t>(p[0]) | static_cast<std::uint32_t>(p[1]) << 8 |
           static_cast<std::uint32_t>(p[2]) << 16 | static_cast<std::uint32_t>(p[3]) << 24;
}

struct Mensagem { std::uint32_t id; std::string texto; };

std::vector<std::uint8_t> serializar(const Mensagem& m) {
    std::vector<std::uint8_t> buf;
    escrever_u32(buf, m.id);
    escrever_u32(buf, static_cast<std::uint32_t>(m.texto.size()));   // prefixo de tamanho
    buf.insert(buf.end(), m.texto.begin(), m.texto.end());
    return buf;
}

Mensagem desserializar(const std::vector<std::uint8_t>& buf) {
    Mensagem m;
    m.id = ler_u32(buf.data());
    std::uint32_t n = ler_u32(buf.data() + 4);
    m.texto.assign(buf.begin() + 8, buf.begin() + 8 + n);            // em produção: validar n <= buf.size() - 8
    return m;
}

int main() {
    auto bytes = serializar({7, "olá"});
    auto m = desserializar(bytes);
    std::cout << bytes.size() << ' ' << m.id << ' ' << m.texto << '\n';   // 12 7 olá

    // bit_cast: reinterpretação segura de bytes (C++20)
    float f = 1.0f;
    auto bits = std::bit_cast<std::uint32_t>(f);
    std::cout << std::hex << bits << '\n';                                // 3f800000
    std::cout << (std::endian::native == std::endian::little ? "little" : "big") << '\n';
}
```

> [!danger] Dados externos não são confiáveis
> Ao desserializar, **valide tamanhos e limites** antes de alocar ou copiar: um prefixo de tamanho forjado causa estouro de buffer (UB) ou esgotamento de memória. Veja [[Comportamento Indefinido e Não Especificado]].

> [!tip] Evolução do formato
> Inclua um **número de versão** ou use um formato com schema (Protobuf, FlatBuffers). Números em texto (JSON): serialize com `std::to_chars` para evitar locale ([[Locale]]).

## Veja também

- [[Arquivos fstream]]
- [[Locale]]
- [[sizeof e alignof]]
- [[Comportamento Indefinido e Não Especificado]]

## Exercício

1. Estenda o exemplo para serializar `std::vector<Mensagem>` com versão do formato e validação de tamanhos.
2. Escreva um conversor de `std::uint64_t` para big endian usando `std::byteswap` (C++23) ou deslocamentos.
