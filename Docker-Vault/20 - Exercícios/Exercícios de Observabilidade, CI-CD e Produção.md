---
tags:
  - docker
  - exercicios
  - observabilidade
  - cicd
  - producao
aliases: []
tipo: exercicio
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Fluxo de diagnóstico de problemas]]"
  - "[[Análise de OOM kill]]"
  - "[[Pipeline CI-CD com Docker]]"
  - "[[Estratégias de rollout]]"
  - "[[Checklist de produção]]"
---

# Exercícios de Observabilidade, CI-CD e Produção

## Questões

1. Um container está em `Restarting (1)`. Liste, em ordem, os quatro primeiros comandos que você executa.
2. Como confirmar que um container morreu por falta de memória?
3. A aplicação escuta em `127.0.0.1:3000` e você publicou `-p 3000:3000`. Por que não funciona e como corrigir?
4. Quais as vantagens de logs em **stdout/stderr** e **JSON**?
5. Quais métricas e alertas mínimos você configuraria para um serviço em produção?
6. Cite quatro etapas de um pipeline CI/CD com Docker e uma ferramenta para cada.
7. Por que "construir uma vez, promover" é uma boa prática?
8. Compare **rolling**, **blue-green** e **canary** (uma frase cada).
9. Por que backups precisam ser testados e qual regra de cópias você segue?
10. Dê cinco itens do seu **checklist de produção**.

## Gabarito

1. `docker ps -a`; `docker logs --tail 100 NOME`; `docker inspect -f 'exit={{.State.ExitCode}} oom={{.State.OOMKilled}}' NOME`; `docker update --restart=no NOME && docker run -it --rm --entrypoint sh IMAGEM` (para investigar).
2. `docker inspect -f '{{.State.OOMKilled}}' NOME` (true), `docker events --filter event=oom`, `dmesg -T | grep -i 'out of memory'`.
3. Dentro do container, `127.0.0.1` só é acessível por ele mesmo; a aplicação precisa escutar em **`0.0.0.0`**.
4. Os coletores e o `docker logs` já leem os fluxos padrão; JSON facilita busca, métricas e correlação; evita encher a camada gravável com arquivos.
5. Disponibilidade externa, CPU/memória/disco, reinícios, taxa de erros e latência; alertas para serviço fora do ar, reinícios repetidos, OOM, disco > 80%, 5xx altos.
6. Testes (Docker/Compose), build (Buildx), varredura (Trivy/Scout), push (GHCR/ECR), deploy (SSH/Compose, Argo CD, ECS).
7. Garante que o artefato testado é **o mesmo** que vai à produção (mesmo digest), reduzindo diferenças entre ambientes.
8. **Rolling**: troca réplicas aos poucos; **blue-green**: dois ambientes e troca de tráfego de uma vez; **canary**: pequena fração do tráfego vai à nova versão antes de ampliar.
9. Porque só uma restauração bem-sucedida comprova o backup; regra **3-2-1** (3 cópias, 2 mídias, 1 fora do local).
10. Exemplos: tag fixa/digest, usuário não-root, limites de recursos, healthcheck, logs rotacionados, secrets, TLS, backups testados, monitoramento e alertas.

## Veja também

- [[Fluxo de diagnóstico de problemas]]
- [[Análise de OOM kill]]
- [[Pipeline CI-CD com Docker]]
- [[Estratégias de rollout]]
- [[Checklist de produção]]
- [[MOC - Exercícios - Docker]]
