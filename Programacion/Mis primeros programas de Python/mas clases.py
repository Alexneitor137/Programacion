#Poca escalabilidad y causa redundancia
cliente1.email = "info@jocarsa.com"
cliente1.direccion = "La calle de Jose Vicente"
cliente1.nombre = "Jose Vicente"
cliente1.apellidos = "Carratala Sanchis"

cliente2.email = "info@cliente2.com"
cliente2.direccion = "La calle del cliente2"
cliente2.nombre = "Juan"
cliente2.apellidos = "Garcia"

#Mucho mehor usar clases
class Cliente:
  def _init_(self):
    self.email = ""
    self.direccion = ""
    self.nombre = ""
    self.apellidos = ""

cliente1 = Cliente()
cliente1.email = "info@jocarsa.com"
cliente1.direccion = "La calle de Jose Vicente"
cliente1.nombre = "Jose Vicente"
cliente1.apellidos = "Carratala Sanchis"

cliente2 = Cliente()
cliente2.email = "info@cliente2.com"
cliente2.direccion = "La calle del cliente2"
cliente2.nombre = "Juan"
cliente2.apellidos = "Garcia"