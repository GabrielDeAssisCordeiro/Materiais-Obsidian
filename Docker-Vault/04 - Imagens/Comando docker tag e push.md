---
tags:
  - docker
  - imagens
  - comandos
  - registry
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Tags e digests de imagens]]"
  - "[[Registries]]"
  - "[[Docker Hub]]"
  - "[[Comando docker pull]]"
---

# Comando docker tag e push

## `docker tag`: cria um novo nome para a mesma imagem

```bash
docker tag meu-app:1.0 meuusuario/meu-app:1.0
docker tag meu-app:1.0 meuusuario/meu-app:latest
docker tag meu-app:1.0 registro.exemplo.com:5000/equipe/meu-app:1.0
```

Não duplica dados: são apenas rótulos apontando para o mesmo ID de imagem.

## `docker push`: envia ao registry

```bash
docker login                                   # Docker Hub (usa token de acesso)
docker push meuusuario/meu-app:1.0
docker push --all-tags meuusuario/meu-app

# Registry privado
docker login registro.exemplo.com:5000
docker push registro.exemplo.com:5000/equipe/meu-app:1.0
```

> [!tip] Use tokens de acesso
> No Docker Hub, crie um **Personal Access Token** com o menor escopo necessário em vez de usar a senha da conta. Em CI, guarde o token como segredo da plataforma.

> [!warning] O nome precisa conter o registry
> Sem prefixo de host, o push vai para o Docker Hub. Para outro registry, a tag **deve** começar com o host (ex.: `ghcr.io/...`), senão o Docker tenta enviar para `docker.io/...` e falha por permissão.

> [!bug] `denied: requested access to the resource is denied`
> Causas: não autenticado, namespace errado (seu usuário/organização) ou sem permissão de escrita no repositório.

## Exercício

Crie duas tags para a imagem `alpine:3.20` (`lab/alpine:v1` e `lab/alpine:estavel`), liste e verifique com `docker images` que o IMAGE ID é o mesmo.

## Veja também

- [[Tags e digests de imagens]]
- [[Registries]]
- [[Docker Hub]]
- [[Comando docker pull]]
- [[MOC - Imagens]]
