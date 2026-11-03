---
titulo: "Segregação de Funções"
aliases: ["Separation of Duties", "SoD", "Princípio dos Quatro Olhos"]
tags:
  - automacao-seguranca
  - conceito
  - governanca
tipo: conceito
nivel: intermediario
relacionados:
  - "[[MOC - IA, Governança e Boas Práticas]]"
  - "[[Governança da Automação]]"
  - "[[Human in the Loop - Automação]]"
  - "[[Segurança em Pipelines CI-CD]]"
---

# Segregação de Funções

## Objetivo
Aplicar a segregação de funções (SoD) a automações de segurança, de modo que ninguém, humano ou sistema, controle sozinho um processo crítico de ponta a ponta. Mapa: [[MOC - IA, Governança e Boas Práticas]].

## Conceito
A **segregação de funções** (separation of duties) divide etapas sensíveis entre pessoas ou componentes diferentes, de forma que fraude, erro ou abuso exijam conluio. O **princípio dos quatro olhos** é a forma mais simples: quem propõe não é quem aprova.

**Aplicações típicas em automação de segurança:**

- **Desenvolvimento versus aprovação:** quem escreve um playbook não o promove sozinho a produção; um revisor aprova ([[Segurança em Pipelines CI-CD]]).
- **Solicitação versus aprovação de ações de alto impacto:** o analista que dispara o isolamento de um servidor crítico exige a aprovação de outro, ou do plantonista sênior ([[Human in the Loop - Automação]]).
- **Operação versus auditoria:** quem opera as automações não é dono dos registros de auditoria nem pode apagá-los ([[Trilha de Auditoria]]).
- **Administração do cofre versus uso dos segredos:** administradores do cofre não leem os segredos de produção por padrão ([[Gestão de Segredos]]).
- **Quem constrói a detecção versus quem a valida:** reduz vieses ([[Testes de Detecção]]).
- **Contas separadas:** conta de uso diário distinta da conta administrativa; automações com identidades próprias, e não a de um humano.

**Para sistemas automatizados**, a segregação também significa **separar papéis técnicos**: a identidade que *lê* alertas não é a mesma que *executa* contenções; o componente de IA que *recomenda* não possui a credencial que *age* ([[Riscos de IA em Segurança]]).

**Quando equipes pequenas não permitem separação total**, adotam-se **controles compensatórios**: revisão posterior por terceiro, alertas sobre ações privilegiadas, rodízio e registro imutável.

```mermaid
flowchart LR
    D[Desenvolvedor propõe mudança] --> R[Revisor aprova]
    R --> P[Pipeline implanta]
    P --> O[Operador executa]
    O --> L[(Log imutável)]
    L --> A[Auditor revisa]
```

## Exemplo prático
> [!example] Regra de quatro olhos em código
> O pedido de aprovação rejeita aprovação feita pelo próprio solicitante.

```python
def aprovar(pedido: dict, aprovador: str, papeis: dict) -> bool:
    if aprovador == pedido["solicitante"]:
        raise PermissionError("o solicitante não pode aprovar o próprio pedido")
    if "aprovador_soc" not in papeis.get(aprovador, []):
        raise PermissionError("usuário sem papel de aprovador")
    pedido["aprovado_por"] = aprovador
    return True
```

## Boas práticas
- Mapeie as combinações de papéis incompatíveis e verifique-as periodicamente.
- Registre quem solicitou, quem aprovou e quem executou, como identidades distintas.
- Imponha a regra pela ferramenta (proteção de ramos, workflows de aprovação), não apenas por política escrita.
- Aplique privilégio mínimo e acesso temporário (just-in-time) para funções administrativas.
- Faça recertificação de acessos regularmente ([[Auditoria Contínua]]).

## Erros comuns
- Contas compartilhadas, que anulam a rastreabilidade.
- Administrador que também é aprovador e auditor.
- Aprovação "carimbo", sem análise.
- Ignorar identidades de máquina (contas de serviço) na revisão.

> [!tip] Equipe pequena
> Se não dá para separar pessoas, separe etapas e registre: revisão posterior e alertas sobre ações privilegiadas.

## Para revisar
> [!question] Perguntas
> 1. O que é o princípio dos quatro olhos?
> 2. Cite três pares de funções que devem ser separadas.
> 3. Como aplicar SoD a identidades de automação e de IA?
> 4. Que controles compensatórios existem para equipes pequenas?

## Links relacionados
[[Rollback]], [[Anti-Padrões de Automação de Segurança]], [[Compliance as Code]], [[Aspectos Legais e LGPD]].
