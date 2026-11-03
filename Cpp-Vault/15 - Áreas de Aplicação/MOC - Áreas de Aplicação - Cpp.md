---
titulo: "MOC - Áreas de Aplicação - Cpp"
tags: [cpp, moc, aplicacoes]
aliases: ["MOC Áreas de Aplicação"]
tipo: moc
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Bibliotecas]]", "[[MOC - Concorrência e Corrotinas]]"]
---

# MOC - Áreas de Aplicação - Cpp

Onde o C++ é usado e quais práticas cada área enfatiza.

| Área | Prioridade | Nota |
|---|---|---|
| Embarcados | Recursos mínimos, determinismo | [[Cpp em Sistemas Embarcados]] |
| Jogos | Orçamento de frame, cache | [[Cpp em Jogos]] |
| Finanças/HFT | Latência de cauda | [[Cpp em Finanças e Baixa Latência]] |
| HPC/GPU | Throughput, paralelismo | [[Cpp em HPC e GPU]] |
| Robótica | Tempo real, percepção | [[Cpp em Robótica]] |
| Sistemas/infra | Portabilidade, I/O | [[Cpp em Sistemas Operacionais e Infraestrutura]] |
| Navegadores/BDs | Segurança, escala | [[Cpp em Navegadores e Bancos de Dados]] |
| Web/Portabilidade | Wasm | [[WebAssembly com Cpp]] |
| Integração | Fronteira C/Python | [[Interoperabilidade Cpp com Python e C]] |

```mermaid
quadrantChart
    title Prioridades por área (qualitativo)
    x-axis "Menos recursos" --> "Mais recursos"
    y-axis "Throughput" --> "Latência/determinismo"
    quadrant-1 "Tempo real forte"
    quadrant-2 "Sistemas restritos"
    quadrant-3 "Processamento em lote"
    quadrant-4 "Alta capacidade"
    Embarcados: [0.15, 0.85]
    Robótica: [0.45, 0.8]
    HFT: [0.8, 0.95]
    Jogos: [0.65, 0.6]
    HPC: [0.9, 0.2]
    Bancos de dados: [0.8, 0.4]
```

## Notas

- [[Cpp em Sistemas Embarcados]]
- [[Cpp em Jogos]]
- [[Cpp em Finanças e Baixa Latência]]
- [[Cpp em HPC e GPU]]
- [[Cpp em Robótica]]
- [[Cpp em Sistemas Operacionais e Infraestrutura]]
- [[Cpp em Navegadores e Bancos de Dados]]
- [[WebAssembly com Cpp]]
- [[Interoperabilidade Cpp com Python e C]]

## Veja também

- [[Home - Cpp]]
- [[Casos de Uso do Cpp]]
- [[MOC - Bibliotecas]]
- [[MOC - Avançado e Performance - Cpp]]
