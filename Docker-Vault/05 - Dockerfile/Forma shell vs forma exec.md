---
tags:
  - docker
  - dockerfile
  - instrucao
  - shell
  - exec
  - comparativo
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Instruções CMD e ENTRYPOINT]]"
  - "[[Init, PID 1 e sinais]]"
  - "[[Instrução RUN]]"
---

# Forma shell vs forma exec

`RUN`, `CMD` e `ENTRYPOINT` aceitam duas sintaxes.

| | Forma **shell** | Forma **exec** |
|---|---|---|
| Sintaxe | `CMD python app.py` | `CMD ["python", "app.py"]` |
| Executa via | `/bin/sh -c "..."` | Diretamente o executável |
| Expansão de `$VAR`, `*`, pipes | Sim | **Não** (a menos que você chame um shell) |
| PID 1 | O shell | **A aplicação** |
| Recebe SIGTERM do `docker stop` | Normalmente **não** | **Sim** |
| JSON válido | Não | Sim (aspas duplas obrigatórias) |

```dockerfile
# ❌ O shell é o PID 1 e pode engolir o SIGTERM
CMD python app.py

# ✅ Sinais chegam ao Python
CMD ["python", "app.py"]

# ✅ Precisa de expansão de variável? Chame o shell explicitamente e use exec
CMD ["sh", "-c", "exec python app.py --porta \"$PORTA\""]
```

> [!bug] `docker stop` demora 10 segundos
> Sintoma típico da forma shell: o SIGTERM não chega à aplicação e o Docker aplica SIGKILL após o timeout.

> [!info] Aspas simples quebram a forma exec
> `CMD ['python','app.py']` não é JSON válido; o Docker o tratará como forma shell, com resultado inesperado.

## Exercício

Construa duas imagens com `CMD sleep 300` e `CMD ["sleep","300"]` e meça o tempo de `docker stop` em cada uma.

## Veja também

- [[Instruções CMD e ENTRYPOINT]]
- [[Init, PID 1 e sinais]]
- [[Instrução RUN]]
- [[MOC - Dockerfile]]
