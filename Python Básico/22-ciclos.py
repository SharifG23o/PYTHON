"""
Programa que muestra el uso de Ciclos en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

"""
BUCLES-CICLOS-LOOPS
Son un mecanismo para iterar, es decir
repetir un mecanismo o ejecución de código 
varias veces
"""

# WHILE

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1


mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1
else:  # Ejecuta justo cuando deja de cumplirse la condición
    # La aplicación del else es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa, hemos salido del bucle")

print("\n")


while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Mi condición es igual a 15")

    print("Mi condición es menor que 20")
    print(mi_condicion)


"""
Si yo necesito detener una ejecución a 
partir de que una condición se cumpla uso break
"""

print("\n")
mi_condicion = 0
while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Se detiene la ejecución")

        break  # Detiene súbitamente el ciclo, sin importar que la condición se siga cumpliendo
    print(mi_condicion)

print("La ejecucuón continúa")


# FOR

"""
Utilizo el bucle for para iterar un listado de 
elementos a partir de una condición
"""

print("\n")

mi_lista = [35, 24, 62, 52, 30, 30, 17]

for elemento in mi_lista:
    print(elemento)

print("\n")

mi_tupla = (18, 1.80, "Sharif", "Giraldo", "Shaggy")
for elemento in mi_tupla:
    print(elemento)

print("\n")

mi_set = {"Sharif", "Giraldo", 18}
for elemento in mi_set:
    print(elemento)

print("\n")

mi_dict = {"Nombre": "Sharif", "Apellido": "Giraldo", "Edad": 18}
for elemento in mi_dict:
    print(elemento)

print("\n")

mi_dict = {"Nombre": "Sharif", "Apellido": "Giraldo", "Edad": 18}
for elemento in list(mi_dict.values()):
    print(elemento)


print("\n")

mi_dict = {"Nombre": "Sharif", "Apellido": "Giraldo", "Edad": 18}
for elemento in mi_dict:
    print(elemento)
    if elemento == "Edad":
        print("Rompiendo ciclo...")
        break
    print("Se ejecuta...")

else:
    print("El bucle for para mi diccionario ha finalizado")

print("Continuando la ejecución...")


for elemento in mi_dict:
    print(elemento)
    if elemento == "Edad":
        continue
    print("Se ejecuta...")

else:
    print("El bucle for para diccionario ha finalizado")


"""
Continue hace algo similar al break, salvo que
no detiene todo el bloque, sino solo la ejecución en ese punto
"""
