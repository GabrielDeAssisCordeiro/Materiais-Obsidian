---
tags:
  - docker
  - fundamentos
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O que é Docker]]"
  - "[[Containers vs Máquinas Virtuais]]"
  - "[[Imagens vs Containers]]"
---

# O problema que o Docker resolve

Antes dos containers, entregar software era frágil. Os problemas clássicos:

1. **"Na minha máquina funciona"**: versões diferentes de linguagem, bibliotecas e sistema operacional entre desenvolvimento, teste e produção.
2. **Inferno de dependências**: duas aplicações no mesmo servidor exigindo versões conflitantes da mesma biblioteca (por exemplo, Python 3.8 e 3.12, ou OpenSSL diferentes).
3. **Onboarding lento**: novos desenvolvedores gastavam dias instalando banco de dados, filas e ferramentas.
4. **Servidores "flocos de neve"**: configurados manualmente, impossíveis de reproduzir com exatidão.
5. **Desperdício de recursos**: uma VM inteira para cada aplicação pequena.

## Como o Docker responde a cada problema

| Problema | Solução com containers |
|---|---|
| Diferença entre ambientes | A **mesma imagem** roda em dev, CI e produção. |
| Dependências conflitantes | Cada container tem seu próprio sistema de arquivos isolado. |
| Onboarding lento | `docker compose up` sobe toda a stack do projeto. |
| Servidores manuais | Infraestrutura descrita em arquivos versionados no Git. |
| Desperdício | Containers compartilham o kernel e iniciam em milissegundos. |

> [!example] Exemplo prático
> Duas aplicações com Python diferentes no mesmo host, sem conflito:
> ```bash
> docker run --rm python:3.9-slim python --version
> docker run --rm python:3.12-slim python --version
> ```
> Nenhuma instalação no host foi alterada; cada comando usou o Python empacotado em sua imagem.

> [!warning] Docker não resolve tudo
> Containers não substituem boas práticas de arquitetura, segurança ou observabilidade. Um container mal configurado continua sendo uma aplicação mal configurada, só que mais fácil de distribuir.

## Exercício

Liste três situações do seu dia a dia (estudo ou trabalho) em que "na minha máquina funciona" já causou problema e como uma imagem Docker evitaria cada uma.

## Veja também

- [[O que é Docker]]
- [[Containers vs Máquinas Virtuais]]
- [[Imagens vs Containers]]
- [[MOC - Fundamentos - Docker]]
