# Arquivo: examples/measure_collapse.py
from qsymflow.core import qinit, qrule, qmeasure

qinit()

# Regra que simula o colapso de um qubit ao ser medido
qrule("spin == 'up' or spin == 'down'")

# Simulando leitura com spin indefinido
estado = {"spin": "up"}
print("Estado medido:", qmeasure(estado))
