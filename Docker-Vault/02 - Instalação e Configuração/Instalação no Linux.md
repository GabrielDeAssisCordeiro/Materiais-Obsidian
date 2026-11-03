---
tags:
  - docker
  - instalacao
  - linux
aliases:
  - Instalar Docker no Linux
  - Instalar Docker no Ubuntu
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Pós-instalação no Linux]]"
  - "[[Verificando com hello-world]]"
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Atualização e desinstalação]]"
---

# Instalação no Linux

Este procedimento instala o **Docker Engine** em **Ubuntu/Debian** a partir do repositório oficial `apt` (método recomendado). Outras distribuições (Fedora, RHEL, CentOS Stream, SLES) têm instruções equivalentes na documentação oficial.

> [!info] Requisitos
> Versão de 64 bits de uma distribuição suportada (por exemplo, Ubuntu LTS atual ou Debian estável) e privilégios `sudo`.

## 1. Remover pacotes conflitantes

```bash
# Pacotes não oficiais que conflitam com o Docker CE
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
  sudo apt-get remove -y $pkg
done
```

## 2. Configurar o repositório oficial (Ubuntu)

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl

# Chave GPG oficial
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Repositório (canal stable)
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

> [!tip] Debian
> Em Debian, troque `linux/ubuntu` por `linux/debian` nas duas URLs e use `$VERSION_CODENAME` em vez de `${UBUNTU_CODENAME:-$VERSION_CODENAME}`.

> [!question] Verificar na documentação oficial
> A documentação mais recente pode apresentar o repositório no formato **deb822** (`/etc/apt/sources.list.d/docker.sources`). Ambos os formatos funcionam; confira a página oficial de instalação do Engine para o método atual da sua distribuição.

## 3. Instalar os pacotes

```bash
sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

O serviço inicia automaticamente em Ubuntu/Debian. Confirme:

```bash
sudo systemctl status docker --no-pager
sudo docker run --rm hello-world
```

## Script de conveniência

```bash
# Apenas para ambientes de teste/desenvolvimento, nunca para produção
curl -fsSL https://get.docker.com -o get-docker.sh
less get-docker.sh          # leia antes de executar!
sudo sh get-docker.sh
```

> [!warning] Leia scripts antes de executar
> Executar `curl | sh` às cegas é um risco. O script de conveniência não é recomendado em produção porque não permite controle fino das versões.

## Fixando uma versão específica

```bash
# Lista versões disponíveis no repositório
apt-cache madison docker-ce | head

# Instala uma versão exata (substitua pela string da coluna 3)
VERSION_STRING=<cole-a-versao-aqui>
sudo apt-get install -y docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

> [!info] Engine 29
> Instalações novas do Engine 29 usam o **containerd image store** por padrão; imagens e containers de instalações antigas (que usavam o storage driver clássico) são tratados conforme as notas de migração. Veja [[containerd e runc]].

## Exercício

Instale o Docker Engine em uma VM Ubuntu descartável seguindo os passos acima e execute `docker version`. Qual versão do Engine foi instalada?

## Veja também

- [[Pós-instalação no Linux]]
- [[Verificando com hello-world]]
- [[Docker Desktop vs Docker Engine]]
- [[Atualização e desinstalação]]
- [[MOC - Instalação e Configuração]]
