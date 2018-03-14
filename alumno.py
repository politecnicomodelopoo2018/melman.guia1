import datetime
from materia import Materia

class Alumno(object):
    nombre=None
    apellido=None
    fecha_naccimiento=None

    def __init__(self):
        self.lista_materias = []

    def setnombre(self,nombre):
        self.nombre=nombre

    def setapellido(self,apellido):
        self.apellido=apellido

    def setFechaNac(self,fecha):
        self.fecha_naccimiento=fecha

    def setAgregarNota(self,nota,materia):
        if nota < 1 and nota > 10:
            return False
        for item in self.lista_materias:
            if materia == item:
                item.agragarNota(nota)
                return

    def EdadAct(self):
        edad = datetime.date.today() - self.fecha_naccimiento
        edad = edad.days / 365.25
        edad = int(edad)
        return edad

    def AgragarMateria(self,materia):
        mate=Materia(materia)
        self.lista_materias.append(mate)

