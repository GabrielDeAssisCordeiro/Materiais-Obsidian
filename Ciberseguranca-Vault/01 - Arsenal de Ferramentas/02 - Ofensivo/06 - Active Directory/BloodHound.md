---
titulo: "BloodHound"
tipo: ferramenta
nome: "BloodHound"
categoria: "Ofensivo/Active-Directory"
subcategoria: "Mapeamento de Caminhos de Ataque"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv3 (BloodHound CE)"
linguagem: "JavaScript/C#"
mitre_attack: ["T1482", "T1087.002"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/SpecterOps/BloodHound"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/ad
  - arsenal-de-ferramentas
---

# BloodHound

> Mapeia relações de privilégio em Active Directory usando grafos, revelando caminhos até Domain Admin.

## Como funciona
O coletor (SharpHound) consulta o AD via LDAP e sessões ativas via SMB/WMI para extrair todas as relações relevantes (associações a grupos, permissões ACL, sessões de logon, confianças entre domínios) e as modela como um grafo em banco Neo4j; algoritmos de caminho mais curto sobre esse grafo revelam automaticamente a cadeia de abusos mais curta entre um usuário comum e um privilégio alto.

## Como usar
Executa-se o coletor no ambiente (`SharpHound.exe -c All`) para gerar arquivos JSON, que são importados na interface web do BloodHound CE; a partir daí, consultas pré-construídas ('Find shortest path to Domain Admins') ou consultas Cypher customizadas exploram visualmente os caminhos de ataque identificados.

## Casos de uso
- Identificação de caminhos de escalonamento de privilégio em avaliação de AD
- Priorização de remediação de más configurações críticas

## Alternativas
[[PingCastle]]

## Categoria
[[MOC - Active Directory]]

## Link oficial
https://github.com/SpecterOps/BloodHound
