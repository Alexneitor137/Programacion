#Sirve para poder adjuntar varios valores usando comas
datos = "uno,dos,tres,cuatro,cinco,seis"
#Lo mostramos
print(datos)
#Lo transformamos en una lista atraves de split
partido = datos.split(",")
#Lo mostramos
print(partido)
#Unimos todo de nuevo
nueva_cadena = "|".join(partido)
print(nueva_cadena)