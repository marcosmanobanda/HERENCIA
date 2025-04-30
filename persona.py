class Persona:
    def __init__(self, nombre: str, genero: str, edad: int, direccion: str):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    # @nombre.setter
    # def nombre(self, nuevo_nombre):
    #     if isinstance(nuevo_nombre, str) and nuevo_nombre:
    #         self._nombre = nuevo_nombre
    #     else:
    #         raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def genero(self):
        return self._genero

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        if isinstance(nueva_direccion, str) and nueva_direccion:
            self._direccion = nueva_direccion
        else:
            raise ValueError("La dirección debe ser una cadena no vacía.")

    def __str__(self):
        return str(self.__dict__)

print(__name__)
# Ejemplo de uso
persona1 = Persona("Guillermo", "Masculino", 30, "Guayaquil, Ecuador")
print(persona1)

# Modificando atributos de manera controlada
persona1.nombre = "Guillermo Pérez"
persona1.edad = 31
print(persona1)