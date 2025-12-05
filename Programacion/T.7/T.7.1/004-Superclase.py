class Persona():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
  def dameDatos(self):
    return self.nombre+self.apellidos

class Profesor(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
  	super().__init__(nombre, apellidos, email,direccion)
  
class Alumno(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)
  
    
alumno1 = Alumno("Manolo","Carratala","Manolino@gmaila.com","Calle Falsa 123")
print(alumno1.dameDatos())

profesor1 = Profesor("Alejandro","Calderón","Alex@gmail.com","Avenida Siempre Viva 742")
print(profesor1.dameDatos())