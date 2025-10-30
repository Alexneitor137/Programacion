'''
    Entrenaiento de dragones
    v0.1 Alejandro Calderón Sánchez
  	Este programa clasifica y entrena a dos dragones
'''
## EN ESTE BLOQUE DEFINIMOS LAS VARIABLES Y PEDIMOS LA INFORMACION AL USUARIO ##
nombre_dragon_a = input("Introduce el nombre del dragón A: ")
edad_dragon_a = input("Introduce la edad del dragón A: ")
clasificacion_dragon_a = ""
fuerza_dragon_a = 0

nombre_dragon_b = input("Introduce el nombre del dragón B: ")
edad_dragon_b = input("Introduce la edad del dragón B: ")
clasificacion_dragon_b = ""
fuerza_dragon_b = 0

## MOSTRAMOS AL USUARIO LOS DATOS QUE INTRODUJO ##
print("-----------------------------------------------------")
print("El nombre del dragon A es:", nombre_dragon_a)
print("La edad del dragon A es:", edad_dragon_a)
print("-----------------------------------------------------")
print("El nombre del dragon B es:", nombre_dragon_b)
print("La edad del dragon B es:", edad_dragon_b)
print("")

## EN ESTE BLOQUE NOS ASEGURAMOS QUE LOS VALORES SEAN ENTEROS ##
try:
    edad_dragon_a = int(edad_dragon_a)
    print("He convertido la edad A correctamente")
except:
    edad_dragon_a = 100
    print("No he convertido la edad A correctamente")
    
try:
    edad_dragon_b = int(edad_dragon_b)
    print("He convertido la edad B correctamente")
except:
    edad_dragon_b = 100
    print("No he convertido la edad B correctamente")
    
## EN ESTE BLOQUE CLASIFICAMOS A LOS DRAGONES ##    
if edad_dragon_a < 50:
    clasificacion_dragon_a = "Joven"
elif edad_dragon_a >= 50 and edad_dragon_a <= 199:
    clasificacion_dragon_a = "Adulto"
elif edad_dragon_a >= 200:
    clasificacion_dragon_a = "Anciano"
print("El dragon A es:", clasificacion_dragon_a)
    
if edad_dragon_b < 50:
    clasificacion_dragon_b = "Joven"
elif edad_dragon_b >= 50 and edad_dragon_b <= 199:
    clasificacion_dragon_b = "Adulto"
elif edad_dragon_b >= 200:
    clasificacion_dragon_b = "Anciano"
print("El dragon B es:", clasificacion_dragon_b)

## AHORA LOS ENTRENAMOS ##
for dia in range (1,4):

## ENTRENAMOS AL DRAGON A ## 
    if clasificacion_dragon_a == "Joven":
        fuerza_dragon_a += 2
    elif clasificacion_dragon_a == "Adulto":
        fuerza_dragon_a += 1
    elif clasificacion_dragon_a == "Anciano":
        fuerza_dragon_a += 1
 
## MOSTRAMOS LA INFORMACIÓN AL USUARIO ##       
    print("--------------- Final del dia" , dia,"---------------")
    print("El dragon A ahora tiene ", fuerza_dragon_a,"de fuerza")
    print("-----------------------------------------------------")
    
## ENTRENAMOS AL DRAGON B ##    
    if clasificacion_dragon_b == "Joven":
        fuerza_dragon_b += 2
    elif clasificacion_dragon_b == "Adulto":
        fuerza_dragon_b += 1
    elif clasificacion_dragon_b == "Anciano":
        fuerza_dragon_b += 1

## MOSTRAMOS AL INFORMACIÓN AL USUARIO ##        
    print("--------------- Final del dia" , dia,"---------------")
    print("El dragon B ahora tiene ", fuerza_dragon_b,"de fuerza")

    print("-----------------------------------------------------")
