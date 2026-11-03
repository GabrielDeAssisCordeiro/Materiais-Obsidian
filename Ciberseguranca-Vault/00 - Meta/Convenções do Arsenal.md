---
titulo: "Convenções do Arsenal"
tipo: guia
categoria: "Meta"
tags:
  - ciberseguranca
  - guia
---
# Convenções do Arsenal

Catálogo de ferramentas, conceitos e padrões de cibersegurança, organizado por área. O conteúdo é de referência para estudo, defesa e testes **autorizados** (pentest com escopo definido, laboratórios e CTFs).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `00 - Meta` | Convenções, fluxo típico de pentest e referência cruzada com a matriz ATT&CK |
| `01 - MOCs` | MOCs das grandes áreas (Ofensivo, Defensivo, DFIR e Engenharia Reversa) |
| `02` a `09` | Ferramentas por área, em subpastas numeradas por categoria, cada uma com um `MOC - <Categoria>` |
| `10 - Fundamentos` | Conceitos, padrões e frameworks, cheatsheets |

O ponto de partida é o [[MOC - Arsenal de Cibersegurança]].

## Notas de ferramenta

Cada ferramenta segue o mesmo roteiro: resumo em uma frase, **Como funciona**, **Como usar**, **Casos de uso**, **Alternativas**, **Categoria** (link para o MOC) e **Link oficial**.

## Propriedades

| Propriedade | Valores |
|---|---|
| `titulo`, `nome` | Nome da ferramenta ou do tópico |
| `tipo` | `ferramenta`, `conceito`, `padrao`, `cheatsheet`, `moc`, `referencia` ou `guia` |
| `categoria`, `subcategoria` | Área e tipo de uso |
| `plataformas`, `licenca`, `linguagem` | Dados técnicos da ferramenta |
| `mitre_attack` | Técnicas ATT&CK associadas (por exemplo `T1071`) |
| `nivel` | `iniciante`, `intermediario` ou `avancado` |
| `situacao` | `ativo` ou `legado` |
| `link_oficial` | Página oficial |

## Tags

Toda nota leva `ciberseguranca` e a tag do seu `tipo`. As notas de ferramenta também levam uma tag hierárquica da categoria, como `ofensivo/exploracao`, `defensivo/siem`, `dfir/memoria` ou `reversa/debugger`.

## Veja também

- [[README]]
- [[Glossário#Cibersegurança (Arsenal)]]
