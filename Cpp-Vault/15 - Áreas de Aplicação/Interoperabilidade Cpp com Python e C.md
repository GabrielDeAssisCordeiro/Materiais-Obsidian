---
titulo: "Interoperabilidade: C++ com C, Python e outras linguagens"
tags: [cpp, aplicacoes, extern-c, ffi, python]
aliases: ["Interoperabilidade", "pybind11", "nanobind", "ctypes", "Cython", "Cpp e Python", "API C"]
tipo: area
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[ABI]]", "[[Linkage]]", "[[Bibliotecas Estáticas e Dinâmicas]]"]
---

# Interoperabilidade: C++ com C, Python e outras linguagens

A fronteira entre linguagens passa quase sempre pela **ABI do C** ([[ABI]]): funções `extern "C"`, tipos simples (inteiros, ponteiros, `struct` de layout padrão) e *handles* opacos.

## Padrão: API C estável sobre uma implementação C++

```cpp
// g++ -std=c++20 -Wall -Wextra -fPIC
#include <cstddef>
#include <iostream>
#include <new>
#include <string>
#include <vector>

// ---------- Implementação C++ (interna) ----------
class Acumulador {
public:
    void somar(double v) { valores_.push_back(v); }
    double total() const { double s = 0; for (double v : valores_) s += v; return s; }
private:
    std::vector<double> valores_;
};

// ---------- API C (estável; sem exceções atravessando a fronteira) ----------
extern "C" {
struct acc_t;                                                       // tipo opaco para o chamador

acc_t* acc_criar() noexcept { return reinterpret_cast<acc_t*>(new (std::nothrow) Acumulador); }
void   acc_destruir(acc_t* a) noexcept { delete reinterpret_cast<Acumulador*>(a); }

int acc_somar(acc_t* a, double v) noexcept {                       // retorna 0 em sucesso
    try { reinterpret_cast<Acumulador*>(a)->somar(v); return 0; }
    catch (...) { return -1; }                                      // NUNCA deixe exceção cruzar a fronteira
}
double acc_total(const acc_t* a) noexcept { return reinterpret_cast<const Acumulador*>(a)->total(); }
}

int main() {                                                        // uso (poderia ser C, Python/ctypes, Rust...)
    acc_t* a = acc_criar();
    acc_somar(a, 1.5);
    acc_somar(a, 2.5);
    std::cout << acc_total(a) << '\n';                              // 4
    acc_destruir(a);
}
```

```python
# Python com ctypes: carregando a biblioteca compartilhada gerada (libacc.so)
import ctypes
lib = ctypes.CDLL("./libacc.so")
lib.acc_criar.restype = ctypes.c_void_p
lib.acc_somar.argtypes = [ctypes.c_void_p, ctypes.c_double]
lib.acc_total.argtypes = [ctypes.c_void_p]
lib.acc_total.restype = ctypes.c_double

a = lib.acc_criar()
lib.acc_somar(a, 1.5)
print(lib.acc_total(a))
lib.acc_destruir(a)
```

## pybind11 / nanobind

Geram *bindings* Python diretamente de código C++ moderno, convertendo `std::vector`, `std::string`, `std::optional`, NumPy arrays, e expondo classes.

```cpp
// [nv] c++ -O3 -std=c++20 -shared -fPIC $(python3 -m pybind11 --includes) modulo.cpp -o modulo$(python3-config --extension-suffix)   (requer pybind11; indisponível no ambiente de teste do vault)
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <numeric>
#include <vector>

namespace py = pybind11;

double media(const std::vector<double>& v) {
    return v.empty() ? 0.0 : std::accumulate(v.begin(), v.end(), 0.0) / static_cast<double>(v.size());
}

struct Contador {
    int n = 0;
    void incrementa() { ++n; }
};

PYBIND11_MODULE(modulo, m) {
    m.doc() = "Exemplo pybind11";
    m.def("media", &media, "Média de uma lista", py::arg("valores"));
    py::class_<Contador>(m, "Contador")
        .def(py::init<>())
        .def("incrementa", &Contador::incrementa)
        .def_readonly("n", &Contador::n);
}
```

```python
import modulo
print(modulo.media([1.0, 2.0, 3.0]))     # 2.0
c = modulo.Contador(); c.incrementa(); print(c.n)
```

| Ferramenta | Destino | Observação |
|---|---|---|
| **pybind11**, **nanobind** | Python | nanobind: menor e mais rápido |
| **Cython**, **cffi**, **ctypes** | Python | API C |
| **SWIG** | Várias | Geração automática (verbosa) |
| **cxx**, **bindgen**/**autocxx** | Rust | Segurança e ergonomia |
| **JNI/JNA** | Java | |
| **P/Invoke** | C# | API C |
| **Node-API (napi)** | Node.js | |

> [!danger] Regras de ouro
> 1. **Exceções não cruzam** fronteiras C: capture e converta em código de erro.
> 2. Defina **quem possui** a memória e quem a libera (mesmo *runtime*/alocador).
> 3. Não exponha `std::string`/`std::vector` por uma ABI C++ entre binários diferentes ([[Bibliotecas Estáticas e Dinâmicas]]).
> 4. Cuidado com a **GIL** do Python e com threads que chamam o interpretador.

## Veja também

- [[ABI]]
- [[Linkage]]
- [[WebAssembly com Cpp]]
- [[Bibliotecas Estáticas e Dinâmicas]]
- [[MOC - Áreas de Aplicação - Cpp]]

## Exercício

1. Gere `libacc.so` e chame com `ctypes`.
2. Exponha uma classe C++ com pybind11 e libere a GIL durante uma operação demorada.
