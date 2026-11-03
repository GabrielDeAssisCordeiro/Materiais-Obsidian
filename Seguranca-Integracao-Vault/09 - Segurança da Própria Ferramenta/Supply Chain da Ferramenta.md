---
titulo: "Supply Chain da Ferramenta"
aliases: ["Supply chain", "Cadeia de suprimentos"]
tags:
  - integracao-seguranca
  - conceito
  - seguranca-da-ferramenta
  - supply-chain
tipo: conceito
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[SBOM - CycloneDX e SPDX]]"
  - "[[SLSA]]"
  - "[[Assinatura de Artefatos - Sigstore e cosign]]"
---

# Supply Chain da Ferramenta

## Resumo

Uma ferramenta de segurança típica depende de dezenas ou centenas de bibliotecas, imagens base, actions de CI e plugins. Cada uma é código de terceiros executado com os privilégios da ferramenta e, frequentemente, com acesso a credenciais valiosas. Ataques à **cadeia de suprimentos** exploram isso: pacotes maliciosos com nomes parecidos (*typosquatting*), contas de mantenedores comprometidas, dependências que mudam de dono, *build* adulterado. A defesa combina **reduzir** dependências, **fixar** versões e hashes, **monitorar** vulnerabilidades, **verificar** integridade e **produzir** artefatos assinados, com SBOM e proveniência.

## Conceitos-chave

- **Dependências diretas e transitivas:** o risco está principalmente nas transitivas.
- **Lockfiles e pinagem por hash:** `requirements.txt` com `--require-hashes`, `go.sum`, `package-lock.json`.
- **Typosquatting e dependency confusion:** pacotes com nome parecido ou nomes internos publicados em índices públicos.
- **Auditoria de vulnerabilidades:** `pip-audit`, `govulncheck`, Dependabot, Trivy.
- **Atualização com revisão:** PRs automáticos, com testes e *cooldown* para versões muito recentes.
- **Espelho/registry privado** com controle de origem.
- **Integridade do build:** [[SLSA]], [[Assinatura de Artefatos - Sigstore e cosign]], [[SBOM - CycloneDX e SPDX]].
- **Minimizar superfície:** menos dependências, bibliotecas padrão quando suficientes.

## Como funciona

```mermaid
flowchart LR
  D[Nova dependência proposta] --> R[Revisão: necessidade, manutenção, licença]
  R --> P[Fixa versão + hash no lockfile]
  P --> A[CI: pip-audit / govulncheck / Trivy]
  A --> B[Build isolado + SBOM]
  B --> S[Assinatura + proveniência]
  S --> REG[(Registry)]
  M[Monitoramento contínuo de CVEs no SBOM] --> T[Ticket / PR de atualização]
  REG --> M
```

A adoção de uma dependência é uma decisão de risco. A revisão considera atividade do projeto, quantidade de mantenedores, histórico de vulnerabilidades e se o recurso justifica o código adicional.

## Exemplo prático

Instalação com verificação de hash e auditoria (Python):

```bash
# Gera um arquivo com hashes (pip-tools)
pip-compile --generate-hashes requirements.in -o requirements.txt

# Instala exigindo hashes: qualquer divergência aborta
pip install --require-hashes -r requirements.txt

# Audita vulnerabilidades conhecidas
pip-audit -r requirements.txt
```

Equivalentes em Go:

```bash
go mod verify          # confere integridade dos módulos baixados
govulncheck ./...      # vulnerabilidades alcançáveis pelo código
```

Configuração do Dependabot com atualização semanal e agrupamento:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule: {interval: "weekly"}
    open-pull-requests-limit: 5
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule: {interval: "weekly"}
```

> [!example] Dependency confusion
> Configure o gerenciador de pacotes para resolver nomes internos **apenas** no registry privado.

## Boas práticas

- Fixe versões e hashes; atualize por PRs revisados.
- Remova dependências sem uso e prefira a biblioteca padrão.
- Gere e guarde SBOM por release; monitore novos CVEs.
- Use runners de CI isolados e sem acesso a segredos desnecessários durante a instalação de dependências.

## Erros comuns

- `pip install` sem versão ou hash em produção.
- Atualizar automaticamente tudo, sem testes nem revisão.
- Ignorar GitHub Actions e imagens base como dependências.
- Dependências abandonadas mantidas por anos.
- Publicar pacotes internos com nomes que podem colidir com índices públicos.

> [!warning] Incidentes reais
> Comprometimentos de pacotes populares já aconteceram em diversos ecossistemas; trate cada dependência como código que você executa.

## Referências para aprofundar

- OpenSSF Scorecard e *Best Practices Badge*; SLSA; OWASP Software Component Verification Standard (SCVS).

## Veja também

- [[SBOM - CycloneDX e SPDX]]
- [[SLSA]]
- [[Assinatura de Artefatos - Sigstore e cosign]]
- [[Gestão de Segredos na Ferramenta]]
- [[MOC - Segurança da Própria Ferramenta]]

#seguranca/ferramenta/supply-chain #seguranca/supply-chain
