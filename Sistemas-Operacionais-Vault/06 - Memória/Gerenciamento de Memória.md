---
titulo: "Gerenciamento de Memória"
tags:
  - sistemas-operacionais
  - conceito
  - memoria
tipo: conceito
nivel: iniciante
relacionados:
  - "[[Paginação]]"
  - "[[Segmentação]]"
  - "[[Memória Virtual]]"
  - "[[Alocadores de Memória]]"
---

# Gerenciamento de Memória

## Resumo

O gerenciador de memória do SO tem quatro tarefas: **alocar** memória a processos, **proteger** cada um dos demais, **realocar** (programas não sabem onde serão carregados) e **organizar** a hierarquia (registradores, caches, RAM, disco).

## Hierarquia de memória

| Nível | Capacidade típica | Latência aproximada |
|---|---|---|
| Registradores | ~1 KB | < 1 ns |
| Cache L1 / L2 / L3 | 32 KB a dezenas de MB | 1 a 40 ns |
| RAM | GBs | ~80 ns |
| SSD NVMe | TBs | ~20-100 µs |
| HDD | TBs | ~5-10 ms |

## Evolução das técnicas

```mermaid
flowchart LR
    A[Sem abstração: endereços físicos] --> B[Partições fixas]
    B --> C[Partições variáveis]
    C --> D[Swapping de processos inteiros]
    D --> E[Segmentação]
    D --> F[Paginação]
    E --> G[Memória virtual: paginação sob demanda]
    F --> G
```

## Alocação contígua e fragmentação

| Estratégia | Descrição |
|---|---|
| **First fit** | Primeiro buraco que serve; rápido |
| **Best fit** | Menor buraco suficiente; deixa pedaços minúsculos |
| **Worst fit** | Maior buraco; costuma ser pior |

- **Fragmentação externa**: espaço livre total existe, mas dividido em buracos pequenos. A **compactação** resolve, com custo alto.
- **Fragmentação interna**: espaço desperdiçado dentro de um bloco alocado (ex.: página parcialmente usada).

> [!info] Regra dos 50%
> Com first fit, para N blocos alocados, cerca de N/2 buracos aparecem: cerca de **1/3 da memória** pode ficar inutilizável por fragmentação externa. A paginação elimina esse problema.

## Proteção e realocação: registradores base e limite

Hardware simples: cada acesso é verificado contra `[base, base + limite)` e somado à base. Foi substituído pela MMU com tabelas de páginas.

```c
// Simulação de tradução base/limite
long traduz(long virt, long base, long limite) {
    if (virt < 0 || virt >= limite) return -1;   // violação de proteção
    return base + virt;
}
```

## MMU e endereços

A **MMU** (*Memory Management Unit*) traduz **endereço virtual** (usado pela CPU) em **endereço físico** a cada acesso, aplicando proteção (leitura/escrita/execução, usuário/supervisor). Ver [[Paginação]] e [[TLB - Translation Lookaside Buffer]].

## Exemplo prático

```bash
# Linux: resumo de memória
free -h
cat /proc/meminfo | head -10
# Mapeamento de um processo (endereços virtuais)
pmap -x $$ | head
# Fragmentação do alocador buddy do kernel
cat /proc/buddyinfo
```

```powershell
Get-CimInstance Win32_OperatingSystem | Select TotalVisibleMemorySize, FreePhysicalMemory
Get-Process | Sort WorkingSet -Descending | Select -First 5 Name, WorkingSet
```

## Pontos-chave

- Hierarquia: quanto mais perto da CPU, mais rápido e menor.
- Fragmentação externa e interna motivam a paginação.
- A MMU faz tradução e proteção por hardware.

## Veja também

[[Segmentação]] · [[Paginação]] · [[Memória Virtual]] · [[MOC - Gerenciamento de Memória]]
