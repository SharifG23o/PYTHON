"""
Programa que muestra el uso de Diccionarios en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

"""
Un diccionario en Python es una colección de elementos, 
donde cada uno tiene una llave key y un valor value. 
Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.

Algunas propiedades de los diccionario en Python son las siguientes:

Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
Son indexados, los elementos del diccionario son accesibles a través del key.
Y son anidados, un diccionario puede contener a otro diccionario en su campo value.

Tomado de: https://ellibrodepython.com/diccionarios-en-python
"""
#Formas de crear un diccionario

my_dict=dict()
my_other_dict={}

print(type(my_dict)) #<class 'dict'>
print(type(my_other_dict)) #<class 'dict'>


my_other_dict={"Nombre":"Sharif", "Apellido":"Giraldo", "Edad":18}

my_dict={"Nombre":"Sharif", "Apellido":"Giraldo", "Edad":18, "Lenguajes":{"Python","Java","C"}, 1:1.80 } #En este caso se nos presenta un diccionario que contiene un set dentro

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))

print(len(my_dict))


print(my_dict["Nombre"])#Llamo a la key o clave del dato en el dict e imprime el nombre

#Actualizo el valor asignado a nombre
my_dict["Nombre"]="Alejandro"
print(my_dict["Nombre"])


#Añado un valor al diccionario
my_dict["Calle"]="Calle de los Programadores"
print(my_dict)

#OPERACIONES CON DICCIONARIOS

print(my_dict.get("Apellido"))
#get() Return the value for key if key is in the dictionary, else default

del my_dict["Calle"]# del, por defecto, elimina el key value seleccionado
print(my_dict)

print(my_dict.items())
#items()
#(method) def items() -> dict_items[str | int, Any]
#Return a set-like object providing a view on the dict's items.

print(my_dict.values())
#values() Return an object providing a view on the dict's values.

print(my_dict.keys())
#keys() Return a set-like object providing a view on the dict's keys

print(my_dict.popitem())

print(my_dict.pop("Edad"))
#pop() remove specified key and return the corresponding value.

#If the key is not found, return the default if given; otherwise, raise a KeyError.

print(my_dict.fromkeys("Estrato"))
#fromkeys() Create a new dictionary with keys from iterable and values set to value.

print(my_dict.setdefault("Nombre"))

print(my_dict.update())
print(my_dict.copy())
print(my_dict.clear())

my_dict={"Nombre":"Sharif", "Apellido":"Giraldo", "Edad":18, "Lenguajes":{"Python","Java","C"}, 1:1.80 }

print("Nombre" in my_dict)#Busca las llaves o keys