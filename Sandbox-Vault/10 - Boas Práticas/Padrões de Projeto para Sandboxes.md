---
tags:
  - boas-praticas
  - arquitetura
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Defesa em Profundidade]]"
  - "[[Arquiteturas de Sandbox para Agentes]]"
---
# Padrões de Projeto para Sandboxes

| Padrão | Ideia |
|---|---|
| **Sandbox por execução** | Ambiente novo a cada tarefa; nada persiste |
| **Broker / proxy de privilégios** | A sandbox pede ações a um serviço confiável e estreito, em vez de ter o privilégio |
| **Passagem de capacidades** | Entregar à sandbox apenas "alças" (diretório, socket) específicas |
| **Pool aquecido** | Sandboxes pré-criadas para baixa latência |
| **Jailer** | O próprio gerenciador da sandbox é confinado (ex.: jailer do Firecracker) |
| **Rede de saída mediada** | Proxy com allowlist, DNS interno |
| **Camadas aninhadas** | VM → container → processo com seccomp |
| **Separação de privilégios** | Componente que lê entrada não confiável ≠ componente com privilégios |

## Veja também

- [[Arquiteturas de Sandbox para Agentes]]
- [[Defesa em Profundidade]]
- [[Como Escolher o Nível de Isolamento]]
- [[MOC - Boas Práticas]]
