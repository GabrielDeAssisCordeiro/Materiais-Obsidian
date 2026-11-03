---
titulo: "Tipos de Sistemas Operacionais"
tags:
  - sistemas-operacionais
  - conceito
  - fundamentos
tipo: conceito
nivel: iniciante
relacionados:
  - "[[SO em Lote (Batch)]]"
  - "[[SO de Tempo Compartilhado]]"
  - "[[SO de Tempo Real (RTOS)]]"
  - "[[SO Distribuído]]"
  - "[[SO Embarcado]]"
  - "[[SO Mobile]]"
---

# Tipos de Sistemas Operacionais

## Resumo

SOs são classificados pelo **objetivo principal**: maximizar vazão, responder ao usuário, cumprir prazos, coordenar várias máquinas, caber em hardware mínimo ou rodar em dispositivos móveis.

## Quadro comparativo

| Tipo | Objetivo principal | Interação | Exemplos |
|---|---|---|---|
| [[SO em Lote (Batch)]] | Vazão (jobs por hora) | Nenhuma durante a execução | IBM OS/360 (lote), jobs de mainframe |
| [[SO de Tempo Compartilhado]] | Tempo de resposta | Interativa, vários usuários | UNIX, Linux, Windows, macOS |
| [[SO de Tempo Real (RTOS)]] | Previsibilidade de prazos | Reação a eventos externos | FreeRTOS, VxWorks, QNX, RTLinux |
| [[SO Distribuído]] | Transparência entre máquinas | Cluster visto como um sistema | Plan 9, Amoeba, clusters modernos |
| [[SO Embarcado]] | Pouco recurso, confiabilidade | Dedicada ao dispositivo | Zephyr, FreeRTOS, Linux embarcado |
| [[SO Mobile]] | Energia, toque, sandbox | Toque e sensores | Android, iOS |

## Eixos para classificar

- **Número de usuários**: monousuário x multiusuário.
- **Número de tarefas**: monotarefa x multitarefa.
- **Prazo**: tempo real *hard* (prazo perdido é falha) x *soft* (degrada qualidade).
- **Escopo**: máquina única x distribuído.
- **Recursos**: servidor/desktop x embarcado.

```mermaid
flowchart LR
    A[Quer cumprir prazos garantidos?] -->|Sim| RT[Tempo real]
    A -->|Não| B[Vários usuários interativos?]
    B -->|Sim| TS[Tempo compartilhado]
    B -->|Não| C[Processa filas de jobs?]
    C -->|Sim| BA[Batch]
    C -->|Não| D[Hardware mínimo?]
    D -->|Sim| EM[Embarcado]
    D -->|Não| E[Dispositivo móvel?]
    E -->|Sim| MO[Mobile]
    E -->|Não| DI[Distribuído ou uso geral]
```

> [!warning] Categorias se sobrepõem
> Um Android é mobile, tempo compartilhado e, em dispositivos específicos, embarcado. O QNX é tempo real e embarcado. Classifique pela **característica dominante** em cada contexto.

## Exemplo prático

```bash
# Linux de uso geral pode ganhar comportamento de tempo real com PREEMPT_RT
uname -v | grep -i preempt
# Ver a política de escalonamento de um processo
chrt -p $$
```

## Pontos-chave

- Não existe "melhor tipo": cada um otimiza uma métrica diferente.
- Sistemas modernos de uso geral misturam características de vários tipos.
- A escolha do tipo influencia o [[Escalonamento de Processos]].

## Veja também

[[O que é um Sistema Operacional]] · [[História e Evolução dos Sistemas Operacionais]] · [[MOC - Fundamentos - SO]]
