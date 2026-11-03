---
titulo: "gRPC e Protobuf"
tags: [cpp, bibliotecas, protobuf, serializacao]
aliases: ["Protobuf", "Protocol Buffers", ".proto", "protoc", "FlatBuffers", "Cap'n Proto"]
tipo: biblioteca
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Serialização]]", "[[Asio e Rede]]", "[[vcpkg e Conan]]"]
---

# gRPC e Protobuf

- **Protocol Buffers (protobuf)**: formato binário **com schema** (`.proto`), compacto, com geração de código e evolução compatível.
- **gRPC**: RPC sobre HTTP/2 que usa protobuf para definir **serviços**; suporta *streaming* bidirecional e dezenas de linguagens.

```protobuf
// ola.proto
syntax = "proto3";
package demo;

service Saudador {
  rpc Saudar (PedidoSaudacao) returns (RespostaSaudacao);
}

message PedidoSaudacao  { string nome = 1; }
message RespostaSaudacao { string mensagem = 1; }
```

```bash
protoc --cpp_out=gen --grpc_out=gen --plugin=protoc-gen-grpc=$(which grpc_cpp_plugin) ola.proto
```

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra   (requer gRPC/protobuf e os arquivos gerados ola.pb.h / ola.grpc.pb.h; indisponível no ambiente de teste do vault)
#include <grpcpp/grpcpp.h>
#include "ola.grpc.pb.h"
#include <memory>
#include <string>

class SaudadorImpl final : public demo::Saudador::Service {
    grpc::Status Saudar(grpc::ServerContext*, const demo::PedidoSaudacao* req,
                        demo::RespostaSaudacao* resp) override {
        resp->set_mensagem("Olá, " + req->nome() + "!");
        return grpc::Status::OK;
    }
};

int main() {
    SaudadorImpl servico;
    grpc::ServerBuilder builder;
    builder.AddListeningPort("0.0.0.0:50051", grpc::InsecureServerCredentials());   // use TLS em produção
    builder.RegisterService(&servico);
    std::unique_ptr<grpc::Server> servidor{builder.BuildAndStart()};
    servidor->Wait();
}
```

```cmake
find_package(gRPC CONFIG REQUIRED)
find_package(Protobuf CONFIG REQUIRED)
target_link_libraries(app PRIVATE gRPC::grpc++ protobuf::libprotobuf)
```

| Alternativa | Característica |
|---|---|
| **FlatBuffers** | *Zero-copy*: lê sem desserializar |
| **Cap'n Proto** | *Zero-copy*, RPC próprio |
| **Thrift**, **Avro** | Outros ecossistemas |
| **JSON + HTTP** | Simples e legível ([[nlohmann json e simdjson]]) |

> [!tip] Evolução de schemas
> Nunca reutilize números de campo; marque removidos como `reserved`. Adicione campos novos com valores padrão sensatos.

> [!warning] Cuidados
> Tempo de compilação e dependências são pesados; a **ABI** entre versões de protobuf e gRPC precisa ser consistente ([[ABI]]).

## Veja também

- [[Serialização]]
- [[Asio e Rede]]
- [[vcpkg e Conan]]
- [[Visão Geral das Bibliotecas]]

## Exercício

1. Defina um serviço `Calculadora` com `Somar` e implemente cliente e servidor.
2. Adicione um campo novo ao `.proto` e verifique a compatibilidade com um cliente antigo.
