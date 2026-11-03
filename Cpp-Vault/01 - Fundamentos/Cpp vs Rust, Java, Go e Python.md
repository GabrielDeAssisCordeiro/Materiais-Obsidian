---
titulo: "C++ vs Rust, Java, Go e Python"
tags: [cpp, fundamentos, comparacao, rust, python]
aliases: ["C++ vs Rust", "C++ vs Java", "C++ vs Go", "C++ vs Python", "Comparação entre linguagens"]
tipo: comparacao
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Cpp vs C]]", "[[Casos de Uso do Cpp]]", "[[Filosofia do Cpp]]"]
---

# C++ vs Rust, Java, Go e Python

Não existe "melhor linguagem" em abstrato: cada uma otimiza prioridades diferentes.

## Tabela comparativa

| Critério | C++ | Rust | Java | Go | Python |
|---|---|---|---|---|---|
| Execução | Nativa (AOT) | Nativa (AOT) | JVM (JIT) | Nativa (AOT) | Interpretada (CPython) |
| Tipagem | Estática | Estática | Estática | Estática | Dinâmica |
| Gerência de memória | Manual + RAII | Ownership e borrow checker | Coletor de lixo | Coletor de lixo | Contagem de referências + GC |
| Segurança de memória | Responsabilidade do programador (ferramentas ajudam) | Garantida em código *safe* | Garantida (JVM) | Garantida (exceto `unsafe`) | Garantida |
| Desempenho típico | Muito alto | Muito alto | Alto | Alto | Baixo a médio |
| Latência previsível | Sim | Sim | Pausas de GC (reduzidas em coletores modernos) | Pausas curtas de GC | Não |
| Concorrência | Threads, atômicos, corrotinas | Threads, `async`, tipos `Send`/`Sync` | Threads, executores, *virtual threads* | Goroutines e canais | GIL (CPython tradicional), `asyncio` |
| Metaprogramação | Templates, `constexpr`, concepts; reflexão no C++26 | Macros e traits | Reflexão em runtime | Genéricos (desde 1.18) | Dinâmica |
| Curva de aprendizado | Íngreme | Íngreme | Moderada | Suave | Suave |
| Ecossistema legado | Enorme (décadas) | Crescente | Enorme | Médio | Enorme |
| Compilação | Lenta em projetos grandes | Lenta | Rápida | Muito rápida | N/A |

> [!info] Interpretação
> Tabelas simplificam. Há exceções (por exemplo, PyPy, GraalVM, Cython), e as linguagens evoluem.

## Quando cada uma brilha

- **C++**: máximo controle e desempenho, código legado/HPC/jogos, interoperar com C e GPUs.
- **Rust**: sistemas novos em que segurança de memória verificada em compilação é prioridade.
- **Java**: aplicações corporativas, back-ends de grande escala, Android (com Kotlin).
- **Go**: serviços de rede, ferramentas de infraestrutura, simplicidade e builds rápidos.
- **Python**: ciência de dados, automação, prototipagem, *scripting* (muitas bibliotecas têm núcleo em C++).

## Um mesmo trecho: somar os pares de uma lista

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3, 4, 5, 6};

    // Filtra pares e soma, sem alocar vetor intermediário (views são preguiçosas).
    auto pares = v | std::views::filter([](int x) { return x % 2 == 0; });
    int soma = std::accumulate(pares.begin(), pares.end(), 0);

    std::cout << soma << '\n';   // 12
}
```

Em Python seria `sum(x for x in v if x % 2 == 0)`: mais curto, porém executado por um interpretador. O C++ moderno aproxima a expressividade sem abrir mão de desempenho.

> [!tip] Segurança de memória e C++
> A discussão sobre segurança de memória é central no debate atual. O C++ responde com ferramentas (sanitizers, análise estática), bibliotecas "hardened" e, no C++26, comportamento errôneo para leituras não inicializadas — ver [[Cpp26 Visão Geral]].

## Veja também

- [[Cpp vs C]]
- [[Casos de Uso do Cpp]]
- [[Filosofia do Cpp]]
- [[Cpp26 Visão Geral]]

## Exercício

1. Para um microsserviço de rede simples com prazo curto, qual linguagem da tabela você escolheria e por quê?
2. Quais características do C++ explicam o uso dele no núcleo de bibliotecas Python de computação numérica?
