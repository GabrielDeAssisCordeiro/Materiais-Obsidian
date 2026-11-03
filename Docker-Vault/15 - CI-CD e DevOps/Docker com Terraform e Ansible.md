---
tags:
  - docker
  - cicd
  - devops
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Deploy com Compose via SSH]]"
  - "[[AWS ECR]]"
  - "[[AWS ECS com Fargate]]"
  - "[[GitOps introdução]]"
---

# Docker com Terraform e Ansible

**Infraestrutura como código (IaC)** complementa o Docker: Terraform/Ansible preparam e configuram a infraestrutura onde os containers rodam.

| Ferramenta | Papel típico |
|---|---|
| **Terraform / OpenTofu** | Provisiona **recursos** (VPC, VMs, ECR, ECS, bancos, DNS) de forma declarativa |
| **Ansible** | Configura servidores (instala Docker, aplica hardening) e implanta stacks Compose |
| **Docker/Compose** | Empacota e executa a aplicação |

## Terraform: provider Docker (laboratório)

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:1.27"
  keep_locally = false
}

resource "docker_container" "web" {
  name  = "web-terraform"
  image = docker_image.nginx.image_id

  ports {
    internal = 80
    external = 8080
  }
}
```

```bash
terraform init
terraform plan
terraform apply
terraform destroy
```

> [!info] Uso mais comum do Terraform
> Em produção, o Terraform geralmente cria a **infraestrutura** (repositório ECR, cluster ECS, serviço, balanceador), enquanto o pipeline publica imagens e atualiza a versão (via variável ou `aws ecs update-service`).

## Ansible: instalar Docker e subir um stack

```bash
ansible-galaxy collection install community.docker
```

```yaml
- name: Implantar a aplicação
  hosts: servidores
  become: true
  tasks:
    - name: Garante o diretório da aplicação
      ansible.builtin.file:
        path: /srv/app
        state: directory
        mode: "0755"

    - name: Copia o compose.yaml
      ansible.builtin.copy:
        src: compose.yaml
        dest: /srv/app/compose.yaml
        mode: "0644"

    - name: Sobe a stack
      community.docker.docker_compose_v2:
        project_src: /srv/app
        pull: always
        state: present
```

```bash
ansible-playbook -i inventario.ini deploy.yaml
```

> [!question] Verificar na documentação oficial
> Os módulos (`docker_compose_v2`) e versões mínimas da coleção `community.docker`, e o provider `kreuzwerker/docker`, mudam com o tempo; confirme nas respectivas documentações.

> [!warning] Estado e segredos
> O estado do Terraform pode conter segredos; armazene-o em um backend remoto criptografado e com controle de acesso.

## Exercício

Escreva um playbook Ansible que instala o Docker em uma VM de laboratório e implanta o `compose.yaml` do seu projeto.

## Veja também

- [[Deploy com Compose via SSH]]
- [[AWS ECR]]
- [[AWS ECS com Fargate]]
- [[GitOps introdução]]
- [[MOC - CI-CD e DevOps]]
