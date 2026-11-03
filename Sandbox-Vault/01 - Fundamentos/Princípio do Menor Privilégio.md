---
tags:
  - fundamentos
  - seguranca
aliases:
  - "Least Privilege"
  - "PoLP"
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O que é um Ambiente Sandbox]]"
  - "[[Capabilities do Linux]]"
  - "[[Superfície de Ataque]]"
  - "[[Defesa em Profundidade]]"
---
# Princípio do Menor Privilégio

O **princípio do menor privilégio** (*Principle of Least Privilege*, PoLP) diz que cada processo, usuário ou componente deve receber **apenas** as permissões necessárias para cumprir sua função, e **somente pelo tempo necessário**.

## Por que importa para sandboxes

Uma sandbox é a aplicação prática do princípio: começamos de "nada é permitido" (*deny by default*) e liberamos explicitamente o mínimo.

| Em vez de... | Prefira... |
|---|---|
| Rodar como `root` | Usuário sem privilégios (ou *rootless*) |
| Todas as capabilities | `--cap-drop=ALL` e adicionar só o necessário |
| Sistema de arquivos gravável | Raiz somente leitura + `tmpfs` para temporários |
| Rede liberada | Rede desativada ou lista de destinos permitidos |
| Credenciais de longa duração | Tokens curtos com escopo mínimo |

## Exemplo prático

```bash
# Container com privilégios mínimos (conceitual; detalhes em Como Criar)
docker run --rm --read-only --cap-drop=ALL --network none \
  --user 65534:65534 alpine:3 id
```

> [!tip] Pense em allowlist, não em blocklist
> Listas de bloqueio sempre esquecem algo. Listas de permissão falham "fechadas": o que não foi previsto simplesmente não funciona.

> [!warning] Privilégio acumulado
> Permissões "temporárias" que ninguém revoga viram a regra. Revise periodicamente — ver [[Defesa em Profundidade]].

## Exercício

Pegue um programa que você usa (ex.: um script de backup) e escreva a lista mínima de arquivos, rede e permissões de que ele realmente precisa.

## Veja também

- [[O que é um Ambiente Sandbox]]
- [[Capabilities do Linux]]
- [[Superfície de Ataque]]
- [[Isolamento e Contenção]]
