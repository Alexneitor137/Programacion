import random
from flask import Flask, render_template

app = Flask(__name__)

PATRON = set(range(1, 10))  # {1,2,3,4,5,6,7,8,9}


def fila_valida(fila):
    """Comprueba que la fila contiene exactamente los números del 1 al 9."""
    return len(fila) == 9 and set(fila) == PATRON


def columnas_validas_parciales(sudoku):
    """
    Comprueba que, para el número de filas actual,
    ninguna columna tiene números repetidos.
    """
    num_filas = len(sudoku)
    num_columnas = 9

    for c in range(num_columnas):
        columna = [sudoku[f][c] for f in range(num_filas)]
        if len(columna) != len(set(columna)):  # hay repetidos
            return False
    return True


def sudoku_valido_completo(sudoku):
    """Validación final: todas las filas y todas las columnas son válidas."""
    # Filas
    for fila in sudoku:
        if not fila_valida(fila):
            return False

    # Columnas
    for c in range(9):
        columna = [sudoku[f][c] for f in range(9)]
        if set(columna) != PATRON:
            return False

    return True


import random
from flask import Flask, render_template

app = Flask(__name__)


def es_valido(grid, fila, col, num):
    """Comprueba si `num` puede ponerse en grid[fila][col]."""

    # Fila
    if num in grid[fila]:
        return False

    # Columna
    for f in range(9):
        if grid[f][col] == num:
            return False

    # Bloque 3x3
    bloque_fila = (fila // 3) * 3
    bloque_col = (col // 3) * 3
    for f in range(bloque_fila, bloque_fila + 3):
        for c in range(bloque_col, bloque_col + 3):
            if grid[f][c] == num:
                return False

    return True


def resolver_sudoku(grid):
    """
    Backtracking: intenta rellenar la cuadrícula.
    Devuelve True si se ha podido resolver, False si no.
    """

    # Buscar la siguiente celda vacía (0)
    for fila in range(9):
        for col in range(9):
            if grid[fila][col] == 0:
                # Probamos números del 1 al 9 en orden aleatorio
                candidatos = list(range(1, 10))
                random.shuffle(candidatos)

                for num in candidatos:
                    if es_valido(grid, fila, col, num):
                        grid[fila][col] = num
                        if resolver_sudoku(grid):
                            return True
                        # backtrack
                        grid[fila][col] = 0

                # Si ningún número sirve, devolvemos False
                return False

    # Si no quedan celdas vacías, está resuelto
    return True


def generar_sudoku_completo():
    """Genera un sudoku completo válido (9x9) usando backtracking."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(grid)
    return grid


def sudoku_a_bloques(sudoku):
    """
    Convierte el sudoku (9x9) en 9 bloques 3x3.
    Cada bloque es una lista de 9 números.
    """
    bloques = []
    for br in range(3):          # bloque fila
        for bc in range(3):      # bloque columna
            bloque = []
            for r in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    bloque.append(sudoku[r][c])
            bloques.append(bloque)
    return bloques


@app.route("/")
def inicio():
    sudoku = generar_sudoku_completo()
    datos = sudoku_a_bloques(sudoku)
    return render_template("index.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)