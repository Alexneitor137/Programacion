class Cliente:
    def __init__(self, nombre, apellidos, email, direccion):
        # Atributos privados (para usar set/get)
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__direccion = direccion

    # ---------- Métodos GET ----------
    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_email(self):
        return self.__email

    def get_direccion(self):
        return self.__direccion

    # ---------- Métodos SET ----------
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def set_email(self, email):
        self.__email = email

    def set_direccion(self, direccion):
        self.__direccion = direccion

    # ---------- Mostrar información ----------
    def mostrar_info(self):
        print("Nombre:", self.__nombre)
        print("Apellidos:", self.__apellidos)
        print("Email:", self.__email)
        print("Dirección:", self.__direccion)


# ---------- Instanciación del objeto con parámetros ----------
cliente1 = Cliente("Juan", "Pérez Gómez", "Juancho@gmail.com", "Burjassot")
cliente2 = Cliente("Carlos", "Gómez Carreras", "Carlos@gmail.com", "Xirivella")
cliente3 = Cliente("Marta", "Sánchez Baldes", "Marta@gmail.com", "Madrid")

# Mostrar información
cliente1.mostrar_info()

cliente2.mostrar_info()

cliente3.mostrar_info()
# Modificamos los datos del cliente1 usando SET
cliente1.set_email("Juanchi@gmail.com")
cliente1.set_nombre("Juan Carlos")

print("\nDespués de actualizar los datos:")
cliente1.mostrar_info()

# Leer un dato concreto usando GET
print("\nNombre obtenido con get_nombre():", cliente1.get_nombre())

