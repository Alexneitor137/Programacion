import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.bin","wb")
    pickle.dump(menu,archivo)
    archivo.close()
    elif opcion == 4