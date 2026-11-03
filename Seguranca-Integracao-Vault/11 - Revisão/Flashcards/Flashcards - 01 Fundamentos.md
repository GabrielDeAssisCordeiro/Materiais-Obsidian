---
titulo: "Flashcards - 01 Fundamentos"
aliases: ["Flashcards 01"]
tags:
  - integracao-seguranca
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Modelo CIA e Princípios de Segurança]]"
  - "[[SDLC e SSDLC]]"
  - "[[Modelagem de Ameaças - STRIDE e PASTA]]"
---

# Flashcards - 01 Fundamentos

## Resumo

Cartões de revisão do módulo **Fundamentos**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Modelo CIA e Princípios de Segurança]], [[SDLC e SSDLC]], [[Modelagem de Ameaças - STRIDE e PASTA]], [[MITRE ATT&CK - Integração]].

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

O que significa CIA?::Confidencialidade, Integridade e Disponibilidade.
O que é shift-left?::Antecipar atividades de segurança para o início do ciclo de desenvolvimento, quando corrigir é mais barato.
Quais são as seis categorias do STRIDE?::Spoofing, Tampering, Repudiation, Information disclosure, Denial of service e Elevation of privilege.
Qual propriedade o Spoofing viola?::Autenticidade.
O que é o MITRE ATT&CK?::Base de conhecimento de táticas, técnicas e procedimentos de adversários, construída a partir de observações reais.
Qual a diferença entre tática e técnica no ATT&CK?::Tática é o objetivo do adversário; técnica é como ele o atinge.
Qual a diferença entre OWASP Top 10 e ASVS?::O Top 10 é um documento de conscientização sobre riscos; o ASVS é um catálogo de requisitos verificáveis em três níveis.
Quais são as funções do NIST CSF 2.0?::Govern, Identify, Protect, Detect, Respond e Recover.
O que são IG1, IG2 e IG3 nos CIS Controls?::Grupos de implementação conforme maturidade e risco; o IG1 representa a higiene básica.
O que o SAST analisa?::O código-fonte, sem executá-lo.
Qual a diferença entre DAST e SAST?::O DAST testa a aplicação em execução, de fora; o SAST analisa o código de forma estática.
Qual é a função de um SOAR?::Orquestrar e automatizar a resposta por meio de playbooks e integrações, com gestão de casos.
O que faz uma ferramenta de SCA?::Inventaria as dependências de terceiros e as cruza com bases de vulnerabilidades.
O que diz o princípio do menor privilégio?::Cada identidade recebe apenas as permissões necessárias, pelo tempo necessário.

## Veja também

- [[Modelo CIA e Princípios de Segurança]]
- [[SDLC e SSDLC]]
- [[Modelagem de Ameaças - STRIDE e PASTA]]
- [[MITRE ATT&CK - Integração]]
- [[MOC - Revisão - Integração]]
- [[Como usar este vault - Integração]]

#flashcards #seguranca/revisao/flashcards
