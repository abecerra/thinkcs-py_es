
def impar(n):
    """ Calcula el enesimo impar
    >>>impar(0)
    1
    >>>impar(1)
    3
    """
    return 2*n + 1

def factorial(n):
    """ Cacula n!
    >>> factorial(4)
    24
    >>> factorial(3)
    6
    """
    j=1
    acum = 1
    while j<=n:
        acum = acum *j
        j = j+1
    return acum

def menosUnoPot(n):
    """
    Calcula (-1)**n
    >>> menosUnoPot(7)
    -1.0
    >>> menosUnoPot(12)
    1.0
    """
    if n%2==0:
        return 1.0
    else:
        return -1.0

# Calcula seno(x) con la formula:
# http://en.wikipedia.org/wiki/Sine#Series_definition
# sen(x) = x -(x^3)/2! + (x^5)/5! ...
#        = sumatoria de ((-1)^n) (x^(2n+1)) / (2n+1)!
#  la sumatoria va de 0 a infinito
# en la siguiente funcion va de 0 a 24

def seno(x):
    """ Calcula el seno de x (en radianes)
    """
    n = 0
    suma = 0
    while n < 25:
        termino = menosUnoPot(n) * (x ** impar(n))
        termino = termino / factorial(impar(n))
        #print termino, factorial(impar(n))
        suma = suma + termino
        n = n + 1
    return suma

from math import sin

def comparacion():
    print(sin(0.3), seno(0.3))
    print(sin(0.4), seno(0.4))
    print(sin(0.5), seno(0.5))

comparacion()
    

