"""
Programa que muestra el uso de Clases en Python
Autor: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia: GNU GPL v3
"""

"""
A+i como una función no es de utilidad para ejecutar una 
tarea concreta, las clases nos ayudan a crear objetos, es decir
todo lo que está dentro de la clase responde a una lógica correspondiente a ella
"""


# DEFINIR UNA CLASE

class Persona:
    pass
# pass


"""
La sentencia Python pass es una operación nula que no hace nada cuando se ejecuta.
 La sentencia pass suele utilizarse como marcador de posición en el código Python 
 cuando se necesita código, pero no se requiere ninguna acción.

 Tomado de: https://www.datacamp.com/es/tutorial/python-pass

"""


class MiPersona:
    # La clases las palabras se escribe todo junto, mayúscula la primera y sucesivamente
    pass


class MiPersona:
    pass


print(MiPersona)
# <class '__main__.MiPersona'>
print(MiPersona())
# <__main__.MiPersona object at 0x000001822B376A50>


# CONSTRUCTORES

class Persona:
    def __init__(self):
        # __init__ es una palabra reservada del sistema que nos sirve para crear un constructor de clase
        pass


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


mi_persona = Persona("Sharif", "Giraldo")
print(mi_persona.nombre)
# Sharif
print(f"Nombre: {mi_persona.nombre}, Apellido: {mi_persona.apellido}")


"""
class Persona:
    def __init__():
        nombre="Sharif"
        apellido="Giraldo"
        
mi_persona=Persona()
print(f"Nombre: {mi_persona.nombre}, Apellido: {mi_persona.apellido}")

TypeError: Persona.__init__() takes 0 positional arguments but 1 was given


class Persona:
    def __init__(self):
        nombre="Sharif"
        apellido="Giraldo"
        
mi_persona=Persona()
print(f"Nombre: {mi_persona.nombre}, Apellido: {mi_persona.apellido}")

TypeError: Persona.__init__() missing 2 required positional arguments: 'nombre' and 'apellido'

"""


class Persona:
    def __init__(self):
        self.nombre = "Sharif"
        self.apellido = "Giraldo"


mi_persona = Persona()
print(f"Nombre de la persona: {
      mi_persona.nombre}, Apellido de la persona: {mi_persona.apellido}")


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre_completo = f"{nombre} {apellido}"


mi_persona = Persona("Sharif", "Giraldo")
print(mi_persona.nombre_completo)

# almacena el nombre completo y de esta manera se imprime el valor de los parámetros


# ALMACENANDO FUNCIONES EN LA CLASE


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre_completo = f"{nombre} {apellido}"

    def caminar(self,):
        print(f"{self.nombre_completo} está caminando")


mi_persona = Persona("Sharif", "Giraldo")
print(mi_persona.nombre_completo)
mi_persona.caminar()  # Sharif Giraldo está caminando


class Persona:
    def __init__(self, nombre, apellido, apodo="Sin apodo"):
        self.nombre_completo = f"{nombre} {apellido} ({apodo})"

    def caminar(self,):
        print(f"{self.nombre_completo} está caminando")

mi_persona = Persona("Sharif", "Giraldo")
print(mi_persona.nombre_completo)
mi_persona.caminar()


mi_otra_persona = Persona("Luis", "Quintero", "Lucho")
print(mi_otra_persona.nombre_completo)
mi_otra_persona.caminar()

mi_otra_persona.nombre_completo = "Gustavo Cerati Gus"
print(mi_otra_persona.nombre_completo)


#ATRIBUTOS PRIVADOS

class Persona:
    def __init__(self, nombre, apellido, apodo="Sin apodo"):
        self.nombre_completo = f"{nombre} {apellido} ({apodo})"
        self.__nombre=nombre #atributo privado

    def caminar(self,):
        print(f"{self.nombre_completo} está caminando")

mi_persona = Persona("Sharif", "Giraldo")
print(mi_persona.nombre_completo)
mi_persona.caminar()


#GETTER

class Persona:
    def __init__(self, nombre, apellido, apodo="Sin apodo"):
        self.nombre_completo = f"{nombre} {apellido} ({apodo})"
        self.__nombre=nombre #atributo privado
    
    def get_nombre(self): #GETTER
        return self.__nombre

    def caminar(self,):
        print(f"{self.nombre_completo} está caminando")

mi_persona = Persona("Sharif", "Giraldo")
print(mi_persona.nombre_completo)
mi_persona.caminar()

print(mi_persona.get_nombre())