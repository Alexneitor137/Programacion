class Cliente:
    """
    Representa a un cliente en una tienda virtual.
    """
    def __init__(self, nombre, apellidos, email, direccion):
        """
        Constructor de la clase Cliente. Inicializa las propiedades.

        :param nombre: Nombre del cliente.
        :param apellidos: Apellidos del cliente.
        :param email: Correo electrónico del cliente.
        :param direccion: Dirección de envío del cliente.
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion

    def __str__(self):
        """
        Método especial para obtener una representación en cadena del objeto Cliente.
        """
        return (f"Nombre Completo: {self.nombre} {self.apellidos}\n"
                f"Email: {self.email}\n"
                f"Dirección: {self.direccion}")

# Creación del primer objeto Cliente
cliente1 = Cliente(
    nombre="Jose Vicente",
    apellidos="Carratala Sanchis",
    email="jose.vicente@ejemplo.com",
    direccion="Calle Falsa 123, Ciudad A"
)

# Creación del segundo objeto Cliente
cliente2 = Cliente(
    nombre="Maria",
    apellidos="Lopez Gonzalez",
    email="maria.lopez@ejemplo.com",
    direccion="Avenida Siempre Viva 742, Ciudad B"
)

# Imprimir los datos del Cliente 1
print("--- Datos del Cliente 1 ---")
# Usamos directamente print, que llama internamente al método __str__
print(cliente1)

print("\n")

# Imprimir los datos del Cliente 2
print("--- Datos del Cliente 2 ---")
print(cliente2)