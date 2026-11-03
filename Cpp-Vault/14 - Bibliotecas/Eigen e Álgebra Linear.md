---
titulo: "Eigen e álgebra linear"
tags: [cpp, bibliotecas, simd]
aliases: ["Eigen", "Álgebra linear", "Armadillo", "xtensor", "BLAS", "LAPACK", "std::linalg", "mdspan"]
tipo: biblioteca
nivel: intermediario
padrao: C++14
criado: 2026-10-24
relacionados: ["[[Visão Geral das Bibliotecas]]", "[[SIMD e Vetorização - Cpp]]", "[[Cpp em HPC e GPU]]"]
---

# Eigen e álgebra linear

**Eigen** é uma biblioteca *header-only* de álgebra linear em templates: matrizes, vetores, decomposições (LU, QR, SVD, Cholesky), solvers e geometria. Usa *expression templates* (cálculo preguiçoso, fusão de laços) e **SIMD** automático ([[SIMD e Vetorização - Cpp]]).

```cpp
// [nv] g++ -std=c++20 -O2 -march=native -I/usr/include/eigen3   (requer Eigen 3; indisponível no ambiente de teste do vault)
#include <Eigen/Dense>
#include <iostream>

int main() {
    Eigen::Matrix3d A;
    A << 2, 0, 0,
         0, 3, 0,
         0, 0, 4;
    Eigen::Vector3d b{1, 2, 3};

    Eigen::Vector3d x = A.colPivHouseholderQr().solve(b);          // resolve A x = b
    std::cout << x.transpose() << '\n';                            // 0.5 0.666667 0.75

    Eigen::MatrixXd M = Eigen::MatrixXd::Random(4, 4);             // tamanho dinâmico
    std::cout << (M * M.transpose()).trace() << '\n';

    Eigen::VectorXd v = Eigen::VectorXd::LinSpaced(5, 0.0, 1.0);
    std::cout << v.norm() << ' ' << v.sum() << '\n';
}
```

```cmake
find_package(Eigen3 3.4 REQUIRED NO_MODULE)
target_link_libraries(app PRIVATE Eigen3::Eigen)
```

> [!warning] Armadilha `auto` com expression templates
> `auto C = A * B;` guarda uma **expressão**, não o resultado; usá-la depois pode referenciar temporários destruídos (UB). Use `Eigen::MatrixXd C = A * B;` ou `.eval()`.

| Opção | Característica |
|---|---|
| **Eigen** | Rica, header-only, ótima para dimensões pequenas e médias |
| **Armadillo** | Sintaxe estilo MATLAB; usa BLAS/LAPACK |
| **xtensor** | Arrays N-dimensionais estilo NumPy |
| **BLAS/LAPACK** (OpenBLAS, MKL) | Padrão da indústria para matrizes grandes |
| **`std::mdspan`** (C++23) | Visão multidimensional não proprietária |
| **`std::linalg`** (C++26) | Interface padrão sobre BLAS |

> [!tip] Desempenho
> Compile com `-O2/-O3` e `-march=native` (ou `-mavx2`); sem otimização, Eigen é **muito** lento. Armazenamento *column-major* por padrão: percorra por colunas.

## Veja também

- [[Visão Geral das Bibliotecas]]
- [[SIMD e Vetorização - Cpp]]
- [[span]]
- [[Cpp em HPC e GPU]]

## Exercício

1. Resolva um sistema linear 1000×1000 com Eigen e meça o tempo com `-O0` e `-O3`.
2. Mostre o bug do `auto` com uma expressão e corrija.
