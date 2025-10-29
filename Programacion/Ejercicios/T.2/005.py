class JuegoDeEstrategia:
    # Variables de clase (almacenan el tiempo total de juego)
    tiempoEuropa = 0
    tiempoHearts = 0

    # Método para registrar horas en Europa Universalis IV
    def registrarHorasEuropa(horas):
        JuegoDeEstrategia.tiempoEuropa += horas

    # Método para registrar horas en Hearts of Iron IV
    def registrarHorasHearts(horas):
        JuegoDeEstrategia.tiempoHearts += horas

    # Método para mostrar el tiempo total jugado
    def mostrarTiempos():
        print("Horas jugadas en Europa Universalis IV:", JuegoDeEstrategia.tiempoEuropa)
        print("Horas jugadas en Hearts of Iron IV:", JuegoDeEstrategia.tiempoHearts)
        total = JuegoDeEstrategia.tiempoEuropa + JuegoDeEstrategia.tiempoHearts
        print("Tiempo total jugado:", total, "horas")

# Registrar horas de juego directamente desde la clase
JuegoDeEstrategia.registrarHorasEuropa(2)      # 2 horas en Europa Universalis IV
JuegoDeEstrategia.registrarHorasHearts(1.5)   # 1.5 horas en Hearts of Iron IV

# Mostrar resultados
JuegoDeEstrategia.mostrarTiempos()