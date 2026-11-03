---
tags:
  - docker
  - moc
aliases:
  - Dockerfile
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Dockerfile

Todas as instruções do Dockerfile, cache de camadas, `.dockerignore`, multi-stage, heredocs e a diretiva de sintaxe, com boas práticas consolidadas.

> [!tip] Sugestão de leitura
> [[Introdução ao Dockerfile]] → [[Instrução RUN]] → [[Instruções COPY e ADD]] → [[Instruções CMD e ENTRYPOINT]] → [[Cache de camadas e ordem das instruções]] → [[Multi-stage builds]] → [[Boas práticas de Dockerfile]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Introdução ao Dockerfile]] — Primeiro Dockerfile completo e visão geral das instruções
- [[Instrução FROM]] — Imagem base, estágios e ARG antes do FROM
- [[Instrução RUN]] — Comandos de build, agrupamento e limpeza
- [[Instruções COPY e ADD]] — Copiar arquivos; diferenças entre COPY e ADD
- [[Instruções CMD e ENTRYPOINT]] — Diferenças, combinações e boas práticas
- [[Forma shell vs forma exec]] — Sintaxes, PID 1 e sinais
- [[Instruções ENV e ARG]] — ENV vs ARG e segurança
- [[Instruções WORKDIR e USER]] — Diretório de trabalho e usuário não-root
- [[Instruções EXPOSE e VOLUME]] — Documentar portas e declarar volumes
- [[Instrução HEALTHCHECK]] — Healthcheck embutido na imagem
- [[Instruções LABEL, SHELL, STOPSIGNAL e ONBUILD]] — Metadados, shell, sinal de parada e gatilhos
- [[Arquivo .dockerignore]] — Reduzir o contexto e evitar vazamentos
- [[Cache de camadas e ordem das instruções]] — Estratégia de ordenação para aproveitar o cache
- [[Multi-stage builds]] — Estágios de build e execução (diagrama)
- [[Heredocs no Dockerfile]] — Scripts e arquivos inline com <<EOF
- [[Sintaxe do Dockerfile e syntax directive]] — # syntax= e diretivas de parser
- [[Boas práticas de Dockerfile]] — Checklist e exemplo consolidado

## Veja também

- [[Home - Docker]]
