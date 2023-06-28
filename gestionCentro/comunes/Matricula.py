class Matricula():
    def __init__(self, idmatricula, ciclo, curso, asignaturas):
        self.idmatricula = idmatricula
        self.ciclo = ciclo
        self.curso = curso
        self.asignaturas = asignaturas

    def __str__(self):
        asignaturas_str = ' ||| '.join(str(a) for a in self.asignaturas)
        return str(self.idmatricula) + " | " + self.ciclo + " | " + str(self.curso) + " | " + str(asignaturas_str)



    def añadirAsignatura(self, asignatura):
       self.asignaturas.add(asignatura)

    def renunciarConvocatoria(self, asignatura):
        self.asignaturas.remove(asignatura)

