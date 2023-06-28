from comunes.Asignatura import Asignatura
from comunes.Matricula import Matricula
from comunes.Contacto import Contacto
from comunes.Grupo import Grupo
from personal.Profesor import Profesor
from personal.Alumno import Alumno


asig1 = Asignatura("Lenguajes de marcas", "DAW", 1, 200)
asig2 = Asignatura("Programacion", "DAW", 1, 300)
asig3 = Asignatura("Lenguajes de servidor", "DAW", 2, 250)
asig4 = Asignatura("Lenguajes de cliente", "DAW", 2, 400)
asig5 = Asignatura("Lenguajes de marcas", "DAM", 1, 210)
asig6 = Asignatura("Programacion", "DAM", 1, 320)
asig7 = Asignatura("Aplicaciones para moviles", "DAM", 2, 270)
asig8 = Asignatura("Acceso a datos", "DAM", 2, 310)

#Los conjuntos no permiten duplicados inicialmente.
conjunto1 = {asig5, asig6, asig5}
conjunto2 = {asig7, asig8}
conjunto3 = {asig1, asig2}
conjunto4 = {asig3, asig4}


listaContactos1 = [611111111,611111112,611111113]
listaContactos2 = [611111114,611111115,611111116]
listaContactos3 = [611111117,611111118,611111119]
listaContactos4 = [611111110,611111120,611111130]
listaContactos5 = [611111140,611111150,611111160]
listaContactos6 = [611111170,611111180,611111190]
listaContactos7 = [611111100,611111102,611111103]
listaContactos8 = [611111104,611111105,611111106]

contacto1 = Contacto(listaContactos1, "@gmail.com")
contacto2 = Contacto(listaContactos2, "@gmail.com")
contacto3 = Contacto(listaContactos3, "@gmail.com")
contacto4 = Contacto(listaContactos4, "@gmail.com")
contacto5 = Contacto(listaContactos5, "@gmail.com")
contacto6 = Contacto(listaContactos6, "@gmail.com")
contacto7 = Contacto(listaContactos7, "@gmail.com")
contacto8 = Contacto(listaContactos8, "@gmail.com")


matricula1 = Matricula(1, "DAM", 1, conjunto1)
matricula2 = Matricula(2, "DAM", 3, conjunto2)
matricula3 = Matricula(3, "DAW", 1, conjunto3)
matricula4 = Matricula(4, "DAW", 2, conjunto4)

alum1 = Alumno("Mario", "Román", "04245321G", 20, 1, matricula1, contacto1)
alum2 = Alumno("Jesus", "Tonto", "01111111A", 80, 2, matricula1, contacto2)
alum3 = Alumno("Alfonso", "Díaz", "0111111B", 20, 3, matricula2, contacto3)
alum4 = Alumno("Marisa", "Velarde", "01111111C", 40, 4, matricula2, contacto4)
alum5 = Alumno("Tovías", "Eustaquio", "01111111D", 30, 5, matricula3, contacto5)
alum6 = Alumno("Vinicius", "Vini", "01111111E", 22, 6, matricula3, contacto6)
alum7 = Alumno("Ruben", "Ruiz", "01111111F", 25, 7, matricula4, contacto7)
alum8 = Alumno("Ramiro", "Ramiro", "01111111G", 30, 8, matricula4, contacto8)

listaAlumDam1 = [alum1,alum2]
listaAlumDam2 = [alum3,alum4]
listaAlumDaw1 = [alum5,alum6]
listaAlumDaw2 = [alum7,alum8]

#Ordeno por nombre y apellidos las listas de alumnos
listaAlumDam1.sort()
listaAlumDam2.sort()
listaAlumDaw1.sort()
listaAlumDaw2.sort()

grupo1 = Grupo("DAM", 1, listaAlumDam1)
grupo2 = Grupo("DAM", 2, listaAlumDam2)
grupo3 = Grupo("DAW", 1, listaAlumDaw1)
grupo4 = Grupo("DAW", 2, listaAlumDaw2)

listaAsigDam1 = [asig5, asig6]
listaAsigDam2 = [asig7, asig8]
listaAsigDaw1 = [asig1,asig2]
listaAsigDaw2 = [asig3, asig4]

listaGrupo1 = [grupo2,grupo1]
listaGrupo2 = [grupo3,grupo4]
listaGrupo3 = [grupo1,grupo3]
listaGrupo4 = [grupo4,grupo2]

#Ordeno por curso y ciclo las listas de grupos
listaGrupo1.sort()
listaGrupo2.sort()
listaGrupo3.sort()
listaGrupo4.sort()

profesor1 = Profesor("Ruben", "Ruiz", "00000000A", 40, 9, listaAsigDam1, listaGrupo1, 200)
profesor2 = Profesor("Marisa", "Martin", "00000000B", 30, 10, listaAsigDam2, listaGrupo3, 100)
profesor3 = Profesor("Ramiro", "Velazquez", "00000000C", 40, 11, listaAsigDaw1, listaGrupo4, 150)
profesor4 = Profesor("Fernando", "Mateo", "00000000D", 43, 12, listaAsigDaw2, listaGrupo2, 210)

#Muestro los grupos ordenados de los profesores por Curso y ciclo
for g in profesor1.grupos:
    print(g)
print()

#Recorro el conjunto1 para mostrar que no salen asignaturas duplicadas
for a in conjunto1:
    print(a)
print()

#Recorro la listaAlumDam2 para mostrar que los alumnos están ordenados por nombre y apellidos
for a in listaAlumDam1:
    print(a)
print()

#Uso de los métodos de la clase Contacto
print(contacto1.__str__())
contacto1.añadirTlf(600000000)
print(contacto1.__str__())

contacto1.eliminarTlf(600000000)
print(contacto1.__str__())
print()

#Uso de los métodos de la clase Grupo
print(grupo1.__str__())
grupo1.altaAlumno(alum3)
print(grupo1.__str__())
grupo1.bajaAlumno(alum3)
print(grupo1.__str__())
print()

#Uso de los métodos de la clase Matrícula
print(matricula1.__str__())
matricula1.añadirAsignatura(asig3)
print(matricula1.__str__())
matricula1.renunciarConvocatoria(asig3)
print(matricula1.__str__())
print()

#Uso de los métodos de la clase Profesor
print(profesor1.__str__())
profesor1.añadirGrupo(grupo3)
profesor1.añadirAsignatura(asig8)
print(profesor1.__str__())


