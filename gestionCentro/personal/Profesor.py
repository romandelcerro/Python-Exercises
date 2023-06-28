from personal.PersonalDocente import PersonalDocente


class Profesor(PersonalDocente):
    def __init__(self, nombre, apellidos, dni, edad, id, asignaturas, grupos, horaslectivas):
        PersonalDocente.__init__(self,nombre,apellidos,dni,edad,id)
        self.asignaturas = asignaturas
        self.grupos = grupos
        self.horaslectivas = horaslectivas

    def __str__(self):
        asignatura = ' --- '.join(str(a) for a in self.asignaturas)
        grupo = ' --- '.join(str(g) for g in self.grupos)
        return self.nombre + " | " + self.apellidos + " | " + self.dni + " | " + str(self.edad) \
            + " | " + str(self.id) + " | " + str(asignatura) + " | " + str(grupo) + " | " + str(self.horaslectivas)

    def añadirGrupo(self, grupo):
        self.grupos.append(grupo)

    def añadirAsignatura(self,asignatura):
        self.asignaturas.append(asignatura)

