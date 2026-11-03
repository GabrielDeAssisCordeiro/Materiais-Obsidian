---
tags:
  - docker
  - fundamentos
  - introducao
aliases:
  - Introdução ao Docker
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O problema que o Docker resolve]]"
  - "[[Containers vs Máquinas Virtuais]]"
  - "[[Arquitetura do Docker]]"
  - "[[Ecossistema Docker]]"
---

# O que é Docker

**Docker** é uma plataforma aberta para **construir, distribuir e executar aplicações em containers**. Um container empacota o código da aplicação junto com suas dependências (bibliotecas, runtime, configurações) em uma unidade isolada, leve e portátil que roda da mesma forma em qualquer host com um runtime compatível.

## A ideia central

- Você descreve o ambiente em um arquivo (o **Dockerfile**).
- O Docker constrói uma **imagem** imutável a partir dele.
- A imagem é executada como um ou mais **containers**: processos isolados do restante do sistema por recursos do kernel Linux.

> [!info] Docker não é uma máquina virtual
> Containers compartilham o **kernel do host**. Não há um sistema operacional completo por container, e por isso eles iniciam em milissegundos e ocupam pouca memória. Veja [[Containers vs Máquinas Virtuais]].

## Primeiro contato

```bash
# Baixa (se necessário) e executa um container de teste
docker run --rm hello-world

# Executa um servidor web Nginx em segundo plano, publicando a porta 8080
docker run -d --name web -p 8080:80 nginx:1.27

# Acessa o servidor (em outro terminal)
curl -I http://localhost:8080

# Remove o container (-f força a parada)
docker rm -f web
```

## Por que usar Docker?

| Benefício | Explicação |
|---|---|
| Portabilidade | "Funciona na minha máquina" passa a funcionar em qualquer lugar. |
| Isolamento | Cada aplicação tem seu próprio sistema de arquivos, rede e processos. |
| Reprodutibilidade | O ambiente é código versionável (Dockerfile + Compose). |
| Eficiência | Menos overhead que VMs; muitos containers por host. |
| Entrega contínua | Imagens versionadas tornam o deploy e o rollback previsíveis. |

> [!tip] Termos que você verá o tempo todo
> **Imagem** (modelo somente leitura), **container** (instância em execução), **registry** (repositório de imagens), **volume** (dados persistentes) e **rede** (comunicação entre containers). Todos têm notas próprias neste vault.

## Exercício

1. Execute `docker run --rm hello-world` e leia cada etapa da mensagem de saída.
2. Explique, com suas palavras, por que um container não é uma VM.

## Veja também

- [[O problema que o Docker resolve]]
- [[Containers vs Máquinas Virtuais]]
- [[Arquitetura do Docker]]
- [[Ecossistema Docker]]
- [[MOC - Fundamentos - Docker]]
