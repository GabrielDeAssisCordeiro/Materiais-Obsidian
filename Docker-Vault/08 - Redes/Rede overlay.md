---
tags:
  - docker
  - redes
  - swarm
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Swarm]]"
  - "[[Visão geral das redes Docker]]"
  - "[[iptables e firewall com Docker]]"
---

# Rede overlay

A rede **overlay** conecta containers em **vários hosts Docker** usando túneis VXLAN. É o padrão do **modo Swarm** para comunicação entre serviços.

```bash
# Requer um Swarm inicializado
docker swarm init

# Rede overlay; --attachable permite conectar containers avulsos (docker run)
docker network create --driver overlay --attachable rede-cluster

# Rede com tráfego de dados criptografado
docker network create --driver overlay --opt encrypted rede-segura
```

## Portas necessárias entre os nós

| Porta | Protocolo | Função |
|---|---|---|
| 2377 | TCP | Gerenciamento do cluster (managers) |
| 7946 | TCP e UDP | Comunicação entre nós (*gossip*) |
| 4789 | UDP | Tráfego VXLAN da overlay |

> [!warning] Libere as portas apenas entre os nós
> Essas portas não devem ficar expostas à Internet. Restrinja por firewall/security groups.

> [!info] Descoberta de serviços
> Em overlay, o DNS interno resolve nomes de **serviços** para um IP virtual (VIP) com balanceamento entre as tarefas, ou para todos os IPs (modo `dnsrr`).

> [!tip] Criptografia tem custo
> `--opt encrypted` usa IPsec e reduz o desempenho; habilite quando o tráfego atravessar redes não confiáveis.

## Exercício

Inicialize um Swarm de um único nó, crie uma rede overlay `--attachable` e conecte dois containers `alpine` a ela, testando `ping` por nome.

## Veja também

- [[Visão geral do Swarm]]
- [[Visão geral das redes Docker]]
- [[iptables e firewall com Docker]]
- [[MOC - Redes]]
