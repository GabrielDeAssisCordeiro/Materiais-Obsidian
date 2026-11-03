---
tags:
  - docker
  - registries
  - seguranca
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Docker Hub]]"
  - "[[Comando docker tag e push]]"
  - "[[Automação de publicação de imagens]]"
---

# Login e tokens de acesso

O `docker login` guarda credenciais para o registry. **Nunca** use a senha da conta em scripts: use **tokens de acesso**.

## Criar um token (Docker Hub)

Conta → **Settings → Personal access tokens → Generate new token**. Escolha o escopo mínimo:

| Escopo | Permite |
|---|---|
| Read-only | `pull` |
| Read & Write | `pull` e `push` |
| Read, Write, Delete | Também excluir imagens/tags |

## Login seguro

```bash
# O token vem de uma variável (ou de um cofre) e é lido pela entrada padrão
echo "$DOCKER_TOKEN" | docker login -u meuusuario --password-stdin

# Outro registry
echo "$TOKEN" | docker login ghcr.io -u USUARIO --password-stdin
```

> [!danger] Não use `-p SENHA` na linha de comando
> A senha fica no histórico do shell e visível na lista de processos. Use sempre `--password-stdin`.

## Onde ficam as credenciais

O arquivo `~/.docker/config.json` guarda as credenciais. Sem um *credential helper*, elas ficam em **base64 (não criptografadas)**.

```json
{
  "credsStore": "desktop"
}
```

| Helper | Plataforma |
|---|---|
| `desktop` / `osxkeychain` | macOS (Keychain) |
| `wincred` / `desktop` | Windows |
| `secretservice` ou `pass` | Linux |

> [!tip] Em CI
> Use segredos da plataforma (GitHub Secrets, GitLab CI variables protegidas) e tokens com escopo e validade mínimos; rotacione periodicamente.

## Exercício

Gere um token somente leitura, faça login com `--password-stdin`, tente um `push` (deve falhar) e revogue o token no final.

## Veja também

- [[Docker Hub]]
- [[Comando docker tag e push]]
- [[Automação de publicação de imagens]]
- [[MOC - Registries]]
