# Arquivo: examples/bell_state.py
from qsymflow.core import qinit, qrule, qmeasure

# Inicializa o sistema simbólico
qinit()

# Regra representando entrelaçamento: se q0 é 1, q1 também deve ser 1
qrule("(q0 and q1) or (not q0 and not q1)")

# Simulação de um estado entrelaçado (Bell)
estado = {"q0": True, "q1": True}
resultado = qmeasure(estado)
print("Resultado entrelaçado:", resultado)
