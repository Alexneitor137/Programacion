import math
import datetime

cuadras_requeridas = int(0)
caballos = int(0)
caballos = int(input("¿Cuantos caballos tienes?: "))
CAPACIDAD_POR_CUADRA = int(3)

d = int(input("Dia: "))
m = int(input("Mes: "))
y = int(input("Año: "))
date = datetime.date(y,m,d)
print("Fecha final: ",date)

cuadras_requeridas = math.ceil(caballos / CAPACIDAD_POR_CUADRA)
print("Necesitas",cuadras_requeridas,"cuadras para mantener a todos tus caballos")

diadelasemana = date.weekday()
print(diadelasemana)
diadelasemana = date.isoweekday()
print(diadelasemana)