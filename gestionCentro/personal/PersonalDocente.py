from abc import ABC, abstractmethod

class PersonalDocente(ABC):

    @abstractmethod
    def __init__(self, nombre, apellidos, dni, edad, id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad
        self.id = id

    @abstractmethod
    def __str__(self):
        return self.nombre + self.apellidos + self.dni + self.edad + self.id
