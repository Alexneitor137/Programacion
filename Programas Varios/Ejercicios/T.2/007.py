import math  # Asegúrate de importar el módulo math

numero_caballos = int(input("¿Cuantos caballos hay disponibles?: "))

CABALLOS_POR_CUADRA = 3

# Usamos math.ceil para redondear hacia arriba
numero_cuadras = math.ceil(numero_caballos / CABALLOS_POR_CUADRA)

print("Tienes", numero_caballos, "caballos")
print("Necesitarías", numero_cuadras, "cuadras para el transporte")
print("Necesitarías", numero_cuadras, "cuadras")