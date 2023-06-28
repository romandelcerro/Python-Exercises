from personal.PersonalDocente import PersonalDocente


class Alumno(PersonalDocente):
    def __init__(self, nombre, apellidos, dni, edad ,id, matricula, contactos):
        PersonalDocente.__init__(self,nombre, apellidos, dni, edad, id)
        self.matricula = matricula
        self.contactos = contactos

    def __str__(self):
        return self.nombre + " | " + self.apellidos + " | "+ self.dni + " | "+ str(self.edad) +  " | " + str(self.id)+\
            " | " + str(self.matricula) + " | " + str(self.contactos)

    #Funcion que utiliza .sort() para ordenar objetos Alumno por nombre y apellidos
    def __lt__(self, other):
        if self.nombre == other.nombre:
            return self.apellidos < other.apellidos
        return self.nombre < other.nombre
