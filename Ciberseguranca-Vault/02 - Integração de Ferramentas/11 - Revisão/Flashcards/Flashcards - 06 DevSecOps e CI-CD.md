---
titulo: "Flashcards - 06 DevSecOps e CI-CD"
aliases: ["Flashcards 06"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Security Gates e Shift-Left]]"
  - "[[GitHub Actions]]"
  - "[[SBOM - CycloneDX e SPDX]]"
---

# Flashcards - 06 DevSecOps e CI-CD

## Resumo

Cartões de revisão do módulo **DevSecOps e CI-CD**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Security Gates e Shift-Left]], [[GitHub Actions]], [[SBOM - CycloneDX e SPDX]], [[Assinatura de Artefatos - Sigstore e cosign]].

## Como funciona

Instale o plugin Spaced Repetition e use *Review flashcards*. O algoritmo agenda a próxima revisão conforme sua avaliação (fácil, bom, difícil).

## Exemplo prático

Responda mentalmente antes de virar o cartão. Se errar, releia a nota de origem e reformule o cartão com suas palavras.

## Boas práticas

- Revise um pouco todos os dias.
- Crie cartões próprios para pontos que você errou.
- Mantenha respostas curtas.

## Erros comuns

- Decorar sem entender a razão.
- Acumular revisões atrasadas.
- Cartões longos demais.

## Referências para aprofundar

Plugin Spaced Repetition para Obsidian.

## Flashcards

#flashcards

O que é um security gate?::Ponto de decisão automatizado que interrompe o fluxo se um critério de segurança for violado.
Por que fixar actions pelo SHA?::Tags são mutáveis; o SHA fixa o código exato.
Qual o risco do pull_request_target?::Roda com privilégios do repositório base; usar código de fork nele é perigoso.
Pre-commit substitui o CI?::Não; hooks locais podem ser ignorados, então o CI repete as verificações.
O que é um SBOM?::Inventário formal de componentes, versões e licenças de um software.
Qual a diferença entre CycloneDX e SPDX?::CycloneDX é orientado a segurança (OWASP); SPDX é forte em licenciamento (ISO/IEC 5962).
O que é VEX?::Declaração de que uma vulnerabilidade é ou não explorável no produto.
Como funciona o cosign keyless?::Assina com certificado efêmero do Fulcio ligado a uma identidade OIDC, registrado no Rekor.
Assinar a tag ou o digest de uma imagem?::Sempre o digest.
O que é o SLSA?::Framework de níveis de garantia sobre como um artefato foi construído, baseado em proveniência.
O que é OPA/Rego?::Motor de políticas e linguagem declarativa para decisões como código.
O que aconteceu com o tfsec?::Foi incorporado ao Trivy, via trivy config.
O que é o Checkov?::Scanner de IaC multi-framework (Terraform, Kubernetes, CloudFormation e outros).

## Veja também

- [[Security Gates e Shift-Left]]
- [[GitHub Actions]]
- [[SBOM - CycloneDX e SPDX]]
- [[Assinatura de Artefatos - Sigstore e cosign]]
- [[MOC - Revisão - Integração]]

#flashcards #seguranca/revisao/flashcards
