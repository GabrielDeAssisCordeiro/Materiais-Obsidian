---
titulo: "C++ em jogos"
tags: [cpp, aplicacoes, jogos]
aliases: ["Jogos", "Game dev", "Unreal Engine", "Godot", "Game loop"]
tipo: area
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[SDL e SFML]]", "[[Cache e Localidade de Dados]]", "[[vector]]"]
---

# C++ em jogos

C++ domina *engines* e jogos AAA por exigir **desempenho previsível**, controle de memória e acesso a APIs gráficas (Vulkan, DirectX 12, Metal, OpenGL).

| Motor | Observação |
|---|---|
| **Unreal Engine** | C++ (com *garbage collector* próprio para `UObject`) e Blueprints |
| **Godot** | Núcleo em C++; GDExtension para C++ |
| **Unity** | Núcleo em C++; *scripts* em C#; DOTS/Burst |
| **O3DE**, **Bevy (Rust)**, **raylib**, **SDL/SFML** | Alternativas e bibliotecas ([[SDL e SFML]]) |

## Arquitetura: *game loop* e **orçamento de frame**

```mermaid
flowchart LR
    I[Entrada] --> U["Atualizar (física, IA)"] --> R[Renderizar] --> A[Áudio/rede]
    A --> I
```

A 60 FPS são **16,6 ms** por quadro: alocações imprevisíveis, *page faults* e *cache misses* causam falhas de quadro (*stutter*).

## ECS e *data-oriented design*

Em vez de hierarquias de objetos (cada `Inimigo` com muitos membros espalhados), organize dados por **componentes contíguos**, processados em lote — melhor uso de cache ([[Cache e Localidade de Dados]]).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>
#include <vector>

struct Posicao { float x, y; };
struct Velocidade { float dx, dy; };

// "Structure of Arrays": cada componente em um vetor contíguo
struct Mundo {
    std::vector<Posicao> posicoes;
    std::vector<Velocidade> velocidades;

    std::size_t criar(Posicao p, Velocidade v) {
        posicoes.push_back(p);
        velocidades.push_back(v);
        return posicoes.size() - 1;
    }
};

void sistema_movimento(Mundo& m, float dt) {                         // laço simples: ótimo para cache e SIMD
    for (std::size_t i = 0; i < m.posicoes.size(); ++i) {
        m.posicoes[i].x += m.velocidades[i].dx * dt;
        m.posicoes[i].y += m.velocidades[i].dy * dt;
    }
}

int main() {
    Mundo m;
    for (int i = 0; i < 1000; ++i) m.criar({0, 0}, {1.0f, 2.0f});
    for (int frame = 0; frame < 60; ++frame) sistema_movimento(m, 1.0f / 60.0f);
    std::cout << m.posicoes[0].x << ' ' << m.posicoes[0].y << '\n';  // 1 2
}
```

Bibliotecas ECS: **EnTT**, **flecs**.

## Práticas comuns

- **Passo de tempo fixo** para física; interpolar a renderização.
- **Alocadores próprios** (arena/pool por frame — [[Alocadores Introdução]]) e *object pools*.
- Evitar exceções e RTTI em código quente; `-fno-exceptions` é comum.
- Multithreading com **jobs/tarefas** (*work stealing*), não uma thread por sistema ([[TBB e OpenMP]]).
- *Hot reload* de código, *profilers* de GPU/CPU (RenderDoc, Tracy, PIX) — [[Profiling e Benchmarking]].
- Linguagens de *script* embutidas: Lua, C#, Python, WebAssembly.

> [!tip] Evite
> Cadeias de `shared_ptr`, `virtual` em laços críticos, `std::map` por quadro, e `new`/`delete` espalhados.

## Veja também

- [[SDL e SFML]]
- [[Cache e Localidade de Dados]]
- [[Alocadores Introdução]]
- [[MOC - Áreas de Aplicação - Cpp]]

## Exercício

1. Estenda o ECS com componente `Vida` e um sistema de dano; meça o tempo.
2. Compare AoS (`vector<Entidade>`) e SoA no mesmo sistema de movimento com 10⁶ entidades.
