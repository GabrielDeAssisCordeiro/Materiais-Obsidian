---
titulo: "Nomes antigos, domínios falsos e como verificar a fonte"
tags:
  - openclaw
  - conceito
  - historia
tipo: conceito
aliases: ['Typosquatting']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://www.morphllm.com/clawdbot"
  - "https://docs.openclaw.ai/"
  - "https://horadecodar.com.br/openclaw-github/"
  - "https://pr.capitalpress.com/article/The-Final-Evolution-Viral-Sensation-Clawdbot-Completes-Its-Journey-from-Moltbot-to-OpenClaw/697dbd36ca2cd60002adabd0"
relacionados:
  - "[[Linha do tempo Clawdbot, Moltbot e OpenClaw]]"
  - "[[ClawHub, plugins e o ecossistema]]"
  - "[[Licença MIT e OpenClaw Foundation]]"
  - "[[Tour rápido de instalação e primeira conversa]]"
---

# Nomes antigos, domínios falsos e como verificar a fonte

## Objetivo

Aprender a distinguir fontes oficiais de imitações, um risco real em projetos que mudaram de nome e viralizaram.

## Explicação

Quando um projeto muda de nome duas vezes em poucos dias, sobram nomes antigos, domínios abandonados e pacotes parecidos. Relatos de terceiros dizem que, logo após a renomeação para Moltbot, surgiram domínios imitadores e que houve até uma tomada de contas de redes sociais durante a troca de nomes. Um desses relatos recomenda tratar como suspeito qualquer download, repositório ou pacote npm com os nomes antigos. Isso é de terceiros, mas a postura (desconfiar até verificar) é a correta.

**Endereços que a documentação oficial usa:**

| Item | Endereço |
|---|---|
| Site e script de instalação | `openclaw.ai` |
| Documentação | `docs.openclaw.ai` |
| Código | `github.com/openclaw/openclaw` |
| Fundação | `openclaw.org` |
| Pacote npm | `openclaw` |

> [!warning] Domínios que não constam como oficiais
> Um comunicado de imprensa pago, de janeiro de 2026, afirma que o projeto migrou para `openclaw.my`. Isso não aparece na documentação oficial, que usa `openclaw.ai`. Sem confirmação nas fontes oficiais, trate esse domínio como não oficial.

**Checklist de verificação (defesa):**

1. Chegue ao site pelo repositório oficial ou pela documentação, não por anúncios ou buscas.
2. Confira o domínio letra por letra antes de rodar qualquer instalador.
3. Em npm, confira o nome do pacote, o publicador e o histórico de versões.
4. Prefira instalar a partir de uma versão marcada e leia o conteúdo do script antes de executar.
5. Desconfie de "versões" com nomes antigos (clawdbot, moltbot) ou de apps de terceiros que prometem "rodar o OpenClaw" sem origem verificável.

## Exemplo prático

Baixar o instalador, ler e só depois executar:

```bash
curl -fsSL https://openclaw.ai/install.sh -o install.sh
less install.sh
bash install.sh
```

Esse é o mesmo script do comando oficial `curl -fsSL https://openclaw.ai/install.sh | bash`, com uma pausa para revisão. Faça isso em uma VM ou container de teste na primeira vez.

## Armadilhas comuns

- Seguir o primeiro resultado de busca que "parece oficial".
- Instalar extensões de navegador ou apps móveis que usam o nome sem vínculo com o projeto.
- Confiar em um domínio só porque ele tem HTTPS: o cadeado não prova identidade do dono.

## Resumo

- Nomes antigos e domínios parecidos são vetores de fraude.
- Fontes oficiais: `openclaw.ai`, `docs.openclaw.ai`, `github.com/openclaw/openclaw`.
- Baixe, leia e só então execute scripts.
- Domínios fora da documentação oficial são suspeitos até prova em contrário.

## Relacionados

- [[Linha do tempo Clawdbot, Moltbot e OpenClaw]]
- [[ClawHub, plugins e o ecossistema]]
- [[Tour rápido de instalação e primeira conversa]]
- [[MOC - Ameaças e Riscos|Ameaças e Riscos]]

## Exercícios

1. Por que mudanças de nome aumentam o risco de fraude?
2. Quais são os endereços oficiais citados na documentação?
3. Que verificações fazer antes de executar um instalador por pipe?
4. Um HTTPS válido garante que o site é oficial? Explique.
