import random

# Genera un número entero aleatorio entre 1 y 50 (ambos inclusive).
numero_aleatorio = random.randint(1, 50)

# Define el número máximo de intentos permitidos.
intentos = 6

print("--- Juego de Adivinar el Número (1-50) ---")

# Inicia un bucle principal.
while intentos > 0:
    
    print(f"\nTe quedan {intentos} intentos")
    
    # Se inicializa el intento para el bucle.
    intento = None
    
    # 🌟 Uso de try/except para validar la entrada 🌟
    try:
        # Pide la entrada y trata de convertirla a entero.
        intento_str = input("Decide qué número crees que es: ")
        intento = int(intento_str)
        
    except ValueError:
        # Si la conversión falla (ej. el usuario escribe 'hola'), se ejecuta este bloque.
        print(" ¡Entrada inválida! Por favor, ingresa un número entero.")
        # Usamos 'continue' para saltar el resto de la iteración y NO gastar un intento.
        continue

    # 1. Condición de Victoria:
    if intento == numero_aleatorio:
        print(" ¡Felicidades!")
        print(f"Has acertado que el número secreto era: {numero_aleatorio}")
        break  # Termina el juego.
    
    # Si no acierta, decrementa el contador de intentos antes de dar la pista.
    intentos -= 1
    
    # 2. Pistas (Demasiado alto/bajo):
    if intento < numero_aleatorio:
        print(" Has fallado. El número es más alto.")
    elif intento > numero_aleatorio:
        print("Has fallado. El número es más bajo.")
        
    # 3. Condición de Derrota (Verificación después de decrementar):
    if intentos == 0:
        print("\n Has perdido. Te quedaste sin intentos.")
        print(f"El número secreto era: {numero_aleatorio}")
        break  # Termina el juego.

print("--- Fin del juego ---")
   