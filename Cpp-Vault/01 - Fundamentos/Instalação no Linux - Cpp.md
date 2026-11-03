---
titulo: "Instalação no Linux - Cpp"
tags: [cpp, fundamentos, instalacao, linux]
aliases: ["Instalar C++ no Linux", "Setup Linux"]
tipo: procedimento
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Instalação no Windows]]", "[[Instalação no macOS - Cpp]]", "[[IDEs e Editores]]"]
---

# Instalação no Linux - Cpp

Em Linux, o conjunto mínimo é: **compilador**, **depurador** (GDB), **CMake** e **Ninja**.

## Debian / Ubuntu

```bash
sudo apt update
sudo apt install build-essential gdb cmake ninja-build clang clang-format clang-tidy valgrind
```

`build-essential` instala `g++`, `make` e cabeçalhos básicos.

## Fedora / RHEL

```bash
sudo dnf install gcc-c++ gdb cmake ninja-build clang clang-tools-extra valgrind
```

## Arch Linux

```bash
sudo pacman -S base-devel gdb cmake ninja clang valgrind
```

## Verificando a instalação

```bash
g++ --version
clang++ --version
cmake --version
gdb --version
```

## Compilador mais novo que o da distribuição

Distribuições estáveis trazem versões antigas. Opções:

- Pacotes alternativos (por exemplo, PPAs ou repositórios `gcc-NN`/`g++-NN` e `clang-NN`).
- Contêineres Docker com a imagem oficial `gcc:<versão>`.
- Compilar o GCC a partir do código-fonte (demorado).

> [!tip] Várias versões lado a lado
> Em Debian/Ubuntu é comum instalar `g++-14` e chamar `g++-14` explicitamente, ou usar `update-alternatives` para escolher a versão padrão.

> [!question] Verificar na documentação oficial
> Nomes de pacotes variam entre releases das distribuições. Consulte a documentação da sua distro se um pacote não for encontrado.

## Teste rápido

```bash
cat > ola.cpp <<'EOF'
#include <iostream>
int main() { std::cout << "Olá, C++!\n"; }
EOF
g++ -std=c++20 -Wall -Wextra ola.cpp -o ola && ./ola
```

## Veja também

- [[Instalação no Windows]]
- [[Instalação no macOS - Cpp]]
- [[IDEs e Editores]]
- [[Compiladores GCC Clang e MSVC]]
- [[Primeiro Programa]]

## Exercício

1. Instale o ambiente e compile o teste rápido. Rode `g++ -v` e anote a versão e a *target*.
2. Descubra o padrão C++ default do seu `g++` (`g++ -dM -E -x c++ /dev/null | grep __cplusplus`).
