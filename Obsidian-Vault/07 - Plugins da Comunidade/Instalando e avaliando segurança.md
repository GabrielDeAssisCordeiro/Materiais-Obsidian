---
tags: [plugins-comunidade, seguranca, tutorial]
aliases: [Instalar plugins, Segurança de plugins, Avaliar plugins]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Plugins da comunidade e Restricted Mode]]", "[[Backup]]", "[[Pasta .obsidian]]"]
---

# Instalando e avaliando segurança

## Instalar
1. **Settings → Community plugins** → desative o Restricted Mode ([[Plugins da comunidade e Restricted Mode]]).
2. **Browse** → pesquise → **Install** → **Enable**.
3. Configure na seção do plugin e defina atalhos se necessário ([[Hotkeys]]).
4. Instalação manual: copie a pasta do plugin para `.obsidian/plugins/` ([[Pasta .obsidian]]).

## Avaliar antes de instalar
| Critério | O que olhar |
|---|---|
| Popularidade | downloads e estrelas no repositório |
| Manutenção | último commit e resposta a *issues* |
| Código | aberto, legível, sem ofuscação |
| Licença | clara e permissiva |
| Permissões de rede | o plugin deve declarar uso de rede, telemetria ou anúncios |
| Escopo | faz só o que promete? |
| Plataformas | funciona no mobile ou é só desktop? |

## Boas práticas
- Teste em um **vault de teste** antes do principal.
- Faça [[Backup]] antes de instalar ou atualizar.
- Instale poucos plugins; cada um é código com acesso ao seu vault.
- Leia o changelog antes de atualizar.
- Plugins que executam scripts (ex.: [[Templater]], [[DataviewJS]]) merecem mais atenção.

> [!warning] Sem sandbox
> Plugins não rodam isolados: um plugin malicioso pode ler, alterar ou enviar seus arquivos.

> [!question] Verificar na documentação oficial
> Confirme as diretrizes atuais para desenvolvedores de plugins e o processo de revisão do diretório.

## Veja também
- [[Desempenho]]
- [[Solução de problemas]]

## Exercício
Escolha um plugin, preencha a tabela de critérios para ele e decida se instala.
