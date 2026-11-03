---
tags:
  - como-criar
aliases:
  - "venv"
  - "Python isolado"
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Caso - Desenvolvimento Seguro]]"
  - "[[Criar Sandbox com Docker]]"
---
# Criar Ambientes Python Isolados

> [!warning] `venv` isola **dependências**, não segurança
> Um ambiente virtual não impede acesso a arquivos nem à rede. Para código não confiável, use containers/VMs.

## venv com dependências verificadas

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --require-hashes -r requirements.txt   # exige hashes fixos
pip list
deactivate
```

Gere `requirements.txt` com hashes usando `pip-compile --generate-hashes` (pacote `pip-tools`).

## Dev Container restrito (`.devcontainer/devcontainer.json`)

```json
{
  "name": "python-isolado",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "remoteUser": "vscode",
  "runArgs": ["--cap-drop=ALL", "--security-opt=no-new-privileges"],
  "mounts": [],
  "postCreateCommand": "pip install --require-hashes -r requirements.txt"
}
```

> [!tip] Não monte `~/.ssh`, `~/.aws` nem o `home` no devcontainer. Use *agent forwarding* ou tokens de escopo mínimo.

## Exercício

Crie um devcontainer sem montagens e verifique que `ls ~/.ssh` não mostra suas chaves reais.

## Veja também

- [[Caso - Desenvolvimento Seguro]]
- [[Criar Sandbox com Docker]]
- [[Sandbox por Containers]]
- [[MOC - Como Criar]]
