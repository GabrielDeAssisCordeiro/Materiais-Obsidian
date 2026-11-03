---
tags:
  - docker
  - cicd
  - pipeline
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Pipeline CI-CD com Docker]]"
  - "[[Login e tokens de acesso]]"
  - "[[Proteção do docker.sock]]"
---

# Jenkins com Docker

`Jenkinsfile` declarativo que usa o Docker do agente para construir, testar e publicar.

```groovy
pipeline {
  agent any

  environment {
    REGISTRY = 'registry.exemplo.com'
    IMAGE    = "${REGISTRY}/equipe/app"
    TAG      = "${env.GIT_COMMIT.take(7)}"
  }

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t $IMAGE:$TAG .'
      }
    }

    stage('Test') {
      steps {
        sh 'docker run --rm $IMAGE:$TAG npm test'
      }
    }

    stage('Push') {
      when { branch 'main' }
      steps {
        withCredentials([usernamePassword(
            credentialsId: 'registry-creds',
            usernameVariable: 'REG_USER',
            passwordVariable: 'REG_PASS')]) {
          sh 'echo "$REG_PASS" | docker login $REGISTRY -u "$REG_USER" --password-stdin'
          sh 'docker push $IMAGE:$TAG'
        }
      }
    }
  }

  post {
    always {
      sh 'docker logout $REGISTRY || true'
      sh 'docker image prune -f || true'
    }
  }
}
```

## Agentes em container

Com o plugin *Docker Pipeline*, cada estágio pode rodar dentro de um container (ferramentas isoladas e versionadas):

```groovy
pipeline {
  agent { docker { image 'node:22-alpine' } }
  stages {
    stage('Teste') { steps { sh 'npm ci && npm test' } }
  }
}
```

> [!danger] Acesso ao Docker = poder de root no agente
> Agentes que usam o socket do Docker devem ser **isolados e efêmeros** (VMs/containers descartáveis) e não compartilhados com projetos não confiáveis. Veja [[Proteção do docker.sock]].

> [!tip] Credenciais
> Use o *Credentials Binding* para injetar secrets e `--password-stdin` para o login, nunca `-p` na linha de comando.

## Exercício

Execute um Jenkins de laboratório em container, crie um pipeline com o `Jenkinsfile` acima apontando para um repositório simples e valide o estágio de teste.

## Veja também

- [[Pipeline CI-CD com Docker]]
- [[Login e tokens de acesso]]
- [[Proteção do docker.sock]]
- [[MOC - CI-CD e DevOps]]
