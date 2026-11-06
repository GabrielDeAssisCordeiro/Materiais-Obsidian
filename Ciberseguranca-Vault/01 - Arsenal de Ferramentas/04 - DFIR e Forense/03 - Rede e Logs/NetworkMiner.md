---
titulo: "NetworkMiner"
tipo: ferramenta
nome: "NetworkMiner"
categoria: "DFIR/Rede-e-Logs"
subcategoria: "Forense de Rede Orientada a Artefatos"
plataformas: ["Windows", "Linux (via Mono)"]
licenca: "Gratuito (versão Free)"
linguagem: "C#"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.netresec.com/?page=NetworkMiner"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/rede
  - arsenal-de-ferramentas
---

# NetworkMiner

> Ferramenta forense de rede que reconstrói artefatos (arquivos, imagens, credenciais) a partir de capturas PCAP.

## Como funciona
Em vez de exibir pacote por pacote como o Wireshark, reorganiza automaticamente o conteúdo da captura por 'hosts' e extrai diretamente os artefatos transferidos (arquivos, imagens, credenciais em texto claro, certificados) reconstruindo-os prontos para visualização, priorizando a perspectiva de investigação forense sobre a perspectiva de protocolo.

## Como usar
Basta abrir o arquivo PCAP na interface; as abas organizadas por categoria ('Files', 'Credentials', 'Images', 'Hosts') listam automaticamente tudo o que foi reconstruído da captura, sem necessidade de escrever filtros manualmente.

## Casos de uso
- Extração rápida de arquivos/credenciais trafegados em uma captura
- Triagem forense inicial de uma captura de rede sem conhecimento profundo de protocolos

## Alternativas
[[Wireshark]]

## Categoria
[[MOC - Rede e Logs]]

## Link oficial
https://www.netresec.com/?page=NetworkMiner
