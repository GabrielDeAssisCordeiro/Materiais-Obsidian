---
titulo: "Ansible"
tipo: ferramenta
nome: "Ansible"
categoria: "Defensivo/Hardening-e-Baselines"
subcategoria: "Automação de Configuração (Hardening as Code)"
plataformas: ["Linux", "Windows (via WinRM)"]
licenca: "GPLv3"
linguagem: "Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.ansible.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/hardening
  - arsenal-de-ferramentas
---

# Ansible

> Ferramenta de automação de configuração usada para aplicar e manter hardening de forma consistente e versionada.

## Como funciona
Descreve o estado desejado de um sistema (serviços habilitados, permissões, pacotes instalados) em 'playbooks' YAML declarativos, aplicados remotamente via SSH/WinRM sem necessidade de agente permanente no host gerenciado; a execução é idempotente — rodar o mesmo playbook repetidamente só altera o que ainda não está no estado desejado.

## Como usar
Define-se um inventário de hosts e um playbook (ex.: baseado em roles públicas de hardening como `dev-sec/ansible-collection-hardening`) e executa-se `ansible-playbook -i inventario hardening.yml`, aplicando as configurações de segurança definidas em todos os hosts do inventário de forma consistente.

## Casos de uso
- Aplicação consistente de hardening em frotas de servidores
- Hardening versionado como código (infraestrutura como código)

## Alternativas
[[Lynis]]

## Categoria
[[MOC - Hardening e Baselines]]

## Link oficial
https://www.ansible.com/
