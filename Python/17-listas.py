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
print(len(mi_otra_lista))#Longitud de elementos que componen la lista
print(mi_otra_lista.count("Sharif"))#Muestra el número de ocurrencias de un dato o elemento que haya en la lista

edad, altura, nombre,apellido= mi_otra_lista #Cada elemento, debe ir asignado al orden correspondiente de como se haya designado en la lista
print(nombre)#Puede ser un foco de errores, dado que mi lista se puede modificar o mutar

print("\n")

nombre,altura,edad,apellido=mi_otra_lista[2],mi_otra_lista[1],mi_otra_lista[0], mi_otra_lista[3]
print(edad)#Es una forma algo 'Rebuscada' y algo complicada de aplicarlo en un programa
#Además, es un posible foco de errores

print("\n")


#CONCATENACIÓN DE LISTAS
print(mi_lista+mi_otra_lista)

print("\n")

#TIPADO DINÁMICO
mi_lista="Hola Python"
print(mi_lista)#Ya NO es lista, puesto que he definido la variable como una de tipo str
print(type(mi_lista))#Verifica que ahora es definida como str

print("\n")

mi_lista=["Hola mundo"]
print(mi_lista)