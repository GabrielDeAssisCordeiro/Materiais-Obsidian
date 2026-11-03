---
tags:
  - devops
  - dev
aliases:
  - "Terraform"
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Ambientes Efêmeros]]"
  - "[[Preview Environments]]"
---
# Infraestrutura como Código

IaC descreve a infraestrutura em arquivos versionados, tornando ambientes **reprodutíveis e descartáveis**.

## Terraform (um ambiente por workspace)

```hcl
terraform {
  required_providers {
    docker = { source = "kreuzwerker/docker", version = "~> 3.0" }
  }
}

resource "docker_image" "app" {
  name = "nginx:alpine"
}

resource "docker_container" "app" {
  name  = "app-${terraform.workspace}"
  image = docker_image.app.image_id
  read_only = true
  capabilities { drop = ["ALL"] }
}
```

```bash
terraform init
terraform workspace new pr-123
terraform apply -auto-approve
terraform destroy -auto-approve
```

## Ansible (preparar um host de laboratório)

```yaml
- hosts: lab
  become: true
  tasks:
    - name: Instalar Podman
      ansible.builtin.apt:
        name: [podman, uidmap]
        state: present
        update_cache: true
    - name: Criar usuário sem privilégios
      ansible.builtin.user:
        name: sandbox
        shell: /bin/bash
        create_home: true
```

> [!question] Verificar na documentação oficial
> Atributos do provider `docker` e versões variam; consulte os registros oficiais.

## Exercício

Crie e destrua dois workspaces e observe que os containers não colidem.

## Veja também

- [[Ambientes Efêmeros]]
- [[Preview Environments]]
- [[Ambientes de Staging e Promoção]]
- [[MOC - Dev e DevOps]]
