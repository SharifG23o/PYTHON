"""
Programa que muestra el uso de Condicionales en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""


"""
Los condicionales representan la manera de implementar
flujos de ejecución en nuestro programa

"""

# SINTAXIS


"""
Su forma es: 

Se cumple condición - Ejecuto 

"""

mi_condicion = False

if mi_condicion:  # Para que se ejecute debe ser verdadero en este caso
    print("Se ejecuta la condición del if")

print("La ejecución continúa")


mi_condicion = True

if mi_condicion:  # Para que se ejecute debe ser verdadero en este caso
    print("Se ejecuta la condición del if")

print("La ejecución continúa")


mi_condicion = False

if mi_condicion == True:
    """
    Si bien se le puede asignar el true a la variable, 
    es algo redundante, dado que implicitamente al hacer un if
    se debe cumplir la condición, que predeterminadamente es un true

    if mi_condicion == if mi_condicion==True

    """

    print("Se ejecuta la condición del if")

print("La ejecución continúa")

print("\n")

mi_condicion = 5*2
# (variable) mi_condicion: Literal[10]

if mi_condicion:

    # (variable) mi_condicion: Literal[10]

    print("Se ejecuta la condición de este segundo if")

print("La ejecución continúa")


# DELIMITANDO LA CONDICIÓN:

mi_condicion = 5*2


if mi_condicion == 11:

    print("Se ejecuta la condición de este  if")

print("La ejecución continúa")


mi_condicion = 5*2


if mi_condicion == 10:

    print("Se ejecuta la condición de este  if")

print("La ejecución continúa")


mi_condicion = 5*2


if mi_condicion >= 10:

    print("Se ejecuta la condición de este tercer if")

print("La ejecución continúa")

mi_condicion = 5*2


if mi_condicion > 10:

    print("Se ejecuta la condición de este tercer if")

print("La ejecución continúa")

# Si quiero que se ejecute cuando la condición no se cumpla

mi_condicion = 5*2


if mi_condicion > 10:

    print("Es mayor que 10")

else:
    print("Es menor o igual que 10")

print("La ejecución continúa")

"""
Tener un else es como decir:

Si no se cumple esta condición, ejecuta la otra que se encuentra aquí

"""


# MÁS DE UNA CONDICIÓN

mi_condicion = 5*2


# Para que funcione el if, ahora debe cumplir estas 2 condiciones
if mi_condicion > 10 and mi_condicion < 20:

    print("Es mayor que 10 y menor que 20")

else:
    print("Es menor o igual que 10 o mayor que 20")

print("La ejecución continúa")


print("\n")

mi_condicion = 5*5


# Para que funcione el if, ahora debe cumplir estas 2 condiciones
if mi_condicion > 10 and mi_condicion < 20:

    print("Es mayor que 10 y menor que 20")

else:
    print("Es menor o igual que 10 o mayor que 20")

print("La ejecución continúa")


print("\n")

mi_condicion = 5*3


if mi_condicion > 10 and mi_condicion < 20:

    print("Es mayor que 10 y menor que 20")

else:
    print("Es menor o igual que 10 o mayor que 20")

print("La ejecución continúa")


# elif
# if y elif necesitan de una condición
print("\n")

mi_condicion = 1*1

if mi_condicion > 10 and mi_condicion < 20:

    print("Es mayor que 10 y menor que 20")
elif mi_condicion == 1:
    print("Es igual a 1")

else:
    print("Es menor o igual que 10 o mayor que 20")

print("La ejecución continúa")


my_string = "Mi cadena de texto "
if my_string:
    print("Mi cadena de texto no es vacía")


my_string = "Mi cadena de texto "
if my_string == "Mi cadena de texto ":
    print("Mis cadenas de texto coinciden")


my_string = "Mi cadena de texto "
if my_string != "Mi cadena de textoooooo ":
    print("Mis cadenas de texto no coinciden")
else:
    print("Las cadenas de texto coinciden")


"""
Si ahora niego la condición de mi cadena
la condición de mi ejecución se va a cumplir

"""
my_string = ""
if not my_string:
    print("Mi cadena de texto  es vacía")
