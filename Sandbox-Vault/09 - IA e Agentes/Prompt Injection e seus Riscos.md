---
tags:
  - ia
  - agentes
aliases:
  - "Prompt injection"
  - "Injeção de prompt"
tipo: ia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox para Código Gerado por IA]]"
  - "[[Permissões de Agentes de IA]]"
---
# Prompt Injection e seus Riscos

**Prompt injection** é quando texto não confiável (página web, e-mail, arquivo, resultado de ferramenta) contém instruções que o modelo trata como se viessem do usuário.

| Tipo | Descrição |
|---|---|
| Direta | O próprio usuário tenta contornar as regras do sistema |
| **Indireta** | Instruções escondidas em conteúdo que o agente lê (páginas, documentos, e-mails, issues) |

## Por que sandbox importa

Não há defesa perfeita contra injeção no nível do modelo. A estratégia segura é **limitar o dano**: assumir que o modelo pode ser enganado e garantir que, mesmo assim, ele **não possa** fazer coisas graves.

> [!danger] A combinação perigosa
> Um agente que ao mesmo tempo (1) acessa **dados privados**, (2) lê **conteúdo não confiável** e (3) pode **comunicar-se para fora** (rede, e-mail, links) é vulnerável à exfiltração. Remova pelo menos uma das três pernas.

## Mitigações

1. Menor privilégio e sandbox — [[Permissões de Agentes de IA]].
2. Sem segredos nem dados sensíveis no ambiente de execução.
3. Saída de rede por lista de permissão — [[Limites de Rede e Sistema de Arquivos para Agentes]].
4. Aprovação humana para ações sensíveis — [[Aprovação Humana em Ações Sensíveis]].
5. Separar contextos: o agente que lê conteúdo externo não deve ter as mesmas permissões que o que age em sistemas internos.
6. Registro e revisão de ações.
7. Filtros de entrada/saída ajudam, mas **não são suficientes**.

> [!question] Verificar na documentação oficial
> Consulte o OWASP Top 10 para aplicações com LLM (categoria de *prompt injection*) para a taxonomia e orientações atuais.

## Exercício

Dado um agente que lê e-mails e pode responder, identifique quais das três pernas existem e como remover uma.

## Veja também

- [[Sandbox para Código Gerado por IA]]
- [[Permissões de Agentes de IA]]
- [[Aprovação Humana em Ações Sensíveis]]
- [[MOC - IA e Agentes]]
