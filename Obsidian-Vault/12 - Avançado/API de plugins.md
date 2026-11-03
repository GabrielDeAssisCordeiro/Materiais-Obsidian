---
tags: [avancado, plugin, integracao]
aliases: [Plugin API, Criar plugin, Desenvolvimento de plugins]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Instalando e avaliando segurança]]", "[[DataviewJS]]", "[[Pasta .obsidian]]"]
---

# API de plugins

Introdução ao desenvolvimento de plugins para Obsidian, em **TypeScript**.

## Começando
1. Clone o repositório *sample plugin* oficial.
2. Instale dependências (`npm install`) e rode o build (`npm run dev`).
3. Copie ou linke a pasta para `.obsidian/plugins/meu-plugin/` ([[Pasta .obsidian]]).
4. Ative em *Community plugins* ([[Plugins da comunidade e Restricted Mode]]).

## Arquivos essenciais
- `manifest.json`: id, nome, versão, versão mínima do app.
- `main.ts` → `main.js`: o código.
- `styles.css`: estilos opcionais.

## Exemplo mínimo
```typescript
import { Plugin, Notice } from "obsidian";

export default class MeuPlugin extends Plugin {
  async onload() {
    this.addCommand({
      id: "ola",
      name: "Dizer olá",
      callback: () => new Notice("Olá, Obsidian!"),
    });
  }
}
```

## Conceitos
`Plugin`, `Vault`, `Workspace`, `MetadataCache`, `Modal`, `PluginSettingTab`.

> [!question] Verificar na documentação oficial
> Confirme a API atual em docs.obsidian.md (Developer docs) e as regras de submissão ao diretório.

> [!warning] Segurança
> Declare uso de rede e evite coletar dados sem aviso ([[Instalando e avaliando segurança]]).

## Veja também
- [[CLI e automação]]
- [[DataviewJS]]

## Exercício
Crie o plugin mínimo acima em um vault de teste e rode o comando.
