"""
Programa que muestra el uso de Tuplas en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""


"""
Las tuplas en Python o tuples son muy similares a las listas, pero con dos diferencias. 
Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, 
y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, 
las tuplas pueden ser más rápidas

Tomado de: https://ellibrodepython.com/tuplas-python
"""

# Formas de definir una tupla
my_tuple = tuple()
my_other_tuple = ()


my_tuple = (35, 1.80, "Sharif", "Giraldo", "ProjectX")
print(my_tuple)
print(type(my_tuple))  # Su tipo es tupla

print(my_tuple[0])  # Accedo a los elementos
print(my_tuple[-1])
# print(my_tuple[4])IndexError: tuple index out of range
# print(my_tuple[-6])IndexError: tuple index out of range

# Cuenta las ocurrencias de lo ingresado y busca cuántos de ellos hay en la tupa
print(my_tuple.count("Sharif"))
# Nos indica el índice donde se encuentra el dato puesto en la función
print(my_tuple.index(1.80))
print(my_tuple.index("Sharif"))


"""
my_tuple[1]=1.80
print(my_tuple)
#LAS TUPLAS SON INMUTABLES A DIFERENCIA DE LAS LISTAS
TypeError: 'tuple' object does not support item assignment
"""
my_other_tuple = (35, 60, 30)

# Concatenación de Tuplas
print(my_tuple+my_other_tuple)

my_sum_tuple = my_tuple+my_other_tuple
print(my_sum_tuple)

# Slicing en la tupla
print(my_sum_tuple[3:6])

# Si quiero volver la tupla mutable, procedemos a convertirla en lista

my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Techmath"
my_tuple.insert(1, "Azul")

print(my_tuple)
print(tuple(my_tuple))
my_tuple = tuple(my_tuple)
print(type(my_tuple))

"""
Cuanto más inmutables sean los datos, mejor
puesto que hace que nuestro programa sea más seguro

"""
# del elimina la variable de my_tuple

"""
del my_tuple
print(my_tuple)

TypeError: 'tuple' object does not support item assignment

"""
"""
del my_tuple[2]
TypeError: 'tuple' object doesn't support item deletion
"""
