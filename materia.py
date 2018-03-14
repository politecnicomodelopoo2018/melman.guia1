from alumno import Alumno

class Materia(object):
    nombre=None

    def __init__(self):
        self.lista_notas = []

    def agregarNota(self,nota):
        self.ListaNotas.append(nota)

    def mayorNota(self):
        return max(self.lista_notas)

    def menorNota(self):
        return min(self.lista_notas)

    def PromedioNota(self):
        return sum(self.lista_notas)/len(self.lista_notas)