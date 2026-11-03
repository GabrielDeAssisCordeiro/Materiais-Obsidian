---
tags:
  - exercicios
aliases: []
tipo: exercicio
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Sandbox por MicroVMs]]"
  - "[[Sandbox por WebAssembly]]"
  - "[[Sandbox para Código Gerado por IA]]"
---
# Exercícios - Avançado

1. **gVisor:** rode um container com `runsc` e compare `dmesg` e desempenho de E/S com `runc` ([[Criar Sandbox com gVisor]]).
2. **microVM:** inicie uma microVM Firecracker sem rede e verifique a ausência de interfaces ([[Criar Sandbox com Firecracker]]).
3. **Wasm:** prove, com Wasmtime, que um módulo só acessa o diretório liberado ([[Criar Sandbox com WebAssembly e Wasmtime]]).
4. **Modelo de ameaças:** modele uma plataforma de execução de código de alunos com STRIDE ([[Modelo de Ameaças]]).
5. **Agente de IA:** implemente [[Criar Sandbox para Código de IA]] com proxy de saída e allowlist ([[Limites de Rede e Sistema de Arquivos para Agentes]]).
6. **Laboratório de análise:** monte e valide o isolamento do [[Criar Laboratório de Malware Seguro]] **sem executar nenhuma amostra**; analise apenas o arquivo de teste da nota [[YARA e Regras de Detecção]].
7. **Estudo de caso:** leia um aviso oficial de CVE e escreva "o que falhou / camada que teria ajudado" ([[Caso Real - Dirty COW]]).

## Veja também

- [[Exercícios - Intermediário]]
- [[MOC - Exercícios e Casos]]
- [[Modelo de Ameaças]]
