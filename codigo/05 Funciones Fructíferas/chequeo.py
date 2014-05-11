# -*- coding: utf-8 -*-

# Funciones booleanas para chequear tipos

def esEntero(a):
    """ Averigua si a es entero
    >>> esEntero(4)
    True
    >>> esEntero("5")
    False
    """
    return type(a)==type(1)

def esFlotante(a):
    """ Averigua si a es Flotante
    >>> esFlotante(4.3)
    True
    >>> esFlotante("5")
    False
    """
    
    return type(a)==type(1.0)

def esCadena(a):
    """ Averigua si a es cadena
    >>> esCadena("hola mundo")
    True
    >>> esCadena(5)
    False
    """
    return type(a)==type("hola")

def esLista(a):
    """ Averigua si a es una lista
    >>> esLista([4,5,6,7])
    True
    >>> esLista(4)
    False
    """
    return type(a)==type([1,2])


def esNumero(a):
    """ Averigua si a es un número
    >>> esNumero(4)
    True
    >>> esNumero(4.1)
    True
    >>> esNumero("5")
    False
    """
    return type(a)==type(1) or type(a)==type(1.0)

    

# Esto es para ejecutar las pruebas de
# todas las funciones:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
