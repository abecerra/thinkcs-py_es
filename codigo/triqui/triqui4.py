# -*- coding: utf-8 -*-
# Triqui

def crear():
    """ Crea una matriz 3x3 vacia"""
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m



def imprimir(tablero):
    """ Imprime el tablero de juego"""
    for i in range(3):
        print("|", end=' ')
        for j in range(3):
            print(tablero[i][j], end=' ')
        print("|")


def ganaDiagonal1(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 1"""
    for i in range(3):
        if tablero[i][i]!=jugador:
            return False
    return True

def ganaDiagonal2(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 2"""
    for i in range(3):
        if tablero[i][2-i]!=jugador:
            return False
    return True

# Ahora añadimos filas y columnas
def ganaFila(fila,jugador,tablero):
    """Chequea si el jugador gana en la fila dada"""
    for i in range(3):
        if tablero[fila][i]!=jugador:
            return False
    return True

def ganaHorizontal(jugador,tablero):
    """ Chequea todas las filas """
    for i in range(3):
        if ganaFila(i,jugador,tablero):
            return True
    return False


def ganaColumna(columna,jugador,tablero):
    """Chequea si el jugador gana en la columna dada"""
    for i in range(3):
        if tablero[i][columna]!=jugador:
            return False
    return True

def ganaVertical(jugador,tablero):
    """ Chequea todas las columnas """
    for i in range(3):
        if ganaColumna(i,jugador,tablero):
            return True
    return False


triqui = crear()

while True:
    print("Juegue jugador O")
    f = eval(input("fila? "))
    c = eval(input("columna? "))
    triqui[f][c] = "O"
    imprimir(triqui)
    if ganaDiagonal1("O",triqui) or ganaDiagonal2("O",triqui) or ganaHorizontal("O",triqui) or ganaVertical("O",triqui):
        print("Gana el jugador O!!!!")
        break
    print("Juegue jugador X")
    f = eval(input("fila? "))
    c = eval(input("columna? "))
    triqui[f][c] = "X"
    imprimir(triqui)
    if ganaDiagonal1("X",triqui) or ganaDiagonal2("X",triqui) or ganaHorizontal("X",triqui) or ganaVertical("X",triqui):
        print("Gana el jugador X!!!!")
        break
