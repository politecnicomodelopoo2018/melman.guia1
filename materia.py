class Materia(object):
    nombre=None

    def __init__(self):
        self.lista_notas = []

    def agregarNota(self,nota):
        self.lista_notas.append(nota)
        return(self.lista_notas)

    def mayorNotaMateria(self,lista_notas):
        return max(lista_notas)

    def menorNotaMateria(self,lista_notas):
        return min(lista_notas)

    def PromedioNotaMateria(self,lista_notas):
        return sum(lista_notas)/len(lista_notas)