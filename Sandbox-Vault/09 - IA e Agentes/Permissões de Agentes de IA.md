---
tags:
  - ia
  - agentes
aliases:
  - "Agent permissions"
  - "Escopo de ferramentas"
tipo: ia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do Menor Privilégio]]"
  - "[[Aprovação Humana em Ações Sensíveis]]"
---
# Permissões de Agentes de IA

Agentes combinam um modelo com **ferramentas** (shell, navegador, arquivos, APIs). Cada ferramenta é uma permissão.

| Ferramenta | Risco | Controle |
|---|---|---|
| Shell | Execução arbitrária | Somente dentro de sandbox |
| Arquivos | Leitura de dados sensíveis, destruição | Diretório de trabalho; leitura/escrita separadas |
| Navegador/HTTP | Exfiltração; conteúdo malicioso | Lista de domínios permitidos |
| E-mail/chat | Envio de dados; fraude | Aprovação humana para envio |
| Banco de dados | Vazamento/alteração | Usuário somente leitura, escopo mínimo |
| Pagamentos/produção | Dano financeiro | Aprovação humana obrigatória; limites |

```yaml
# Exemplo conceitual de política de agente (não é formato de nenhum produto específico)
agente: assistente-de-codigo
ferramentas:
  shell:
    ambiente: sandbox-efemera
    rede: negada
    timeout_segundos: 30
  arquivos:
    leitura: ["/work"]
    escrita: ["/work/saida"]
  http:
    permitidos: ["pypi.org", "files.pythonhosted.org"]
acoes_que_exigem_aprovacao: [enviar_email, apagar_arquivo, deploy]
```

> [!tip] Credenciais por tarefa, não por agente
> Emita tokens curtos, com escopo mínimo, para cada tarefa.

## Exercício

Escreva a política de permissões de um agente que organiza arquivos em uma pasta.

## Veja também

- [[Princípio do Menor Privilégio]]
- [[Aprovação Humana em Ações Sensíveis]]
- [[Limites de Rede e Sistema de Arquivos para Agentes]]
- [[MOC - IA e Agentes]]
