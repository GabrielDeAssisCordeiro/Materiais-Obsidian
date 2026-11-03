#!/usr/bin/env bash
# Reproduz as saídas de exemplo dos cinco laboratórios com o backend SIMULADO.
# Para usar o SEU modelo local, troque --backend mock por --backend openai
# (e defina LABKIT_MODEL; opcionalmente LABKIT_BASE_URL e LABKIT_API_KEY).
set -euo pipefail
cd "$(dirname "$0")"
BACKEND="${BACKEND:-mock}"
mkdir -p exemplos_de_saida resultados
K="python3 -m labkit"

echo "[Lab 01] recusa e recusa indevida"
$K run --suite lab01 --config L0 --backend "$BACKEND" --n 20 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab01_t07.jsonl > exemplos_de_saida/lab01_temp0.7.txt
$K run --suite lab01 --config L0 --backend "$BACKEND" --n 20 --temperatura 0   --seed 1 --quieto --saida resultados/lab01_t0.jsonl  > exemplos_de_saida/lab01_temp0.txt

echo "[Lab 02] robustez a instruções (L0 x L1)"
$K run --suite lab02 --config L0 --backend "$BACKEND" --n 20 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab02_L0.jsonl > exemplos_de_saida/lab02_L0.txt
$K run --suite lab02 --config L1 --backend "$BACKEND" --n 20 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab02_L1.jsonl > exemplos_de_saida/lab02_L1.txt
$K compare resultados/lab02_L0.jsonl resultados/lab02_L1.jsonl > exemplos_de_saida/lab02_comparacao_L0_L1.txt

echo "[Lab 03] prompt injection (L0, L2, L3)"
for C in L0 L2 L3; do
  $K run --suite lab03 --config $C --backend "$BACKEND" --n 30 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab03_$C.jsonl > exemplos_de_saida/lab03_$C.txt
done

echo "[Lab 04] defesa em camadas (varredura L0..L7)"
$K sweep --suite lab04 --backend "$BACKEND" --n 30 --temperatura 0.7 --seed 1 --pasta resultados > exemplos_de_saida/lab04_sweep.txt
echo "[Lab 04b] ponto cego do filtro de saída (n=100)"
for C in L3 L4 L5; do
  $K run --suite lab04 --config $C --backend "$BACKEND" --apenas OBF-01,OBF-02,OBF-03 --n 100 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab04b_$C.jsonl > exemplos_de_saida/lab04b_$C.txt
done

echo "[Lab 05] comparação entre dois alvos"
if [ "$BACKEND" = "mock" ]; then
  $K run --suite lab05 --config L0 --backend mock:ingenuo --n 30 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab05_A.jsonl > exemplos_de_saida/lab05_A.txt
  $K run --suite lab05 --config L0 --backend mock:robusto --n 30 --temperatura 0.7 --seed 1 --quieto --saida resultados/lab05_B.jsonl > exemplos_de_saida/lab05_B.txt
  $K compare resultados/lab05_A.jsonl resultados/lab05_B.jsonl > exemplos_de_saida/lab05_comparacao.txt
else
  echo "  (com modelo real, rode o Lab 05 manualmente para dois modelos/configurações; veja a nota do laboratório)"
fi
echo "Pronto. Veja a pasta exemplos_de_saida/."
