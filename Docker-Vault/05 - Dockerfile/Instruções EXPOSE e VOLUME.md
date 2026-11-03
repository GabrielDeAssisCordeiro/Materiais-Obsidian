---
tags:
  - docker
  - dockerfile
  - instrucao
aliases: []
tipo: instrucao
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Publicação de portas]]"
  - "[[Volumes nomeados]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instruções EXPOSE e VOLUME

## EXPOSE

Documenta em qual porta a aplicação escuta. **Não publica** a porta.

```dockerfile
EXPOSE 8080
EXPOSE 53/udp
```

A publicação ocorre com `docker run -p` (ou `-P` para publicar todas as portas expostas). Veja [[Publicação de portas]].

## VOLUME

Declara um ponto de montagem que será um **volume anônimo** se nenhum volume for fornecido no `run`.

```dockerfile
VOLUME /var/lib/dados
```

> [!warning] Evite `VOLUME` em imagens de aplicação
> - Alterações no diretório **após** a instrução `VOLUME`, no Dockerfile, são descartadas.
> - Gera volumes anônimos difíceis de rastrear e que se acumulam.
> - Quem usa a imagem não consegue "desfazer" a declaração.
>
> Prefira documentar o caminho e usar `-v nome:/caminho` ou `volumes:` no Compose. Imagens de banco de dados (como `postgres`) usam `VOLUME` por segurança dos dados.

> [!tip] Em Compose
> `ports:` publica; `expose:` apenas documenta e permite a comunicação entre serviços da mesma rede (que já é livre em redes definidas pelo usuário).

## Exercício

Construa uma imagem com `VOLUME /dados`, execute-a e use `docker volume ls` e `docker inspect` para encontrar o volume anônimo criado.

## Veja também

- [[Publicação de portas]]
- [[Volumes nomeados]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
