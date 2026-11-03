---
tags:
  - docker
  - observabilidade
  - depuracao
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Comando docker exec e attach]]"
  - "[[Superfície de ataque e imagens mínimas]]"
  - "[[Containers em loop de reinício]]"
---

# Docker Debug

O **Docker Debug** abre um shell de depuração em **qualquer container ou imagem**, inclusive os *slim* e *distroless* (sem shell), fornecendo um *toolbox* com ferramentas (editores, `curl`, `htop`, etc.) **sem alterar a imagem**.

```bash
docker debug meu-container          # container em execução (ou parado)
docker debug nginx:1.27             # inspeciona uma imagem
```

Dentro da sessão, o sistema de arquivos do container aparece normalmente e você pode instalar ferramentas extras no toolbox (por exemplo, com `install`), sem persistir na imagem do alvo.

> [!question] Verificar na documentação oficial
> O Docker Debug depende da versão do Docker Desktop/CLI e do **plano** da conta (historicamente, recurso de assinaturas pagas). Confirme disponibilidade e sintaxe na documentação.

## Alternativas sem o Docker Debug

```bash
# 1) Container auxiliar compartilhando os namespaces do alvo
docker run -it --rm \
  --pid=container:ALVO \
  --network=container:ALVO \
  nicolaka/netshoot

# 2) Variante de depuração da imagem (ex.: distroless :debug) em ambiente de teste
docker run -it --rm --entrypoint sh gcr.io/distroless/static-debian12:debug

# 3) Copiar arquivos para análise
docker cp ALVO:/caminho/arquivo ./arquivo
```

> [!warning] Compartilhar PID dá visibilidade dos processos do alvo
> Faça isso apenas em ambientes que você administra; não use em produção compartilhada sem controle de acesso.

## Exercício

Escolha uma imagem distroless, rode-a e tente depurá-la com a alternativa do container auxiliar (`--pid=container:` e `--network=container:`).

## Veja também

- [[Comando docker exec e attach]]
- [[Superfície de ataque e imagens mínimas]]
- [[Containers em loop de reinício]]
- [[MOC - Observabilidade e Depuração]]
