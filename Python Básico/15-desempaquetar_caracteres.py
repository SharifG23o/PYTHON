"""
Programa que muestra el uso de Desempaquetar Caracteres en Strings en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("\n")

# Division de Strings

language_slice = language[1:3]  # Del primer al tercer caracter
print(language_slice)

language_slice = language[1:]  # Del primer al último caracter
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]  # Forma de evitar caracteres
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)
