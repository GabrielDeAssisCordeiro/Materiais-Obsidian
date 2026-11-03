---
tags:
  - ia
  - agentes
aliases:
  - "Checklist agentes"
tipo: checklist
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox para Código Gerado por IA]]"
  - "[[Checklist de Auditoria de Sandbox]]"
---
# Checklist de Segurança para Agentes

- [ ] Código de LLM roda **somente** em sandbox efêmera
- [ ] Fronteira adequada ao risco (microVM/gVisor para multi-inquilino)
- [ ] Sem segredos no ambiente da sandbox
- [ ] Rede negada ou saída por lista de permissão
- [ ] Sistema de arquivos restrito a diretórios explícitos
- [ ] Limites de CPU, memória, processos, disco e tempo
- [ ] Ações sensíveis exigem aprovação humana clara
- [ ] Conteúdo externo tratado como não confiável (injeção indireta)
- [ ] Menos de três "pernas" da combinação perigosa
- [ ] Logs de ações enviados para fora da sandbox
- [ ] Sandbox nunca compartilhada entre usuários
- [ ] Conectores/plugins revisados e com versões fixas

## Veja também

- [[Sandbox para Código Gerado por IA]]
- [[Checklist de Auditoria de Sandbox]]
- [[Prompt Injection e seus Riscos]]
- [[MOC - IA e Agentes]]
