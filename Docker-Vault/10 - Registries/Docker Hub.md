---
tags:
  - docker
  - registries
  - docker-hub
aliases:
  - Hub
  - docker.io
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Login e tokens de acesso]]"
  - "[[Registries]]"
  - "[[Imagens oficiais, verificadas e de editores]]"
  - "[[Comando docker tag e push]]"
  - "[[Versionamento e tags imutáveis]]"
---

# Docker Hub

O **Docker Hub** é o registry padrão do Docker: hospeda imagens oficiais, de editores verificados e de qualquer usuário ou organização.

## Repositórios públicos e privados

| Tipo | Quem acessa | Observações |
|---|---|---|
| **Público** | Qualquer pessoa pode fazer `pull` | Ideal para projetos open source |
| **Privado** | Apenas membros autorizados | Número de repositórios privados depende do plano |

Nomenclatura: `usuario-ou-organizacao/repositorio:tag`. Imagens oficiais ficam no namespace implícito `library/` (`nginx` = `docker.io/library/nginx`).

## Fluxo básico de publicação

```bash
docker login -u meuusuario              # use um token de acesso como senha
docker build -t meuusuario/meu-app:1.0 .
docker push meuusuario/meu-app:1.0
docker pull meuusuario/meu-app:1.0
docker logout
```

## Pesquisar

```bash
docker search python --limit 5
docker search nginx --filter is-official=true
```

> [!warning] Limites de pull
> O Docker Hub aplica **limites de taxa de pull** a usuários anônimos e gratuitos. Em CI e clusters, autentique-se, use um **espelho (*pull-through cache*)** ou copie as imagens para seu próprio registry.

> [!question] Verificar na documentação oficial
> Os limites de pull, os planos e a política de retenção de imagens inativas mudam com frequência. Consulte as páginas de "Usage and limits" e de planos do Docker Hub.

> [!tip] Organização e equipes
> Use **organizações** e equipes para controlar quem pode ler e escrever, e **tokens de acesso de organização** para automação.

## Exercício

Crie uma conta no Docker Hub, publique uma imagem pública simples (ex.: o exemplo "Olá, Docker") e depois baixe-a em outra máquina ou após remover a imagem local.

## Veja também

- [[Login e tokens de acesso]]
- [[Registries]]
- [[Imagens oficiais, verificadas e de editores]]
- [[Comando docker tag e push]]
- [[Versionamento e tags imutáveis]]
- [[MOC - Registries]]
