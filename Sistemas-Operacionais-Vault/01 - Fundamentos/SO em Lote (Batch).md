---
titulo: "SO em Lote (Batch)"
tags:
  - sistemas-operacionais
  - conceito
  - fundamentos
tipo: conceito
nivel: iniciante
relacionados:
  - "[[Tipos de Sistemas Operacionais]]"
  - "[[SO de Tempo Compartilhado]]"
  - "[[História e Evolução dos Sistemas Operacionais]]"
---

# SO em Lote (Batch)

## Resumo

Em sistemas **batch**, o usuário entrega um *job* (programa + dados + instruções de controle) e só recebe o resultado depois. Não há interação durante a execução; o objetivo é **maximizar a vazão** e a utilização da CPU.

## Funcionamento

1. Os jobs são lidos (originalmente de cartões perfurados) e gravados em fita ou disco.
2. Um **monitor residente** carrega e executa um job por vez.
3. A saída é impressa ou gravada para o usuário.
4. Com **multiprogramação**, vários jobs ficam na memória; enquanto um espera E/S, outro usa a CPU.

```mermaid
flowchart LR
    S[Submissão de jobs] --> F[Fila de jobs]
    F --> E[Escalonador de jobs]
    E --> M[Memória / CPU]
    M --> R[Resultado]
```

## Linguagem de controle de jobs (JCL)

Em mainframes, o JCL descreve o job. Exemplo conceitual:

```text
//MEUJOB  JOB  (CONTA),'RELATORIO',CLASS=A
//PASSO1  EXEC PGM=SORT
//SORTIN  DD   DSN=DADOS.ENTRADA,DISP=SHR
//SORTOUT DD   DSN=DADOS.SAIDA,DISP=(NEW,CATLG)
```

## Exemplo moderno

Processamento em lote continua vivo: faturamento, folha de pagamento, ETL noturno.

```bash
# Agendar um job com cron (todo dia às 02:00)
echo "0 2 * * * /opt/scripts/fechamento.sh" | crontab -
# Ou rodar em fila com 'at'
echo "/opt/scripts/relatorio.sh" | at 23:30
```

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Alta utilização da CPU | Sem interatividade |
| Simples de implementar | Tempo de retorno (turnaround) alto |
| Bom para cargas repetitivas | Depuração difícil; um erro só aparece no fim |
| Jobs podem rodar fora do horário de pico | Um job lento atrasa os demais (sem preempção) |

> [!info] Métricas típicas
> **Vazão** (jobs/hora), **tempo de retorno** (da submissão ao fim) e **utilização da CPU**. Ver [[Escalonamento de Processos]].

## Pontos-chave

- Foco em eficiência, não em resposta.
- Ancestral da multiprogramação e do [[SO de Tempo Compartilhado]].
- Ainda usado em mainframes (z/OS) e em sistemas de processamento noturno.

## Veja também

[[Tipos de Sistemas Operacionais]] · [[MOC - Fundamentos - SO]]
