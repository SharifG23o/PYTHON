"""
Programa que muestra el uso de Strings en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

my_string="Si puedes imaginarlo, puedes programarlo"
my_other_string="Hola mundo"

print(len(my_string))
print(len(my_other_string))

#len mide la longitud del contenido de la variable

print("\n")

print(my_string + " " + my_other_string)

print("\n")

#SALTO DE LÍNEA
my_new_string="Este es un String\ncon salto de línea"
print(my_new_string)

#TABULACIONES

my_tab_string="\tEste es un string con tabulación"
print(my_tab_string)

#ESCAPAR STRINGS

my_scape_string="\tEste es un String \n escapado"
print(my_scape_string)

print("\n")

my_scape_string="\\tEste es un String \n escapado"
print(my_scape_string)
#La doble barra(\\) hace que se anule la tabulación o salto de línea

print("\n")

#FORMATEAR STRINGS

name,surname,age="Sharif","Giraldo",18

print("Mi nombre es %s %s y mi edad es %d")


print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
#con format no es necesario %s, se pone {}


print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))


"""
%s hace que el primer texto que yo le envíe formateado a la cadena
lo incluye en el espacio deseado
"""
"""
{} se usa en el format 

"""

#Inferencia de datos

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

"""
La f string sirve para formatear e inferir el valor de las 
variables previamente definidas

"""