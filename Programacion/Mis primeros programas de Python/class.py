class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

print("Programa de gestion de clientes")
print("1. Inserta cliente")
print("2. Lista clientes")
print("Programa de gestion de clientes")
print("Programa de gestion de clientes")
print("Programa de gestion de clientes")

clientes = [] #Creo una lista vacia

while True: #Desata un bucle infinito pero controlado

  opcion =  input("Escoge una opcion: ")
  opcion = int(opcion) #convierto a estero