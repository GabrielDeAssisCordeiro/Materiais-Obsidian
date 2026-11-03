---
tags:
  - referencia
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Glossário#Sandboxes e isolamento]]"
  - "[[Erros Comuns em Sandboxes]]"
---
# FAQ de Sandboxes

**Container é uma sandbox segura?**
É uma forma de sandbox, mas compartilha o kernel do host. Para código hostil, prefira microVM, gVisor ou VM — veja [[Sandbox vs VM vs Container vs Jail vs chroot]].

**`chroot` basta?**
Não. Não é fronteira de segurança.

**Posso analisar malware no Windows Sandbox?**
Serve para abrir arquivos suspeitos rapidamente, mas um laboratório de análise exige rede controlada, snapshots e telemetria — veja [[Laboratório de Análise de Malware]].

**Rootless resolve tudo?**
Reduz o impacto de uma fuga, mas não elimina vulnerabilidades — combine com [[Defesa em Profundidade]].

**Posso usar dados reais em staging?**
Evite. Prefira sintéticos; veja [[Conformidade e LGPD]].

**Como executo código de um LLM com segurança?**
Em sandbox efêmera, sem segredos e com rede restrita — [[Sandbox para Código Gerado por IA]].

**A VM é 100% segura?**
Não. Há histórico de fugas via hipervisor e dispositivos emulados — [[Fuga de Sandbox]].

**Qual é o erro mais comum?**
Liberar demais "só para funcionar" — [[Erros Comuns em Sandboxes]].

## Veja também

- [[Glossário#Sandboxes e isolamento]]
- [[Erros Comuns em Sandboxes]]
- [[MOC - Referência - Sandbox]]
