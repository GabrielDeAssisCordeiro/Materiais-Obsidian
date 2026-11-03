---
titulo: "Google Dorking"
tipo: ferramenta
nome: "Google Dorking"
categoria: "OSINT"
subcategoria: "Técnica de Busca Avançada (conceitual)"
plataformas: ["Web"]
licenca: "N/A (técnica, não software)"
linguagem: "N/A"
mitre_attack: ["T1593.002"]
nivel: iniciante
situacao: ativo
link_oficial: "https://www.google.com/"
tags:
  - ciberseguranca
  - ferramenta
  - osint
---

# Google Dorking

> Conjunto de operadores de busca avançada do Google usados para localizar informações expostas não intencionalmente.

## Como funciona
Operadores especiais de busca (`site:`, `filetype:`, `intitle:`, `inurl:`) permitem restringir resultados a domínios, tipos de arquivo ou padrões de URL/título específicos, revelando documentos, painéis administrativos ou arquivos de configuração indexados publicamente que a organização não pretendia expor, simplesmente combinando esses operadores de forma direcionada.

## Como usar
Exemplos de uso: `site:alvo.com filetype:pdf confidencial` busca PDFs confidenciais indexados do domínio alvo; `intitle:'index of' site:alvo.com` procura listagens de diretório expostas acidentalmente. Bancos de dorks (ex.: Google Hacking Database/GHDB) catalogam combinações conhecidas eficazes.

## Casos de uso
- Identificação de documentos/arquivos sensíveis indexados publicamente
- Reconhecimento passivo sem interação direta com a infraestrutura do alvo

## Alternativas
[[Shodan]]

## Categoria
[[MOC - OSINT]]

## Link oficial
https://www.google.com/
