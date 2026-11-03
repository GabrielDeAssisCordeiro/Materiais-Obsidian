---
tags:
  - docker
  - desenvolvimento
  - dockerfile
  - multi-stage
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Multi-stage builds]]"
  - "[[Hot reload em containers]]"
  - "[[Instruções WORKDIR e USER]]"
  - "[[PHP em Docker]]"
---

# ASP.NET Core em Docker

Imagens oficiais da Microsoft: `sdk` (build) e `aspnet` (execução). A partir do .NET 8, as imagens de runtime escutam na porta **8080** e incluem um usuário não-root `app`.

```dockerfile
# syntax=docker/dockerfile:1

# ---------- Build ----------
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY *.csproj ./
RUN --mount=type=cache,target=/root/.nuget/packages dotnet restore
COPY . .
RUN --mount=type=cache,target=/root/.nuget/packages \
    dotnet publish -c Release -o /out --no-restore

# ---------- Produção ----------
FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS prod
WORKDIR /app
COPY --from=build /out .
USER $APP_UID
EXPOSE 8080
ENTRYPOINT ["dotnet", "MeuApp.dll"]
```

> [!info] Nome da DLL
> Troque `MeuApp.dll` pelo nome do assembly do seu projeto (nome do `.csproj`).

## Desenvolvimento

```yaml
services:
  api:
    image: mcr.microsoft.com/dotnet/sdk:10.0
    working_dir: /src
    command: dotnet watch run --urls http://0.0.0.0:8080
    ports:
      - "8080:8080"
    volumes:
      - ./:/src
```

> [!tip] Boas práticas .NET
> - Mantenha `COPY *.csproj` e `dotnet restore` antes do código para aproveitar o cache.
> - Use `--no-restore` no publish; considere imagens `-alpine` ou *chiseled* (Ubuntu mínimo) para reduzir superfície.
> - Defina `ASPNETCORE_URLS` apenas se precisar mudar a porta padrão.

> [!question] Verificar na documentação oficial
> Use a versão do .NET **suportada** no momento (LTS atual); ajuste as tags `10.0` conforme o seu projeto e consulte o Docker Hub e a documentação da Microsoft.

## Exercício

Crie uma Web API mínima (`dotnet new webapi`) e containerize com o Dockerfile acima, confirmando a execução como usuário não-root.

## Veja também

- [[Multi-stage builds]]
- [[Hot reload em containers]]
- [[Instruções WORKDIR e USER]]
- [[PHP em Docker]]
- [[MOC - Desenvolvimento]]
