---
titulo: "Gestão de Segredos na Ferramenta"
aliases: ["Secret management", "Secret zero", "Credenciais efêmeras"]
tags:
  - integracao-seguranca
  - conceito
  - seguranca-da-ferramenta
  - segredos
tipo: conceito
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[API Keys e Gestão de Credenciais]]"
  - "[[Integração com Gestão de Segredos - Vault e gitleaks]]"
  - "[[Privilégio Mínimo e Hardening de Containers]]"
---

# Gestão de Segredos na Ferramenta

## Resumo

Uma ferramenta de segurança integra-se a muitos sistemas e, por isso, **concentra credenciais** valiosas: tokens de API, chaves de scanners, senhas de contas de serviço, certificados. Se a ferramenta for comprometida, essas credenciais são o prêmio. **Gestão de segredos na ferramenta** significa que cada segredo tem origem controlada (cofre), escopo mínimo, vida curta, uso auditado e nunca aparece em código, imagens, logs, mensagens de erro ou *dumps*. O desafio central é o **secret zero**: como a própria ferramenta obtém a primeira credencial para acessar o cofre sem embuti-la.

## Conceitos-chave

- **Fontes de segredo:** cofre (Vault, cloud KMS/Secrets Manager), variáveis injetadas, arquivos montados (`/run/secrets`), tmpfs.
- **Secret zero:** resolvido por **identidade de workload** (Kubernetes ServiceAccount, IAM role, OIDC do CI, AppRole com *response wrapping*).
- **Credenciais dinâmicas e efêmeras:** geradas sob demanda, com TTL.
- **Rotação:** automática e sem *downtime* (duas credenciais válidas em transição).
- **Escopo por integração:** uma credencial por serviço e por ambiente.
- **Proteção em memória e em tipos:** tipos que ocultam o valor (`SecretStr`), evitar `repr` e logs.
- **Revogação e resposta a vazamento.**

## Como funciona

```mermaid
sequenceDiagram
  participant P as Pod / Processo
  participant I as Identidade da plataforma
  participant V as Cofre
  participant S as Sistema externo
  P->>I: Prova de identidade (token da plataforma)
  I-->>P: Token de curta duração
  P->>V: Autentica e solicita segredo
  V-->>P: Credencial com TTL
  P->>S: Usa a credencial
  Note over P,V: Renova antes do TTL; descarta ao expirar
```

A aplicação não carrega segredos estáticos: apresenta sua identidade e recebe credenciais temporárias. Em caso de comprometimento do processo, a janela de uso da credencial é curta e a revogação é simples.

## Exemplo prático

Configuração que nunca imprime o segredo (Python/pydantic):

```python
from pathlib import Path
from pydantic import SecretStr
from pydantic_settings import BaseSettings

def ler_segredo_arquivo(nome: str) -> SecretStr:
    # Segredos montados como arquivos em tmpfs (ex.: Docker/Kubernetes secrets)
    caminho = Path("/run/secrets") / nome
    return SecretStr(caminho.read_text(encoding="utf-8").strip())

class Config(BaseSettings):
    jira_url: str
    jira_token: SecretStr           # str(config.jira_token) -> '**********'

cfg = Config(jira_url="https://jira.local", jira_token=ler_segredo_arquivo("jira_token"))
print(cfg)                          # o token aparece mascarado
usar = cfg.jira_token.get_secret_value()   # só no ponto de uso
```

> [!tip] Teste de vazamento
> Inclua no CI um teste que força erros e verifica que o valor do segredo não aparece em logs nem em mensagens de exceção.

## Boas práticas

- Prefira identidade de workload a segredos estáticos.
- Defina TTL curto e automatize a rotação.
- Nunca coloque segredos em argumentos de linha de comando, URLs, `ENV` do Dockerfile ou imagens.
- Monitore uso anômalo de credenciais e tenha um plano de revogação ensaiado.

## Erros comuns

- Reaproveitar a mesma credencial em dev, homologação e produção.
- Segredo em variável de ambiente exposta por *dump* de processo ou endpoint de debug.
- Imprimir configuração completa na inicialização.
- Rotação que derruba a integração por falta de transição.

> [!question] Exercício
> Se o container da sua ferramenta fosse comprometido agora, quais credenciais o invasor obteria e por quanto tempo elas valeriam?

## Referências para aprofundar

- OWASP Secrets Management Cheat Sheet; documentação de Workload Identity (Kubernetes, cloud); HashiCorp Vault.

## Veja também

- [[API Keys e Gestão de Credenciais]]
- [[Integração com Gestão de Segredos - Vault e gitleaks]]
- [[Privilégio Mínimo e Hardening de Containers]]
- [[Supply Chain da Ferramenta]]
- [[MOC - Segurança da Própria Ferramenta]]

#seguranca/ferramenta/segredos #seguranca/segredos
