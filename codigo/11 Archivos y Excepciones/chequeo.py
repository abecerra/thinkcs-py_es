# -*- coding: utf-8 -*-

# Funciones booleanas para chequear tipos

def esEntero(a):
    """ Averigua si a es entero
    >>> esEntero(4)
    True
    >>> esEntero("5")
    False
    """
    if type(a)==type(1):
        return True
    else:
        raise TypeError("Se espera un numero entero")
        

def esFlotante(a):
    """ Averigua si a es Flotante
    >>> esFlotante(4.3)
    True
    >>> esFlotante("5")
    False
    """
    if type(a)==type(1.0):
        return True
    else:
        raise TypeError("Se espera un numero flotante")
    

def esCadena(a):
    """ Averigua si a es cadena
    >>> esCadena("hola mundo")
    True
    >>> esCadena(5)
    False
    """
    if type(a)==type("hola"):
        return True
    else:
        raise TypeError("Se espera una cadena")
    

def esLista(a):
    """ Averigua si a es una lista
    >>> esLista([4,5,6,7])
    True
    >>> esLista(4)
    False
    """
    if type(a)==type([1,2]):
        return True
    else:
        raise TypeError("Se espera una lista")
    


def esNumero(a):
    """ Averigua si a es un número
    >>> esNumero(4)
    True
    >>> esNumero(4.1)
    True
    >>> esNumero("5")
    False
    """
    if type(a)==type(1) or type(a)==type(1.0):
        return True
    else:
        raise TypeError("Se espera un numero")
    

    

# Esto es para ejecutar las pruebas de
# todas las funciones:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
