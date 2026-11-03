---
tags:
  - docker
  - containers
  - init
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Comandos create, start, stop, restart e kill]]"
  - "[[Namespaces]]"
  - "[[Comando docker run]]"
---

# Init, PID 1 e sinais

Dentro do container, o processo principal é o **PID 1**. Ele tem duas particularidades no Linux:

1. **Sinais**: o kernel não aplica o tratamento padrão a PID 1. Sem um *handler* explícito, SIGTERM é ignorado e o `docker stop` espera o timeout e aplica SIGKILL.
2. **Zumbis**: PID 1 deve fazer *reaping* de processos filhos órfãos; aplicações comuns não fazem isso.

## Problema clássico: shell como PID 1

```dockerfile
# ❌ forma shell: o PID 1 é /bin/sh -c, que NÃO repassa SIGTERM à aplicação
CMD python app.py

# ✅ forma exec: a aplicação é o PID 1 e recebe os sinais diretamente
CMD ["python", "app.py"]
```

## Solução: `--init`

```bash
# Executa o tini como PID 1: repassa sinais e colhe zumbis
docker run -d --init --name app alpine:3.20 sleep 300
docker exec app ps
```

No Compose: `init: true` no serviço.

```bash
# Teste do efeito: tempo para parar
time docker stop app
```

> [!tip] Scripts de entrypoint
> Se usar um script shell como `ENTRYPOINT`, termine-o com `exec "$@"` para substituir o shell pela aplicação:
> ```sh
> #!/bin/sh
> set -e
> # ... preparação ...
> exec "$@"
> ```

> [!info] `STOPSIGNAL`
> Algumas aplicações encerram graciosamente com outro sinal (ex.: Nginx com SIGQUIT). Defina `STOPSIGNAL SIGQUIT` no Dockerfile ou `--stop-signal`.

## Exercício

Compare o tempo de `docker stop` para um container com `CMD sleep 300` (forma shell) e `CMD ["sleep","300"]` (forma exec), usando imagens construídas por você.

## Veja também

- [[Comandos create, start, stop, restart e kill]]
- [[Namespaces]]
- [[Comando docker run]]
- [[MOC - Containers]]
