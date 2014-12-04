# -*- coding: utf-8 -*-

def areaRectangulo(base,altura):
    """ Calcula el area de un Rectángulo
    Parámetros:
        - base: número
        - altura: número
    Pruebas:
    >>> areaRectangulo(3,4)
    12
    >>> areaRectangulo(8,5)
    40
    """
    if type(base) == type(1) or type(base) == type(1.0):
        if type(altura) == type(1) or type(altura) == type(1.0):
            return base * altura
    else:
        print "ERROR: la base y la altura deben ser números"
        return 0


def areaCuadrado(lado):
    """ Calcula el area de un cuadrado
    Parámetros:
        - lado: número
    Pruebas:
    >>> areaCuadrado(5)
    25
    >>> areaCuadrado(10.0)
    100.0
    """
    if type(lado) == type(1) or type(lado)==type(1.0):
        return areaRectangulo(lado,lado)
    else:
        print "ERROR: el lado debe ser un número"
        return 0


# Esto es para ejecutar las pruebas de
# todas las funciones:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
