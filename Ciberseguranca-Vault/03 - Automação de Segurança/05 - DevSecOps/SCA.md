---
titulo: "SCA"
aliases: ["Software Composition Analysis", "Análise de Composição de Software"]
tags:
  - ciberseguranca
  - automacao-de-seguranca
  - conceito
  - devsecops
tipo: conceito
nivel: intermediario
relacionados:
  - "[[MOC - DevSecOps]]"
  - "[[SBOM]]"
  - "[[SAST]]"
  - "[[Priorização com CVSS, EPSS e KEV]]"
---

# SCA

## Objetivo
Identificar e tratar vulnerabilidades e riscos de licença em dependências de terceiros, de forma contínua e integrada ao pipeline. Mapa: [[MOC - DevSecOps]].

## Conceito
Aplicações modernas são majoritariamente compostas de bibliotecas de terceiros. O **SCA** (Software Composition Analysis) inventaria essas dependências, diretas e transitivas, e as compara com bases de vulnerabilidades (CVE, avisos de ecossistemas, OSV) e de licenças. O resultado alimenta o [[SBOM]] e a priorização de correções.

**O que o SCA verifica:**

- **Vulnerabilidades conhecidas** em versões usadas.
- **Dependências transitivas:** pacotes trazidos por outros pacotes.
- **Licenças:** incompatibilidades legais.
- **Saúde do pacote:** abandono, mantenedor único, typosquatting e confusão de dependências (riscos da cadeia de suprimentos).

**Priorização inteligente:** nem toda vulnerabilidade em dependência é explorável. Fatores úteis: a função vulnerável é realmente chamada (alcançabilidade)? Está no [[Priorização com CVSS, EPSS e KEV|KEV]]? Há correção disponível? A dependência é de produção ou apenas de teste?

```mermaid
flowchart LR
    A[Manifestos e lockfiles] --> B[Resolver árvore de dependências]
    B --> C[Cruzar com bases de vulnerabilidades]
    C --> D[Filtrar por alcançabilidade e exposição]
    D --> E[PR automático de atualização]
    E --> F[Testes]
    F --> G[Merge]
```

## Exemplo prático
> [!example] Falha só para alta severidade com correção disponível
> O pipeline gera o inventário e falha apenas para vulnerabilidades críticas com versão corrigida, evitando bloquear quem não tem como agir.

```bash
#!/usr/bin/env bash
set -euo pipefail
# Auditoria de dependências Python (somente leitura)
pip install --quiet pip-audit
pip-audit -r requirements.txt --format json > auditoria.json
python - <<'EOF'
import json, sys
dados = json.load(open("auditoria.json"))
criticos = [d["name"] for d in dados.get("dependencies", []) if d.get("vulns")]
print("Dependências com vulnerabilidades:", criticos)
sys.exit(1 if criticos else 0)
EOF
```

## Boas práticas
- Use arquivos de trava (lockfiles) para versões reproduzíveis.
- Automatize pull requests de atualização com testes.
- Defina política de licenças permitidas.
- Fixe e verifique integridade (hashes) das dependências.
- Reavalie periodicamente, pois novas falhas surgem em versões já implantadas ([[Varredura Contínua de Vulnerabilidades]]).

## Erros comuns
- Olhar só dependências diretas.
- Ignorar o ambiente de build e as dependências de desenvolvimento.
- Atualizar sem testar, quebrando a aplicação.
- Contar vulnerabilidades sem filtrar por alcançabilidade.

> [!warning] Cadeia de suprimentos
> Pacotes maliciosos com nomes parecidos aos legítimos existem. Valide a origem e use registros internos de confiança.

## Para revisar
> [!question] Perguntas
> 1. O que são dependências transitivas?
> 2. Que critérios reduzem o ruído de achados de SCA?
> 3. Qual o papel do lockfile?
> 4. O que é confusão de dependências?

## Links relacionados
[[Secret Scanning]], [[Scan de Containers]], [[Segurança em Pipelines CI-CD]], [[Shift Left]].
