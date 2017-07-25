# -*- coding: utf-8 -*-

# Un juego de "Triqui" o "Tic-Tac-Toe" para dos jugadores
# Convenciones:
# El tablero es una matriz 3x3
# Si tablero[i][j] es:
#    ' ': nadie ha jugado en esa casilla
#    'O': el primer jugador jugó en esa casilla
#    'X': el segundo jugador jugó en esa casilla


# Como todo programa empieza con algo mínimo

def crear():
    """ Crea una matrix 3x3 vacia"""
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
        
triqui = crear()
imprimir(triqui)

