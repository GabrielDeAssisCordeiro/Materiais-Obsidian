---
titulo: "SDL e SFML (multimídia e jogos 2D)"
tags: [cpp, bibliotecas, jogos]
aliases: ["SDL", "SDL2", "SDL3", "SFML", "raylib", "Dear ImGui", "OpenGL", "Vulkan", "Biblioteca de jogos"]
tipo: biblioteca
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Cpp em Jogos]]", "[[Visão Geral das Bibliotecas]]", "[[Classes e Structs]]"]
---

# SDL e SFML (multimídia e jogos 2D)

| Biblioteca | Linguagem | Características | Licença |
|---|---|---|---|
| **SDL** (2 e 3) | C (usável em C++) | Janela, entrada, áudio, renderização 2D, contexto OpenGL/Vulkan/Metal; base de muitos jogos | zlib |
| **SFML** | C++ orientada a objetos | Janela, gráficos 2D, áudio, rede; API fácil | zlib |
| **raylib** | C (bindings C++) | Muito simples para aprender | zlib |
| **Dear ImGui** | C++ | GUI imediata (ferramentas, depuração) | MIT |
| **GLFW** + **OpenGL/Vulkan** | C | Janela + API gráfica de baixo nível | zlib |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lSDL2   (requer SDL2; indisponível no ambiente de teste do vault)
#include <SDL2/SDL.h>
#include <memory>

struct SdlDeleter {
    void operator()(SDL_Window* w) const { SDL_DestroyWindow(w); }
    void operator()(SDL_Renderer* r) const { SDL_DestroyRenderer(r); }
};

int main(int, char**) {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) return 1;

    std::unique_ptr<SDL_Window, SdlDeleter> janela{
        SDL_CreateWindow("Demo", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, 0)};
    std::unique_ptr<SDL_Renderer, SdlDeleter> render{
        SDL_CreateRenderer(janela.get(), -1, SDL_RENDERER_ACCELERATED)};          // RAII em recursos C

    SDL_Rect quadrado{100, 100, 64, 64};
    for (bool rodando = true; rodando;) {
        for (SDL_Event e; SDL_PollEvent(&e);) if (e.type == SDL_QUIT) rodando = false;
        SDL_SetRenderDrawColor(render.get(), 20, 20, 30, 255);
        SDL_RenderClear(render.get());
        SDL_SetRenderDrawColor(render.get(), 240, 180, 40, 255);
        SDL_RenderFillRect(render.get(), &quadrado);
        SDL_RenderPresent(render.get());
    }
    SDL_Quit();
}
```

> [!tip] Padrão de projeto: *game loop*
> `ler entrada → atualizar (dt fixo ou variável) → renderizar`. Use **passo de tempo fixo** para a física e interpole a renderização.

> [!info] RAII sobre APIs C
> O exemplo mostra o uso de `unique_ptr` com **deleter customizado** ([[Deleters Customizados]]) para recursos de bibliotecas C — evita vazamentos mesmo em saídas antecipadas.

## Veja também

- [[Cpp em Jogos]]
- [[Deleters Customizados]]
- [[Visão Geral das Bibliotecas]]
- [[Cache e Localidade de Dados]]

## Exercício

1. Faça um quadrado controlado pelas setas com passo de tempo fixo.
2. Troque os recursos crus por `unique_ptr` com deleters para `SDL_Texture`.
