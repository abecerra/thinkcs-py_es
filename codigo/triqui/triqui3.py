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
        print "|",
        for j in range(3):
            print tablero[i][j],
        print "|"

# Ahora añadimos análisis del tablero con
# las siguientes funciones:

def ganaDiagonal1(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 1 \"""
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

triqui = crear()

while True:
    print "Juegue jugador O"
    f = input("fila? ")
    c = input("columna? ")
    triqui[f][c] = "O"
    imprimir(triqui)
    if ganaDiagonal1("O",triqui) or ganaDiagonal2("O",triqui):
        print "Gana el jugador O!!!!"
        break
    print "Juegue jugador X"
    f = input("fila? ")
    c = input("columna? ")
    triqui[f][c] = "X"
    imprimir(triqui)
    if ganaDiagonal1("X",triqui) or ganaDiagonal2("X",triqui):
        print "Gana el jugador X!!!!"
        break
