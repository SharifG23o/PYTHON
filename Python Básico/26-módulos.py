"""
Programa que muestra el uso de Módulos en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

"""
Un módulo o module en Python es un fichero .py que alberga un conjunto de funciones,
variables o clases y que puede ser usado por otros módulos. Nos permiten reutilizar 
código y organizarlo mejor en namespaces

Tomado de: https://ellibrodepython.com/modulos-python

"""


# importar función en concreto
from modulo import sumar_dos_valores,imprimir_nombre

#importar módulo
import modulo

modulo.sumar_dos_valores(3,7)


sumar_dos_valores(2,3)
imprimir_nombre("Sharif","Giraldo")

import math 

print(math.cos(90))
print(math.sqrt(9))
print(math.radians(360))
print(math.pi)
print(math.pow(2,4))

from math import pi as PI_VALUE
print(PI_VALUE)
import random

