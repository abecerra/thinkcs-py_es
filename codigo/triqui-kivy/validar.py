# -*- coding: utf-8 -*-
# aqui están todas las funciones del triqui viejo
# listas para reutilizar

def crear():
    """ Crea una matriz 3x3 vacia """
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m

def ganaDiagonal1(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 1 \ """
    for i in range(3):
        if tablero[i][i]!=jugador:
            return False
    return True

def ganaDiagonal2(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 2 / """
    for i in range(3):
        if tablero[i][2-i]!=jugador:
            return False
    return True

def ganaFila(fila,jugador,tablero):
    """Chequea si el jugador gana en la fila dada - """
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
    """Chequea si el jugador gana en la columna dada | """
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

def gana(jugador,tablero):
    """ Analiza si el jugador gana la partida """
    diag = ganaDiagonal1(jugador,tablero) or ganaDiagonal2(jugador,tablero)
    linea = ganaHorizontal(jugador,tablero) or ganaVertical(jugador,tablero)
    return  diag or linea

def empate(tablero):
    """ Revisa si hay un empate """
    for i in range(3):
        for j in range(3):
            if tablero[i][j]==' ':
                return False
    return True
