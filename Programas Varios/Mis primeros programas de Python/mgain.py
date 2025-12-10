class Gato():
    def __init__(self): #El construcyor de ejecuta si o si
        self.edad = 0
        
    def maulla(self): #El resto de métodos solo se ejecutan si los llamas
        return "El gato esta maullando"
        
        gato1 = Gato()
        print(gato1.edad)
        gato1.edad = 5
        print(gato1.edad)
        
        print(gato1.maulla())
