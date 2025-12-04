numeros = [1,2,"3",4,"cinco"]
print(numeros)

def calculadoble():
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero*2)
        except:
            print("(No Valido)")
    
calculadoble()