# Deben escribirse con camelCase
# Deben tener un verbo (infinitivo o imperativo) y un objeto directo
# Deben tener un nombre descriptivo

def diHola():
  print("Te digo hola")
  
diHola()

def diAdios(nombre):
  print("Hasta luego,", nombre)
  
diAdios("Ana")

def calculaSuma(operando1, operando2):
  resultado = operando1 + operando2
  return resultado

print(calculaSuma(4,3))