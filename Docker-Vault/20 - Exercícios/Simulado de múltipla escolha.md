---
tags:
  - docker
  - exercicios
aliases: []
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Glossário#Docker]]"
  - "[[Flashcards de Docker]]"
  - "[[Livros, cursos e certificações]]"
---

# Simulado de múltipla escolha

Vinte questões no estilo de provas de certificação. Responda e confira o gabarito no final.

1. Qual instrução do Dockerfile **não** publica portas?
   A) `EXPOSE`  B) `docker run -p`  C) `docker run -P`  D) `ports:` no Compose

2. Qual driver de rede permite comunicação entre containers em hosts diferentes?
   A) bridge  B) host  C) overlay  D) none

3. O que acontece com os dados gravados na camada gravável ao remover o container?
   A) Vão para um volume anônimo  B) São apagados  C) Vão para a imagem  D) Ficam em `/var/lib/docker/volumes`

4. Qual é a forma exec correta?
   A) `CMD python app.py`  B) `CMD ['python','app.py']`  C) `CMD ["python","app.py"]`  D) `CMD [python, app.py]`

5. Qual opção reinicia o container sempre, **exceto** se foi parado manualmente?
   A) `no`  B) `always`  C) `on-failure`  D) `unless-stopped`

6. Qual comando remove containers parados, redes sem uso e imagens dangling?
   A) `docker rm -a`  B) `docker system prune`  C) `docker volume prune`  D) `docker image rm`

7. Qual recurso do kernel limita o uso de memória de um container?
   A) namespaces  B) seccomp  C) cgroups  D) AppArmor

8. Em Compose, como esperar um banco ficar **saudável**?
   A) `depends_on: [db]`  B) `depends_on` com `condition: service_healthy`  C) `links`  D) `wait: db`

9. Qual a melhor forma de passar um segredo para o build sem vazá-lo na imagem?
   A) `ARG`  B) `ENV`  C) `RUN --mount=type=secret`  D) `COPY`

10. Qual é a diferença principal entre `CMD` e `ENTRYPOINT`?
    A) Nenhuma  B) `CMD` é o padrão substituível; `ENTRYPOINT` é o executável fixo  C) `ENTRYPOINT` só roda no build  D) `CMD` é obrigatório

11. Um container termina com código 137 e `OOMKilled=true`. Qual a causa?
    A) Erro de sintaxe  B) Falta de memória  C) Porta ocupada  D) Imagem corrompida

12. Qual tipo de montagem é apropriado para persistir dados de um banco em produção?
    A) tmpfs  B) bind mount de `/tmp`  C) volume nomeado  D) camada gravável

13. O que faz `docker compose down -v`?
    A) Só para os containers  B) Remove containers, redes e **volumes** nomeados do projeto  C) Remove imagens  D) Lista volumes

14. Qual componente é o runtime de baixo nível que segue a OCI Runtime Spec?
    A) dockerd  B) containerd  C) runc  D) Buildx

15. Qual a vantagem de um multi-stage build?
    A) Build mais lento  B) Imagem final menor e sem ferramentas de build  C) Usa mais camadas  D) Permite rodar como root

16. Por que o `ufw` pode não bloquear uma porta publicada pelo Docker?
    A) O Docker desativa o ufw  B) O Docker insere regras de iptables que são avaliadas antes  C) O ufw não suporta TCP  D) Containers usam UDP

17. Qual comando mostra os eventos do daemon em tempo real?
    A) `docker logs`  B) `docker events`  C) `docker stats`  D) `docker top`

18. No Swarm, qual objeto representa **um container** agendado por um serviço?
    A) Node  B) Stack  C) Task  D) Config

19. Qual a forma recomendada de referenciar uma imagem de forma **imutável**?
    A) `imagem:latest`  B) `imagem:1`  C) `imagem@sha256:...`  D) `imagem:stable`

20. Qual prática reduz o impacto de um escape de container?
    A) `--privileged`  B) Montar `docker.sock`  C) Usuário não-root, `cap-drop ALL`, seccomp e rootless  D) `--pid=host`

## Gabarito

| Questão | Resposta | Explicação |
|---|---|---|
| 1 | A | `EXPOSE` apenas documenta |
| 2 | C | `overlay` conecta hosts (Swarm) |
| 3 | B | A camada gravável é descartada com o container |
| 4 | C | JSON com aspas duplas |
| 5 | D | `unless-stopped` respeita a parada manual |
| 6 | B | `docker system prune` |
| 7 | C | cgroups limitam recursos |
| 8 | B | `condition: service_healthy` |
| 9 | C | Secret mount não grava na imagem |
| 10 | B | Padrão substituível vs executável fixo |
| 11 | B | 137 = SIGKILL; OOM kill |
| 12 | C | Volume nomeado |
| 13 | B | `-v` remove volumes nomeados |
| 14 | C | runc |
| 15 | B | Imagem final enxuta |
| 16 | B | Regras do Docker entram antes |
| 17 | B | `docker events` |
| 18 | C | Task |
| 19 | C | Digest é imutável |
| 20 | C | Defesa em camadas |

> [!tip] Pontuação
> 18–20: excelente · 14–17: bom, revise os erros · abaixo de 14: revise as pastas indicadas nas notas relacionadas.

## Veja também

- [[Glossário#Docker]]
- [[Flashcards de Docker]]
- [[Livros, cursos e certificações]]
- [[MOC - Exercícios - Docker]]
