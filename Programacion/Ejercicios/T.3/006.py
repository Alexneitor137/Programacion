def raizSegura(numero):
    try:
        # Verificamos si es número (int o float)
        if isinstance(numero, (int, float)):
            # Aserción 1: El número no debe ser negativo
            assert numero >= 0, "El número no puede ser negativo"
            return numero ** 0.5
        
        # Si es una cadena, intentamos convertirla
        elif isinstance(numero, str):
            try:
                num_float = float(numero)
                # Aserción 2: El número convertido debe ser no negativo
                assert num_float >= 0, "El número convertido no puede ser negativo"
                return num_float ** 0.5
            except ValueError:
                # No se pudo convertir la cadena a número
                return 0

    except AssertionError as e:
        # Si la aserción falla, mostramos el mensaje de error
        print(f"Aserción fallida: {e}")
    except Exception as e:
        # Capturamos cualquier otro error inesperado
        print(f"Error inesperado: {e}")
    
    # Si algo falla, devolvemos 0
    return 0


# 🔍 Pruebas de funcionamiento
print(raizSegura(4))        # ✅ Debería devolver 2.0
print(raizSegura("9"))      # ✅ Debería devolver 3.0
print(raizSegura("-1"))     # ⚠️ Debería devolver 0 (aserción fallida)
print(raizSegura("abc"))    # ⚠️ Debería devolver 0 (error de conversión)
print(raizSegura(-25))      # ⚠️ Debería devolver 0 (aserción fallida)
