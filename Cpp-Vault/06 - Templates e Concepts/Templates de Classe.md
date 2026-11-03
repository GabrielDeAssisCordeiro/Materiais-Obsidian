---
titulo: "Templates de classe"
tags: [cpp, templates, genericos, classes]
aliases: ["Templates de classe", "Class templates", "Classe genérica", "Membros de template"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Templates de Função]]", "[[Especialização de Templates]]", "[[CTAD]]"]
---

# Templates de classe

Permitem criar **tipos genéricos**: `std::vector<T>`, `std::unique_ptr<T>`, `std::map<K, V>` são templates de classe.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

template <typename T>
class Pilha {
public:
    void empilha(const T& v) { dados_.push_back(v); }
    void empilha(T&& v) { dados_.push_back(std::move(v)); }

    template <typename... Args>
    T& emplace(Args&&... args) {                        // template de MEMBRO dentro de template de classe
        return dados_.emplace_back(std::forward<Args>(args)...);
    }

    T desempilha() {
        if (dados_.empty()) throw std::out_of_range("pilha vazia");
        T topo = std::move(dados_.back());
        dados_.pop_back();
        return topo;
    }

    const T& topo() const { return dados_.back(); }
    bool vazia() const { return dados_.empty(); }
    std::size_t tamanho() const { return dados_.size(); }

private:
    std::vector<T> dados_;
};

int main() {
    Pilha<int> pi;                         // instancia Pilha<int>
    pi.empilha(1);
    pi.empilha(2);
    std::cout << pi.desempilha() << pi.tamanho() << '\n';      // 21

    Pilha<std::pair<int, std::string>> pp;                    // tipo composto
    pp.emplace(1, "um");
    std::cout << pp.topo().second << '\n';
}
```

## Definindo membros fora da classe

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <utility>

template <typename T>
class Caixa {
public:
    explicit Caixa(T v);
    T get() const;
    template <typename U> Caixa<U> converte() const;   // template de membro
private:
    T valor_;
};

template <typename T>
Caixa<T>::Caixa(T v) : valor_(std::move(v)) {}         // repete 'template <typename T>' e usa Caixa<T>::

template <typename T>
T Caixa<T>::get() const { return valor_; }

template <typename T>
template <typename U>                                   // dois níveis de template
Caixa<U> Caixa<T>::converte() const { return Caixa<U>(static_cast<U>(valor_)); }

int main() {
    Caixa<int> c{7};
    std::cout << c.converte<double>().get() / 2 << '\n';   // 3.5
}
```

## Detalhes importantes

| Tópico | Regra |
|---|---|
| Instanciação **preguiçosa** | Só os membros **usados** são instanciados |
| `typename` para tipos dependentes | `typename Container::value_type x;` |
| `template` para membros dependentes | `obj.template metodo<int>()` |
| Tipos dependentes e base dependente | Em bases dependentes use `this->membro` ou `Base<T>::membro` |
| Membros `static` | Um por **instanciação** (`Pilha<int>` e `Pilha<double>` têm estáticos distintos) |
| `friend` | `template <typename U> friend class Outra;` |

> [!warning] Nome dependente precisa de `typename`
> ```cpp
> template <typename C> void f() {
>     C::iterator it;                      // erro: C::iterator é tipo ou valor? (ambíguo)
>     typename C::iterator it2;            // correto
> }
> ```

## Aliases de template

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <map>
#include <string>
#include <vector>

template <typename T> using Lista = std::vector<T>;
template <typename V> using MapaPorNome = std::map<std::string, V>;

int main() {
    Lista<int> a{1, 2, 3};
    MapaPorNome<double> m{{"pi", 3.14}};
    return static_cast<int>(a.size() + m.size());
}
```

## Veja também

- [[Templates de Função]]
- [[Especialização de Templates]]
- [[CTAD]]
- [[Parâmetros Não-Tipo]]
- [[Concepts e requires]]

## Exercício

1. Implemente `Par<A, B>` com `primeiro()`/`segundo()` e uma função `trocar()` que retorna `Par<B, A>`.
2. Explique por que `Pilha<int>::desempilha` só é compilada se for chamada.
