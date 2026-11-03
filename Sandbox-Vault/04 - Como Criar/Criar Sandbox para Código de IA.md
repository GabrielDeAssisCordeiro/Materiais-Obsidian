---
tags:
  - como-criar
aliases:
  - "Code interpreter caseiro"
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox para Código Gerado por IA]]"
  - "[[Criar Sandbox com Docker]]"
---
# Criar Sandbox para Código de IA

Exemplo em Python que executa código gerado por um modelo dentro de um container descartável e restrito.

```python
import os, pathlib, subprocess, tempfile, uuid

def executar_python(codigo: str, timeout: int = 10) -> dict:
    nome = f"sandbox-{uuid.uuid4().hex[:8]}"
    with tempfile.TemporaryDirectory() as d:
        os.chmod(d, 0o755)
        arq = pathlib.Path(d) / "main.py"
        arq.write_text(codigo, encoding="utf-8")
        os.chmod(arq, 0o644)
        cmd = [
            "docker", "run", "--rm", "--name", nome,
            "--network", "none", "--read-only",
            "--tmpfs", "/tmp:rw,noexec,nosuid,size=16m",
            "--cap-drop=ALL", "--security-opt", "no-new-privileges",
            "--memory", "256m", "--memory-swap", "256m",
            "--cpus", "0.5", "--pids-limit", "64",
            "--user", "65534:65534",
            "-v", f"{d}:/work:ro", "-w", "/work",
            "python:3.12-alpine", "python", "main.py",
        ]
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return {"stdout": p.stdout[:10000], "stderr": p.stderr[:10000], "code": p.returncode}
        except subprocess.TimeoutExpired:
            subprocess.run(["docker", "kill", nome], capture_output=True)
            return {"stdout": "", "stderr": "tempo esgotado", "code": -1}

print(executar_python("print(sum(range(10)))"))
```

## Pontos de atenção

- Limite o tamanho da saída (já truncada).
- **Um container por execução**; nada persiste.
- Sem rede e sem segredos no ambiente.
- Para risco maior, troque o runtime por `--runtime=runsc` ([[Criar Sandbox com gVisor]]) ou use microVMs ([[Criar Sandbox com Firecracker]]).

> [!danger] O socket do Docker no processo orquestrador é sensível
> Quem controla o orquestrador controla o Docker. Proteja a API que recebe o código (autenticação, limites de taxa).

## Exercício

Execute `import socket; socket.create_connection(('1.1.1.1',53))` pela função e explique o erro.

## Veja também

- [[Sandbox para Código Gerado por IA]]
- [[Criar Sandbox com Docker]]
- [[Criar Sandbox com gVisor]]
- [[Criar Sandbox com Firecracker]]
- [[MOC - Como Criar]]
