archivo = open("clientes.csv","r")

lineas = archivo.readlines()

for linea in lineas:
    partido = lineas.split(",")
    print(partido)