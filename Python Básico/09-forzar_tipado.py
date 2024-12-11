"""
Programa que muestra como forzar el tipado de una variable
Autor: Sharif Giraldo Obandp
Fecha: Nobiembre de 2024
Licencia: GNU GPL v3
"""

# Forzamos el tipado
address: str = "Mi dirección"
address: int = 32
address = True

print(address)
print(type(address))

# Guarda el último valor
# Python es débilmente tipado
