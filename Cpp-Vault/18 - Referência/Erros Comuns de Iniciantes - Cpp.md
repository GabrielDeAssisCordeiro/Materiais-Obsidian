---
titulo: "Erros Comuns de Iniciantes - Cpp"
tags: [cpp, referencia, erros, boas-praticas]
aliases: ["Erros de iniciantes", "Armadilhas de iniciante", "Beginner mistakes"]
tipo: referencia
nivel: iniciante
padrao: C++20
criado: 2026-10-24
relacionados: ["[[FAQ - Cpp]]", "[[Catálogo de Armadilhas e UB]]", "[[Tabela de Erros de Compilador e Linker]]"]
---

# Erros Comuns de Iniciantes - Cpp

Cada item: **sintoma → causa → correção**. Os trechos "ERRO" não devem ser compilados como estão.

## 1. Variável não inicializada

```cpp
// ERRO: int x; std::cout << x;     // valor indeterminado (UB ao ler)
```

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    int x{};                                // CORREÇÃO: inicialize sempre
    std::cout << x << '\n';
}
```

## 2. `=` em vez de `==`

```cpp
// ERRO: if (n = 5) { ... }        // atribui 5 e sempre é verdadeiro
// CORREÇÃO: if (n == 5)           // -Wall avisa: "suggest parentheses around assignment"
```

## 3. Divisão inteira e conversões

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    int a = 7, b = 2;
    std::cout << a / b << ' ' << static_cast<double>(a) / b << '\n';   // 3 3.5: converta ANTES de dividir
    std::cout << 0.1 + 0.2 << ' ' << (0.1 + 0.2 == 0.3) << '\n';       // 0.3 0 : não compare double com ==
}
```

## 4. Fora dos limites e sinal vs sem sinal

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3};
    // for (int i = 0; i <= v.size(); ++i) ...   ERRO: <= acessa v[3] (UB) e compara int com size_t
    for (std::size_t i = 0; i < v.size(); ++i) std::cout << v[i];       // correto
    for (int x : v) std::cout << x;                                     // melhor: range-for
    std::cout << '\n';
}
```

> [!bug] Armadilha do `size_t`
> `for (unsigned i = n - 1; i >= 0; --i)` é **laço infinito** (sem sinal nunca é negativo). Use `for (std::size_t i = n; i-- > 0;)`.

## 5. Retornar referência/ponteiro para local

```cpp
// ERRO: int& f() { int x = 1; return x; }   // x morre ao sair: referência pendente (UB)
// CORREÇÃO: retorne por VALOR: int f() { int x = 1; return x; }
```

## 6. Esquecer `delete` / usar `delete` errado

```cpp
// ERRO: int* p = new int[10]; ... delete p;   // deve ser delete[] p  (UB)
// CORREÇÃO: std::vector<int> v(10);  // ou std::make_unique<int[]>(10)
```

## 7. Copiar objetos grandes sem querer

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

std::size_t conta(const std::vector<std::string>& v) { return v.size(); }   // const& : sem cópia
// std::size_t conta_ruim(std::vector<std::string> v)                       // COPIA o vetor inteiro

int main() {
    std::vector<std::string> v(1000, "texto");
    for (const auto& s : v) (void)s;                                        // 'const auto&' evita copiar cada string
    std::cout << conta(v) << '\n';
}
```

## 8. Misturar `cin >>` e `getline`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <limits>
#include <sstream>
#include <string>

int main() {
    std::istringstream in{"42\nMaria Silva\n"};          // simula o teclado
    int idade;
    in >> idade;                                          // deixa o '\n' no buffer
    in.ignore(std::numeric_limits<std::streamsize>::max(), '\n');   // descarte o resto da linha ANTES do getline
    std::string nome;
    std::getline(in, nome);
    std::cout << idade << ' ' << nome << '\n';
}
```

## 9. Switch sem `break`; `;` depois de `if`/`for`

```cpp
// ERRO:  for (int i = 0; i < 3; ++i);     // o ';' vira o corpo vazio
//          std::cout << i;                 // executa uma vez só (e 'i' nem existe aqui)
// ERRO:  case 1: fazA(); case 2: fazB();   // sem break, cai no próximo (use break ou [[fallthrough]])
```

## 10. Includes e `using namespace std;` em header

> [!warning] `using namespace std;` em headers
> Polui **todos** os arquivos que incluem o header e causa colisões (`count`, `min`, `distance`). Em `.cpp` pequenos é tolerável; em headers, **nunca**.

## 11. Recursos sem RAII e exceções

Chamar `fopen`/`new`/`lock()` manual e depois uma função que lança deixa o recurso vazar: use [[RAII]] (`ifstream`, `unique_ptr`, `lock_guard`).

## 12. Ignorar os avisos do compilador

Compile **sempre** com `-Wall -Wextra` (e `-Wpedantic`); trate avisos como bugs. Veja [[Flags Essenciais do Compilador]].

## Veja também

- [[FAQ - Cpp]]
- [[Catálogo de Armadilhas e UB]]
- [[Tabela de Erros de Compilador e Linker]]
- [[Comportamento Indefinido e Não Especificado]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Para cada item acima, escreva um programa curto que reproduza o erro e rode com `-fsanitize=address,undefined`.
2. Reescreva seu último programa aplicando RAII e `const&` onde faz sentido.
