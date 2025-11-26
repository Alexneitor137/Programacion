numeros = [1,2,"3",4,"cinco","patata"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculadoble():
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero*2)
        except:
            centinela = False
            for i in range(0,len(numeros_etiquetas)):
                if numero == numeros_etiquetas[i]:
                    print(i*2)
            if centinela == False:
                print("Mira tio, se intento y no se pudo")
            
    
calculadoble()