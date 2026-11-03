---
titulo: "Soluções para Deadlock"
tags:
  - sistemas-operacionais
  - conceito
  - sincronizacao
tipo: conceito
nivel: avancado
relacionados:
  - "[[Deadlock (Impasse)]]"
  - "[[Mutex]]"
  - "[[Problemas Clássicos de Sincronização]]"
---

# Soluções para Deadlock

## Resumo

Há quatro abordagens: **ignorar**, **prevenir**, **evitar** e **detectar e recuperar**. A escolha depende do custo da falha e da sobrecarga aceitável.

| Abordagem | Ideia | Custo | Onde é usada |
|---|---|---|---|
| **Avestruz** | Ignorar; reiniciar se ocorrer | Nenhum | UNIX e Windows para recursos do SO; deadlocks raros |
| **Prevenção** | Quebrar uma condição de Coffman por projeto | Restrições de uso | Ordem de travas em kernels, aplicações |
| **Evitação** | Decidir dinamicamente só conceder estados seguros | Exige conhecer demandas máximas | Raramente (algoritmo do banqueiro) |
| **Detecção e recuperação** | Permitir, detectar e corrigir | Custo do algoritmo e de abortar | Bancos de dados, sistemas distribuídos |

## 1. Prevenção: quebrar uma condição

| Condição | Como quebrar | Limitação |
|---|---|---|
| Exclusão mútua | Tornar recursos compartilháveis (leitura, *spooling*) | Nem todo recurso permite |
| Posse e espera | Pedir **todos** os recursos de uma vez, ou liberar antes de pedir outros | Baixa utilização, inanição |
| Não preempção | Tomar recursos (liberar se o próximo pedido falhar; `trylock`) | Só serve para recursos salváveis (CPU, memória) |
| **Espera circular** | **Ordem global** de aquisição | A mais usada: simples e eficaz |

```c
// Ordem global por endereço: evita deadlock ao travar duas contas
void transferir(conta *a, conta *b, long v) {
    conta *primeiro = (a < b) ? a : b;
    conta *segundo  = (a < b) ? b : a;
    pthread_mutex_lock(&primeiro->m);
    pthread_mutex_lock(&segundo->m);
    a->saldo -= v; b->saldo += v;
    pthread_mutex_unlock(&segundo->m);
    pthread_mutex_unlock(&primeiro->m);
}
```

```cpp
// C++17: bloqueia vários mutexes de uma vez, sem deadlock
std::scoped_lock lk(a.m, b.m);
```

```c
// Quebrar "não preempção" com trylock e recuo
for (;;) {
    pthread_mutex_lock(&A);
    if (pthread_mutex_trylock(&B) == 0) break;   // conseguiu os dois
    pthread_mutex_unlock(&A);                    // recua e tenta depois
    usleep(rand() % 1000);                       // atraso aleatório evita livelock
}
```

## 2. Evitação: algoritmo do banqueiro

O SO só concede um recurso se o sistema permanecer em um **estado seguro**: existe uma sequência em que todos os processos podem terminar. Precisa conhecer o **máximo** que cada processo pode pedir.

Estruturas (n processos, m tipos de recurso): `Disponível[m]`, `Máximo[n][m]`, `Alocado[n][m]`, `Necessidade = Máximo - Alocado`.

**Algoritmo de segurança**:

1. `Trabalho = Disponível`; todos `Terminou = falso`.
2. Procure um processo i não terminado com `Necessidade[i] <= Trabalho`.
3. Se existe: `Trabalho += Alocado[i]`, marque como terminado e repita.
4. Se todos terminam, o estado é **seguro**.

```python
def estado_seguro(disponivel, maximo, alocado):
    n, m = len(maximo), len(disponivel)
    necessidade = [[maximo[i][j] - alocado[i][j] for j in range(m)] for i in range(n)]
    trabalho, fim, seq = disponivel[:], [False] * n, []
    while len(seq) < n:
        for i in range(n):
            if not fim[i] and all(necessidade[i][j] <= trabalho[j] for j in range(m)):
                trabalho = [trabalho[j] + alocado[i][j] for j in range(m)]
                fim[i] = True; seq.append(i)
                break
        else:
            return False, []            # nenhum pode prosseguir: inseguro
    return True, seq

# Exemplo: 5 processos, 3 tipos de recurso
disp = [3, 3, 2]
maxi = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
aloc = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
print(estado_seguro(disp, maxi, aloc))     # (True, [1, 3, 4, 0, 2])
```

> [!info] Limitação
> Exige o máximo conhecido antecipadamente e número fixo de processos, o que raramente acontece. Por isso o banqueiro é sobretudo didático.

## 3. Detecção e recuperação

**Detecção**: mantém-se o **grafo de espera** (wait-for) e busca-se ciclo periodicamente (DFS). Bancos de dados e *lockdep* do Linux usam essa ideia.

**Recuperação**:

| Estratégia | Detalhe |
|---|---|
| Abortar todos os processos do impasse | Simples, caro |
| Abortar um por vez até quebrar o ciclo | Escolher a **vítima**: menor custo, menos trabalho feito, menos recursos, menos reinícios |
| **Preempção com rollback** | Retomar de um ponto salvo (transações desfazem) |
| Timeout | Desistir após esperar demais (comum em aplicações e RPC) |

> [!tip] Evitar inanição na escolha da vítima
> Se a mesma vítima for escolhida sempre, ela nunca termina. Inclua o número de reinícios no custo.

## Boas práticas na prática

1. Defina e documente uma **hierarquia de travas**.
2. Mantenha seções críticas curtas e evite chamar código externo com trava segura.
3. Use **timeouts** (`pthread_mutex_timedlock`) para diagnosticar.
4. Prefira estruturas de mais alto nível: filas, canais, *actors*, memória transacional.
5. Teste com ferramentas: **lockdep** (kernel), ThreadSanitizer, Helgrind, `jstack`.

## Vantagens e desvantagens por abordagem

| Abordagem | Vantagens | Desvantagens |
|---|---|---|
| Ignorar | Zero custo | Travamento sem aviso |
| Prevenção | Garantia estática | Restritiva, reduz concorrência |
| Evitação | Garantia dinâmica | Pouco prática; precisa de máximos |
| Detecção | Flexível; sem restrições | Sobrecarga; recuperação perde trabalho |

## Pontos-chave

- Quebrar qualquer uma das 4 condições impede o deadlock; a **ordem global de travas** é o método prático mais usado.
- Banqueiro = estado seguro; detecção = ciclo no grafo de espera.
- Timeouts e ferramentas de diagnóstico completam a defesa.

## Veja também

[[Deadlock (Impasse)]] · [[Mutex]] · [[Problemas Clássicos de Sincronização]] · [[MOC - Sincronização]]
