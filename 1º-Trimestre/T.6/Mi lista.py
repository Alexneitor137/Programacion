import json


print("Lista de videojuegos v0.1")

lista_de_la_compra = []

while True:
    print("Selecciona una opcion")
    print("1.-Añadir un elemento a la lista")
    print("2.-Leer la lista")
    opcion = int(input("Tu opción: "))

    if opcion == 1:
        print("Añadimos un elemento a la lista: ")
        nombre = input("Indica el nombre del Videojuego: ")
        precio = input("Indica el precio: ")
        salida = input("Induca su fecha de salida: ")
        lista_de_la_compra.append({"nombre":nombre,"precio":precio,"salida":salida})
        archivo = open("lista.json","w")
        json.dump(lista_de_la_compra,archivo)
        archivo.close()
    elif opcion == 2:
        print("Listamos los elementos de la lista: ")
        for juego in lista_de_la_compra:
            print("#################################")
            print("Juego:",juego['nombre'])
            print("Precio:",juego['precio'])
            print("Fecha de salida",juego['salida'])
            print("#################################")