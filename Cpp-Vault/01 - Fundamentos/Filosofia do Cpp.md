---
titulo: "Filosofia do C++"
tags: [cpp, fundamentos]
aliases: ["Zero-overhead", "Abstração sem custo", "Filosofia do C++"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[O que é Cpp]]", "[[Cpp vs C]]", "[[Casos de Uso do Cpp]]"]
---

# Filosofia do C++

## O princípio de zero-overhead

Formulado por Bjarne Stroustrup, resume-se em duas ideias:

1. **Você não paga pelo que não usa.** Recursos que não aparecem no programa não adicionam custo.
2. **O que você usa, não poderia ser escrito à mão com mais eficiência.** Uma abstração bem projetada compila para algo tão bom quanto o código de baixo nível equivalente.

Isso é chamado de **abstração sem custo** (*zero-cost abstraction*) — custo de execução, não de compilação: templates e abstrações pesadas podem aumentar o tempo de compilação.

## Outros princípios

- **Proximidade do hardware:** é possível controlar layout de memória, alinhamento e instruções.
- **Segurança de tipos** quando possível, com "saídas de emergência" explícitas (casts).
- **Multiparadigma:** a linguagem não impõe um único estilo.
- **Compatibilidade:** código antigo continua compilando; por isso há muitas armadilhas históricas.
- **Determinismo de recursos:** destrutores executam em pontos previsíveis (RAII).

## Demonstração: abstrações que não custam memória

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>
#include <memory>

int main() {
    // std::array tem o mesmo tamanho de um array C: nenhum campo extra.
    static_assert(sizeof(std::array<int, 4>) == sizeof(int[4]));

    // unique_ptr com deleter padrão ocupa o mesmo que um ponteiro puro
    // (garantia prática nas implementações principais, não do padrão).
    static_assert(sizeof(std::unique_ptr<int>) == sizeof(int*));

    std::cout << "sem overhead de tamanho\n";
}
```

> [!warning] "Zero-overhead" não significa "sem custo nenhum"
> - Funções virtuais exigem uma chamada indireta via vtable e um ponteiro por objeto.
> - `std::shared_ptr` mantém um bloco de controle com contadores atômicos.
> - Exceções têm custo (pequeno no caminho feliz, alto ao lançar).
> - Templates aumentam o código gerado e o tempo de compilação.
>
> A filosofia diz que você paga **apenas quando usa** esses recursos.

## Consequências para quem aprende

| Princípio | Consequência |
|---|---|
| Sem coleta de lixo | Você precisa entender tempo de vida de objetos |
| Sem verificações automáticas de limites em `operator[]` | Acessos fora do limite são comportamento indefinido (UB) |
| Controle total | Muitos caminhos para a mesma tarefa; é preciso conhecer boas práticas |

> [!tip] Resumo prático
> Prefira abstrações da biblioteca padrão (`std::vector`, `std::string`, smart pointers). Elas são seguras **e** rápidas; só desça de nível quando medir que é necessário.

## Veja também

- [[O que é Cpp]]
- [[Cpp vs C]]
- [[Cpp vs Rust, Java, Go e Python]]
- [[Casos de Uso do Cpp]]

## Exercício

1. Dê um exemplo de abstração do C++ que tem custo de execução e explique por que isso não viola o princípio de zero-overhead.
2. Execute o exemplo acima e use `sizeof` para comparar `std::shared_ptr<int>` com `int*`.
