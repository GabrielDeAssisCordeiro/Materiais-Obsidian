---
titulo: "Flashcards - 09 Segurança da Própria Ferramenta"
aliases: ["Flashcards 09"]
tags:
  - integracao-seguranca
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Validacao de Entrada]]"
  - "[[SSRF Injeção e Desserialização Insegura]]"
  - "[[Gestão de Segredos na Ferramenta]]"
---

# Flashcards - 09 Segurança da Própria Ferramenta

## Resumo

Cartões de revisão do módulo **Segurança da Própria Ferramenta**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Validacao de Entrada]], [[SSRF Injeção e Desserialização Insegura]], [[Gestão de Segredos na Ferramenta]], [[Privilégio Mínimo e Hardening de Containers]].

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

Plugin Spaced Repetition para Obsidian; veja [[Como usar este vault - Integração]].

## Flashcards

#flashcards

Por que preferir allowlist a denylist na validação?::Aceitar apenas o permitido é mais robusto do que tentar listar tudo que é perigoso.
O que é SSRF?::Induzir o servidor a fazer requisições a destinos que o atacante não alcançaria diretamente.
Quais as defesas básicas contra SSRF?::Allowlist de hosts, verificar IP resolvido público, não seguir redirecionamentos e restringir egress.
O que evitar na desserialização de dados externos?::pickle e yaml.load; use JSON com schema e yaml.safe_load.
O que é secret zero?::O problema de obter a primeira credencial sem embuti-la; resolve-se com identidade de workload.
Quais medidas básicas de hardening de container?::Usuário não root, filesystem somente leitura, drop de capabilities, seccomp e limites de recursos.
Por que não montar docker.sock num container?::Equivale a dar controle total do host.
O que é typosquatting?::Pacote com nome parecido com um popular, para enganar a instalação.
O que é dependency confusion?::Pacote público com o mesmo nome de um interno resolvido indevidamente.
Como o hash chain protege a auditoria?::Cada registro inclui o hash do anterior; adulterar quebra a cadeia.
O que é a LGPD?::A Lei Geral de Proteção de Dados Pessoais, Lei 13.709/2018.
Pseudonimização e anonimização são equivalentes?::Não; dado pseudonimizado continua sendo pessoal, a anonimização é irreversível.
O que prevê o art. 48 da LGPD?::Comunicação de incidente de segurança à ANPD e aos titulares quando houver risco ou dano relevante.

## Veja também

- [[Validacao de Entrada]]
- [[SSRF Injeção e Desserialização Insegura]]
- [[Gestão de Segredos na Ferramenta]]
- [[Privilégio Mínimo e Hardening de Containers]]
- [[MOC - Revisão - Integração]]
- [[Como usar este vault - Integração]]

#flashcards #seguranca/revisao/flashcards
