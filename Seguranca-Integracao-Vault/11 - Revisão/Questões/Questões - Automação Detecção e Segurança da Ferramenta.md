---
titulo: "Questões - Automação Detecção e Segurança da Ferramenta"
aliases: ["Automação, Detecção e Segurança da Ferramenta"]
tags:
  - integracao-seguranca
  - revisao
  - questoes
  - quiz
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Automação de Resposta a Incidentes]]"
  - "[[Regras Sigma]]"
  - "[[Testes de Regras de Detecção]]"
---

# Questões - Automação Detecção e Segurança da Ferramenta

## Resumo

11 questões de múltipla escolha sobre **Automação, Detecção e Segurança da Ferramenta**, com gabarito comentado (clique no callout para expandir).

## Conceitos-chave

- Cada questão tem quatro alternativas e um comentário que explica o raciocínio.
- Conteúdo-fonte: [[Automação de Resposta a Incidentes]], [[Regras Sigma]], [[Testes de Regras de Detecção]], [[SSRF Injeção e Desserialização Insegura]], [[LGPD e Privacidade]].

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

Qual desenho é mais seguro para uma contenção automática?

- A) Escopo amplo, sem expiração
- B) Escopo limitado, expiração, auditoria e aprovação para alvos críticos
- C) Sem registro
- D) Sem verificação posterior

> [!success]- Gabarito: B
> Limitar blast radius, expirar bloqueios e exigir aprovação em ativos críticos reduz o risco.

### Questão 2

O MTTD mede:

- A) Tempo até a contenção
- B) Tempo entre o início do incidente e a detecção
- C) Tempo de recuperação
- D) Tempo de atendimento do ticket

> [!success]- Gabarito: B
> MTTD: Mean Time To Detect.

### Questão 3

Se ninguém responde a um pedido de aprovação de ação destrutiva, a política padrão deve ser:

- A) Executar mesmo assim
- B) Não executar e escalar
- C) Apagar o pedido
- D) Aprovar automaticamente

> [!success]- Gabarito: B
> Em dúvida, falhe de forma segura: não execute e escale.

### Questão 4

Sigma é:

- A) Um scanner de containers
- B) Um formato genérico de regras para logs
- C) Um broker de mensagens
- D) Um protocolo de autenticação

> [!success]- Gabarito: B
> Regras Sigma são convertidas para consultas do SIEM por backends.

### Questão 5

Qual conjunto de testes é adequado para uma regra de detecção?

- A) Apenas casos positivos
- B) Positivos, negativos, backtesting e emulação em laboratório
- C) Nenhum, pois alertas aparecem sozinhos
- D) Somente em produção

> [!success]- Gabarito: B
> Testar apenas o positivo não detecta falsos positivos nem regressões.

### Questão 6

Qual boa prática se aplica a exceções (allowlist) de regras?

- A) Permanentes e amplas
- B) Específicas, com dono, justificativa e validade
- C) Sem justificativa
- D) Aplicadas a toda a rede interna

> [!success]- Gabarito: B
> Exceções sem prazo viram pontos cegos.

### Questão 7

Qual conjunto de defesas é adequado contra SSRF?

- A) Denylist de palavras
- B) Allowlist de destinos, validar IP resolvido público, sem redirecionamento e egress restrito
- C) Apenas HTTPS
- D) Nenhuma

> [!success]- Gabarito: B
> HTTPS não impede SSRF; é preciso controlar destino e rede.

### Questão 8

Qual função deve ser usada para ler YAML externo em Python?

- A) yaml.load sem Loader
- B) yaml.safe_load
- C) eval
- D) pickle.loads

> [!success]- Gabarito: B
> safe_load evita construção arbitrária de objetos.

### Questão 9

A melhor forma de resolver o 'secret zero' é:

- A) Embutir o segredo na imagem
- B) Usar identidade de workload (como service account/OIDC)
- C) Colocar em README
- D) Enviar por e-mail

> [!success]- Gabarito: B
> A plataforma comprova a identidade e entrega credenciais efêmeras.

### Questão 10

Segundo a LGPD, dado pseudonimizado:

- A) Deixa de ser dado pessoal
- B) Continua sendo dado pessoal
- C) Pode ser publicado livremente
- D) Não exige segurança

> [!success]- Gabarito: B
> Pseudonimização reduz riscos, mas o dado ainda pode ser atribuído a uma pessoa.

### Questão 11

Por que não montar docker.sock dentro de um container?

- A) Deixa a imagem maior
- B) Dá controle total do host ao container
- C) Impede logs
- D) Desativa TLS

> [!success]- Gabarito: B
> Quem controla o socket do Docker controla o host.

## Veja também

- [[Automação de Resposta a Incidentes]]
- [[Regras Sigma]]
- [[Testes de Regras de Detecção]]
- [[SSRF Injeção e Desserialização Insegura]]
- [[LGPD e Privacidade]]
- [[MOC - Revisão - Integração]]

#seguranca/revisao/questoes #quiz
