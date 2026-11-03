---
tags:
  - tipos
aliases:
  - "Windows Sandbox"
  - "Android sandbox"
  - "iOS sandbox"
tipo: tipo-de-sandbox
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Aplicação]]"
  - "[[Criar Sandbox com Windows Sandbox]]"
  - "[[Sandbox por Virtualização Completa]]"
---
# Sandbox de Sistema Operacional

O próprio SO oferece mecanismos de confinamento.

| Plataforma | Mecanismo |
|---|---|
| **Windows Sandbox** | Ambiente Windows descartável, baseado em virtualização (Hyper-V); exige edições Pro/Enterprise/Education |
| Windows (AppContainer, MSIX) | Isolamento de apps com capacidades declaradas |
| **macOS App Sandbox** | *Entitlements* declaram acessos permitidos (arquivos, rede, câmera) |
| **Android** | Cada app roda com UID próprio, SELinux e filtros seccomp |
| **iOS** | Contêiner de dados por app e *entitlements*; revisão e assinatura de código |

> [!info] Windows Sandbox
> Cada abertura é um Windows novo; ao fechar, tudo é descartado. Configuração via arquivo `.wsb` — ver [[Criar Sandbox com Windows Sandbox]].

> [!question] Verificar na documentação oficial
> Requisitos de edição e recursos do Windows Sandbox mudam entre versões do Windows.

## Exercício

Identifique no seu celular quais permissões um app de câmera solicitou e se todas são necessárias.

## Veja também

- [[Sandbox de Aplicação]]
- [[Criar Sandbox com Windows Sandbox]]
- [[Sandbox por Virtualização Completa]]
- [[MOC - Tipos de Sandbox]]
