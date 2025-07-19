from qsymflow.core import qinit, qrule, qmeasure

def main():
    qinit()
    qrule('if spin == up then energy = high')
    qmeasure({'spin': 'up'})

if __name__ == '__main__':
    main()
