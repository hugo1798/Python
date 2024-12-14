class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia

    def __str__(self):
        return (f'ID {self._id},'
                f'Nombre {self._nombre},'
                f'Apellido {self._apellido},'
                f'Membresia {self._membresia}')

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def membresia(self):
        return self._membresia

    @membresia.setter
    def membresia(self, membresia):
        self._membresia = membresia

if __name__ == '__main__':
    cliente1 = Cliente(1, 'Emmanuel', 'Ramos', 900)
    print(cliente1.nombre)
    cliente1.nombre = 'Alejandro'
    print(cliente1.nombre)