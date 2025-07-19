from setuptools import setup, find_packages

setup(
    name='qsymflow',
    version='0.1.0',
    description='Quantum Symbolic Flow Language – DSL simbólica para computação quântica em Python',
    author='Mateus Dang',
    author_email='mteus2030lol@gmail.com',
    url='https://github.com/Mateusdang/qsymflow',
    packages=find_packages(),
    install_requires=['logicflowengine>=0.1.2'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
    entry_points={'console_scripts': ['qsymflow=qsymflow.main:main']},
)
