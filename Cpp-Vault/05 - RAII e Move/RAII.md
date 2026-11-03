---
titulo: "RAII"
tags: [cpp, raii, recursos, destrutores, excecoes]
aliases: ["Resource Acquisition Is Initialization", "Aquisição de recurso é inicialização"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Regra do 0, 3 e 5]]", "[[unique_ptr]]", "[[Construtores e Destrutores]]"]
---

# RAII

**RAII** (*Resource Acquisition Is Initialization*) é o idioma central do C++: **atrelar o ciclo de vida de um recurso ao de um objeto**. O recurso é adquirido no **construtor** e liberado no **destrutor**; como destrutores rodam deterministicamente ao sair do escopo (inclusive por exceção), o recurso nunca vaza.

Recursos: memória, arquivos, *sockets*, *locks*, transações, conexões, handles de GPU.

## Sem RAII vs com RAII

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdio>
#include <stdexcept>

// SEM RAII: cada saída precisa lembrar de fechar
void sem_raii(bool falha) {
    std::FILE* f = std::fopen("/tmp/raii.txt", "w");
    if (!f) return;
    if (falha) {
        std::fclose(f);                         // fácil esquecer em algum ramo
        throw std::runtime_error("falha");
    }
    std::fputs("ok\n", f);
    std::fclose(f);
}

// COM RAII: o destrutor fecha sempre
class Arquivo {
public:
    explicit Arquivo(const char* caminho) : f_(std::fopen(caminho, "w")) {
        if (!f_) throw std::runtime_error("não abriu");    // construtor falhou: objeto não existe
    }
    ~Arquivo() { std::fclose(f_); }
    Arquivo(const Arquivo&) = delete;                       // um dono por recurso
    Arquivo& operator=(const Arquivo&) = delete;
    void escreve(const char* s) { std::fputs(s, f_); }
private:
    std::FILE* f_;
};

void com_raii(bool falha) {
    Arquivo a{"/tmp/raii.txt"};
    if (falha) throw std::runtime_error("falha");           // 'a' é destruído (e fechado) no unwinding
    a.escreve("ok\n");
}

int main() {
    try { com_raii(true); } catch (const std::exception&) {}
    sem_raii(false);
}
```

## RAII na biblioteca padrão

| Recurso | Tipo RAII |
|---|---|
| Memória (heap) | `std::vector`, `std::string`, `std::unique_ptr`, `std::shared_ptr` |
| Arquivos | `std::fstream`, `std::ifstream`, `std::ofstream` |
| Locks | `std::lock_guard`, `std::unique_lock`, `std::scoped_lock` |
| Threads | `std::jthread` (junta no destrutor) |
| Transações/escopo | *scope guards* (`std::experimental::scope_exit`, bibliotecas) |

## Um *scope guard* simples

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <utility>

template <typename F>
class AoSair {                                  // executa F ao destruir
public:
    explicit AoSair(F f) : f_(std::move(f)) {}
    ~AoSair() { if (ativo_) f_(); }
    AoSair(const AoSair&) = delete;
    AoSair& operator=(const AoSair&) = delete;
    void cancelar() { ativo_ = false; }
private:
    F f_;
    bool ativo_ = true;
};

int main() {
    AoSair limpa{[] { std::cout << "limpeza\n"; }};
    std::cout << "trabalhando\n";
}   // imprime "trabalhando" e depois "limpeza"
```

## Princípios

1. **Um recurso, um dono** — o objeto RAII.
2. **Construtor**: adquire e estabelece invariantes; se falhar, lança exceção.
3. **Destrutor**: libera, sem lançar exceções.
4. **Cópia**: proibir (`= delete`), tornar *deep copy* ou *movível* — veja [[Regra do 0, 3 e 5]].
5. Prefira **tipos RAII prontos** a escrever o seu.

> [!tip] Sem `new`/`delete` nem `fopen`/`fclose` soltos em código de aplicação
> Se aparecer um par aquisição/liberação manual, encapsule em uma classe RAII ou use `unique_ptr` com *deleter* ([[Deleters Customizados]]).

> [!warning] RAII não resolve tudo
> Ciclos de `shared_ptr` ([[Ciclos de Referência]]), recursos que não podem ser liberados no destrutor (operações que falham) e *threads* destacadas exigem atenção.

## Veja também

- [[Regra do 0, 3 e 5]]
- [[unique_ptr]]
- [[Construtores e Destrutores]]
- [[Vazamentos e Dangling Pointers]]
- [[Deleters Customizados]]

## Exercício

1. Escreva uma classe RAII `Temporizador` que imprime o tempo decorrido ao ser destruída.
2. Por que o destrutor de uma classe RAII não deve lançar exceções?
