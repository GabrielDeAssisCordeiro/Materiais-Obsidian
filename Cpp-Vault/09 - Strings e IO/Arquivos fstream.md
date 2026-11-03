---
titulo: "Arquivos com fstream"
tags: [cpp, io, arquivos, binario]
aliases: ["fstream", "ifstream", "ofstream", "Ler arquivos", "Escrever arquivos", "Arquivos binários"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Streams e iostream]]", "[[std filesystem]]", "[[RAII]]"]
---

# Arquivos com `fstream`

`<fstream>` oferece `ifstream` (leitura), `ofstream` (escrita) e `fstream` (ambos). São **RAII**: o destrutor fecha o arquivo ([[RAII]]).

## Modos de abertura

| Flag (`std::ios::`) | Significado |
|---|---|
| `in` / `out` | Leitura / escrita |
| `app` | Escreve sempre no fim |
| `trunc` | Apaga o conteúdo ao abrir (padrão de `ofstream`) |
| `ate` | Abre e posiciona no fim |
| `binary` | Sem tradução de fim de linha |

## Texto

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <fstream>
#include <iostream>
#include <string>

int main() {
    const char* caminho = "exemplo_fstream.txt";

    {   // escopo fecha o arquivo (RAII) ao sair
        std::ofstream out{caminho};
        if (!out) { std::cerr << "falha ao abrir\n"; return 1; }
        out << "linha 1\nlinha 2\n" << 42 << '\n';
    }

    std::ifstream in{caminho};
    std::string linha;
    while (std::getline(in, linha))                   // leitura linha a linha
        std::cout << "> " << linha << '\n';

    std::ofstream log{caminho, std::ios::app};        // acrescentar
    log << "fim\n";
}
```

## Binário

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

struct Registro {
    std::int32_t id;
    double valor;
};   // tipo trivialmente copiável: seguro para write/read de bytes na MESMA plataforma

int main() {
    std::vector<Registro> dados{{1, 1.5}, {2, 2.5}};

    std::ofstream out{"dados.bin", std::ios::binary};
    out.write(reinterpret_cast<const char*>(dados.data()),
              static_cast<std::streamsize>(dados.size() * sizeof(Registro)));
    out.close();

    std::ifstream in{"dados.bin", std::ios::binary | std::ios::ate};
    auto bytes = in.tellg();                          // posição no fim = tamanho
    in.seekg(0);
    std::vector<Registro> lidos(static_cast<std::size_t>(bytes) / sizeof(Registro));
    in.read(reinterpret_cast<char*>(lidos.data()), bytes);
    std::cout << lidos.size() << ' ' << lidos[1].valor << '\n';   // 2 2.5
}
```

> [!warning] Binário não é portátil
> Despejar structs bytes-a-bytes depende de **padding**, **endianness** e `sizeof`. Para troca entre máquinas/versões use um formato definido — veja [[Serialização]].

## Ler o arquivo inteiro

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

std::string ler_tudo(const std::string& caminho) {
    std::ifstream in{caminho, std::ios::binary};
    std::ostringstream ss;
    ss << in.rdbuf();                                 // copia o buffer inteiro
    return ss.str();
}

int main() {
    std::ofstream{"tmp_leitura.txt"} << "olá\n";
    std::cout << ler_tudo("tmp_leitura.txt").size() << '\n';   // 5 bytes (á = 2)
}
```

> [!tip] Verificação de erros
> Habilite exceções se preferir: `out.exceptions(std::ios::failbit | std::ios::badbit);`. Cheque `if (!out)` após escrever dados importantes e chame `flush()`/`close()` antes de ler de volta.

## Veja também

- [[Streams e iostream]]
- [[std filesystem]]
- [[Serialização]]
- [[RAII]]

## Exercício

1. Escreva um programa `copiar origem destino` que copia arquivos em blocos de 4 KiB.
2. Conte linhas, palavras e bytes de um arquivo (como `wc`).
