# -*- coding: utf-8 -*-


import turtle

# Función "recursiva": se llama a si misma
def circulo(tortuga):
    """  Pone la tortuga a dar círculos """
    tortuga.forward(10)
    tortuga.left(10)
    circulo(tortuga)

# crea una ventana para dibujar
ventana = turtle.Screen()
# crea una tortuga
andres = turtle.Turtle()

# ahora llamamos la función
circulo(andres)

# circulo es un "ciclo infinito"
# pero Python tiene un límite para los llamados
# recursivos, así que después de un número de
# iteraciones la aborta con un error
