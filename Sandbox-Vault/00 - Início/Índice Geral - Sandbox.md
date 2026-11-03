---
tags:
  - indice
  - moc
aliases: []
tipo: indice
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Sandbox]]"
---
# Índice Geral

Lista de todas as notas do vault, por pasta (os templates ficam em [[MOC - Templates]]).

## 01 - Fundamentos

- [[Capabilities do Linux]]
- [[Cgroups]]
- [[História e Evolução das Sandboxes]]
- [[Isolamento e Contenção]]
- [[MOC - Fundamentos - Sandbox]]
- [[Namespaces do Linux]]
- [[O que é um Ambiente Sandbox]]
- [[Princípio do Menor Privilégio]]
- [[Sandbox vs VM vs Container vs Jail vs chroot]]
- [[Superfície de Ataque]]

## 02 - Casos de Uso

- [[Caso - Abertura de Arquivos e Navegação Suspeitos]]
- [[Caso - Agentes de IA e Código de LLM]]
- [[Caso - Análise de Malware]]
- [[Caso - CI e CD]]
- [[Caso - Desenvolvimento Seguro]]
- [[Caso - Execução de Código Não Confiável]]
- [[Caso - Homologação e Staging]]
- [[Caso - Laboratórios e Aprendizado]]
- [[Caso - Plugins e Extensões]]
- [[Caso - Sandbox de APIs e Pagamentos]]
- [[Caso - Testes de Software e QA]]
- [[MOC - Casos de Uso]]

## 03 - Tipos de Sandbox

- [[Hipervisores Tipo 1 e Tipo 2]]
- [[Honeypots e Cyber Ranges]]
- [[Landlock pledge e unveil]]
- [[MOC - Tipos de Sandbox]]
- [[Sandbox de Aplicação]]
- [[Sandbox de Dados]]
- [[Sandbox de Processo]]
- [[Sandbox de Rede]]
- [[Sandbox de Sistema Operacional]]
- [[Sandbox em Linguagem]]
- [[Sandbox em Nuvem]]
- [[Sandbox por Containers]]
- [[Sandbox por Kernel em Espaço de Usuário]]
- [[Sandbox por MicroVMs]]
- [[Sandbox por Virtualização Completa]]
- [[Sandbox por WebAssembly]]
- [[Seccomp]]

## 04 - Como Criar

- [[Criar Ambientes Python Isolados]]
- [[Criar Laboratório de Malware Seguro]]
- [[Criar Sandbox com Bubblewrap]]
- [[Criar Sandbox com Docker]]
- [[Criar Sandbox com Firecracker]]
- [[Criar Sandbox com Firejail]]
- [[Criar Sandbox com Podman Rootless]]
- [[Criar Sandbox com VMs]]
- [[Criar Sandbox com Vagrant]]
- [[Criar Sandbox com WebAssembly e Wasmtime]]
- [[Criar Sandbox com Windows Sandbox]]
- [[Criar Sandbox com gVisor]]
- [[Criar Sandbox de Desenvolvimento Web e APIs]]
- [[Criar Sandbox para Código de IA]]
- [[MOC - Como Criar]]

## 05 - Cuidados e Segurança

- [[Atualização e Patching]]
- [[Conformidade e LGPD]]
- [[Descarte Seguro]]
- [[Dispositivos USB e Periféricos]]
- [[Endurecimento (Hardening)]]
- [[Erros Comuns em Sandboxes]]
- [[Evasão de Sandbox por Malware]]
- [[Fuga de Sandbox]]
- [[Gerenciamento de Segredos e Credenciais]]
- [[Limites de Recursos]]
- [[Logs e Monitoramento]]
- [[MOC - Cuidados e Segurança]]
- [[Snapshots e Reversão]]
- [[Vazamento por Pastas Compartilhadas e Área de Transferência]]
- [[Vazamento por Rede e DNS]]

## 06 - Ferramentas

- [[Comparativo de Ferramentas]]
- [[Comparativo de Ferramentas de Análise de Malware]]
- [[Comparativo por Nível de Isolamento]]
- [[Ferramenta - AppArmor e SELinux]]
- [[Ferramenta - Bubblewrap]]
- [[Ferramenta - Docker]]
- [[Ferramenta - Firecracker]]
- [[Ferramenta - Firejail]]
- [[Ferramenta - Kata Containers]]
- [[Ferramenta - Podman]]
- [[Ferramenta - Wasmtime]]
- [[Ferramenta - Windows Sandbox]]
- [[Ferramenta - gVisor]]
- [[MOC - Ferramentas]]

## 07 - Análise de Malware

- [[Any.Run Joe Sandbox e Hybrid Analysis]]
- [[Análise Estática e Dinâmica]]
- [[Cuckoo e CAPE]]
- [[FLARE-VM e REMnux]]
- [[Ferramentas de Análise Dinâmica]]
- [[Ferramentas de Análise Estática]]
- [[Fluxo de Triagem de Amostras]]
- [[Indicadores de Comprometimento]]
- [[Laboratório de Análise de Malware]]
- [[MOC - Análise de Malware]]
- [[Relatórios de Análise de Malware]]
- [[YARA e Regras de Detecção]]

## 08 - Dev e DevOps

- [[Ambientes Efêmeros]]
- [[Ambientes de Staging e Promoção]]
- [[Cadeia de Suprimentos de Software]]
- [[Dados de Teste e Mocks]]
- [[Feature Flags]]
- [[Infraestrutura como Código]]
- [[MOC - Dev e DevOps]]
- [[Preview Environments]]
- [[Runners Efêmeros e Pipelines Seguros]]
- [[Testes de Integração com Containers]]

## 09 - IA e Agentes

- [[Aprovação Humana em Ações Sensíveis]]
- [[Arquiteturas de Sandbox para Agentes]]
- [[Checklist de Segurança para Agentes]]
- [[Ferramentas e Conectores de Agentes]]
- [[Limites de Rede e Sistema de Arquivos para Agentes]]
- [[MOC - IA e Agentes]]
- [[Permissões de Agentes de IA]]
- [[Prompt Injection e seus Riscos]]
- [[Sandbox para Código Gerado por IA]]

## 10 - Boas Práticas

- [[Checklist de Auditoria de Sandbox]]
- [[Checklist de Criação de Sandbox]]
- [[Como Escolher o Nível de Isolamento]]
- [[Defesa em Profundidade]]
- [[MOC - Boas Práticas]]
- [[Modelo de Ameaças]]
- [[Padrões de Projeto para Sandboxes]]
- [[Políticas de Ciclo de Vida]]

## 11 - Referência

- [[Cheat Sheet - Docker e Podman]]
- [[Cheat Sheet - Isolamento no Linux]]
- [[Cheat Sheet - VMs]]
- [[FAQ de Sandboxes]]
- [[Glossário#Sandboxes e isolamento]]
- [[MOC - Referência - Sandbox]]
- [[Referências]]
- [[Trilha de Aprendizado - Sandbox]]

## 12 - Exercícios e Casos

- [[Caso Real - CVE-2022-0492 e cgroups]]
- [[Caso Real - Dirty COW]]
- [[Caso Real - Docker API exposta]]
- [[Caso Real - Leaky Vessels CVE-2024-21626]]
- [[Caso Real - Spectre e Meltdown]]
- [[Caso Real - VENOM CVE-2015-3456]]
- [[Caso Real - runc CVE-2019-5736]]
- [[Exercícios - Avançado]]
- [[Exercícios - Iniciante]]
- [[Exercícios - Intermediário]]
- [[Flashcards - Fundamentos]]
- [[Flashcards - Segurança e Ferramentas]]
- [[MOC - Exercícios e Casos]]

## Anexos

- [[MOC - Anexos]]

- [[Espectro de isolamento.canvas]]
- [[Modelo de ameaças.canvas]]
- [[Mapa conceitual de sandbox.canvas]]

## Veja também

- [[Home - Sandbox]]
