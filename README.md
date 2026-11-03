# Guia dos Materiais

> [!abstract] Como usar
> Este vault reúne materiais de estudo independentes, cada um na sua pasta e com índice próprio. Comece pelo índice do assunto que quiser e consulte o [[Glossário]] sempre que um termo não estiver claro.

> [!warning] IMPORTANTE
> Abra a pasta **`Materiais-Obsidian`** inteira como vault. Os links entre notas e os canvases dependem dela como raiz; abrir uma subpasta sozinha deixa links e canvases sem funcionar.

## Materiais

| Material | Pasta | O que cobre | Comece por |
|---|---|---|---|
| Assembly | `Assembly Vault/` | Curso de Assembly do zero ao avançado: x86-64 (NASM e MASM), ARM/AArch64, SIMD e laboratórios | [[00 - Índice\|Índice do Assembly]] |
| Python | `Python-Vault/` | Python do zero ao avançado, com exercícios e projetos práticos | [[00 - Índice Python\|Índice do Python]] |
| Rust | `Rust-Vault/` | Rust do zero ao avançado (edição 2024): ownership, traits, concorrência, async, unsafe, projetos guiados, exercícios e flashcards | [[Home - Rust]] · [[Índice geral - Rust]] |
| C++ | `Cpp-Vault/` | C++ moderno (C++11 a C++23, com notas sobre C++26): linguagem, memória e RAII, templates e concepts, STL e ranges, concorrência, build, testes e projetos | [[Home - Cpp]] · [[Índice Geral - Cpp]] |
| Docker | `Docker-Vault/` | Docker do zero à produção: containers, imagens, Dockerfile, Compose, redes, volumes, segurança, Swarm, observabilidade, CI/CD e IA, com projetos guiados | [[Home - Docker]] · [[Índice geral - Docker]] |
| Obsidian | `Obsidian-Vault/` | Curso completo de Obsidian: Markdown, links, plugins, sincronização e fluxos de trabalho | [[Home - Obsidian]] · [[Índice geral - Obsidian]] |
| Sandboxes | `Sandbox-Vault/` | Ambientes sandbox: conceitos, tipos, ferramentas, análise de malware e uso com IA | [[Home - Sandbox]] · [[Índice Geral - Sandbox]] |
| Sistemas Operacionais | `Sistemas-Operacionais-Vault/` | Sistemas operacionais do básico ao avançado: processos, escalonamento, sincronização, memória, arquivos, E/S, boot, segurança, virtualização, SOs reais e ferramentas de Linux, Windows e macOS | [[Índice Geral - SO]] · [[Mapa de Estudos]] |
| Segurança de IA | `Jailbreaking-Vault/` | Jailbreaking, prompt injection, red teaming e defesas para LLMs, com laboratórios simulados | [[00 - Índice Jailbreaking\|Índice de Segurança de IA]] |
| Cibersegurança | `Ciberseguranca-Vault/` | Arsenal de cibersegurança: catálogo de ferramentas, conceitos e padrões de ofensivo, defensivo, DFIR, engenharia reversa, criptografia, OSINT e cloud | [[MOC - Arsenal de Cibersegurança]] |
| Segurança e Integração | `Seguranca-Integracao-Vault/` | Desenvolvimento e integração de ferramentas de segurança: arquitetura, APIs, SIEM e scanners, DevSecOps, SOAR, detecção como código e segurança da própria ferramenta, com projetos | [[Home - Integração]] · [[Como usar este vault - Integração]] |
| Automação de Segurança | `Automacao-Seguranca-Vault/` | Automação defensiva de segurança: SOC e resposta a incidentes, vulnerabilidades e compliance, DevSecOps, threat intel, laboratórios com scripts, IA e governança | [[Home - Automação]] · [[Convenções - Automação]] |

## Recursos compartilhados

| Recurso | Pasta | Para que serve |
|---|---|---|
| [[Glossário]] | raiz | Termos de todos os materiais, por assunto e tópico |
| [[MOC - Templates]] | `Templates/` | Templates de nota de todos os materiais |
| [[MOC - Anexos]] | `Anexos/` | Canvases e bases |

## Convenções

| Tema | Regra |
|---|---|
| Propriedades | `titulo`, `nivel`, `criado`, `tipo`, `tags`, `aliases` e `relacionados`; nomes em português, minúsculos e sem acento |
| `nivel` | `iniciante`, `intermediario`, `avancado` ou `todos` |
| `criado` | Data no formato `AAAA-MM-DD` |
| Nome da nota | Único em todo o vault. Se o nome se repetir entre materiais, acrescente ` - <Material>` (ex.: `Home - Obsidian`) |
| Título | Um só H1 por nota, igual ao `titulo` (sem o emoji, se houver) |
| Aliases | Um alias por conceito; não repita o mesmo alias em outra nota |
| Tags | Temas amplos, em minúsculas e sem acento; prefira uma tag de tema a uma tag de uso único |
| Links | Nome curto quando for único; caminho completo a partir da raiz quando houver ambiguidade |
| Glossário | Termo novo entra no assunto e no tópico certos do [[Glossário]] |
| Arquivos | Templates em `Templates/` e anexos em `Anexos/`, na raiz |

## Como adicionar um novo material

1. Crie a pasta `Nome-Vault/` na raiz, com subpastas numeradas (`00 - Início`, `01 - …`).
2. Crie o índice em `00 - …/`, com nome único (por exemplo, `00 - Índice <Assunto>`) e as propriedades padrão.
3. Acrescente uma linha na tabela **Materiais** acima.
4. No grafo, crie um grupo de cor com a consulta `path:"Nome-Vault/"`.
5. No [[Glossário]], crie uma seção `## Assunto` e os tópicos `###` com os termos do material.
6. Coloque templates novos em `Templates/` e anexos em `Anexos/`, e liste-os em [[MOC - Templates]] e [[MOC - Anexos]].
7. Confira: nomes de nota únicos, aliases sem repetição e nenhum link em **Links não resolvidos**.
