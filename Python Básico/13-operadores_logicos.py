"""
Programa que muestra el uso de operadores lógicos en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

print(not (True))
print(not (False))
print(True and False)
print(True or False)

print("\n")

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")

print("\n")

print(3 < 4 and "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 > 4 or "Hola" < "Python")

print("\n")

print(3 < 4 or ("Hola" > "Python" and 4 == 4))

print("\n")

print(not (3 > 4))
print(not (3 < 4))
