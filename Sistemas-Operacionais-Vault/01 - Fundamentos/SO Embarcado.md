---
titulo: "SO Embarcado"
tags:
  - sistemas-operacionais
  - conceito
  - fundamentos
tipo: conceito
nivel: intermediario
relacionados:
  - "[[Tipos de Sistemas Operacionais]]"
  - "[[SO de Tempo Real (RTOS)]]"
  - "[[Processo de Boot]]"
---

# SO Embarcado

## Resumo

Um **SO embarcado** roda em dispositivos dedicados (roteadores, eletrodomésticos, carros, sensores) com **restrições de memória, energia, custo e tempo**. Muitas vezes é um [[SO de Tempo Real (RTOS)]]; em dispositivos maiores, é um Linux enxuto.

## Faixas de complexidade

| Nível | Hardware típico | Solução |
|---|---|---|
| Bare metal | Microcontrolador com KBs de RAM | Laço principal + interrupções, sem SO |
| RTOS | MCU com dezenas a centenas de KB | FreeRTOS, Zephyr, ThreadX |
| Linux embarcado | CPU com MMU e MBs a GBs de RAM | Yocto, Buildroot, OpenWrt |
| Android Things/Android Automotive | Infotainment | Android customizado |

## Características

- **Footprint pequeno**: o kernel pode ocupar poucos KB.
- Sem disco: firmware em **flash** (NOR/NAND), com sistemas de arquivos como SquashFS, JFFS2, UBIFS.
- **Boot rápido** e atualização remota segura (OTA com A/B partitions).
- **Watchdog** reinicia o sistema em caso de travamento.
- Gerência de energia: modos de sono e *tickless*.
- Muitas vezes sem MMU: sem memória virtual (ex.: uClinux, Cortex-M).

## Exemplo prático

```c
// Bare metal em microcontrolador: laço principal + interrupção de timer
volatile uint8_t flag_timer = 0;

void TIMER_IRQHandler(void) {   // rotina de interrupção
    flag_timer = 1;
}

int main(void) {
    hardware_init();
    for (;;) {
        if (flag_timer) {
            flag_timer = 0;
            piscar_led();
        }
        dormir_ate_proxima_interrupcao();  // economiza energia
    }
}
```

```bash
# Linux embarcado com Buildroot (exemplo de fluxo)
git clone https://gitlab.com/buildroot.org/buildroot.git
cd buildroot && make raspberrypi4_64_defconfig && make
```

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Baixo custo e consumo | Recursos escassos limitam funcionalidades |
| Alta confiabilidade quando bem projetado | Atualização e depuração no campo são difíceis |
| Otimizado para uma tarefa | Menor portabilidade (acoplado ao hardware) |

> [!warning] Segurança
> Dispositivos embarcados com senhas padrão e sem atualização são alvo comum de botnets. Planeje **atualização segura** e **inicialização verificada** desde o projeto.

## Pontos-chave

- Escolha o nível mínimo de SO que atende o requisito.
- RTOS para prazos; Linux embarcado para rede, sistemas de arquivos e ecossistema.
- Boot e atualização são pontos críticos ([[Processo de Boot]]).

## Veja também

[[Tipos de Sistemas Operacionais]] · [[MOC - Fundamentos - SO]]
