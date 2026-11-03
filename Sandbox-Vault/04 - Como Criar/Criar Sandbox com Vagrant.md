---
tags:
  - como-criar
aliases:
  - "Vagrant"
  - "Vagrantfile"
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Virtualização Completa]]"
  - "[[Criar Sandbox com VMs]]"
---
# Criar Sandbox com Vagrant

**Vagrant** descreve VMs em código (`Vagrantfile`), tornando laboratórios reproduzíveis.

```ruby
# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"          # confira o box atual
  config.vm.hostname = "lab-vagrant"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.synced_folder ".", "/vagrant", disabled: true   # sem pasta compartilhada
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--clipboard-mode", "disabled"]
    vb.customize ["modifyvm", :id, "--draganddrop", "disabled"]
  end
  config.vm.provision "shell", inline: "apt-get update && apt-get -y upgrade"
end
```

```bash
vagrant up
vagrant ssh
vagrant snapshot save limpo
vagrant snapshot restore limpo
vagrant destroy -f
```

> [!question] Verificar na documentação oficial
> Nomes de *boxes* e provedores disponíveis mudam; consulte o catálogo oficial e o licenciamento atual do Vagrant.

## Exercício

Escreva um Vagrantfile que cria duas VMs em rede privada e teste a comunicação entre elas.

## Veja também

- [[Criar Sandbox com VMs]]
- [[Sandbox por Virtualização Completa]]
- [[Caso - Laboratórios e Aprendizado]]
- [[MOC - Como Criar]]
