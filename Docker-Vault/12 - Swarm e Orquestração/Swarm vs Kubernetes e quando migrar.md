---
tags:
  - docker
  - swarm
  - kubernetes
  - comparativo
  - orquestracao
aliases: []
tipo: comparativo
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Compose vs Swarm vs Kubernetes]]"
  - "[[Kompose e Kubernetes no Docker Desktop]]"
  - "[[Visão geral do Swarm]]"
---

# Swarm vs Kubernetes e quando migrar

| Critério | Docker Swarm | Kubernetes |
|---|---|---|
| Curva de aprendizado | **Baixa** (reaproveita Docker/Compose) | Alta |
| Instalação | `docker swarm init` | Distribuições, kubeadm ou serviços gerenciados |
| Modelo | Services/stacks | Pods, Deployments, Services, Ingress, etc. |
| Ecossistema | Menor | **Enorme** (operators, Helm, service mesh, observabilidade) |
| Escalabilidade e recursos avançados | Moderada | Muito alta (HPA, VPA, afinidades, CRDs) |
| Serviços gerenciados na nuvem | Praticamente inexistentes | EKS, GKE, AKS e outros |
| Armazenamento persistente | Básico | CSI, StorageClasses, StatefulSets |
| Mercado de trabalho | Reduzido | **Padrão da indústria** |

## Quando migrar para Kubernetes

- Necessidade de **autoscaling** horizontal/vertical.
- Ecossistema de ferramentas (Helm, operadores, GitOps com Argo CD/Flux).
- Cargas com estado complexas, multi-tenant e políticas de rede avançadas.
- Preferência por **serviços gerenciados** da nuvem.
- Equipe dedicada e demanda de **crescimento significativo**.

## Quando o Swarm (ou apenas Compose) ainda basta

- Poucos serviços, poucos nós, equipe pequena.
- Simplicidade operacional é mais importante que recursos avançados.
- A aplicação cabe em **um único host** (Compose já resolve).

> [!tip] Caminho de adoção gradual
> Compose em um host → Swarm para alta disponibilidade simples → Kubernetes (preferencialmente gerenciado) quando a complexidade e a escala justificarem.

> [!question] Verificar na documentação oficial
> Verifique o status atual do Swarm no seu ambiente (suporte, versões) antes de decidir; a recomendação mais comum para novos projetos de grande escala é Kubernetes.

## Exercício

Para um projeto seu real ou imaginado, preencha a tabela acima com as necessidades dele e conclua qual opção escolheria e por quê.

## Veja também

- [[Compose vs Swarm vs Kubernetes]]
- [[Kompose e Kubernetes no Docker Desktop]]
- [[Visão geral do Swarm]]
- [[MOC - Swarm e Orquestração]]
