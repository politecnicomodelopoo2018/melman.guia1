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

























































































v1.setnombre("nicolas")