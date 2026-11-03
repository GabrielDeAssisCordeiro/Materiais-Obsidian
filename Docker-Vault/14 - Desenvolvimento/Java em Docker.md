---
tags:
  - docker
  - desenvolvimento
  - dockerfile
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Multi-stage builds]]"
  - "[[Cache mounts]]"
  - "[[Limites de recursos - Docker]]"
  - "[[Go em Docker]]"
---

# Java em Docker

Exemplo para **Spring Boot** com Maven.

```dockerfile
# syntax=docker/dockerfile:1

# ---------- Build ----------
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN --mount=type=cache,target=/root/.m2 mvn -q -B dependency:go-offline
COPY src ./src
RUN --mount=type=cache,target=/root/.m2 mvn -q -B -DskipTests package \
 && cp target/*.jar /app/app.jar

# ---------- Produção ----------
FROM eclipse-temurin:21-jre AS prod
WORKDIR /app
RUN useradd --system --uid 10001 --no-create-home app
COPY --from=build /app/app.jar app.jar
USER 10001
EXPOSE 8080
# A JVM respeita limites de cgroup; defina a fração de memória usada pelo heap
ENTRYPOINT ["java", "-XX:MaxRAMPercentage=75.0", "-jar", "/app/app.jar"]
```

## Desenvolvimento

```yaml
services:
  api:
    image: maven:3.9-eclipse-temurin-21
    working_dir: /app
    command: mvn -B spring-boot:run
    ports:
      - "8080:8080"
    volumes:
      - ./:/app
      - m2_cache:/root/.m2
volumes:
  m2_cache:
```

> [!tip] Boas práticas Java
> - Use `-XX:MaxRAMPercentage` (e não `-Xmx` fixo) para acompanhar o limite do container.
> - Considere **layered jars** do Spring Boot (`java -Djarmode=layertools`) para melhor cache, ou **Jib/Buildpacks** para gerar imagens sem Dockerfile.
> - `eclipse-temurin:21-jre` é menor que a imagem com JDK completo.
> - Defina limites de memória e CPU (veja [[Limites de recursos - Docker]]).

> [!bug] Falta de memória na inicialização
> A JVM pode consumir mais que o esperado (metaspace, threads, buffers). Deixe margem entre o heap e o limite do container.

> [!question] Verificar na documentação oficial
> As tags `maven:3.9-eclipse-temurin-21` e `eclipse-temurin:21-jre` devem ser conferidas no Docker Hub; versões LTS mais novas do Java podem estar disponíveis.

## Exercício

Containerize uma aplicação Spring Boot mínima com o Dockerfile acima e meça o tempo do segundo build após alterar apenas um arquivo em `src/`.

## Veja também

- [[Multi-stage builds]]
- [[Cache mounts]]
- [[Limites de recursos - Docker]]
- [[Go em Docker]]
- [[MOC - Desenvolvimento]]
