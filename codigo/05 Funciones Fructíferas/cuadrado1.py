# -*- coding: utf-8 -*-

def cuadrado1(x):
    """ calcula el cuadrado de x
        parámetros:
            - x : número
        Pruebas:
        >>> cuadrado1(0)
        0
        >>> cuadrado1(9)
        81
        >>> cuadrado1(-3)
        9
    """
    if type(x) == type(0):
        return x ** 2
    else:
        print "ERROR: se espera un entero"
        return 0


def cuadrado2(x):
    """ calcula el cuadrado de x
        parámetros:
            - x : número
        Pruebas:
        >>> cuadrado2(0)
        0
        >>> cuadrado2(9)
        81
        >>> cuadrado2(-3)
        9
    """
    if type(x) == type(0) or type(x)==type(1.0):
        return x ** 2
    else:
        print "ERROR: se espera un número"
        return 0

# Esto es para ejecutar las pruebas de
# todas las funciones:

if __name__ == '__main__':
    import doctest
    doctest.testmod()


