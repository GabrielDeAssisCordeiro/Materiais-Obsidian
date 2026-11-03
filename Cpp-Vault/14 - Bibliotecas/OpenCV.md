---
titulo: "OpenCV"
tags: [cpp, bibliotecas, imagens]
aliases: ["OpenCV", "cv::Mat", "Visão computacional", "Processamento de imagens", "Halide", "dlib"]
tipo: biblioteca
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Visão Geral das Bibliotecas]]", "[[Cpp em Robótica]]", "[[Eigen e Álgebra Linear]]"]
---

# OpenCV

Biblioteca de **visão computacional** e processamento de imagens/vídeo (licença **Apache 2.0** nas versões 4.5+). Cobre filtros, detecção de bordas/objetos, calibração de câmera, rastreamento, aprendizado de máquina clássico e inferência de redes (módulo `dnn`).

| Módulo | Função |
|---|---|
| `core` | `cv::Mat` (matriz/imagem), operações básicas |
| `imgproc` | Filtros, transformações, histogramas, contornos |
| `imgcodecs` / `videoio` | Ler/gravar imagens e vídeo/câmeras |
| `highgui` | Janelas simples |
| `features2d`, `calib3d` | Pontos de interesse, calibração, estéreo |
| `dnn` | Inferência de redes neurais (ONNX, TensorFlow…) |
| `objdetect` | Haar/HOG, QR code |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra $(pkg-config --cflags --libs opencv4)   (requer OpenCV 4; indisponível no ambiente de teste do vault)
#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv) {
    if (argc < 2) { std::cerr << "uso: " << argv[0] << " imagem\n"; return 1; }

    cv::Mat img = cv::imread(argv[1], cv::IMREAD_COLOR);          // BGR (não RGB!)
    if (img.empty()) { std::cerr << "falha ao ler a imagem\n"; return 1; }

    cv::Mat cinza, borrada, bordas;
    cv::cvtColor(img, cinza, cv::COLOR_BGR2GRAY);
    cv::GaussianBlur(cinza, borrada, cv::Size(5, 5), 1.5);
    cv::Canny(borrada, bordas, 50, 150);                            // detecção de bordas

    cv::imwrite("bordas.png", bordas);
    std::cout << img.cols << 'x' << img.rows << " canais=" << img.channels() << '\n';
}
```

```cmake
find_package(OpenCV REQUIRED COMPONENTS core imgproc imgcodecs)
target_link_libraries(app PRIVATE ${OpenCV_LIBS})
```

> [!warning] Pegadinhas
> - `cv::Mat` tem **semântica de referência** (contagem de referências): `b = a` **não copia** os pixels; use `a.clone()`.
> - Canais em ordem **BGR**.
> - Acesso por `at<T>(y, x)` com tipo errado causa UB; prefira ponteiros por linha ou iteradores em laços críticos.
> - Muitas funções têm versões **CUDA/OpenCL** (`cv::UMat`) — veja [[Cpp em HPC e GPU]].

## Veja também

- [[Visão Geral das Bibliotecas]]
- [[Cpp em Robótica]]
- [[Cpp em HPC e GPU]]
- [[Eigen e Álgebra Linear]]

## Exercício

1. Escreva um programa que detecta bordas em uma imagem e salva o resultado.
2. Demonstre a semântica de referência de `cv::Mat` com `clone()`.
