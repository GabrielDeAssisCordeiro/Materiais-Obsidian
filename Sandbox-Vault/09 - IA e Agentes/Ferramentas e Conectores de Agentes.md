---
tags:
  - ia
  - agentes
aliases:
  - "MCP"
  - "Plugins de agentes"
tipo: ia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Permissões de Agentes de IA]]"
  - "[[Cadeia de Suprimentos de Software]]"
---
# Ferramentas e Conectores de Agentes

Conectores (como servidores MCP e plugins) dão ao agente acesso a sistemas externos. Cada um é **código e permissões de terceiros**.

- Instale apenas conectores de origem confiável; revise o que cada ferramenta pode ler/escrever.
- Dê **tokens de escopo mínimo** (somente leitura sempre que possível).
- Execute conectores locais em sandbox/container, sem acesso ao `home`.
- Trate **descrições e saídas de ferramentas como entrada não confiável** (vetor de injeção).
- Registre chamadas de ferramentas e revise periodicamente.

> [!warning] Cadeia de suprimentos
> Atualizações de um conector podem mudar seu comportamento. Fixe versões e revise mudanças — ver [[Cadeia de Suprimentos de Software]].

## Veja também

- [[Permissões de Agentes de IA]]
- [[Cadeia de Suprimentos de Software]]
- [[Prompt Injection e seus Riscos]]
- [[MOC - IA e Agentes]]
