# -*- coding: utf-8 -*-


import turtle


def rotarPorSiempre(tortuga):
    """  Pone la tortuga a dar círculos por siempre"""
    while True:
        tortuga.forward(10)
        tortuga.left(10)


# crea una ventana para dibujar
ventana = turtle.Screen()
# crea una tortuga
andres = turtle.Turtle()

# ahora llamamos la función
rotarPorSiempre(andres)


# El ciclo infinito se puede terminar cerrando la ventana
# que contiene a la tortuga
