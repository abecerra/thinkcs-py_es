#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Triqui para dos jugadores
# Convenciones:
# El tablero es una matriz 3x3
# Si tablero[i][j] es:
#    ' ': nadie ha jugado en esa casilla
#    'O': el primer jugador jugó en esa casilla
#    'X': el segundo jugador jugó en esa casilla

def crear():
    """ Crea una matrix 3x3 vacia """
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m

def imprimir(tablero):
    """ Imprime el tablero de juego"""
    for i in range(3):
        print('|',end='')
        for j in range(3):
            print(tablero[i][j],end='') 
        print('|')

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

# Es mejor poner esto en una función fructífera!
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

def valido(n):
    return 0<=n<=2

# Y que jugar tenga menos responsabilidades
def jugar(jugador,tablero):
    """ Registra una jugada en el tablero de juego
        Imprime el tablero después de la jugada
    """
    while True:     
        print("Juegue jugador ", jugador)
        f = int(input("fila? "))
        c = int(input("columna? "))
        if type(f)==type(c)==type(1) and valido(f) and valido(c) and tablero[f][c]==' ':
            tablero[f][c] = jugador
            break
        else:
            print("Posición inválida!")

    imprimir(tablero)

# El ciclo principal del juego se pone
# en __main__
if __name__ == '__main__':
    triqui = crear()
    imprimir(triqui)

    while True:
        jugar("O",triqui)
        if empate(triqui):
            print("Empate !!!")
            break
        if gana("O",triqui):
            print("Gana el jugador O !!!!")
            break
        jugar("X",triqui)
        if gana("X",triqui):
            print("Gana el jugador X !!!!")
            break
        if empate(triqui):
            print("Empate !!!")
            break
