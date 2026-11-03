---
titulo: "Referências - Cpp"
tags: [cpp, memoria]
aliases: ["References", "T&", "const T&", "Referência vs ponteiro"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Ponteiros]]", "[[Lvalue e Rvalue]]", "[[Funções - Cpp]]"]
---

# Referências - Cpp

Uma **referência** é um **apelido** (*alias*) para um objeto existente. Depois de ligada, ela **é** o objeto: toda operação na referência acontece no original.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

void incrementa(int& n) { ++n; }                          // modifica o argumento original
void imprime(const std::string& s) { std::cout << s << '\n'; }   // lê sem copiar

int& maior(int& a, int& b) { return a > b ? a : b; }      // retorna referência ao próprio objeto

int main() {
    int x = 5;
    int& r = x;                      // r é outro nome para x
    r = 10;
    std::cout << x << '\n';          // 10

    incrementa(x);
    std::cout << x << '\n';          // 11

    int a = 1, b = 2;
    maior(a, b) = 99;                // atribui ao maior: b passa a ser 99
    std::cout << a << ' ' << b << '\n';   // 1 99

    imprime("literal vira std::string temporária, ligada a const&");

    std::vector<int> v{1, 2, 3};
    for (int& e : v) e *= 10;        // modifica os elementos no lugar
    std::cout << v[2] << '\n';       // 30
}
```

## Regras das referências

1. **Devem ser inicializadas** na declaração.
2. **Não podem ser reatribuídas** a outro objeto (`r = y` copia o valor de `y` para o objeto referido).
3. **Não existe referência nula** (um programa válido nunca a cria).
4. **Não têm endereço próprio** observável: `&r` é o endereço do objeto referido.

## Referências para `const` e temporários

`const T&` pode ligar-se a **rvalues** (temporários). O temporário tem a vida **estendida** até o fim da referência.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

int main() {
    const std::string& r = std::string("temporário");   // vida estendida até o fim de r
    std::cout << r << '\n';

    // std::string& nr = std::string("x");               // erro: referência não const não liga a rvalue
}
```

## Referência vs ponteiro

| | Referência | Ponteiro |
|---|---|---|
| Pode ser nula | Não | Sim (`nullptr`) |
| Pode ser reatribuída | Não | Sim |
| Precisa de `*` para acessar | Não (sintaxe natural) | Sim |
| Aritmética | Não | Sim |
| Em contêineres | Não (use `std::reference_wrapper`) | Sim |
| Uso típico | Parâmetros e retornos que **não** podem ser nulos | Opcional, estruturas ligadas, APIs C |

## Referências em classes

Membros referência exigem inicialização na lista de inicialização do construtor e tornam a classe **não atribuível** (a atribuição padrão fica deletada). Prefira ponteiros ou `std::reference_wrapper` quando precisar reatribuir.

## Referências de rvalue (`T&&`)

Introduzidas no C++11, permitem **mover** recursos de temporários — a base da semântica de movimento. Veja [[Lvalue e Rvalue]].

> [!danger] Referência pendente
> ```cpp
> const int& ruim() { int x = 1; return x; }   // referência para variável local: UB ao usar
> std::vector<int> v{1};
> int& primeiro = v[0];
> v.push_back(2);                              // pode realocar: 'primeiro' fica pendente (UB)
> ```
> **Correção:** retorne por valor; não guarde referências a elementos depois de operações que podem realocar o contêiner.

## Veja também

- [[Ponteiros]]
- [[Lvalue e Rvalue]]
- [[Funções - Cpp]]
- [[Vazamentos e Dangling Pointers]]

## Exercício

1. Escreva `void troca(int& a, int& b)` e compare com a versão com ponteiros.
2. Explique por que `const std::string& r = "abc";` funciona e `std::string& r = "abc";` não.
