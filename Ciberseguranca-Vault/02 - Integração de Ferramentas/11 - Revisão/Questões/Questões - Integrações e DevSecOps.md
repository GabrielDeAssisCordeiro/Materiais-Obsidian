---
titulo: "Questões - Integrações e DevSecOps"
aliases: ["Integrações e DevSecOps"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - revisao
  - questoes
  - quiz
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Integração com SIEM - Splunk Elastic e Wazuh]]"
  - "[[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]]"
  - "[[Integração com Gestão de Segredos - Vault e gitleaks]]"
---

# Questões - Integrações e DevSecOps

## Resumo

12 questões de múltipla escolha sobre **Integrações e DevSecOps**, com gabarito comentado (clique no callout para expandir).

## Conceitos-chave

- Cada questão tem quatro alternativas e um comentário que explica o raciocínio.
- Conteúdo-fonte: [[Integração com SIEM - Splunk Elastic e Wazuh]], [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]], [[Integração com Gestão de Segredos - Vault e gitleaks]], [[Security Gates e Shift-Left]], [[Assinatura de Artefatos - Sigstore e cosign]].

## Como funciona

Responda sem consultar as notas, depois abra o gabarito. Para cada erro, releia a nota de origem e crie um flashcard.

## Exemplo prático

> [!question] Estratégia
> Elimine primeiro as alternativas claramente incorretas; depois justifique a escolhida em uma frase.

## Boas práticas

- Faça as questões em blocos curtos e espaçados.
- Anote o motivo de cada erro.

## Erros comuns

- Marcar por intuição sem justificar.
- Ler o gabarito antes de tentar.

## Referências para aprofundar

Notas de origem listadas em Conceitos-chave.

## Questões

### Questão 1

Como o Splunk HEC autentica requisições?

- A) Basic com usuário e senha
- B) Cabeçalho Authorization: Splunk <token>
- C) Cookie de sessão
- D) Sem autenticação

> [!success]- Gabarito: B
> O HEC usa token no cabeçalho Authorization com o prefixo Splunk.

### Questão 2

Na API _bulk do Elasticsearch, o que indica falha parcial?

- A) Sempre HTTP 500
- B) errors: true na resposta, mesmo com HTTP 200
- C) Nunca há falha parcial
- D) Cabeçalho Retry-After

> [!success]- Gabarito: B
> É preciso inspecionar os itens da resposta, pois o status HTTP pode ser 200.

### Questão 3

No JSON do Trivy, o campo Vulnerabilities de um resultado pode ser:

- A) Sempre uma lista
- B) Nulo, e deve ser tratado
- C) Uma string
- D) Um número

> [!success]- Gabarito: B
> Pode vir nulo; trate como lista vazia para evitar exceções.

### Questão 4

O gitleaks encontrou um segredo no histórico. Qual a primeira ação?

- A) Apagar o último commit
- B) Revogar e rotacionar o segredo
- C) Ignorar
- D) Mudar o nome do repositório

> [!success]- Gabarito: B
> O segredo deve ser considerado comprometido; revogue e rotacione, depois limpe o histórico se necessário.

### Questão 5

O AppRole do Vault ajuda a resolver principalmente:

- A) Compressão de logs
- B) Autenticação de aplicações no cofre
- C) Escaneamento de imagens
- D) Geração de SBOM

> [!success]- Gabarito: B
> AppRole autentica aplicações (role_id + secret_id) e se relaciona ao problema do secret zero.

### Questão 6

Como evitar tickets duplicados ao integrar com Jira?

- A) Criar sempre um novo
- B) Usar chave de deduplicação determinística em label ou registro local
- C) Aumentar o timeout
- D) Usar GET no lugar de POST

> [!success]- Gabarito: B
> Chave estável (hash) permite buscar antes de criar, implementando idempotência.

### Questão 7

O que evitar ao usar o VirusTotal em um enriquecedor?

- A) Cache
- B) Respeitar cotas
- C) Enviar arquivos confidenciais da empresa
- D) Consultar por hash

> [!success]- Gabarito: C
> Uploads podem ficar acessíveis a terceiros; consulte por hash.

### Questão 8

Qual prática de hardening do GitHub Actions é correta?

- A) permissions: write-all
- B) Fixar actions de terceiros pelo SHA e usar permissões mínimas
- C) Usar pull_request_target com checkout do fork
- D) Imprimir segredos para depurar

> [!success]- Gabarito: B
> Permissões mínimas e SHA pinning reduzem o risco de supply chain.

### Questão 9

Como adotar gates de segurança sem travar as equipes?

- A) Tudo bloqueante no dia 1
- B) Começar informativo, medir ruído e promover regras de alta confiança
- C) Nunca bloquear
- D) Gate sem exceções

> [!success]- Gabarito: B
> Adoção gradual com métricas de falsos positivos aumenta a adesão.

### Questão 10

O formato CycloneDX é mantido por qual organização?

- A) OWASP
- B) ISO apenas
- C) Microsoft
- D) Elastic

> [!success]- Gabarito: A
> CycloneDX é um padrão do OWASP; SPDX é da Linux Foundation.

### Questão 11

Ao verificar uma assinatura com cosign keyless, é essencial:

- A) Aceitar qualquer assinatura válida
- B) Especificar identidade e emissor OIDC esperados
- C) Verificar a tag, não o digest
- D) Desativar o Rekor

> [!success]- Gabarito: B
> Sem restringir identidade e emissor, qualquer assinante válido seria aceito.

### Questão 12

O que o SLSA busca garantir?

- A) Ausência total de vulnerabilidades
- B) Origem e integridade do build via proveniência
- C) Velocidade do CI
- D) Cobertura de testes

> [!success]- Gabarito: B
> SLSA trata da integridade da cadeia de build, não de bugs no código.

## Veja também

- [[Integração com SIEM - Splunk Elastic e Wazuh]]
- [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]]
- [[Integração com Gestão de Segredos - Vault e gitleaks]]
- [[Security Gates e Shift-Left]]
- [[Assinatura de Artefatos - Sigstore e cosign]]
- [[MOC - Revisão - Integração]]

#seguranca/revisao/questoes #quiz
