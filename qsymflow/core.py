from qsymflow.logic_engine import evaluate_expression

def qinit():
    print('[QSymFlow] Quantum system initialized.')

def qrule(rule: str):
    print(f'[QSymFlow] Rule defined: {rule}')

def qmeasure(context):
    print(f'[QSymFlow] Measuring with context: {context}')
