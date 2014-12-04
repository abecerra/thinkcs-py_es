# -*- coding: utf-8 -*-

def areaRectangulo(base,altura):
    """ Calcula el area de un Rectángulo
    Parámetros:
        - base: número
        - altura: número
    """
    if type(base) == type(1) or type(base) == type(1.0):
        if type(altura) == type(1) or type(altura) == type(1.0):
            print(base * altura)
    else:
        print("ERROR: la base y la altura deben ser números")


def areaCuadrado(lado):
    """ Calcula el area de un cuadrado
    Parámetros:
        - lado: número
    """
    if type(lado) == type(1) or type(lado)==type(1.0):
        areaRectangulo(lado,lado)
    else:
        print("ERROR: el lado debe ser un número")

    
areaRectangulo(4, 5)
areaRectangulo("3", "algo")
areaCuadrado(5)
areaCuadrado("4")
areaCuadrado("tomate")
