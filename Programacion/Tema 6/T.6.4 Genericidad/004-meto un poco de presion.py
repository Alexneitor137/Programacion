numeros = [1,2,"3",4,"cinco"]
print(numeros)

def calculadoble():
    for numero in numeros:
        numero = int(numero)
        print(numero*2)
    
calculadoble()