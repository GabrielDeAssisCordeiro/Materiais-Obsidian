---
tags:
  - ia
  - agentes
aliases: []
tipo: ia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Permissões de Agentes de IA]]"
  - "[[Prompt Injection e seus Riscos]]"
---
# Aprovação Humana em Ações Sensíveis

Para ações irreversíveis ou de alto impacto, o agente **propõe** e um humano **aprova**.

| Ação | Aprovação |
|---|---|
| Ler arquivos no diretório de trabalho | Não necessária |
| Executar código em sandbox sem rede | Não necessária |
| Instalar pacotes | Opcional (lista de permissão) |
| Enviar e-mails/mensagens, publicar | **Sim** |
| Apagar dados, alterar produção, pagar | **Sim** |

> [!tip] Mostre o que será feito, não só "Aprovar?"
> A tela de aprovação deve exibir comando, destino e efeito esperado em linguagem clara.

> [!warning] Fadiga de aprovação
> Se tudo exige aprovação, as pessoas aprovam sem ler. Reserve a confirmação para o que importa e deixe o resto contido pela sandbox.

## Veja também

- [[Permissões de Agentes de IA]]
- [[Prompt Injection e seus Riscos]]
- [[Checklist de Segurança para Agentes]]
- [[MOC - IA e Agentes]]
