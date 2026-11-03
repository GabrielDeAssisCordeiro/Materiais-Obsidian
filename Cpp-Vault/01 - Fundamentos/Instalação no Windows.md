---
titulo: "Instalação no Windows"
tags: [cpp, fundamentos, instalacao, windows]
aliases: ["Instalar C++ no Windows", "Setup Windows"]
tipo: procedimento
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Instalação no Linux - Cpp]]", "[[Instalação no macOS - Cpp]]", "[[IDEs e Editores]]"]
---

# Instalação no Windows

Há três caminhos principais. Escolha **um** para começar.

| Opção | Compilador | Quando usar |
|---|---|---|
| **Visual Studio** (Community) ou Build Tools | MSVC (e opcionalmente clang-cl) | Desenvolvimento nativo Windows, depuração integrada |
| **MSYS2** | GCC/Clang (MinGW-w64) | Ambiente parecido com Linux, bom para aprender |
| **WSL 2** (Windows Subsystem for Linux) | GCC/Clang do Linux | Fluxo idêntico ao Linux dentro do Windows |

## Opção 1: Visual Studio / Build Tools

1. Baixe o instalador no site da Microsoft (Visual Studio Community é gratuito para uso individual e educacional).
2. Marque a carga de trabalho **"Desenvolvimento para desktop com C++"** (e, opcionalmente, "Ferramentas do CMake para Windows").
3. Abra o **"Developer Command Prompt"** ou **"Developer PowerShell"** (necessário para ter `cl.exe` no PATH).

```bat
cl /std:c++20 /EHsc /W4 ola.cpp
ola.exe
```

> [!question] Verificar na documentação oficial
> O nome da edição e das cargas de trabalho do Visual Studio muda entre versões. Consulte learn.microsoft.com.

## Opção 2: MSYS2 (MinGW-w64)

1. Instale em msys2.org e abra o terminal **UCRT64**.
2. Instale as ferramentas:

```bash
pacman -Syu
pacman -S mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb mingw-w64-ucrt-x86_64-cmake mingw-w64-ucrt-x86_64-ninja
```

3. Compile como no Linux: `g++ -std=c++20 -Wall -Wextra ola.cpp -o ola`.

## Opção 3: WSL 2

```powershell
wsl --install
```

Depois siga [[Instalação no Linux - Cpp]] dentro da distribuição (geralmente Ubuntu). O VS Code integra com WSL pela extensão "WSL".

## Diferenças que importam

| Tema | MSVC | GCC/Clang |
|---|---|---|
| Flags | `/std:c++20`, `/W4`, `/O2`, `/Zi`, `/EHsc` | `-std=c++20`, `-Wall -Wextra`, `-O2`, `-g` |
| Executável | `.exe`, objetos `.obj` | `.exe` (MinGW) ou sem extensão (Linux) |
| `__cplusplus` | Só correto com `/Zc:__cplusplus`; use `_MSVC_LANG` | Correto |

Veja [[Flags Essenciais do Compilador]] para a tabela de equivalência.

## Veja também

- [[Instalação no Linux - Cpp]]
- [[Instalação no macOS - Cpp]]
- [[IDEs e Editores]]
- [[Compiladores GCC Clang e MSVC]]

## Exercício

1. Escolha uma das três opções, instale e compile o [[Primeiro Programa]].
2. Descubra o valor de `_MSVC_LANG` ao compilar com `/std:c++20`.
