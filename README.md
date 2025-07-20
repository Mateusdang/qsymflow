QSymFlow – Quantum Symbolic Flow Language

## 📖 Descrição

QSymFlow é uma linguagem simbólica de domínio específico (DSL) implementada em Python para modelagem e simulação de sistemas quânticos utilizando expressões lógicas e regras simbólicas.

Utilizando a biblioteca logicflowengine, o QSymFlow permite representar estados de qubits, entrelaçamento (entanglement) e fluxos de decisão quântica através de expressões booleanas interpretáveis.

Esse projeto é voltado para pesquisadores, estudantes e desenvolvedores nas áreas de:

Computação quântica simbólica e lógica

Sistemas de decisão inteligente com lógica formal

Ensino e visualização de fenômenos quânticos

Pesquisas em AI híbrida com regras simbólicas

## ⚙️ Funcionalidades

Inicialização simbólica de sistemas quânticos

Definição de regras lógicas para estados e decisões

Simulação de medições quânticas simbólicas

Integração transparente com a biblioteca logicflowengine

Estrutura modular para expansão e customização


## 🚀 Instalação

**Requer Python 3.7+.**


Instale via pip:


``` python
pip install qsymflow
```

Ou, para instalação local em modo editável (desenvolvimento):

```bash
git clone https://github.com/Mateusdang/qsymflow.git
cd qsymflow
pip install -e .
```

## 🔬 Exemplos Práticos de Computação Quântica Simbólica

**🔁 1. Simulação de Entrelaçamento (Bell State)**

```python
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

```
💡 Neste exemplo, simulamos um estado Bell onde q0 e q1 devem sempre estar em sincronia. Isso representa o entrelaçamento quântico de forma simbólica e lógica. 

**🎯 2. Colapso de Estado após Medição**
```python
# Arquivo: examples/measure_collapse.py
from qsymflow.core import qinit, qrule, qmeasure

qinit()

# Regra que simula o colapso de um qubit ao ser medido
qrule("spin == 'up' or spin == 'down'")

# Simulando leitura com spin indefinido
estado = {"spin": "up"}
print("Estado medido:", qmeasure(estado))

```
💡 Aqui mostramos como simular a medição quântica: ao observar o sistema, ele assume um valor definido — uma abstração simbólica do colapso da função de onda.

**🧠 3. Sistema de Decisão Quântico-Simbólico**

```python
# Arquivo: examples/quantum_decision.py
from qsymflow.core import qinit, qrule, qmeasure

qinit()

# Regras que representam decisões baseadas em condições
qrule("risco_alto and not backup_ativo")

entrada = {"risco_alto": True, "backup_ativo": False}
decisao = qmeasure(entrada)

print("Ação necessária:", decisao)  # True = risco sem backup

```
💡 Este exemplo ilustra como sistemas inteligentes podem usar lógica simbólica inspirada na incerteza quântica para tomar decisões sob ambiguidade.

## 📁 Estrutura do Projeto

**Arduino**
```bash
qsymflow/
├── __init__.py
├── core.py
├── logic_engine.py
├── main.py
├── qsymflow/
└── examples/
    ├── bell_state.py
    ├── measure_collapse.py
    └── quantum_decision.py
README.md
setup.py
requirements.txt
pyproject.toml
```

## ⚙️ Executando o projeto

**Após a instalação, você pode rodar o simulador interativo:**

```bash
python -m qsymflow.main

Para executar o exemplo Bell State:


# Entrelaçamento Bell
python -m qsymflow.examples.bell_state

# Medição simbólica
python -m qsymflow.examples.measure_collapse

# Decisão baseada em risco
python -m qsymflow.examples.quantum_decision

```

## 📦 Deploy & Distribuição

1. Preparar o ambiente
Ter Python 3.7+

Criar ambiente virtual (opcional, recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```
2. Instalar dependências

```bash
pip install -r requirements.txt
```
3. Instalar pacote localmente

```bash
pip install -e .
```

4. Testar execução local

```bash
python -m qsymflow.main
```



## 👨‍💻 Autor

Mateus Dang
https://github.com/Mateusdang

📄 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.


**⭐ Agradecimentos**

Este projeto utiliza a biblioteca logicflowengine para avaliação lógica de expressões.

https://pypi.org/project/logicflowengine/
