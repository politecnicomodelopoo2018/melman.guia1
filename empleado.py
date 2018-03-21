import datetime

class Empleado(object):
    nombre=None
    apellido=None
    telefono=None
    fecha_Nac=None
    fecha_ingre=None

    def __init__(self):

        fecha_dias = []
        asist = []
        cuando =[]
        porcentaje = []
#weekday devuelve dia de la semana por numero empieza 0 lunes
    def dia_ingrso(self,fecha):
        self.fecha_ingreso=self.fecha_dias[0].days

    def ingreso(self,dia):
        self.asist += dia

    def chequeo(self):
        for item in self.asist
            dia=item.weekday
            if self.cuando[dia]==True
                cant_asist+=1



    def porcentaje(self):
        porcen_total = 0
        i=0
        for item in self.porcentaje:
            porcen_total += item
            i+=1
        return(porcen_total/i)