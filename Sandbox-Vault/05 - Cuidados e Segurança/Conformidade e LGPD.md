---
tags:
  - seguranca
aliases:
  - "Dados pessoais"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Dados]]"
  - "[[Caso - Homologação e Staging]]"
---
# Conformidade e LGPD

A **LGPD** (Lei nº 13.709/2018) se aplica ao tratamento de dados pessoais, inclusive em ambientes de teste e sandbox.

- **Minimização:** não use dados reais sem necessidade; prefira [[Sandbox de Dados]] sintético.
- **Pseudonimização** não elimina a aplicação da lei.
- **Base legal e finalidade:** teste não é automaticamente base legal para usar dados de clientes.
- **Segurança:** aplique as mesmas proteções de produção a cópias com dados reais.
- **Serviços online de sandbox:** enviar arquivos com dados pessoais a terceiros pode ser transferência de dados; avalie contratos e localização.
- **Retenção e descarte:** defina prazos e comprove a eliminação.

> [!question] Verificar na documentação oficial
> Este material é educativo e não é aconselhamento jurídico. Consulte o texto da lei, orientações da ANPD e o jurídico/DPO da sua organização.

## Exercício

Liste os campos pessoais de uma tabela sua e proponha, para cada um, mascaramento ou geração sintética.

## Veja também

- [[Sandbox de Dados]]
- [[Descarte Seguro]]
- [[Caso - Homologação e Staging]]
- [[MOC - Cuidados e Segurança]]
