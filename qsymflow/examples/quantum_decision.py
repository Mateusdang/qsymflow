# Arquivo: examples/quantum_decision.py
from qsymflow.core import qinit, qrule, qmeasure

qinit()

# Regras que representam decisões baseadas em condições
qrule("risco_alto and not backup_ativo")

entrada = {"risco_alto": True, "backup_ativo": False}
decisao = qmeasure(entrada)

print("Ação necessária:", decisao)  # True = risco sem backup
