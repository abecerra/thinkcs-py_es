# -*- coding: utf-8 -*-

def cuadrado1(x):
    """ calcula el cuadrado de x
        parámetros:
            - x : número
    """
    if type(x) == type(0):
        return x ** 2
    else:
        print("ERROR: se espera un entero")
        return 0


def cuadrado2(x):
    """ calcula el cuadrado de x
        parámetros:
            - x : número
    """
    if type(x) == type(0) or type(x)==type(1.0):
        return x ** 2
    else:
        print("ERROR: se espera un número")
        return 0

# cuadrado(8)
# cuadrado("2")

def areaRectangulo1(base,altura):
    """ calcula el area de un rectangulo
        parámetros:
            - base: número
            - altura: número
    """
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
    if type(base) == type(0) or type(base)==type(1.0):
        if type(altura) == type(0) or type(altura)==type(1.0):
            return base * altura
    else:
        print("ERROR: la base y la altura deben ser numeros")
        return 0


areaRectangulo2(4, 5.2)
areaRectangulo2("4", "5.2")

def esEntero(a):
    return type(a)==type(1)

def esCadena(a):
    return 

def esNumero(a):
    return type(a)==type(1) or type(a)==type(1.0)
    

def areaRectangulo3(base,altura):
    """ calcula el area de un rectangulo
        parámetros:
            - base: número
            - altura: número
    """
    if esNumero(base) and esNumero(altura):
            print(base * altura)
    else:
        print("ERROR: la base y la altura deben ser numeros")

def porsiempre():
    print("*********")
    porsiempre()

def poruntiempo(t):
    if t>0:
        print("**********")
        poruntiempo(t-1)

def poruntiempo1(t):
    if t>0:
        print(t)
        poruntiempo1(t-1)

# Esto es para ejecutar las pruebas de
# todas las funciones:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
