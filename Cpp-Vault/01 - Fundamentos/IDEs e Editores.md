---
titulo: "IDEs e editores"
tags: [cpp, fundamentos]
aliases: ["IDEs para C++", "Editores para C++", "VS Code C++", "CLion"]
tipo: ferramenta
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Instalação no Linux - Cpp]]", "[[Compiladores GCC Clang e MSVC]]", "[[Flags Essenciais do Compilador]]"]
---

# IDEs e editores

| Ferramenta | Tipo | Pontos fortes | Observações |
|---|---|---|---|
| **Visual Studio Code** | Editor extensível | Leve, multiplataforma, ótimo com CMake | Extensões: clangd, CMake Tools, CodeLLDB/C++ debug |
| **CLion** (JetBrains) | IDE | Refatoração forte, CMake nativo, depurador integrado | Pago (há licenças gratuitas para uso não comercial/educacional; verifique a política atual) |
| **Visual Studio** | IDE | Melhor depurador no Windows, MSVC integrado | Windows |
| **Qt Creator** | IDE | Excelente para projetos Qt, bom em CMake | Multiplataforma |
| **Xcode** | IDE | Ecossistema Apple | macOS |
| **Vim/Neovim, Emacs** | Editores | Altamente configuráveis | Use com clangd via LSP |

## O que importa: servidor de linguagem

Quase todo editor moderno usa **LSP** (*Language Server Protocol*). Para C++, o servidor mais popular é o **clangd**, que depende de um arquivo `compile_commands.json` gerado pelo build.

```bash
# Com CMake: exporta os comandos de compilação para o clangd
cmake -S . -B build -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
ln -sf build/compile_commands.json .   # clangd procura na raiz do projeto
```

```cmake
# CMakeLists.txt — alternativa dentro do projeto
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

## Configuração mínima recomendada (VS Code)

1. Instale as extensões **clangd** e **CMake Tools** (desative o IntelliSense da extensão C/C++ da Microsoft se usar clangd, para evitar conflito).
2. Ative formatação com `clang-format` (arquivo `.clang-format` na raiz).
3. Configure depuração com **CodeLLDB** ou o depurador C++ da extensão oficial.

> [!tip] Uma IDE não substitui entender o build
> Aprenda a compilar pela linha de comando ([[Flags Essenciais do Compilador]] e [[Pipeline de Compilação - Cpp]]). Quando a IDE falha, é o que resolve.

## Veja também

- [[Instalação no Linux - Cpp]]
- [[Instalação no Windows]]
- [[Instalação no macOS - Cpp]]
- [[Primeiro Programa]]

## Exercício

1. Configure o clangd no seu editor e verifique se o autocompletar de `std::vector` funciona.
2. Gere um `compile_commands.json` e abra-o. O que ele registra para cada arquivo?
