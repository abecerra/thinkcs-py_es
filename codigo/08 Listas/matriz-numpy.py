# -*- coding: utf-8 -*-
# Una matriz con el paquete numpy
# para calculos científicos
# hay que instalarlo!

import numpy

def crearmatriz(n):
    return numpy.zeros( (n,n), dtype=numpy.int)


def imprimir(matriz,n):
    for i in range(n):
        print("|", end=' ')
        for j in range(n):
            print(matriz[i,j]," ", end=' ') 
        print("|")
        
T = crearmatriz(5)
print(T)
imprimir(T,5)


