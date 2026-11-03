---
titulo: "std::weak_ptr"
tags: [cpp, smart-pointers, weak_ptr]
aliases: ["std::weak_ptr", "weak_ptr", "Referência fraca", "lock()", "expired()"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[shared_ptr]]", "[[Ciclos de Referência]]", "[[unique_ptr]]"]
---

# `std::weak_ptr`

`weak_ptr<T>` é uma **referência não-possuidora** a um objeto gerenciado por `shared_ptr`: **observa** sem prolongar a vida. Serve para quebrar ciclos e para caches/observadores.

- Não incrementa a contagem **forte** (apenas a **fraca**).
- Não permite acesso direto: é preciso `lock()` para obter um `shared_ptr` temporário (ou nulo, se o objeto já morreu).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>

struct Dado { int v = 42; ~Dado() { std::cout << "Dado destruído\n"; } };

int main() {
    std::weak_ptr<Dado> fraco;
    {
        auto forte = std::make_shared<Dado>();
        fraco = forte;                                        // não aumenta use_count
        std::cout << forte.use_count() << ' ' << fraco.expired() << '\n';   // 1 0

        if (auto p = fraco.lock()) {                          // promove a shared_ptr temporário
            std::cout << "vivo: " << p->v << '\n';
        }
    }                                                         // 'forte' morre aqui: objeto destruído
    std::cout << fraco.expired() << '\n';                     // 1
    if (auto p = fraco.lock()) std::cout << "não deveria\n";
    else std::cout << "objeto já destruído\n";
}
```

## Por que `lock()` e não `expired()` + acesso

> [!bug] Condição de corrida (TOCTOU)
> ```cpp
> if (!w.expired()) {        // verifica...
>     use(*w.lock());        // ...e o objeto pode ter morrido entre as duas linhas (outra thread)
> }
> ```
> **Correção:** `if (auto p = w.lock()) { use(*p); }` — a promoção é atômica e mantém o objeto vivo durante o uso.

## Casos de uso

| Caso | Descrição |
|---|---|
| **Quebrar ciclos** | O "pai" tem `shared_ptr` para filhos; o filho tem `weak_ptr` para o pai ([[Ciclos de Referência]]) |
| **Cache** | Mapa de `weak_ptr` para objetos que podem ser descartados quando ninguém os usa |
| **Observadores/callbacks** | A lista de assinantes não deve manter vivos os objetos |
| **`enable_shared_from_this`** | Internamente guarda um `weak_ptr` ao próprio objeto |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <map>
#include <memory>
#include <string>

struct Imagem { explicit Imagem(std::string n) : nome(std::move(n)) { std::cout << "carregando " << nome << '\n'; } std::string nome; };

std::shared_ptr<Imagem> carrega(const std::string& nome) {
    static std::map<std::string, std::weak_ptr<Imagem>> cache;
    if (auto p = cache[nome].lock()) return p;               // ainda em uso: reaproveita
    auto novo = std::make_shared<Imagem>(nome);
    cache[nome] = novo;
    return novo;
}

int main() {
    auto a = carrega("gato.png");                            // carrega
    auto b = carrega("gato.png");                            // reaproveita (sem novo "carregando")
    std::cout << (a == b) << '\n';                           // 1
}
```

## Veja também

- [[shared_ptr]]
- [[Ciclos de Referência]]
- [[unique_ptr]]
- [[Vazamentos e Dangling Pointers]]

## Exercício

1. Implemente um cache de objetos pesados com `weak_ptr` e mostre que o objeto é recriado após ser liberado.
2. Por que `weak_ptr` não tem `operator*` nem `operator->`?
