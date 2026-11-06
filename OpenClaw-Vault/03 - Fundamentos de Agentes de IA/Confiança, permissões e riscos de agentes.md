---
titulo: "Confiança, permissões e riscos de agentes"
tags:
  - openclaw
  - conceito
  - agentes-de-ia
tipo: conceito
aliases: ['Riscos de agentes', 'Fronteira de confiança']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/start/why-openclaw"
  - "https://docs.openclaw.ai/concepts/architecture"
  - "https://docs.openclaw.ai/gateway/security"
relacionados:
  - "[[O que é um agente de IA]]"
  - "[[Uso de ferramentas e tool calling]]"
  - "[[Memória e contexto em agentes]]"
  - "[[O OpenClaw versus um chatbot]]"
---

# Confiança, permissões e riscos de agentes

## Objetivo

Aprender o vocabulário mínimo de segurança de agentes, antes de estudar os controles específicos do OpenClaw.

## Explicação

**Fronteira de confiança.** Divide o que você controla do que não controla. Em um agente, o texto que chega de fora (mensagens de terceiros, páginas, e-mails, arquivos baixados) **não é confiável**, mas entra no mesmo contexto que as suas instruções.

**Injeção de prompt (prompt injection).** Texto externo que tenta fazer o modelo seguir ordens do atacante. A variante **indireta** esconde a instrução em conteúdo que o agente lê por conta própria, como uma página web ou um e-mail. Como o agente pode agir, o dano potencial vai além de uma resposta errada: pode virar execução de comando ou vazamento de dados. Segundo fornecedores de segurança, nenhuma solução elimina o problema por completo; o objetivo é reduzir a probabilidade e limitar o impacto.

**Mínimo privilégio.** O agente deve ter só as permissões de que precisa: pastas específicas, ferramentas necessárias, contas de teste e credenciais com escopo reduzido.

**Política em código versus pedido no prompt.** A documentação do OpenClaw argumenta que a segurança real vem de regras impostas pelo runtime e pelo sistema operacional, e que listas de recursos não dizem onde fica a fronteira de confiança. Ela também informa que o sandbox vem **desligado por padrão**, então uma instalação padrão não está isolada por si só.

| Risco | Exemplo | Defesa geral |
|---|---|---|
| Injeção indireta | Página com instrução oculta | Limitar ferramentas, aprovar ações sensíveis, usar modelo forte |
| Permissão excessiva | Agente com acesso a todo o disco | Mínimo privilégio, sandbox, usuário dedicado |
| Exposição de rede | Painel acessível pela internet | Escutar só em loopback, autenticação, acesso remoto seguro |
| Extensão maliciosa | Skill com script nocivo | Auditar antes de instalar |
| Vazamento de segredo | Token em texto simples na memória | Gestão de segredos, permissões de arquivo |

Cada linha tem seu aprofundamento em [[MOC - Segurança e Hardening|Segurança e Hardening]] e [[MOC - Ameaças e Riscos|Ameaças e Riscos]].

## Exemplo prático

Antes de ligar uma nova ferramenta, responda por escrito:

```markdown
Ferramenta: ______
Que dados ela lê? ______
Que ações ela executa? ______
O que acontece se uma instrução maliciosa chegar pelos dados que ela lê? ______
Qual é o menor acesso que cumpre a tarefa? ______
```

Se não conseguir responder à penúltima pergunta, não habilite ainda.

## Armadilhas comuns

- Supor que um modelo mais inteligente é imune a injeção.
- Dar ao agente a sua conta principal "só para testar".
- Achar que um aviso no prompt ("nunca faça X") substitui uma regra imposta em código.

## Resumo

- Conteúdo externo é não confiável, mesmo quando entra pelo canal certo.
- Injeção indireta é o risco central de agentes que leem a web e e-mails.
- Mínimo privilégio e política em código são as defesas estruturais.
- No OpenClaw, o sandbox vem desligado por padrão.

## Relacionados

- [[O que é um agente de IA]]
- [[Uso de ferramentas e tool calling]]
- [[Memória e contexto em agentes]]
- [[O OpenClaw versus um chatbot]]
- [[MOC - Segurança e Hardening|Segurança e Hardening]]

## Exercícios

1. O que é injeção de prompt indireta?
2. Por que o dano potencial é maior em um agente do que em um chatbot?
3. O que significa mínimo privilégio na prática?
4. O que a documentação diz sobre o estado padrão do sandbox?
5. Preencha o questionário do exemplo para uma ferramenta de e-mail.
