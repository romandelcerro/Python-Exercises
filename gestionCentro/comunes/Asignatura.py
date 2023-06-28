class Asignatura():
    def __init__(self,nombre,ciclo,curso,horas):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso
        self.horas = horas

    def __str__(self):
        return self.nombre + " | " + self.ciclo + " | " +  str(self.curso) + " | " +  str(self.horas) + " horas"
