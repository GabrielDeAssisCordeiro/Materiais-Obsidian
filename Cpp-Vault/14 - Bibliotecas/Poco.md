---
titulo: "Poco"
tags: [cpp, bibliotecas, utilitarios, rede]
aliases: ["Poco", "POCO C++ Libraries", "Poco::Net", "Poco::Util", "Qt vs Poco"]
tipo: biblioteca
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Visão Geral das Bibliotecas]]", "[[Boost]]", "[[Asio e Rede]]"]
---

# Poco

**POCO C++ Libraries**: coleção de bibliotecas C++ de uso geral e de **rede/aplicações**, com API moderna e consistente (licença **Boost Software License**). Foco em aplicações de servidor, IoT e utilitários multiplataforma.

| Módulo | Função |
|---|---|
| `Foundation` | Strings, datas, logging, threads, arquivos, expressões regulares, eventos |
| `Net` | Sockets, HTTP client/server, FTP, SMTP, WebSocket |
| `Util` | Aplicações de servidor, opções, configuração (XML, JSON, INI) |
| `JSON`, `XML` | Parsers |
| `Data` | Acesso a bancos (SQLite, MySQL, ODBC, PostgreSQL) |
| `Crypto`, `NetSSL` | OpenSSL |
| `Zip` | Arquivos ZIP |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lPocoNet -lPocoFoundation   (requer POCO; indisponível no ambiente de teste do vault)
#include <Poco/Net/HTTPClientSession.h>
#include <Poco/Net/HTTPRequest.h>
#include <Poco/Net/HTTPResponse.h>
#include <Poco/StreamCopier.h>
#include <iostream>

int main() {
    Poco::Net::HTTPClientSession sessao{"example.com", 80};
    Poco::Net::HTTPRequest req{Poco::Net::HTTPRequest::HTTP_GET, "/", Poco::Net::HTTPMessage::HTTP_1_1};
    sessao.sendRequest(req);

    Poco::Net::HTTPResponse resp;
    std::istream& corpo = sessao.receiveResponse(resp);
    std::cout << resp.getStatus() << ' ' << resp.getReason() << '\n';
    Poco::StreamCopier::copyStream(corpo, std::cout);
}
```

> [!info] Poco vs Boost vs Qt
> Poco é mais "coeso" e menor que o Boost, voltado para **aplicações de rede e infraestrutura**. Qt é maior, com GUI. Boost.Asio tem foco em I/O assíncrono de alto desempenho.

> [!question] Verificar na documentação oficial
> Versão atual, módulos e padrão C++ mínimo em pocoproject.org.

## Veja também

- [[Visão Geral das Bibliotecas]]
- [[Boost]]
- [[Asio e Rede]]
- [[std filesystem]]

## Exercício

1. Faça um cliente HTTP simples com Poco e compare com a versão em Asio/Beast.
2. Leia uma configuração INI com `Poco::Util::PropertyFileConfiguration`.
