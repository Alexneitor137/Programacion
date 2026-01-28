import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nombre")
parser.add_argument("--apellidos")

args = parser.parse_args()

diccionario = vars(args)
print(diccionario)

# Usar esta linea en el terminal para que funcione: python3 '.\009-Argumentos con nombre.py'--nombre "alejandro" --apellidos "C S"