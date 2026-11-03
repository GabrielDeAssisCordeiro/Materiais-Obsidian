---
titulo: "Vazamentos e *dangling pointers*"
tags: [cpp, memoria, vazamento, sanitizers]
aliases: ["Memory leak", "Dangling pointer", "Use-after-free", "Double free", "Ponteiro pendente"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[new e delete]]", "[[nullptr]]", "[[Stack vs Heap]]"]
---

# Vazamentos e *dangling pointers*

## Principais bugs de memória

| Bug | O que acontece | Consequência |
|---|---|---|
| **Vazamento** (*leak*) | Memória alocada nunca é liberada | Consumo crescente de memória |
| **Use-after-free** | Usar memória depois de `delete` | UB, corrupção, falha de segurança |
| **Double free** | `delete` duas vezes no mesmo bloco | UB, corrupção do heap |
| **Dangling pointer/reference** | Ponteiro/referência para objeto que não existe mais | UB |
| **Buffer overflow** | Escrever além dos limites | UB, vulnerabilidade |
| **Leitura não inicializada** | Usar valor indeterminado | UB (C++26: *erroneous behavior*) |

## Vazamento

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <memory>
#include <stdexcept>

void vaza(bool falha) {
    int* p = new int[1000];       // alocado
    if (falha) throw std::runtime_error("erro");   // sai SEM liberar: vazamento
    delete[] p;                   // só chega aqui no caminho feliz
}

void seguro(bool falha) {
    auto p = std::make_unique<int[]>(1000);        // RAII: libera em qualquer saída
    if (falha) throw std::runtime_error("erro");
}

int main() {
    try { vaza(true); } catch (...) {}      // vazou 4000 bytes
    try { seguro(true); } catch (...) {}    // não vaza
}
```

> [!tip] Como achar vazamentos
> `g++ -fsanitize=address -g` (AddressSanitizer inclui LeakSanitizer no Linux) ou `valgrind --leak-check=full ./app`.

## Ponteiros e referências pendentes

> [!danger] Exemplos de dangling (propositalmente inválidos)
> ```cpp
> // 1) Retornar endereço de variável local
> int* f() { int x = 5; return &x; }          // x morre; retorno é pendente
>
> // 2) Usar após delete
> int* p = new int(1);
> delete p;
> *p = 2;                                     // use-after-free: UB
>
> // 3) Invalidação de iterador/ponteiro por realocação
> std::vector<int> v{1, 2, 3};
> int* primeiro = &v[0];
> v.push_back(4);                             // pode realocar o buffer
> *primeiro = 9;                              // possivelmente pendente: UB
>
> // 4) Referência a temporário
> const std::string& r = std::string("a") + "b";   // OK: vida estendida
> std::string_view sv = std::string("a") + "b";    // PENDENTE: o temporário morre no ';'
> ```
> **Correções:** retorne por valor; não use após `delete`; recalcule ponteiros depois de modificar contêineres; guarde o `std::string` em uma variável antes de criar o `string_view`.

## Defesas em C++ moderno

1. **RAII** e **smart pointers** em vez de `new`/`delete`.
2. **Regra do zero**: deixe contêineres e smart pointers gerenciarem recursos.
3. **Posse clara**: `unique_ptr` = dono único; `T*`/`T&` = observador; `shared_ptr` só quando há posse compartilhada real.
4. **Sanitizers** em desenvolvimento e CI: ASan, UBSan, LSan.
5. **Avisos**: `-Wall -Wextra`, `-Wdangling-pointer`, `clang-tidy` (`bugprone-*`, `cppcoreguidelines-*`).
6. **Hardening** da biblioteca padrão e perfis de segurança (veja a seção de avançado).

```bash
g++ -std=c++20 -g -fsanitize=address,undefined -fno-omit-frame-pointer app.cpp -o app
./app    # o relatório mostra o tipo de erro, a pilha e onde o bloco foi alocado/liberado
```

> [!warning] `p = nullptr` após `delete` não basta
> Outros ponteiros para o mesmo bloco continuam pendentes. A solução real é **posse única e clara**.

## Veja também

- [[new e delete]]
- [[nullptr]]
- [[Stack vs Heap]]
- [[Referências - Cpp]]

## Exercício

1. Compile o `vaza(true)` com `-fsanitize=address` e interprete o relatório.
2. Reproduza o caso 3 (invalidação por `push_back`) e observe o resultado com ASan.
