---
titulo: "SO de Tempo Real (RTOS)"
tags:
  - sistemas-operacionais
  - conceito
  - fundamentos
tipo: conceito
nivel: intermediario
relacionados:
  - "[[Tipos de Sistemas Operacionais]]"
  - "[[SO Embarcado]]"
  - "[[Escalonamento de Processos]]"
  - "[[Interrupções]]"
---

# SO de Tempo Real (RTOS)

## Resumo

Um **sistema de tempo real** é correto quando produz o resultado certo **dentro do prazo**. O foco é **previsibilidade (determinismo)**, não velocidade média.

## Hard x Soft x Firm

| Classe | Prazo perdido significa | Exemplos |
|---|---|---|
| **Hard** | Falha catastrófica | Freios ABS, marcapasso, controle de voo |
| **Firm** | Resultado inútil, sem dano grave | Alguns sistemas de aquisição de dados |
| **Soft** | Qualidade degradada | Streaming de vídeo, jogos, VoIP |

## Características de um RTOS

- **Latência de interrupção** e **jitter** limitados e conhecidos.
- Escalonamento por **prioridades preemptivo**, com algoritmos como Rate Monotonic (RM) e Earliest Deadline First (EDF).
- Kernel pequeno, frequentemente microkernel ([[Microkernel]]).
- Evita fontes de imprevisibilidade: paginação em disco, alocação dinâmica sem limite, esperas sem timeout.
- Tratamento de **inversão de prioridade** com herança de prioridade.

> [!warning] Inversão de prioridade
> Uma tarefa de baixa prioridade segura um mutex; a de alta espera; uma de média prioridade preempta a baixa. A de alta fica bloqueada indefinidamente. Foi o bug famoso do Mars Pathfinder (1997), resolvido ativando herança de prioridade. Ver [[Escalonamento de Processos]].

## Teste de escalonabilidade (Rate Monotonic)

Para *n* tarefas periódicas com utilização total U = Σ(Ci/Ti), o RM garante os prazos se
U ≤ n(2^(1/n) − 1). Para n = 3, o limite é aproximadamente 0,78.

## Exemplos de RTOS

| RTOS | Observação |
|---|---|
| FreeRTOS | Muito usado em microcontroladores |
| Zephyr | Open source, IoT |
| VxWorks | Aeroespacial, industrial |
| QNX | Microkernel, automotivo |
| Linux com PREEMPT_RT | Tempo real suave/firme em uso geral |

## Exemplo prático

```c
// FreeRTOS: tarefa periódica a cada 10 ms
#include "FreeRTOS.h"
#include "task.h"

void vTarefaControle(void *pv) {
    TickType_t ultimo = xTaskGetTickCount();
    for (;;) {
        ler_sensor();
        atualizar_atuador();
        vTaskDelayUntil(&ultimo, pdMS_TO_TICKS(10)); // período fixo, sem deriva
    }
}

int main(void) {
    xTaskCreate(vTarefaControle, "controle", 256, NULL, 3, NULL);
    vTaskStartScheduler();
    for (;;) {}
}
```

```bash
# Linux: rodar processo com política FIFO de tempo real, prioridade 50
sudo chrt -f 50 ./meu_programa
```

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Prazos garantidos | Menor vazão média |
| Latência previsível | Projeto e testes mais difíceis |
| Footprint pequeno | Menos recursos (sem memória virtual completa, por exemplo) |

## Pontos-chave

- Tempo real ≠ rápido; é **determinístico**.
- Prioridades e herança de prioridade são centrais.
- Ver também [[SO Embarcado]].

## Veja também

[[Tipos de Sistemas Operacionais]] · [[MOC - Fundamentos - SO]]
