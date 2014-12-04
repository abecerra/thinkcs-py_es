# -*- coding: cp1252 -*-


# Tuplas


# Crear
AlfabetoDNA = 'A','C','G','T'

# Desempacar
n1,n2,n3,n4 = AlfabetoDNA


def cadenaValidaDNA(cadena):
    """ 
    >>> cadenaValidaDNA("ACCTG")
    True
    >>> cadenaValidaDNA("987987987CGH")
    False
    """

    c = 0
    for i in cadena:
        if i in AlfabetoDNA:
            c = c +1
            
    return c == len(cadena)


def cadenaValidaDNA2(cadena):
    """ 
    >>> cadenaValidaDNA("ACCTG")
    True
    >>> cadenaValidaDNA("987987987CGH")
    False
    """

    for i in cadena:
        if not (i in AlfabetoDNA):
            return False
            
    return True


# Funciona para cadenas, listas y tuplas
def contar(secuencia,elemento):
    """ cuenta cuantas veces está elemento en la secuencia
    >>> contar("abcdeaba",'a')
    3
    >>> contar( ('a','b','c','a'),'a')
    2
    >>> contar( [1,2,10,2,3,4],2)
    2
    >>> contar( ["lunes","martes"], "lunes")
    1
    """

    c = 0
    for s in secuencia:
        if s == elemento:
            c = c +1
    return c

def enRegion(lista, inf, sup):
    """
    >>> enRegion([2,3,4,5], 3,5)
    2
    """
    c = 0
    for s in lista:
        if inf <= s < sup:
            c = c+1
    return c

import random
def listaAleatoria(n):
    L = [0] * n
    for i in range(n):
        L[i]=random.random()
    return L
    
def histograma(lista):
    numRegiones = 8
    Regiones = [0] * numRegiones
    ancho = 1.0 /numRegiones
    for i in range (numRegiones):
        inf = i * ancho
        sup = inf + ancho
        Regiones[i] = enRegion(lista,inf,sup)
        print(Regiones[i])

lista = listaAleatoria(1000)
histograma(lista)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
