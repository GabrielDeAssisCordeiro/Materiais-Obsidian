---
titulo: "Convenções - Automação"
aliases: ["Guia de Estilo"]
tags:
  - automacao-seguranca
  - guia
  - inicio
tipo: guia
nivel: iniciante
relacionados:
  - "[[Home - Automação]]"
  - "[[Template de Conceito - Automação]]"
---
# Convenções - Automação

Este documento define as regras de escrita e organização do material de automação de segurança. Qualquer nota nova deve segui-las e as regras gerais do [[GUIA]].

## Objetivo

Garantir que todas as notas tenham a mesma estrutura, que o grafo seja bem conectado e que a revisão espaçada seja possível.

## Estrutura de pastas

As pastas são numeradas para forçar a ordem didática: `00 - Início`, `01 - Fundamentos`, `02 - Arquitetura e Ferramentas`, `03 - SOC e Resposta a Incidentes`, `04 - Vulnerabilidades e Compliance`, `05 - DevSecOps`, `06 - Threat Intel e Detecção`, `07 - Laboratórios e Scripts`, `08 - IA, Governança e Boas Práticas` e `09 - Revisão`. Cada pasta tem um MOC (Map of Content) listado na [[Home - Automação]]. Os templates ficam em `Templates/`, na raiz do vault ([[MOC - Templates]]).

## Propriedades

Toda nota começa com um bloco YAML:

```yaml
---
titulo: "Título da nota"
aliases: []
tags:
  - automacao-seguranca
  - conceito
  - soar
tipo: conceito          # conceito | playbook | laboratorio | revisao | moc | guia
nivel: intermediario    # iniciante | intermediario | avancado
relacionados:
  - "[[Outra nota]]"
---
```

`relacionados` guarda wikilinks entre aspas, para que o Obsidian os trate como links reais.

## Nomes de nota

O nome do arquivo é o título da nota, com acentos e espaços (por exemplo `Triagem Automática de Alertas.md`). Nomes devem ser únicos em todo o vault; se o nome já existir em outro material, acrescente ` - Automação` (como em `Home - Automação`).

## Links e tags

- Use wikilinks entre notas com generosidade; toda nota deve linkar ao menos o seu MOC e três notas relacionadas.
- Toda nota leva a tag `automacao-seguranca`, a tag do seu `tipo` e a do tema da pasta (por exemplo `soc`, `devsecops` ou `deteccao`).
- Não crie link para nota que ainda não existe.

## Estrutura interna da nota

Cada nota de conteúdo segue: **Objetivo**, **Conceito**, **Exemplo prático**, **Boas práticas**, **Erros comuns**, **Para revisar** (3 a 5 perguntas) e **Links relacionados**.

## Callouts

> [!tip] Dica
> Use para atalhos e recomendações.

> [!warning] Alerta
> Use para riscos operacionais e limites de escopo.

> [!example] Exemplo
> Use para cenários práticos.

> [!question] Revisão
> Use para as perguntas de autoavaliação.

## Diagramas e código

Fluxos e arquiteturas usam blocos `mermaid`. Todo bloco de código indica a linguagem (`python`, `bash`, `powershell`, `yaml`, `json`).

## Segurança do conteúdo

Somente conteúdo defensivo. Sem malware, exploits ou payloads funcionais. Veja o [[Template de Conceito - Automação]] para o esqueleto padrão.

## Erros comuns

- Esquecer as propriedades ou usar valor de `nivel` fora da lista.
- Criar notas órfãs, sem links de entrada.
- Misturar vários conceitos em uma única nota; prefira notas atômicas.

## Para revisar

> [!question] Autoavaliação
> 1. Quais propriedades são obrigatórias?
> 2. Qual a função de um MOC no grafo?
> 3. Quando um nome de nota deve levar o sufixo do material?
