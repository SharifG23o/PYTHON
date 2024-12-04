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

mi_otra_lista_2=["Cafe","Chocolate","Té","Aromática"]


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



edad, altura, nombre,apellido= mi_otra_lista 
#Cada elemento, debe ir asignado al orden correspondiente de como se haya designado en la lista
print(nombre)
#Puede ser un foco de errores, dado que mi lista se puede modificar o mutar

print("\n")

nombre,altura,edad,apellido=mi_otra_lista[2],mi_otra_lista[1],mi_otra_lista[0], mi_otra_lista[3]
print(edad)#Es una forma algo 'Rebuscada' y algo complicada de aplicarlo en un programa
#Además, es un posible foco de errores

print("\n")

#Operaciones con funciones en la lista
print(len(mi_otra_lista))#Longitud de elementos que componen la lista
print(mi_otra_lista.count("Sharif"))#Muestra el número de ocurrencias de un dato o elemento que haya en la lista
mi_otra_lista.append("TechMath")#Añade un elemento a la lista en su final
mi_otra_lista.insert(1,"Rojo")#Añade algo en el índice indicado
mi_otra_lista[1]="Azul"
print(mi_otra_lista)
mi_otra_lista.remove("Azul")#Elimina lo asignado en la lista, o el primero que ha encontrado
print(mi_otra_lista)
mi_otra_lista.reverse()#Cambia el orden de la lista, del último al primer elemento
print(mi_otra_lista)
print(mi_lista.pop())
mi_lista.pop()#Remueve el último elemento de la lista
print(mi_lista)
mi_lista.pop(1)#Remueve el elemento del índice indicado


my_pop_element=mi_lista.pop(0)
print(my_pop_element)#Guardo en forma de variable el elemento a ser eliminado

del mi_otra_lista[1] #del es delete y elimina el elemento específico de ese índice en la lista, en resumen, elimina por índice
#Esta forma elimina totalmente el dato seleccionado
print(mi_otra_lista)

mi_otra_lista.clear()#Limpia toda la lista
print(mi_otra_lista)

mi_otra_lista_copiada=mi_otra_lista_2.copy()#Copia la lista 
print(mi_otra_lista_2)
print(mi_otra_lista_copiada)

mi_otra_lista_2.sort()#Ordena de mayor a menor o lanzar en orden alfabético 
print(mi_otra_lista_2)

print(mi_otra_lista_2[1:3])#Se hace un slice o sublista de los elementos que hay entre ciertos índices

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