# -*- coding: utf-8 -*-



def areaRectangulo1(base,altura):
    """ calcula el area de un rectangulo
        parámetros:
            - base: número
            - altura: número
    """
    # muy ilegible:
    if (type(base) == type(0) or type(base)==type(1.0)) and(type(altura) == type(0) or type(altura)==type(1.0)):
        return base * altura
    else:
        print("ERROR: la base y la altura deben ser numeros")
        return 0

def areaRectangulo2(base,altura):
    """ calcula el area de un rectangulo
        parámetros:
            - base: número
            - altura: número
    """
    # un poco mejor con dos condicionales anidados
    if type(base) == type(0) or type(base)==type(1.0):
        if type(altura) == type(0) or type(altura)==type(1.0):
            return base * altura
    else:
        print("ERROR: la base y la altura deben ser numeros")
        return 0


def esNumero(a):
    return type(a)==type(1) or type(a)==type(1.0)
   

def areaRectangulo(base,altura):
    """ calcula el area de un rectangulo
        parámetros:
            - base: número
            - altura: número
    >>> areaRectangulo(3,8)
    24
    >>> areaRectangulo(12,3)
    36
    """
    # mucho mejor: más legible!
    if esNumero(base) and esNumero(altura):
            return base * altura
    else:
        print("ERROR: la base y la altura deben ser numeros")
        return 0
    

# Esto es para ejecutar las pruebas de
# todas las funciones:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
