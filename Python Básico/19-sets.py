"""
Programa que muestra el uso de Sets en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

"""
Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:

Los elementos de un set son únicos, lo que significa que no puede haber elementos duplicados.
Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
Sus elementos deben ser inmutables

Tomado de: https://ellibrodepython.com/sets-python
"""

my_set = set()
my_other_set = {}
print(type(my_set))  # <class 'set'>
print(type(my_other_set))  # Inicialmente lo tenemos como <class 'dict'>

my_other_set = {"Sharif", "Giraldo", 18}
print(type(my_other_set))  # <class 'set'>

print(len(my_other_set))  # 3
print(my_other_set)


# print(my_other_set[1]) TypeError: 'set' object is not subscriptable

my_set = set(["Sharif", "Sharif", "Giraldo", 18])
print(my_set)


# Funciones u operaciones del sistema con sets


my_other_set.add("Shaggy")  # Add an element to a set.
print(my_other_set)

my_other_set.remove("Shaggy")
# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
print(my_other_set)

my_other_set.discard(18)
# Remove an element from a set if it is a member.
# Unlike set.remove(), the discard() method does not raise
# an exception when an element is missing from the set.
print(my_other_set)

my_other_set.update("Shaggy")
# Update the set, adding elements from all others.
print(my_other_set)

my_other_set = {"Sharif", "Giraldo", 18, "Shaggy", "Uniquindio"}
my_set = {18, "Sharif", "Obando", "CharAt", "Univalle"}


print("Sharif" in my_other_set)
# Arroja true o false dependiendo de si el elemento ingresado se encuentra en el set
print("Junio" in my_other_set)


my_set.clear()  # Limpia todo el set, borra todos sus elementos
print(my_set)  # Aparecerá vacío

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# OPERACIONES DE CONJUNTOS

set_uno = {1, 2, 3, 4, 5}
set_dos = {2, 3, 6, 7, 8, 9}

print(set_uno.union(set_dos))
# union() Return a new set with elements from the set and all others.

print(set_uno.intersection(set_dos))
# intersection() Return a new set with elements common to the set and all others

print(set_uno.difference(set_dos))
print(set_dos.difference(set_uno))
# difference Return a new set with elements in the set that are not in the others

print(set_uno.symmetric_difference(set_dos))
# symmetric_difference() Return a new set with elements in either the set or other but not both.


my_set = {"Sharif", "Giraldo", 18}
my_list = list(my_set)
print(my_list)
print(my_list[1])


my_other_set = {"Python", "Java", "C"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union({"JavaScript", "C++"}))

print(my_new_set.difference(my_set))
