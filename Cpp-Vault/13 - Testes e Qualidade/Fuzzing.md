---
titulo: "Fuzzing"
tags: [cpp, testes, seguranca]
aliases: ["Fuzzing", "libFuzzer", "AFL++", "LLVMFuzzerTestOneInput", "Fuzz testing", "Testes baseados em propriedades"]
tipo: ferramenta
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Sanitizers]]", "[[Serialização]]", "[[Cobertura com gcov e lcov]]"]
---

# Fuzzing

**Fuzzing** alimenta o programa com entradas geradas/mutadas automaticamente, guiado por **cobertura**, para achar *crashes*, estouros de memória e UB. Excelente para **parsers**, decodificadores e protocolos ([[Serialização]]).

| Ferramenta | Característica |
|---|---|
| **libFuzzer** (LLVM) | Em processo; função `LLVMFuzzerTestOneInput`; use com Clang |
| **AFL++** | Fuzzer externo, instrumentação ou modo QEMU |
| **Honggfuzz** | Alternativa com *feedback* de hardware |
| **OSS-Fuzz** | Serviço contínuo do Google para projetos open source |
| **Testes por propriedade** | RapidCheck (estilo QuickCheck) |

```cpp
// [nv] clang++ -std=c++20 -g -O1 -fsanitize=fuzzer,address,undefined   (libFuzzer fornece o main; runtime indisponível no ambiente de teste do vault)
#include <cstddef>
#include <cstdint>
#include <string>

// Função "parser" com bug propositalmente escondido
static int analisar(const std::string& s) {
    if (s.size() >= 4 && s[0] == 'F' && s[1] == 'U' && s[2] == 'Z' && s[3] == 'Z') {
        char* p = nullptr;
        return *p;                          // crash alcançado só com a entrada "FUZZ..."
    }
    return 0;
}

extern "C" int LLVMFuzzerTestOneInput(const std::uint8_t* dados, std::size_t tamanho) {
    analisar(std::string(reinterpret_cast<const char*>(dados), tamanho));
    return 0;                               // sempre 0
}
```

```bash
clang++ -std=c++20 -g -O1 -fsanitize=fuzzer,address,undefined fuzz.cpp -o fuzz
mkdir corpus && ./fuzz corpus/ -max_total_time=60       # o corpus cresce com entradas interessantes
./fuzz crash-<hash>                                       # reproduz um crash salvo
```

```cmake
add_executable(fuzz fuzz.cpp)
target_compile_options(fuzz PRIVATE -fsanitize=fuzzer,address,undefined)
target_link_options(fuzz PRIVATE -fsanitize=fuzzer,address,undefined)
```

> [!tip] Como obter bons resultados
> - Combine com **ASan e UBSan** ([[Sanitizers]]) — o fuzzer acha o caminho, o sanitizer acha o bug.
> - Forneça um **corpus inicial** com amostras reais e um **dicionário** de tokens.
> - A função fuzzada deve ser determinística, rápida e sem efeitos globais.
> - Transforme cada crash em um **teste de regressão** ([[GoogleTest]]).

## Veja também

- [[Sanitizers]]
- [[Serialização]]
- [[Cobertura com gcov e lcov]]
- [[Segurança e Hardening]]

## Exercício

1. Execute o fuzzer no exemplo e observe quanto tempo leva para achar `FUZZ`.
2. Escreva um *fuzz target* para um parser de inteiros seu.
