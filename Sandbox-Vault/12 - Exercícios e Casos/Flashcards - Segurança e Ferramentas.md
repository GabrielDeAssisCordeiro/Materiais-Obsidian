---
tags:
  - exercicios
aliases: []
tipo: flashcards
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Prompt Injection e seus Riscos]]"
  - "[[Modelo de Ameaças]]"
---
# Flashcards - Segurança e Ferramentas

Por que não montar `docker.sock` em uma sandbox?::Quem controla o socket cria containers privilegiados e obtém root no host.
O que é prompt injection indireta?::Instruções maliciosas em conteúdo lido pelo agente (páginas, e-mails, arquivos).
Quais são as três pernas perigosas de um agente?::Dados privados, conteúdo não confiável e canal de comunicação externo.
Por que reverter um snapshot não resolve uma fuga?::O dano ao host persiste; o snapshot só restaura a VM.
DNS pode vazar de uma rede "sem internet"?::Sim; teste com nslookup e capture o tráfego.
Pseudonimização sai do escopo da LGPD?::Não; continua sendo dado pessoal.
O que significa T1497 no MITRE ATT&CK?::Evasão de virtualização/sandbox.
Análise estática ou dinâmica primeiro?::Estática, por ser passiva e segura.
STRIDE significa...?::Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
Por que defesa em profundidade?::Nenhuma barreira é perfeita; camadas independentes limitam o impacto de uma falha.
Quando preferir microVM a container?::Código hostil, multi-inquilino, quando a fronteira do kernel compartilhado é insuficiente.
Por que dar tokens curtos e de escopo mínimo?::Limitam o dano se forem expostos ou abusados.

## Veja também

- [[Flashcards - Fundamentos]]
- [[Glossário#Sandboxes e isolamento]]
- [[MOC - Exercícios e Casos]]
