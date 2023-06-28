class Grupo():
    def __init__(self, ciclo, curso, alumnos):
        if ciclo not in ('DAM', 'DAW') or curso not in (1, 2):
            print("Grupo incorrecto")
        self.ciclo = ciclo
        self.curso = curso
        self.alumnos = alumnos

    def __str__(self):
        alumnos = ' --- '.join(str(a) for a in self.alumnos)
        return self.ciclo + " | " + str(self.curso) + " | " + str(alumnos)

    def altaAlumno(self, alum):
        self.alumnos.append(alum)

    def bajaAlumno(self, alum):
        self.alumnos.remove(alum)

    #Ordeno los grupos por curso y ciclo
    def __lt__(self, other):
        if self.curso == other.curso:
            return self.ciclo < other.ciclo
        return self.curso < other.curso

