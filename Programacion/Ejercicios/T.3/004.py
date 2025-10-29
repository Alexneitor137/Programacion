try:
  print(4/0)
  print("Intento conectarme a la base de datos")
  print("pero falla")
except ZeroDivisionError:
  print("No puedo ejecutar eso")
except Exception as e:
  print(f"Pues por lo menos guardo los datos a un archivo local... {e}")

print("Y el programa continua")