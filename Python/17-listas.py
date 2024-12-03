"""
Programa que muestra el uso de Listas en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

mi_lista=list()
mi_otra_lista=[]
mi_lista=["Gato","Perro","Pato","Loro"]
print(mi_lista)
print(len(mi_lista))

#En una lista puedo guardar diferentes tipos de datos
mi_otra_lista=[35, 1.80, "Sharif", "Giraldo"]
print(mi_otra_lista)
print(type(mi_otra_lista))#El tipo de dato es una 
print(type(mi_lista))


#ACCEDER A LOS VALORES DE LA LISTA

print(mi_otra_lista[1])#Accedo a la altura, cuyo índice es 1

print(len(mi_lista[2]))

print(mi_lista[2])

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])
print(mi_otra_lista[-4])

#print(mi_otra_lista[-5])
#print(mi_otra_lista[4])
"""
IndexError: list index out of range
porque accedo a un índice fuera del rango de la lista
"""

#Operaciones con funciones en la lista