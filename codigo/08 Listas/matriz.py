# -*- coding: utf-8 -*-

# Matriz implementada como lista de filas



m =  [ [0,0,0],
       [0,0,0],
       [0,0,0] ]


print m[0][0] 

def imprimir(matriz):
    """ Imprime el tablero de juego"""
    for i in range(len(matriz)):
        print "|",
        for j in range(len(matriz)):
            print matriz[i][j],
        print "|"
        
imprimir(m)

def crear(n):
    """ Crea una matrix de n x n ceros """
    matriz = []
    for i in range(n):
        # Una fila con n ceros
        fila = n*[0]
        matriz.append(fila)
    return matriz


nueva = crear(6)
print "Matriz nueva de 6x6"
imprimir(nueva)


def identidad(n):
    """ Crea una matriz identidad de nxn """
    m = crear(n)
    # Pone unos en la diagonal
    for i in range(n):
        m[i][i] = 1
    return m

print "Matriz identidad de 4x4"
imprimir(identidad(4))
