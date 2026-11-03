---
titulo: "Casos de uso do C++"
tags: [cpp, fundamentos, aplicacoes]
aliases: ["Onde C++ é usado", "Aplicações do C++"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[O que é Cpp]]", "[[Filosofia do Cpp]]", "[[Cpp vs Rust, Java, Go e Python]]"]
---

# Casos de uso do C++

C++ é escolhido quando **desempenho previsível**, **controle de recursos** ou **interoperabilidade com código existente** são prioridades.

| Área | Exemplos de uso | Por que C++? |
|---|---|---|
| Sistemas e infraestrutura | Sistemas operacionais (partes), drivers, bancos de dados, máquinas virtuais, compiladores | Controle de memória e hardware |
| Jogos | Motores gráficos (Unreal Engine e outros), simulação de física, ferramentas | Latência baixa, uso de GPU, bibliotecas legadas |
| Embarcados e IoT | Firmware, automotivo, aeroespacial | Footprint pequeno, sem runtime pesado |
| Finanças | Negociação de alta frequência (HFT), motores de risco | Latência em microssegundos |
| Computação científica e HPC | Simulações, álgebra linear, física, CFD | Desempenho, vetorização, paralelismo |
| Navegadores | Motores de renderização e JavaScript | Desempenho e código legado enorme |
| Aplicações desktop | Suítes de escritório, CAD, editores de mídia, Qt | Desempenho e bibliotecas nativas |
| Robótica e visão computacional | ROS, OpenCV | Tempo real e integração com hardware |
| Machine learning (infraestrutura) | Núcleos de bibliotecas expostos em Python | Kernels rápidos com *bindings* |

> [!info] Linguagem de "cola"
> Muito software de alto nível (Python, Java, JavaScript) tem núcleo em C++: o código crítico fica em C++ e é exposto por *bindings* (por exemplo, pybind11).

## Quando **não** usar C++

- Scripts rápidos e automações simples (Python/Shell são mais produtivos).
- Aplicações web CRUD típicas, onde a produtividade e o ecossistema pesam mais.
- Equipes sem experiência em gerenciamento de memória e sem tempo para ferramentas de análise ([[Cpp vs Rust, Java, Go e Python]]).

> [!tip] Como escolher
> Pergunte: *o desempenho ou o controle fino realmente são requisitos?* Se a resposta for não, outra linguagem pode entregar mais rápido. Se for sim, C++ tem ecossistema, ferramentas e décadas de otimização de compiladores.

## Veja também

- [[O que é Cpp]]
- [[Filosofia do Cpp]]
- [[Cpp vs C]]
- [[Cpp vs Rust, Java, Go e Python]]

## Exercício

1. Pesquise três produtos que você usa e descubra se têm código em C++.
2. Para um sistema que processa 1 milhão de ordens por segundo com latência de microssegundos, liste dois motivos para considerar C++.
