---
titulo: "Flags essenciais do compilador"
tags: [cpp, fundamentos, flags, gcc, clang, msvc]
aliases: ["Flags do compilador", "-Wall -Wextra", "Opções de compilação"]
tipo: referencia
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Escolhendo o Padrão com -std]]", "[[Pipeline de Compilação - Cpp]]", "[[Compiladores GCC Clang e MSVC]]"]
---

# Flags essenciais do compilador

## GCC / Clang

| Flag | Função |
|---|---|
| `-std=c++20` | Escolhe o padrão ([[Escolhendo o Padrão com -std]]) |
| `-Wall` | Ativa avisos comuns (nome enganoso: não são "todos") |
| `-Wextra` | Avisos adicionais (parâmetros não usados, comparações signed/unsigned...) |
| `-Wpedantic` | Avisa sobre extensões fora do padrão |
| `-Werror` | Transforma avisos em erros (útil em CI) |
| `-Wshadow`, `-Wconversion` | Sombreamento de variáveis; conversões que perdem dados |
| `-O0` | Sem otimização (padrão; melhor para depurar) |
| `-O1`, `-O2`, `-O3` | Níveis crescentes de otimização (`-O2` é o usual em produção) |
| `-Og` | Otimização compatível com depuração |
| `-Os`, `-Oz` | Otimiza tamanho |
| `-g` | Inclui símbolos de depuração |
| `-c` | Compila sem linkar (gera `.o`) |
| `-o nome` | Nome do arquivo de saída |
| `-I dir` | Diretório de cabeçalhos |
| `-L dir`, `-l nome` | Diretório de bibliotecas; liga com `libnome` |
| `-D NOME=valor` | Define macro |
| `-pthread` | Habilita threads POSIX (compilação e link) |
| `-fsanitize=address,undefined` | Sanitizers em tempo de execução |
| `-march=native` | Otimiza para a CPU local (binário não portável) |
| `-E`, `-S` | Só pré-processa; gera assembly |

## MSVC (`cl.exe`)

| Equivalente | MSVC |
|---|---|
| Padrão | `/std:c++17`, `/std:c++20`, `/std:c++latest` |
| Avisos | `/W3`, `/W4` (e `/Wall` muito verboso), `/WX` = tratar como erro |
| Otimização | `/Od` (nenhuma), `/O1`, `/O2`, `/Ox` |
| Depuração | `/Zi` (símbolos), `/Z7` |
| Exceções | `/EHsc` (modelo padrão de exceções C++) |
| Conformidade | `/permissive-` |
| Include / define | `/I dir`, `/D NOME` |
| Sanitizer | `/fsanitize=address` |

## Combinações recomendadas

```bash
# Desenvolvimento: avisos e depuração, com sanitizers
g++ -std=c++20 -Wall -Wextra -Wpedantic -Wshadow -g -O0 \
    -fsanitize=address,undefined main.cpp -o app

# Produção: otimizado
g++ -std=c++20 -Wall -Wextra -O2 -DNDEBUG main.cpp -o app
```

`-DNDEBUG` desativa `assert`.

> [!tip] Sempre compile com avisos
> Trate avisos como bugs em potencial. `-Wall -Wextra` evita boa parte dos problemas de iniciante (variável não inicializada, comparação signed/unsigned, retorno ausente).

> [!warning] `-O3` e `-march=native` não são "mais rápido sempre"
> Meça. Otimizações agressivas podem aumentar o binário, quebrar portabilidade ou expor comportamento indefinido latente (veja [[Filosofia do Cpp]]).

> [!danger] Otimização revela UB
> Código com comportamento indefinido pode "funcionar" em `-O0` e falhar em `-O2`, porque o compilador assume que UB nunca ocorre.

## Exemplo: um aviso útil

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3};
    // Correto: size_t evita o aviso de comparação signed/unsigned
    for (std::size_t i = 0; i < v.size(); ++i)
        std::cout << v[i] << ' ';
    std::cout << '\n';
    // Com 'int i' o -Wextra/-Wsign-compare avisaria: comparison of integer expressions
}
```

## Veja também

- [[Escolhendo o Padrão com -std]]
- [[Pipeline de Compilação - Cpp]]
- [[Compiladores GCC Clang e MSVC]]
- [[Primeiro Programa]]

## Exercício

1. Compile um programa com uma variável não usada com e sem `-Wall`. Compare.
2. Gere um binário com `-O0` e outro com `-O2` para o mesmo código e compare tamanhos com `ls -l`.
