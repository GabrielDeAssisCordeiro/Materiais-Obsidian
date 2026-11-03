---
titulo: "Primeiro programa"
tags: [cpp, fundamentos, iostream]
aliases: ["Primeiro programa em C++"]
tipo: procedimento
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Pipeline de Compilação - Cpp]]", "[[Flags Essenciais do Compilador]]", "[[Instalação no Linux - Cpp]]"]
---

# Primeiro programa

## Olá, mundo

```cpp
// g++ -std=c++20 -Wall -Wextra -o ola ola.cpp
#include <iostream>   // declara std::cout

int main() {                              // ponto de entrada do programa
    std::cout << "Olá, mundo!\n";         // escreve no fluxo de saída padrão
    return 0;                             // opcional em main: o padrão é 0
}
```

Compile e execute:

```bash
g++ -std=c++20 -Wall -Wextra ola.cpp -o ola
./ola          # no Windows (MSVC): ola.exe
```

## Anatomia

| Trecho | Significado |
|---|---|
| `#include <iostream>` | Diretiva do pré-processador: traz as declarações de entrada/saída |
| `int main()` | Função principal; o sistema operacional a chama. Retorna `int` (código de saída) |
| `std::cout` | Objeto de saída padrão; `std::` é o *namespace* da biblioteca padrão |
| `<<` | Operador de inserção em fluxo, encadeável |
| `"..."` | Literal de string (tipo `const char[N]`) |
| `'\n'` | Quebra de linha; mais rápida que `std::endl` (que também descarrega o buffer) |
| `return 0;` | Em `main` pode ser omitido; `0` indica sucesso |

> [!tip] `'\n'` ou `std::endl`?
> Use `'\n'`. `std::endl` insere a quebra **e** força *flush*, o que pode deixar saídas volumosas muito mais lentas.

## Lendo da entrada

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

int main() {
    std::string nome;
    std::cout << "Qual é o seu nome? ";
    std::getline(std::cin, nome);                       // lê a linha inteira
    std::cout << "Olá, " << nome << "!\n";
}
```

## Versão C++23 com `std::print`

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra  (requer GCC 14+, MSVC 17.7+ ou libc++ 18+)
#include <print>

int main() {
    std::println("Olá, {}!", "mundo");   // formatação segura em tipos, estilo Python
}
```

> [!info] `<print>` (C++23)
> Suporte: GCC 14, MSVC 19.37 (VS 2022 17.7), libc++ 18 (com ressalvas).
> [!question] Verificar na documentação oficial
> Confirme a versão mínima do seu compilador na página de suporte da cppreference.

## Erros comuns do primeiro dia

> [!bug] Exemplo inválido proposital: esquecer o `#include`
> ```cpp
> int main() {
>     std::cout << "oi\n";   // erro: 'cout' is not a member of 'std'
> }
> ```
> **Correção:** adicione `#include <iostream>`.

> [!bug] Exemplo inválido proposital: esquecer `std::`
> ```cpp
> #include <iostream>
> int main() {
>     cout << "oi\n";        // erro: 'cout' was not declared in this scope
> }
> ```
> **Correção:** escreva `std::cout` (evite `using namespace std;` em cabeçalhos e, de preferência, em geral).

## Veja também

- [[Pipeline de Compilação - Cpp]]
- [[Flags Essenciais do Compilador]]
- [[Escolhendo o Padrão com -std]]
- [[IDEs e Editores]]
- [[O que é Cpp]]

## Exercício

1. Altere o programa para pedir dois números inteiros e imprimir a soma (`std::cin >> a >> b`).
2. Compile com `-Wall -Wextra` e remova `return 0;`. Houve aviso? Por quê?
