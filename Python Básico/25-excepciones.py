"""
Programa que muestra el uso de Excepciones en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

# print(5+"5") TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""
numero_uno,numero_dos=5,1
numero_dos="1"
print(numero_uno+numero_dos)

TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""

numero_uno, numero_dos = 5, 9
numero_dos = "7"

# Manejo del error:

if type(numero_dos) == int:
    print(numero_uno+numero_dos)
else:
    print("NO se puede realizar una operación entre un tipo int y string")


numero_uno, numero_dos = 5, 9

if type(numero_dos) == int:
    print(numero_uno+numero_dos)
else:
    print("NO se puede realizar una operación entre un tipo int y string")


print("\n")

# TRY- EXCEPT

numero_dos = "1"
try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except:
    print("Se ha producido un error")


numero_dos = 4
try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except:
    print("Se ha producido un error")


print("\n")


# TRY-EXCEPT-ELSE

numero_uno = 2
numero_dos = 20

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except:
    # Se ejecuta si se produce ninguna excepción
    print("Se ha producido un error")

else:
    # Se ejecuta si no se produce ninguna excepción
    print("La ejecución continúa correctamente")


print("\n")

# TRY-EXCEPT-ELSE-FINALLY

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except:
    # Se ejecuta si se produce ninguna excepción
    print("Se ha producido un error")

else:
    # Se ejecuta si no se produce ninguna excepción
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")


print("\n")

numero_dos = "3"

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except:

    print("Se ha producido un error")

else:

    print("La ejecución continúa correctamente")
finally:
    # Se ejecuta siempre con o sin error
    print("La ejecución continúa")


#Captura de excepciones por tipo
print("\n")
try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except TypeError:
    #Solo se ejecuta si se produce un TypeError

    print("Se ha producido un error")


"""

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except ValueError:
   

    print("Se ha producido un error")

TypeError: unsupported operand type(s) for +: 'int' and 'str'

vUELVE A DAR ERROR DADO QUE LE ESPECIFIQUÉ QUE 
LANZARA LA EXCEPCIÓN CUANDO OCURRIERA UN ValueError en vez de un TypeError

"""

#Capta el tipo de error producido, en este caso, un TypeError

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except ValueError:

    print("Se ha producido un ValueError")

except TypeError:

    print("Se ha producido un TypeError")


print("\n")

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except TypeError as error:

    print(error)


print("\n")

try:
    print(numero_uno+numero_dos)
    print("No se ha producido error")

except TypeError as error:

    print(error)

except Exception as exception:
    print(exception)
