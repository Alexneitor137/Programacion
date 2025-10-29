class Nacion:
    def __init__(self, nombre, poblacion, recursos):
        self.nombre = nombre
        self.poblacion = poblacion
        self.recursos = recursos

# Creación del objeto
españa = Nacion("España", 48000000, ["turismo", "agricultura", "energía renovable"])

print("Datos del país:")
print("Nombre: ", españa.nombre)
print("Población: ", españa.poblacion, "habitantes")
print("Recursos principales: ", españa.recursos)