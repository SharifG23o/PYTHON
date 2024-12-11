"""
Programa que muestra el uso de operadores en Python
Autor: Sharif Giraldo Obando
Fecha: Noviembre de 2024
Licencia: GNU GPL v3
"""


print("hola"+"python")  # concatena cadenas
print("hola"*5)  # Imprime la cantidad de veces indicada

my_int = 2*2
print("Hola"*my_int)  # imprime las veces de la multiplicación

my_float = 2.5*2
# Cambio el float por int y obtengo la cadena multiplicada
print("Hola"*int(my_float))


my_float = 2.5*2
# Concatena y dado el cambio de tipo se unen la cadena y el float ahora str
print("Hola"+str(my_float))
