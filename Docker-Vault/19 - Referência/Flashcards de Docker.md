---
tags:
  - docker
  - referencia
  - flashcards
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Glossário#Docker]]"
  - "[[Cheat sheet de comandos Docker]]"
  - "[[FAQ Docker]]"
---

# Flashcards de Docker

Cartões no formato `pergunta::resposta` (compatível com plugins de repetição espaçada, como o Spaced Repetition; nenhum plugin vem pré-instalado). Tente responder antes de ler.

#flashcards/docker

## Fundamentos

O que é uma imagem Docker?::Modelo imutável, formado por camadas somente leitura e metadados, usado para criar containers.
O que é um container?::Processo isolado (namespaces e cgroups) executado a partir de uma imagem, com uma camada gravável.
Containers compartilham qual recurso com o host?::O kernel.
Qual recurso do kernel isola processos, rede e sistema de arquivos?::Namespaces.
Qual recurso do kernel limita CPU e memória?::cgroups.
Qual o driver de armazenamento padrão no Linux?::overlay2 (OverlayFS).
O que é OCI?::Open Container Initiative: especificações de runtime, imagem e distribuição.
Qual a função do runc?::Runtime de baixo nível que cria o container conforme a OCI Runtime Spec.
Qual a função do containerd?::Runtime de alto nível que gerencia o ciclo de vida de containers e imagens.

## Containers

Qual comando lista todos os containers, inclusive parados?::docker ps -a
O que faz docker run --rm?::Remove o container automaticamente quando ele termina.
Qual a diferença entre docker exec e docker attach?::exec cria um novo processo no container; attach conecta ao processo principal (PID 1).
Código de saída 137 indica o quê?::SIGKILL, frequentemente OOM kill (verifique OOMKilled no inspect).
O que EXPOSE faz?::Apenas documenta a porta; não a publica.
Como publicar a porta 80 do container na 8080 do host somente em loopback?::-p 127.0.0.1:8080:80
Qual política de restart não reinicia se o container foi parado manualmente?::unless-stopped
Por que docker stop pode demorar 10 segundos?::A aplicação não trata SIGTERM (comum com CMD em forma shell), e o Docker aplica SIGKILL após o timeout.

## Imagens e Dockerfile

Qual a diferença entre tag e digest?::Tag é um rótulo mutável; digest é o hash imutável do conteúdo.
Por que evitar a tag latest em produção?::Ela muda ao longo do tempo e torna o deploy irreproduzível.
COPY ou ADD: qual preferir?::COPY, por ser mais previsível.
Qual a diferença entre CMD e ENTRYPOINT?::CMD é o comando padrão (substituível); ENTRYPOINT é o executável fixo, ao qual argumentos são anexados.
ARG ou ENV: qual existe em tempo de execução?::ENV.
Para que serve um multi-stage build?::Construir em um estágio com ferramentas e copiar só o resultado para uma imagem final menor e mais segura.
Por que copiar package.json antes do restante do código?::Para aproveitar o cache de camadas das dependências.
O que o .dockerignore faz?::Exclui arquivos do contexto de build, acelerando o build e evitando vazamentos.
Qual a forma exec de CMD?::CMD ["executavel", "arg1"] (JSON com aspas duplas).
Como passar um segredo ao build sem gravá-lo na imagem?::RUN --mount=type=secret.

## Volumes e redes

Qual a diferença entre volume e bind mount?::Volume é gerenciado pelo Docker; bind mount liga um caminho do host.
Qual tipo de montagem fica só na memória?::tmpfs.
A bridge padrão resolve nomes de containers?::Não; redes definidas pelo usuário resolvem.
Como containers na mesma rede se encontram?::Pelo nome do container ou serviço, via DNS interno.
Qual driver de rede conecta containers em vários hosts?::overlay.
Qual endereço o container usa para falar com o host (Docker Desktop)?::host.docker.internal
Por que o ufw não bloqueia portas publicadas?::O Docker insere regras de iptables antes das do ufw.

## Compose

Qual comando sobe a stack em segundo plano?::docker compose up -d
O que docker compose down -v faz de arriscado?::Remove também os volumes nomeados (apaga dados).
Qual campo obsoleto não deve mais ser usado no compose.yaml?::version
Como esperar o banco ficar pronto antes da API?::depends_on com condition: service_healthy e um healthcheck no banco.
O que são profiles no Compose?::Mecanismo para ativar serviços opcionais sob demanda.
Qual comando valida e mostra o compose final?::docker compose config

## Segurança e produção

Qual o princípio básico de segurança em containers?::Menor privilégio.
Por que montar docker.sock em um container é perigoso?::Dá controle total do daemon e, na prática, acesso root ao host.
O que faz --cap-drop ALL?::Remove todas as capabilities do container.
O que faz --read-only?::Monta o sistema de arquivos raiz como somente leitura.
O que é rootless mode?::Daemon e containers executando sem privilégios de root no host.
Para que serve um SBOM?::Listar os componentes de uma imagem para auditoria e resposta a vulnerabilidades.
Qual regra de backup é recomendada?::3-2-1: três cópias, em duas mídias, uma fora do local.
Qual a diferença entre rolling update e blue-green?::Rolling troca réplicas aos poucos; blue-green mantém dois ambientes e muda o tráfego de uma vez.

## Veja também

- [[Glossário#Docker]]
- [[Cheat sheet de comandos Docker]]
- [[FAQ Docker]]
- [[MOC - Referência - Docker]]
