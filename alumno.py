class Alumno(object):
    nombre=None
    apellido=None
    fecha_naccimiento=None

    def __init__(self):
        self.lista_notas = []

    def setnombre(self,nombre):
        self.nombre=nombre

    def setapellido(self,apellido):
        self.apellido=apellido

    def setFechaNac(self,fecha):
        self.fecha_naccimiento=fecha

    def setAgregarNota(self,nota):
        if nota < 1 and nota > 10:
            return false
        self.lista_notas.append(nota)

    def mayorNota(self):
        return max(self.lista_notas)

    def menorNota(self):
        return min(self.lista_notas)

    def PromedioNota(self):
        return sum(self.lista_notas)/len(self.lista_notas)