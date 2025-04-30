from persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, genero, edad, direccion, sueldo):
      Persona.__init__(self, nombre, genero, edad, direccion)
      self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, value):
        self._sueldo = value

if __name__ == '__main__':
    emp1 = Empleado('Luis', 'M', '22', 'Norte',2000)
    print(emp1)
