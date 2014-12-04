# -*- coding: cp1252 -*-
import math
import chequeo

def cuadrado1(x):
    if chequeo.esNumero(x):
        return x ** 2

def cuadrado2(x):
    print(x ** 2)

#cuadrado1(10)
#cuadrado2(10)

#x = cuadrado1(10)
#y = cuadrado2(10)

def distancia(x1,y1,x2,y2):
    """ Calcula la distancia euclidiana
    Parámetros:
      x1,y1: representan un punto en el plano
      x2,y2: representan un punto en R2
    >>> distancia(0,0,5,5)
    7.0710678118654755
    """
    c1 = x2-x1
    c2 = y2-y1
    
    return math.sqrt( cuadrado1(c1)+ cuadrado1(c2))

#distancia(0,0,5,5)
#d = distancia(0,0,5,5)
#print distancia(0,0,5,5)

def comparar(a,b):
    """ compara a y b
    >>> comparar(1,2)
    1
    >>> comparar(2,1)
    -1
    >>> comparar(1,1)
    0
    """
    if a<b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

def definitiva(p1,p2,p3,quices,tareas,proyecto):
    """ Definitiva de informática
    >>> definitiva(3,3,3,3,3,3)
    3.0
    >>> definitiva(5,5,5,5,5,5)
    5.0
    """
    return p1*0.18+p2*0.16+p3*0.16+quices*0.16+tareas*0.16+proyecto*0.18


def pendiente(x1,x2,y1,y2):
    """
    >>> pendiente(1,5,1,5)
    1.0
    """
    return float(y2-y1)/(x2-x1)

def areaCirculo(r):
    return math.pi * (r **2)

def areaDisco(r,R):
    a = areaCirculo(R)
    b = areaCirculo(r)
    return a -b 

 

if __name__ == "__main__":
    import doctest
    doctest.testmod()


    

