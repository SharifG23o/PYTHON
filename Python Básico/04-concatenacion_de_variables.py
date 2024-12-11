"""
Programa que muestra cómo concatenar variables
Autor: Sharif Giraldo Obando
Fecha: Noviembre de 2024
Licencia: GNU GPL v3
"""


my_int_variable = 3
my_float_variable = 23.5
my_str_variable = "Hola mundo"
my_bool_variable = False


# Concatenación de variables en un print
print(my_int_variable, my_float_variable, my_str_variable)

print(type(print(my_int_variable, my_float_variable, my_str_variable)))
# La salida impresa será NoneType, dado que hay varios tipos de datos y es un print

print("Este es el valor de : ", my_bool_variable)
