---
tags:
  - docker
  - dockerfile
  - instrucao
  - comparativo
aliases:
  - CMD vs ENTRYPOINT
  - CMD
  - ENTRYPOINT
tipo: instrucao
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Forma shell vs forma exec]]"
  - "[[Init, PID 1 e sinais]]"
  - "[[Comando docker run]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instruções CMD e ENTRYPOINT

Ambas definem o que o container executa ao iniciar.

- **`CMD`**: comando (ou argumentos) **padrão**, facilmente substituído em `docker run IMAGEM outro-comando`.
- **`ENTRYPOINT`**: o **executável fixo** do container; os argumentos do `run` são **anexados** a ele.

```dockerfile
# Somente CMD: o usuário pode trocar tudo
FROM alpine:3.20
CMD ["echo", "olá"]
```

```dockerfile
# ENTRYPOINT + CMD: ENTRYPOINT é o programa; CMD são os argumentos padrão
FROM alpine:3.20
ENTRYPOINT ["ping", "-c", "3"]
CMD ["localhost"]
```

```bash
docker run --rm ping-img                # ping -c 3 localhost
docker run --rm ping-img 1.1.1.1        # ping -c 3 1.1.1.1  (CMD substituído)
docker run --rm --entrypoint sh -it ping-img   # troca o ENTRYPOINT
```

## Tabela de combinações

| | Sem ENTRYPOINT | `ENTRYPOINT ["a"]` |
|---|---|---|
| Sem CMD | erro: nada para executar | `a` |
| `CMD ["b"]` | `b` | `a b` |
| `docker run img c` | `c` | `a c` |

## CMD vs ENTRYPOINT: quando usar

| Use | Quando |
|---|---|
| `CMD` | A imagem é um ambiente geral (shell, runtime) e o comando varia |
| `ENTRYPOINT` | A imagem *é* um programa (CLI, serviço) com comportamento fixo |
| Ambos | Programa fixo com argumentos padrão alteráveis |

> [!warning] Só vale o último
> Se houver várias instruções `CMD` (ou `ENTRYPOINT`), apenas a **última** tem efeito. Em multi-stage, vale a do estágio final.

> [!tip] Scripts de entrypoint
> Use um script que prepara o ambiente e termina com `exec "$@"`, assim o processo final é o PID 1. Veja [[Init, PID 1 e sinais]].

## Exercício

Construa a imagem com `ENTRYPOINT ["ping","-c","3"]` e `CMD ["localhost"]`. Execute com e sem argumento e depois com `--entrypoint`.

## Veja também

- [[Forma shell vs forma exec]]
- [[Init, PID 1 e sinais]]
- [[Comando docker run]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
