---
titulo: "MOC - Segurança da Própria Ferramenta"
aliases: ["MOC Segurança da Ferramenta"]
tags:
  - integracao-seguranca
  - moc
  - seguranca-da-ferramenta
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[Validacao de Entrada]]"
  - "[[MOC - Observabilidade e Detecção]]"
---

# MOC - Segurança da Própria Ferramenta

## Resumo

Como proteger a própria ferramenta de segurança: entrada, execução, segredos, cadeia de suprimentos, auditoria e privacidade. Volte à [[Home - Integração]].

## Conceitos-chave

Fronteiras de confiança, menor privilégio, defesa em profundidade e responsabilização.

## Como funciona

A ferramenta é alvo valioso por concentrar credenciais e privilégios; cada nota apresenta uma camada de defesa.

## Notas

- [[Validacao de Entrada]] — Fronteira de confiança, schemas e limites.
- [[SSRF Injeção e Desserialização Insegura]] — Prevenção de SSRF, injeção e desserialização insegura.
- [[Gestão de Segredos na Ferramenta]] — Credenciais efêmeras, secret zero e proteção em memória.
- [[Privilégio Mínimo e Hardening de Containers]] — Não root, somente leitura, rede restrita e RBAC mínimo.
- [[Supply Chain da Ferramenta]] — Dependências fixadas, auditadas e assinadas.
- [[Auditoria e Logs de Ações]] — Trilha íntegra de ações sensíveis.
- [[LGPD e Privacidade]] — Minimização, pseudonimização e retenção de dados pessoais.

## Exemplo prático

Um webhook entra por [[Validacao de Entrada]], consulta um destino validado contra SSRF ([[SSRF Injeção e Desserialização Insegura]]), usa credencial efêmera ([[Gestão de Segredos na Ferramenta]]) e deixa trilha ([[Auditoria e Logs de Ações]]).

## Boas práticas

Trate a ferramenta como sistema crítico de produção.

## Erros comuns

Achar que uma ferramenta de segurança é segura por definição.

## Referências para aprofundar

- [[OWASP ASVS]]

## Veja também

- [[Home - Integração]]
- [[MOC - Observabilidade e Detecção]]
- [[MOC - Projetos Práticos]]
