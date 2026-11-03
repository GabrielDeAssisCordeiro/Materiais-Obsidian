---
titulo: "MOC - Arquitetura de Kernels"
tags:
  - sistemas-operacionais
  - moc
  - arquitetura
tipo: moc
nivel: intermediario
relacionados:
  - "[[Kernel Monolítico]]"
  - "[[Microkernel]]"
  - "[[Kernel Híbrido]]"
  - "[[Comparação de Arquiteturas com Exemplos Reais]]"
---

# MOC - Arquitetura de Kernels

> [!info] Pergunta central
> Quanto código deve rodar em modo kernel? A resposta define desempenho, segurança, estabilidade e facilidade de manutenção.

## Modelos de arquitetura

| Nota | Ideia em uma linha |
|---|---|
| [[Kernel Monolítico]] | Todos os serviços do SO em um único binário no modo kernel |
| [[Microkernel]] | Kernel mínimo; serviços em processos de user space |
| [[Kernel Híbrido]] | Estrutura de microkernel com muitos serviços dentro do kernel |
| [[Exokernel]] | Kernel apenas multiplexa recursos; bibliotecas definem abstrações |
| [[Unikernel]] | Aplicação + SO compilados em uma única imagem especializada |
| [[Arquitetura em Camadas]] | Níveis hierárquicos, cada um usando só o nível inferior |

## Comparação

- [[Comparação de Arquiteturas com Exemplos Reais]]: tabela e análise com Linux, Windows NT, macOS/XNU, FreeBSD, Minix, QNX, Android e iOS.

## Pré-requisitos

- [[Kernel vs User Space]]
- [[Modos de Operação da CPU]]
- [[System Calls]]

## Voltar

[[MOC - Fundamentos - SO]]
