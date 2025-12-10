from datetime import datetime 
import math

filas = 0
asistentes = 0
asientos_por_fila = 0
satisfaccion_manolo = 5.4
satisfaccion_carla = 9.7
satisfaccion_juan = 8.5

asistentes = int(input("¿Cuantas personas van a asistir?: "))
asientos_por_fila = int(input("¿Cuantos asientos va a haber por fila?: "))
filas = math.ceil(asistentes / asientos_por_fila)
print("Necesitaras",filas,"filas")

fecha_str = input("Ingresa una fecha (formato DD/MM/AAAA): ")

fecha_evento = datetime.strptime(fecha_str, "%d/%m/%Y")
print("Informe de fecha:")
print("La fecha ingresada es:", fecha_evento.date())
print("Dia: ",fecha_evento.day)
print("Mes: ",fecha_evento.month)
print("Año: ",fecha_evento.year)



satisfaccion_promedio = round(satisfaccion_manolo, satisfaccion_carla, satisfaccion_juan)

print("Satisfaccion promedio: ", satisfaccion_promedio)