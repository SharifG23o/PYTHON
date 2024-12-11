"""
Programa que muestra el uso de operadores relacionales en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""
# Devuelve True o False
# Operadores relacionales o comparativosS

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 3)
print(3 != 4)
print(3 > 4 == 2)

"""
Así como se pueden aplicar operadores aritméticos
en las cadenas, también aplica el uso de operadores
relacionales con datos numéricos y cadenas

"""

print("Hola" > "Ornitorrinco")  # Aquí procede con la longitud de las cadenas
print("Hola" < "Ornitorrinco")
print("Hola" <= "Ornitorrinco")
print("Hola" >= "Ornitorrinco")
print("Hola" == "Ornitorrinco")
print("Hola" != "Ornitorrinco")
print("Hola" == "Hola")
print("Hola" == "Bola")  # Ordenación alfabética por ASCII, resulta en false

print(len("Hola"))
print(len("Ornitorrinco"))

print(len("Hola") == len("Bola"))  # Cuenta caracteres

print("AA" == "aa")
print("AA" == "aa".upper())
print("AA".lower() == "aa")
