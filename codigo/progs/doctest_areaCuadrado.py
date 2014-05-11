# -*- coding: utf-8 -*-

def area(lado):
    """ Calcula el area de un cuadrado
        Parámetros:
            radio: número
        Pruebas:
        >>> area(1)
        1
        >>> area(2)
        4
        >>> area(4)
        16
        >>> area(10)
        100
        
    """
    return lado**2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
