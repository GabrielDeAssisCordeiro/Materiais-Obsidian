---
titulo: "= default e = delete"
tags: [cpp, poo, delete]
aliases: ["= default", "= delete", "Funções membro especiais", "Special member functions"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Construtores e Destrutores]]", "[[Slicing]]", "[[Sobrecarga de Funções]]"]
---

# `= default` e `= delete`

> [!info] Introdução
> **C++11.** `= default` pede ao compilador a implementação padrão; `= delete` **proíbe** a função (qualquer uso é erro de compilação).

## Funções membro especiais

O compilador pode gerar automaticamente (em condições específicas):

| Função | Assinatura | Gerada quando... |
|---|---|---|
| Construtor padrão | `T()` | Nenhum outro construtor declarado |
| Destrutor | `~T()` | Sempre (se não declarado) |
| Construtor de cópia | `T(const T&)` | Não há movimento declarado |
| Atribuição de cópia | `T& operator=(const T&)` | Não há movimento declarado |
| Construtor de movimento | `T(T&&)` | Não há cópia, atribuição nem destrutor declarados |
| Atribuição de movimento | `T& operator=(T&&)` | Idem |

> [!info] Regras de geração detalhadas
> A interação entre elas (Regra do 0, 3 e 5) é tratada na seção de RAII e Move.

## `= default`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

class Usuario {
public:
    Usuario() = default;                               // restaura o construtor padrão
    explicit Usuario(std::string nome) : nome_(std::move(nome)) {}

    Usuario(const Usuario&) = default;                 // cópia padrão (documenta a intenção)
    Usuario& operator=(const Usuario&) = default;
    ~Usuario() = default;

    friend bool operator==(const Usuario&, const Usuario&) = default;   // C++20

    const std::string& nome() const { return nome_; }
private:
    std::string nome_ = "?";
    int nivel_ = 0;
};

int main() {
    Usuario a, b{"ana"};
    a = b;
    std::cout << a.nome() << (a == b) << '\n';   // ana1
}
```

## `= delete`

### 1) Proibir cópia (tipos de posse única)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <utility>

class Recurso {
public:
    Recurso() = default;
    Recurso(const Recurso&) = delete;              // não copiável
    Recurso& operator=(const Recurso&) = delete;
    Recurso(Recurso&&) noexcept = default;         // movível
    Recurso& operator=(Recurso&&) noexcept = default;
};

int main() {
    Recurso a;
    // Recurso b = a;                              // erro: cópia deletada
    Recurso b = std::move(a);                      // ok
    (void)b;
}
```

### 2) Bloquear conversões e sobrecargas indesejadas

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void liga(bool) { std::cout << "bool\n"; }
void liga(int) = delete;                           // impede liga(5) e liga('a')
void liga(double) = delete;

int main() {
    liga(true);
    // liga(5);                                    // erro: uso de função deletada
}
```

### 3) Proibir alocação dinâmica ou criação em certos contextos

```cpp
struct SoNaStack {
    static void* operator new(std::size_t) = delete;   // SoNaStack* p = new SoNaStack;  -> erro
};
```

> [!tip] Vantagem sobre "declarar privado e não definir"
> O truque pré-C++11 produzia erros de linker tardios e mensagens obscuras. `= delete` falha **na compilação**, com mensagem clara, e vale também para funções livres.

> [!warning] Declarar um destrutor ou cópia suprime o movimento
> Se você escrever `~T()` ou `T(const T&)`, o compilador **não** gera movimento implicitamente; o código ainda compila (cai em cópias), mas perde desempenho. Use `= default` explicitamente.

## Veja também

- [[Construtores e Destrutores]]
- [[Slicing]]
- [[Sobrecarga de Funções]]
- [[Lvalue e Rvalue]]

## Exercício

1. Crie `ArquivoRAII` não copiável e movível; tente copiar e leia o erro do compilador.
2. Escreva uma função `raiz(double)` e delete `raiz(int)` para evitar chamadas ambíguas por engano.
