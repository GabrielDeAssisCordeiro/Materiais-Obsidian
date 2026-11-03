---
titulo: "Ninja e Make"
tags: [cpp, build]
aliases: ["Make", "Makefile", "Ninja", "build.ninja", "make -j", "Sistemas de build"]
tipo: ferramenta
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[CMake Moderno e Presets]]", "[[Pipeline de Compilação - Cpp]]", "[[Headers vs Sources]]"]
---

# Ninja e Make

Um **sistema de build** recompila apenas o que mudou, usando um grafo de dependências (arquivos fonte → objetos → executável) e *timestamps*.

| | **Make** | **Ninja** |
|---|---|---|
| Escrito à mão? | Sim (Makefile) | **Geralmente gerado** (por CMake/Meson) |
| Foco | Flexibilidade/general-purpose | **Velocidade** de build incremental |
| Paralelismo | `make -j N` | Paralelo por padrão (usa nº de CPUs) |
| Sintaxe | Rica (variáveis, funções) | Mínima, propositalmente |

## Makefile mínimo

```makefile
# Makefile (use TAB, não espaços, nas linhas de receita)
CXX      := g++
CXXFLAGS := -std=c++20 -Wall -Wextra -O2 -MMD -MP    # -MMD gera .d com dependências de headers
SRC      := $(wildcard src/*.cpp)
OBJ      := $(SRC:src/%.cpp=build/%.o)

app: $(OBJ)
	$(CXX) $^ -o $@

build/%.o: src/%.cpp | build
	$(CXX) $(CXXFLAGS) -c $< -o $@

build:
	mkdir -p build

-include $(OBJ:.o=.d)

clean:
	rm -rf build app
.PHONY: clean
```

| Variável automática | Significado |
|---|---|
| `$@` | Alvo |
| `$<` | Primeira dependência |
| `$^` | Todas as dependências |

```bash
make -j$(nproc)          # compilar em paralelo
make clean
```

## Ninja

Normalmente você **não escreve** `build.ninja`; deixa o CMake gerar:

```bash
cmake -S . -B build -G Ninja
cmake --build build        # chama o ninja
ninja -C build -v          # comandos completos
ninja -C build -t graph | dot -Tsvg > grafo.svg   # visualizar o grafo (Graphviz)
```

> [!tip] Qual usar?
> Para projetos novos com CMake, **Ninja** é a escolha padrão (mais rápido, saída limpa). Makefiles escritos à mão ainda servem para projetos pequenos e *scripts*.

> [!warning] Armadilhas de Make
> - Tabulação obrigatória nas receitas.
> - Esquecer `-MMD`: alterar um header não recompila os `.cpp` que o incluem ([[Headers vs Sources]]).
> - `make -j` com receitas que compartilham arquivos intermediários gera condições de corrida.

## Veja também

- [[CMake Moderno e Presets]]
- [[Meson e Bazel]]
- [[ccache]]
- [[Pipeline de Compilação - Cpp]]

## Exercício

1. Escreva um Makefile para um projeto com três `.cpp` e verifique se alterar um header recompila os arquivos corretos.
2. Gere o grafo do Ninja de um projeto CMake e identifique o caminho crítico.
