---
titulo: "Crescimento da comunidade e ritmo de releases"
tags:
  - openclaw
  - conceito
  - historia
tipo: conceito
aliases: ['Comunidade', 'Versionamento por calendário']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
  - "https://www.morphllm.com/clawdbot"
  - "https://horadecodar.com.br/openclaw-github/"
  - "https://www.heyuan110.com/posts/ai/2026-01-31-openclaw-claude-code-workflow/"
relacionados:
  - "[[Linha do tempo Clawdbot, Moltbot e OpenClaw]]"
  - "[[Licença MIT e OpenClaw Foundation]]"
  - "[[ClawHub, plugins e o ecossistema]]"
  - "[[O que é o OpenClaw]]"
---

# Crescimento da comunidade e ritmo de releases

## Objetivo

Entender como medir o crescimento do projeto sem se apoiar em números de memória, e como ler o versionamento por calendário.

## Explicação

**Crescimento.** Fontes de terceiros relatam um crescimento explosivo: um blog fala em 60 mil estrelas no GitHub em 72 horas e depois em mais de 100 mil; outros textos citam 147 mil ou mais de 250 mil. Os números variam porque foram coletados em datas diferentes e nenhum deles é oficial. Para um valor atual, abra a página do repositório `openclaw/openclaw`.

> [!tip] Como citar métricas
> Registre sempre a data e a fonte ("cerca de X estrelas em tal data, segundo tal blog") e prefira a página do GitHub como fonte primária.

**Onde a comunidade se reúne.** O rodapé da documentação lista Discord, Reddit (r/openclaw), um fórum de comunidade, X, YouTube e outras redes. O fórum de comunidade é o canal indicado para suporte oficial. A documentação existe em vários idiomas, inclusive português do Brasil.

**Versionamento por calendário.** As versões seguem o formato `AAAA.M.N`. A documentação lista, por exemplo, `v2026.6.11`, `v2026.7.1`, `v2026.8.1` (descrita como "OpenClaw 2.0"), várias versões `2026.9.x` e `2026.10.x`. Isso significa três coisas práticas:

1. O número diz **quando**, não a "gravidade" da mudança.
2. Há releases frequentes; consulte as notas de cada versão antes de atualizar.
3. Há canais de release (stable e desenvolvimento), explicados em [[MOC - Operação e Manutenção|Operação e Manutenção]].

**Como o projeto é desenvolvido.** Uma análise de terceiros sobre o fluxo de trabalho de Steinberger destaca documentação versionada junto do código (pasta `docs/` com dezenas de subpastas) e arquivos de orientação para agentes na raiz do repositório, como o `AGENTS.md`.

## Exemplo prático

Para ver a versão instalada e a última disponível, a documentação indica a página de releases e os comandos de atualização. Antes de qualquer atualização, faça um backup do diretório de estado:

```bash
openclaw update
```

> [!warning] Confirme o procedimento
> O comando acima aparece na referência da CLI (`openclaw update`), mas as opções variam por versão e canal. Leia `docs.openclaw.ai/install/updating` antes de rodar em produção; o procedimento completo é tratado na pasta de operação.

## Armadilhas comuns

- Comparar números de estrelas de fontes com datas diferentes.
- Atualizar sem ler as notas de versão, principalmente quando há mudanças de armazenamento.
- Esquecer que um guia pode descrever uma versão de meses atrás.

## Resumo

- Números de estrelas são de terceiros e voláteis; cite com data.
- Versões seguem calendário (`2026.10.x`).
- Há releases frequentes e notas por versão.
- Comunidade: Discord, Reddit, fórum, GitHub.

## Relacionados

- [[Linha do tempo Clawdbot, Moltbot e OpenClaw]]
- [[Licença MIT e OpenClaw Foundation]]
- [[ClawHub, plugins e o ecossistema]]
- [[O que é o OpenClaw]]

## Exercícios

1. Por que números de estrelas citados em blogs diferem entre si?
2. O que significa a versão `v2026.10.7`?
3. Onde você encontra o canal oficial de suporte?
4. Que cuidado tomar antes de atualizar?
