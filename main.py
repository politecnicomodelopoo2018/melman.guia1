from alumno import Alumno
import datetime

v1 = Alumno()

nombre=input("ingrese nombre: ")
v1.setnombre(nombre)

apellido=input("ingrese apellido: ")
v1.setapellido(apellido)

año=int (input("ingrese año de nacimiento: "))
mes=int (input("ingrese mes de nacimiento: "))
dia=int (input("ingrese dia de nacimiento: "))
fecha_nac=datetime.date(año,mes,dia)
v1.setFechaNac(fecha_nac)

edad =datetime.date.today() - v1.fecha_naccimiento
edad=edad.days/365.25
edad=int(edad)
print (edad)
