agenda = [
    [
    "Alejandro",
    "Calderón Sánchez",
    "alex@gmail.com",
    "12345678"
],
    [
    "Manuel",
    "Serrano Lopez",
    "manu@gmail.com",
    "12345687"
]
]

# Acceder al primer elemento
print(agenda[0])
# Acceder al primer elemento del primer elemento
print(agenda[0][0])
# Modificamos el primer valor del primer elemento de la lista
agenda[0][0] = "Jaime"
print(agenda[0][0])