from qsymflow.core import qinit, qrule, qmeasure

qinit()
qrule('q0 + q1 = bell')
qmeasure({'q0': '1'})
