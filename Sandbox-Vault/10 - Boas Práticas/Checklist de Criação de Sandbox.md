---
tags:
  - boas-praticas
  - arquitetura
aliases:
  - "Checklist de criação"
tipo: checklist
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Defesa em Profundidade]]"
  - "[[Endurecimento (Hardening)]]"
---
# Checklist de Criação de Sandbox

**Antes de criar**
- [ ] Defini o modelo de ameaças e o nível de confiança do código
- [ ] Escolhi a fronteira adequada (container, gVisor, microVM, VM)

**Configuração**
- [ ] Usuário sem privilégios; sem `--privileged`
- [ ] `--cap-drop=ALL` e `no-new-privileges`
- [ ] Raiz somente leitura; temporários em `tmpfs`
- [ ] Rede desativada ou saída por allowlist
- [ ] Limites de CPU, memória, processos, disco e tempo
- [ ] Sem segredos; sem montagens do host além do necessário
- [ ] Imagem mínima, fixada por digest e atualizada
- [ ] Integrações (clipboard, pastas, USB) desativadas

**Operação**
- [ ] Logs exportados para fora
- [ ] Teste de isolamento executado e documentado
- [ ] Procedimento de descarte definido

## Veja também

- [[Checklist de Auditoria de Sandbox]]
- [[Defesa em Profundidade]]
- [[Políticas de Ciclo de Vida]]
- [[MOC - Boas Práticas]]
