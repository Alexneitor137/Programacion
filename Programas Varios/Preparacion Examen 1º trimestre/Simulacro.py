import pickle
class Cliente():
    def __init__(self,nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

print("#####Gestion de clientes v0.1#####")
print("#####Alejandro Calderón Sánchez")

clientes = [] #Clientes = lista

try: # Ojo que igual no existe el archivo
    archivo = open("clientes.dat", "rb")
    clientes = pickle.load("archivo")
    archivo.close()
except:
    print("No existe ese archivo de datos")

while True: #Creamos bucle
    archivo = open("clientes.dat", "wb")
    pickle.dump(clientes, archivo)
    archivo.close()

    print("Escoje una opcion: ")
    print("1.Insertar un cliente")
    print("2Listar clientes")
    print("3.Actualizar un cliente")
    print("4.Eliminar un cliente")
    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre, apellidos, email))
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID: ", identificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1
    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email
    elif opcion == 4:
        identificador = int(input("Introduce el ID a eliminar: "))
        confirmacion = input("¿Estas seguro? (S/N): ")
        if confirmacion == "S" or confirmacion == "s" or confirmacion == "SI" or confirmacion == "si":
            clientes.pop(identificador) 
        elif confirmacion == "N" or confirmacion == "n" or confirmacion == "NO" or confirmacion == "no":
            print("Cancelado")
        else:
            print("Opcion no valida")
    archivo = open("clientes.bin", "wb")
    pickle.dump(clientes,archivo)
    archivo.close()