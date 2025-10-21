'''
Primero, importamos el módulo math y lo almacenamos en una variable llamada mi_matematica. Luego usamos esta variable para calcular la raíz cuadrada de un número.
'''
import math

# Guardamos el objeto math en una variable
mi_matematica = math

# Calculamos la raíz cuadrada de un número (por ejemplo, 16)
raiz_cuadrada = mi_matematica.sqrt(16)
print("La raíz cuadrada de 16 es:", raiz_cuadrada)

'''
Definimos una función que calcule el área de un círculo usando la fórmula 
𝐴=𝜋*(𝑟**2).
'''                                                                                                                   
def calcular_area_circulo(radio):
    area = mi_matematica.pi * (radio ** 2)
    return area

'''
Usamos la función anterior para calcular el área de un círculo con radio 5 y mostramos el resultado.
'''
radio = 5
area_resultado = calcular_area_circulo(radio)
print("El área de un círculo con radio", radio, "es:", area_resultado)

'''    
Este ejemplo muestra cómo el módulo math de Python permite realizar cálculos matemáticos de forma precisa y sencilla. Conceptos como la raíz cuadrada y el área de un círculo son fundamentales en muchos contextos prácticos:

En videojuegos históricos, estos cálculos pueden servir para simular trayectorias de proyectiles, áreas de impacto o zonas de control.

En análisis de datos, el uso de math permite aplicar fórmulas estadísticas, calcular desviaciones estándar o analizar tendencias mediante funciones matemáticas básicas.
'''