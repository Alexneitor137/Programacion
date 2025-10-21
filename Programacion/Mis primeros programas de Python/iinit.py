class Gato():
    def __init__(self,edad,nombre,raza): #El construcyor de ejecuta si o si
        self.edad = 0
        self.nombre = nombre
        self.raza = raza
        
    def maulla(self): #El resto de métodos solo se ejecutan si los llamas
        return "El gato esta maullando"
        
gato1 = Gato(5,"Mauro","Esfinge")
