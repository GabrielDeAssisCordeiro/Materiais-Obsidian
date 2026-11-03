---
tags:
  - docker
  - desenvolvimento
  - dockerfile
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Hot reload em containers]]"
  - "[[Bancos de dados locais]]"
  - "[[Instruções COPY e ADD]]"
  - "[[ASP.NET Core em Docker]]"
---

# PHP em Docker

`public/index.php`:

```php
<?php
echo "Olá, Docker! PHP " . PHP_VERSION . "\n";
```

`composer.json`:

```json
{
  "require": {}
}
```

`Dockerfile`:

```dockerfile
# syntax=docker/dockerfile:1

# ---------- Dependências (Composer) ----------
FROM composer:2 AS vendor
WORKDIR /app
COPY composer.json composer.lock* ./
RUN composer install --no-dev --no-interaction --prefer-dist --no-scripts

# ---------- Produção ----------
FROM php:8.3-apache AS prod
# Extensões comuns (exemplo: acesso ao MySQL)
RUN docker-php-ext-install pdo pdo_mysql
# Document root em /var/www/html/public
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf \
 && sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf
COPY --from=vendor /app/vendor /var/www/html/vendor
COPY . /var/www/html
EXPOSE 80
```

```bash
docker build -t php-demo:1.0 .
docker run -d --name php -p 8080:80 php-demo:1.0
curl http://localhost:8080
docker rm -f php
```

## Desenvolvimento: código ao vivo

```yaml
services:
  web:
    build: .
    ports:
      - "8080:80"
    volumes:
      - ./:/var/www/html          # alterações refletem a cada requisição
```

> [!tip] Alternativa: PHP-FPM + Nginx
> Para produção, muitos projetos usam `php:8.3-fpm-alpine` com um container Nginx como servidor web, em serviços separados.

> [!warning] Permissões
> O Apache roda como `www-data`; diretórios de escrita (cache, uploads) precisam pertencer a ele (veja [[Permissões e UID GID em volumes]]).

> [!question] Verificar na documentação oficial
> Confirme as variáveis e o procedimento de *document root* na página da imagem `php` no Docker Hub, e use a versão do PHP suportada pelo seu projeto.

## Exercício

Containerize uma página PHP com bind mount em desenvolvimento e comprove que editar o arquivo muda a resposta sem rebuild.

## Veja também

- [[Hot reload em containers]]
- [[Bancos de dados locais]]
- [[Instruções COPY e ADD]]
- [[ASP.NET Core em Docker]]
- [[MOC - Desenvolvimento]]
