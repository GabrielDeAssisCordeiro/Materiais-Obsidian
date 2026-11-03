---
titulo: "Zeek (Bro)"
tipo: ferramenta
nome: "Zeek (Bro)"
categoria: "Defensivo/IDS-IPS-Firewall"
subcategoria: "Monitoramento de Rede (NSM)"
plataformas: ["Linux", "macOS"]
licenca: "BSD-3-Clause"
linguagem: "C++"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://zeek.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/ids-ips
---

# Zeek (Bro)

> Framework de monitoramento de rede focado em análise de protocolo rica, não apenas detecção por assinatura.

## Como funciona
Em vez de apenas comparar pacotes contra assinaturas, o Zeek decodifica profundamente dezenas de protocolos de aplicação (HTTP, DNS, SSL, SMB) e gera logs estruturados e ricos em metadados para cada conexão observada (ex.: todo certificado TLS visto, toda consulta DNS resolvida), permitindo detecção customizada via sua própria linguagem de script e análise forense retroativa sobre esses logs.

## Como usar
Após configurar os 'nodes' de captura (`zeekctl deploy` em ambientes distribuídos ou execução standalone), o Zeek gera continuamente logs categorizados por protocolo (`conn.log`, `dns.log`, `http.log`); scripts Zeek customizados podem gerar alertas (`notice.log`) para padrões específicos de interesse.

## Casos de uso
- Análise forense retroativa de tráfego de rede via logs ricos
- Detecção customizada baseada em comportamento de protocolo

## Alternativas
[[Suricata]]

## Categoria
[[MOC - IDS, IPS e Firewall]]

## Link oficial
https://zeek.org/
