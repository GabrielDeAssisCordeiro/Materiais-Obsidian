---
titulo: "C++26: visão geral"
tags: [cpp, fundamentos, cpp26, contratos]
aliases: ["C++26", "Novidades do C++26", "Reflexão estática"]
tipo: conceito
nivel: avancado
padrao: C++26
criado: 2026-10-24
relacionados: ["[[História e Evolução dos Padrões]]", "[[Suporte dos Compiladores aos Padrões]]", "[[Escolhendo o Padrão com -std]]"]
---

# C++26: visão geral

> [!info] Estado em 24/10/2026
> O comitê concluiu o trabalho técnico do C++26 em **março de 2026** (reunião de Croydon, Reino Unido). A norma ISO está em fase de publicação. O **GCC 16.1** (abril de 2026) implementa vários recursos: reflexão (`-std=c++26 -freflection`), contratos, expansion statements e erroneous behavior.
> [!question] Verificar na documentação oficial
> Lista final de recursos, números de papers e suporte em cada compilador: confirme em cppreference.com e em isocpp.org.

## Principais recursos

| Recurso | Resumo | Paper |
|---|---|---|
| **Reflexão estática** | Inspecionar e gerar código a partir de tipos, membros, enumeradores em tempo de compilação (`^^T`, `[: :]`, cabeçalho `<meta>`) | P2996 |
| **Contratos** | `pre`, `post` em funções e `contract_assert` em instruções | P2900 |
| **`std::execution`** | Framework assíncrono com *senders/receivers* | P2300 |
| **Comportamento errôneo** | Ler variável automática não inicializada deixa de ser UB; vira *erroneous behavior* (valor definido pela implementação); `[[indeterminate]]` para optar por sair | P2795 |
| **Biblioteca padrão "hardened"** | Pré-condições verificadas (por exemplo, limites em `vector::operator[]`) | P3471 |
| **Expansion statements** | `template for` para iterar sobre pacotes/tuplas em tempo de compilação | P1306 |
| **Pack indexing** | `Ts...[0]` acessa um elemento do pacote | P2662 |
| **`= delete("motivo")`** | Mensagem personalizada ao usar função deletada | P2573 |
| **`#embed`** | Incorpora arquivo binário como array em tempo de compilação | P1967 |
| **`std::inplace_vector`** | Vetor com capacidade fixa, sem alocação dinâmica | P0843 |
| **`std::simd`** | Tipos para programação data-parallel | P1928 |
| **`std::hive`, `std::linalg`** | Contêiner com iteradores estáveis; álgebra linear | P0447, P1673 |

## Exemplo: contratos (sintaxe)

```cpp
// [nv] g++-16 -std=c++26 -fcontracts  (flags podem variar; verificar no GCC 16)
#include <cstddef>

int elemento(const int* p, std::size_t n, std::size_t i)
    pre(p != nullptr)        // pré-condição verificada na chamada
    pre(i < n)
    post(r : r == p[i])      // pós-condição; 'r' nomeia o resultado
{
    contract_assert(n > 0);  // asserção interna de contrato
    return p[i];
}
```

> [!question] Verificar na documentação oficial
> A semântica de avaliação dos contratos (observar, impor, ignorar) e as flags exatas dependem do compilador. Consulte o manual do GCC 16.

## Exemplo: reflexão (nome de um tipo)

```cpp
// [nv] g++-16 -std=c++26 -freflection
#include <meta>
#include <string_view>

struct Ponto { int x; int y; };

// ^^Ponto é o "valor de reflexão" do tipo Ponto
constexpr std::string_view nome = std::meta::identifier_of(^^Ponto);
static_assert(nome == "Ponto");

int main() {}
```

> [!warning] Experimental
> Reflexão e contratos são recursos novos; espere diferenças entre compiladores e mudanças em flags. Use-os em experimentos antes de adotar em produção.

## Comportamento errôneo na prática

```cpp
// [nv] g++-16 -std=c++26 -Wall -Wextra
int main() {
    int x;                 // C++23: valor indeterminado, ler x é UB
                           // C++26: ler x é "erroneous behavior" (bug, mas não UB)
    [[indeterminate]] int y;   // opt-out: mantém o comportamento antigo (útil em buffers grandes)
    (void)y;
    return x;              // programa incorreto: o compilador/ABI pode diagnosticar
}
```

## O que isso muda para quem aprende agora

- Todo o conteúdo de C++17/20/23 deste vault continua válido e é a base.
- Reflexão pode substituir muita metaprogramação baseada em macros e templates (serialização, ORMs, bindings).
- Contratos e *hardening* aproximam o C++ de verificações de segurança mais sistemáticas.

## Veja também

- [[História e Evolução dos Padrões]]
- [[Suporte dos Compiladores aos Padrões]]
- [[Escolhendo o Padrão com -std]]
- [[Cpp vs Rust, Java, Go e Python]]

## Exercício

1. Procure no cppreference a página "C++26" e liste três recursos que não aparecem na tabela acima.
2. Explique por que transformar leitura não inicializada em *erroneous behavior* melhora a segurança sem custo relevante.
