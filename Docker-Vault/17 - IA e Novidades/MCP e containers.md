---
tags:
  - docker
  - ia
  - agentes
  - seguranca
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Model Runner]]"
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Ambientes para ML e LLMs]]"
  - "[[Proteção do docker.sock]]"
---

# MCP e containers

O **Model Context Protocol (MCP)** é um protocolo aberto para conectar **aplicações de IA** (assistentes, agentes, IDEs) a **ferramentas e fontes de dados** por meio de *servidores MCP*.

## Por que containers?

Servidores MCP executam código com acesso a arquivos, rede e credenciais. **Containers isolam** esse código:

- Dependências empacotadas (sem "instalar Node/Python" no host).
- **Isolamento** de arquivos e rede; montagens explícitas e somente leitura.
- Execução reprodutível e fácil de remover.

## Executando um servidor MCP em container (stdio)

```bash
# O cliente de IA inicia o container e conversa pela entrada/saída padrão
docker run -i --rm mcp/fetch
```

Configuração típica de um cliente MCP:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/fetch"]
    }
  }
}
```

## Endurecendo o servidor

```json
{
  "mcpServers": {
    "arquivos": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "--read-only", "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges:true",
        "--network", "none",
        "--mount", "type=bind,src=/caminho/projeto,dst=/workspace,readonly",
        "IMAGEM-DO-SERVIDOR-MCP"
      ]
    }
  }
}
```

## Ecossistema Docker

- **Docker MCP Catalog**: catálogo de servidores MCP empacotados como imagens.
- **MCP Toolkit / Gateway** (Docker Desktop): gerencia e expõe servidores MCP a clientes de forma centralizada.

> [!question] Verificar na documentação oficial
> Nomes de imagens (`mcp/...`), comandos da CLI `docker mcp` e recursos do Toolkit/Gateway evoluem rapidamente; consulte a documentação do Docker e confira a procedência de cada servidor.

> [!danger] Servidores MCP são código de terceiros com acesso a seus dados
> Trate-os como qualquer software não confiável: mínimo de privilégios, **sem rede** quando possível, montagens somente leitura e **nunca** monte `docker.sock` ou o diretório `$HOME` inteiro. Veja [[Princípio do menor privilégio - Docker]].

## Exercício

Execute um servidor MCP simples em container com `--network none` e montagem somente leitura, e descreva o que ele **não** consegue fazer por causa do isolamento.

## Veja também

- [[Docker Model Runner]]
- [[Princípio do menor privilégio - Docker]]
- [[Ambientes para ML e LLMs]]
- [[Proteção do docker.sock]]
- [[MOC - IA e Novidades]]
