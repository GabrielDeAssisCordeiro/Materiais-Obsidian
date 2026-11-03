---
titulo: "CloudSploit"
tipo: ferramenta
nome: "CloudSploit"
categoria: "Ofensivo/Cloud"
subcategoria: "Detecção de Más Configurações"
plataformas: ["Linux", "Node.js"]
licenca: "GPLv3 (parte do Aqua Security)"
linguagem: "JavaScript"
mitre_attack: ["T1526"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/aquasecurity/cloudsploit"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/cloud
---

# CloudSploit

> Motor de detecção de más configurações em ambientes AWS/Azure/GCP/Oracle Cloud.

## Como funciona
Executa uma biblioteca extensa de 'plugins', cada um correspondendo a uma verificação específica (ex.: bucket S3 público, security group aberto a 0.0.0.0/0, MFA não habilitado), coletando a configuração relevante via API do provedor e comparando-a contra o padrão esperado de segurança, retornando resultado PASS/FAIL/WARN por verificação.

## Como usar
Após configurar credenciais em `config.js`, executa-se `node index.js --config config.js`; o resultado pode ser filtrado por plugin ou por serviço, e integra-se facilmente a pipelines de CI para checagem contínua de compliance de infraestrutura como código.

## Casos de uso
- Checagem contínua de compliance de infraestrutura cloud
- Identificação de políticas IAM excessivamente permissivas

## Alternativas
[[ScoutSuite]] · [[Prowler]]

## Categoria
[[MOC - Cloud Ofensivo]]

## Link oficial
https://github.com/aquasecurity/cloudsploit
