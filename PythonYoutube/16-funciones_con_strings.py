"""
Programa que muestra el uso de funciones en Strings en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

language="python"
a,b,c,d,e,f=language

print(language.capitalize())#Pone la primera letra en mayúscula
print(language.upper())#Todo en mayúsculas
print(language.lower())#Todo en minúsculas
print(language.count("a"))#Cuenta cuántos caracteres hay
print(len(language))#Imprime la longitud de la variable
print(language.isnumeric())#Me dice si es un número
print(language.isupper())#Me dice si está en minúscula
print(language.isalpha())
print(language.isascii())
print(language.islower())
print(language.isprintable())
print(language.isdecimal())
print(language.isdigit())
print(language.isidentifier())
print(language.isspace())
print(language.istitle())
print(language.upper().isupper())
print(language.startswith("py"))
print(language.startswith("th"))
