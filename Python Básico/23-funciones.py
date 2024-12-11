"""
Programa que muestra el uso de Funciones en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

# def es la palabra reservada para crear una función


def mi_funcion():  # Definimos la función
    print("Esto es una función")


mi_funcion()


# Lo que está dentro de los paréntesis los denominamos parámetros
def sumar_dos_valores(numero_uno, numero_dos):
    print(numero_uno+numero_dos)


sumar_dos_valores(2, 3)
sumar_dos_valores(234558, 3435305909)


def sumar_dos_valores(numero_uno: int, numero_dos: int):
    print(numero_uno+numero_dos)


sumar_dos_valores(2, 3)
sumar_dos_valores(234558, 3435305909)
sumar_dos_valores(23.5, 7.99)
sumar_dos_valores("3", "1")
"""
En el último caso devolverá 31
dado que a causa del tipado débil de 
Python las 2 cadenas se concatenarán
asi fuerce el tipado como se muestra en el
ejemplo

"""


def dividir_valores(primer_valor, segundo_valor):
    print(primer_valor/segundo_valor)


dividir_valores(2, 1)
dividir_valores(15, 3)
# dividir_valores("3","2") TypeError: unsupported operand type(s) for /: 'str' and 'str'


# no retornará nada, pues el retorno o resultado de una función debe estar asignado a una variable
def sumar_dos_valores_con_return(valor_uno, valor_dos):
    return valor_uno+valor_dos


sumar_dos_valores_con_return(10, 5)


# Esto tampoco retornará nada
def sumar_dos_valores_con_return(valor_uno, valor_dos):
    return valor_uno+valor_dos


mi_resultado = sumar_dos_valores_con_return(10, 5)
mi_resultado = sumar_dos_valores_con_return(1.4, 5.2)
print(mi_resultado)  # None


mi_resultado = sumar_dos_valores_con_return(10, 5)
print(sumar_dos_valores_con_return(10, 5))


mi_resultado = sumar_dos_valores_con_return(10, 5)
print(mi_resultado)


def imprimir_nombre(nombre, apellido):
    print(f"{nombre} {apellido}")


imprimir_nombre("Sharif", "Giraldo")


def imprimir_nombre(nombre, apellido):
    print(f"{nombre} {apellido}")


imprimir_nombre(apellido="Giraldo", nombre="Sharif")


# Le paso un valor por defecto al alias, sin embargo, se sigue imprimiendo lo último que guardé
def imprimir_nombre_con_default(nombre, apellido, apodo="Shari"):
    print(f"{nombre} {apellido} {apodo}")


imprimir_nombre_con_default("Sharif", "Giraldo", "Shaggy")

# Ahora bien:


def imprimir_nombre_con_default(nombre, apellido, apodo="Shari"):
    print(f"{nombre} {apellido} {apodo}")


imprimir_nombre_con_default("Sharif", "Giraldo")

# Dado que:
"""
(function) def imprimir_nombre_con_default(
    nombre: Any,
    apellido: Any,
    apodo: str = "Shari"
) -> None

"""


def imprimir_textos(texto):
    print(texto)


imprimir_textos("Hola mundo")


# Si quiero imprimir varios textos

def imprimir_textos(*texto):
    print(texto)


imprimir_textos("Hola", "Bienveni@s al mundo de la programación", "En python")


def imprimir_textos(*textos):
    for texto in textos:
        print(texto)


imprimir_textos("Hola", "Bienveni@s al mundo de la programación", "En python")
imprimir_textos("Hola ")
