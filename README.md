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

## 📚 Exemplo de Uso

**Python**

```python
from qsymflow.core import qinit, qrule, qmeasure

qinit()
qrule("(temperatura > 30 and umidade < 50) or alerta")
sensor = {"temperatura": 32, "umidade": 45, "alerta": False}
decisao = qmeasure(sensor)
print(f"Decisão: {decisao}")
```

## 📁 Estrutura do Projeto

**Arduino**
```bash
qsymflow/
├── __init__.py
├── core.py
├── logic_engine.py
├── main.py
├── examples/
│   └── bell_state.py
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

Bash

python -m qsymflow.examples.bell_state
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
```bash
https://pypi.org/project/logicflowengine/
```