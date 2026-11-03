---
titulo: "Deleters* customizados"
tags: [cpp, smart-pointers, raii]
aliases: ["Deleter", "Deleters customizados", "unique_ptr com deleter", "Custom deleter"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[unique_ptr]]", "[[shared_ptr]]", "[[RAII]]"]
---

# *Deleters* customizados

Smart pointers podem gerenciar **qualquer recurso**, não só memória de `new`, trocando a função de liberação (*deleter*).

## `unique_ptr`: o deleter faz parte do tipo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdio>
#include <iostream>
#include <memory>

// 1) Struct com operator() (sem custo de tamanho se não tiver estado)
struct FechaArquivo {
    void operator()(std::FILE* f) const { if (f) std::fclose(f); }
};
using ArquivoPtr = std::unique_ptr<std::FILE, FechaArquivo>;

// 2) Ponteiro para função (o unique_ptr fica maior: guarda o ponteiro)
using ArquivoPtr2 = std::unique_ptr<std::FILE, decltype(&std::fclose)>;

// 3) Lambda (C++20: lambdas sem captura são default-constructible; em C++11/14 passe o deleter)
auto fechar = [](std::FILE* f) { if (f) std::fclose(f); };

int main() {
    ArquivoPtr a{std::fopen("/tmp/dl1.txt", "w")};
    if (a) std::fputs("olá\n", a.get());

    ArquivoPtr2 b{std::fopen("/tmp/dl2.txt", "w"), &std::fclose};
    if (b) std::fputs("mundo\n", b.get());

    std::unique_ptr<std::FILE, decltype(fechar)> c{std::fopen("/tmp/dl3.txt", "w"), fechar};
    if (c) std::fputs("!\n", c.get());

    std::cout << sizeof(a) << ' ' << sizeof(b) << '\n';       // 8 16: deleter vazio não ocupa espaço
}
```

## Recursos não-memória

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdlib>
#include <iostream>
#include <memory>

struct LiberaC {                                   // memória alocada com malloc deve usar free
    void operator()(void* p) const noexcept { std::free(p); }
};

int main() {
    std::unique_ptr<int, LiberaC> p{static_cast<int*>(std::malloc(sizeof(int)))};
    *p = 99;
    std::cout << *p << '\n';
}   // free(p), não delete
```

Exemplos reais: `SDL_DestroyWindow`, `sqlite3_close`, `CloseHandle` (Windows), `curl_easy_cleanup`, `fclose`, `dlclose`.

## `shared_ptr`: o deleter **não** faz parte do tipo

O deleter fica guardado no bloco de controle (apagamento de tipo), então `shared_ptr<T>` é igual para qualquer deleter.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> p(new int(5), [](int* x) {
        std::cout << "deleter customizado: " << *x << '\n';
        delete x;
    });
    auto q = p;                                    // mesmo tipo, mesmo deleter
}   // o deleter roda quando o último dono morre
```

## Comparação

| | `unique_ptr<T, D>` | `shared_ptr<T>` |
|---|---|---|
| Deleter no tipo? | **Sim** (`D` é parâmetro de template) | Não |
| Custo de tamanho | `sizeof(D)` extra (0 se vazio) | Dentro do bloco de controle |
| Chamada | Inline possível (sem indireção) | Indireta |

> [!tip] Padrão idiomático
> Defina um *alias* e (idealmente) uma função fábrica que já devolve o ponteiro configurado:
> ```cpp
> ArquivoPtr abre(const char* caminho, const char* modo) { return ArquivoPtr{std::fopen(caminho, modo)}; }
> ```

> [!warning] O deleter só roda se o ponteiro for **não nulo**
> Para `unique_ptr`, o deleter não é chamado em `nullptr`. Para APIs que exigem chamada mesmo com valor "nulo" (handles inteiros como `-1`), escreva uma classe RAII própria.

## Veja também

- [[unique_ptr]]
- [[shared_ptr]]
- [[RAII]]
- [[make_unique e make_shared]]

## Exercício

1. Crie `unique_ptr` com deleter para um handle `int fd` do POSIX (`open`/`close`) — por que o `unique_ptr` não serve diretamente e como contornar com uma classe RAII?
2. Meça `sizeof` de `unique_ptr<int, void(*)(int*)>` vs `unique_ptr<int, StructVazia>`.
