import datetime
from materia import Materia


class Alumno(object):
    nombre = None
    apellido = None
    fecha_naccimiento = None

    def __init__(self):
        self.lista_materias = []

    def setnombre(self, nombre):
        self.nombre = nombre

    def setapellido(self, apellido):
        self.apellido = apellido

    def setFechaNac(self, fecha):
        self.fecha_naccimiento = fecha

    def setAgregarNota(self, nota, materia):
        if nota < 1 and nota > 10:
            return False
        for item in self.lista_materias:
            if materia == item:
                item.agragarNota(nota)
                return

    def mayorNotaAlum(self, materia):
        for item in self.lista_materias:
            if materia == item:
                item.mayorNotaMateria(item.lista_notas)

    def menorNotaAlum(self, materia):
        for item in self.lista_materias:
            if materia == item:
                item.menorNotaMateria(item.lista_notas)

    def PromedioNotaAlum(self, materia):
        for item in self.lista_materias:
            if materia == item:
                item.promedioNotaMateria(item.lista_notas)

    def EdadAct(self):
        edad = datetime.date.today() - self.fecha_naccimiento
        edad = edad.days / 365.25
        edad = int(edad)
        return edad

    def AgragarMateria(self, materia):
        mate = Materia(materia)
        self.lista_materias.append(mate)

    def MenorNotaTotal(self, lista_materias):
        menor_nota = 0
        for item in lista_materias:
            nota_actual = item.menorNotaMateria(item.lista_notas)
            if menor_nota < nota_actual:
                menor_nota = nota_actual
        return (menor_nota)

    def PromedioTotal(self, lista_materias):
        sum_promedio = 0
        for item in lista_materias:
            sum_promedio = sum_promedio + item.promedioNotaMateria
        final_promedio = sum_promedio / len(lista_materias)
        return (final_promedio)

    def MenorPromedioTotal(self, lista_materias):
        menor_promedio = 0
        for item in lista_materias:
            promedio_actual = item.PromedioMateria(item.lista_notas)
            if menor_promedio < promedio_actual:
                menor_promedio = promedio_actual
        return (menor_promedio)

    def MayorPromedioTotal(self, lista_materias):
        mayor_promedio = 0
        for item in lista_materias:
            promedio_actual = item.PromedioMateria(item.lista_notas)
            if mayor_promedio > promedio_actual:
                mayor_promedio = promedio_actual
        return (mayor_promedio)
