---
tags:
  - docker
  - swarm
  - kubernetes
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Swarm vs Kubernetes e quando migrar]]"
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Visão geral do Docker Compose]]"
---

# Kompose e Kubernetes no Docker Desktop

## Kubernetes no Docker Desktop

O Docker Desktop inclui um cluster Kubernetes de **um nó**, ótimo para estudo e testes locais.

1. Abra **Settings → Kubernetes** e marque **Enable Kubernetes**.
2. Aguarde o status "Kubernetes running".

```bash
kubectl config get-contexts
kubectl config use-context docker-desktop
kubectl get nodes
kubectl create deployment web --image=nginx:1.27 --replicas=2
kubectl expose deployment web --port=80 --type=NodePort
kubectl get pods,svc
kubectl delete deployment web && kubectl delete svc web
```

## Kompose: converter Compose em manifestos Kubernetes

O **Kompose** gera arquivos YAML do Kubernetes a partir de um `compose.yaml`.

```bash
# Instale o kompose (consulte a documentação para seu sistema)
kompose convert -f compose.yaml -o k8s/
kubectl apply -f k8s/
```

```yaml
# compose.yaml de exemplo
services:
  web:
    image: nginx:1.27
    ports:
      - "8080:80"
```

> [!warning] Conversão automática é um ponto de partida
> Recursos como `depends_on`, volumes, redes e healthchecks não têm equivalência direta. Revise e ajuste os manifestos gerados (Deployments, Services, PVCs, Ingress).

> [!question] Verificar na documentação oficial
> O comportamento e as opções do Kubernetes no Docker Desktop (por exemplo, modos *kind* e *kubeadm* em versões recentes) e a instalação do Kompose variam por versão. Consulte a documentação de cada ferramenta.

> [!tip] Alternativas locais
> `kind`, `minikube` e `k3d` criam clusters Kubernetes locais mais próximos de multi-nó.

## Exercício

Habilite o Kubernetes no Docker Desktop, implante um `nginx` com 2 réplicas, exponha e acesse. Em seguida converta um `compose.yaml` seu com o Kompose e compare.

## Veja também

- [[Swarm vs Kubernetes e quando migrar]]
- [[Docker Desktop vs Docker Engine]]
- [[Visão geral do Docker Compose]]
- [[MOC - Swarm e Orquestração]]
