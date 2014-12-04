# -*- coding: utf-8 -*-

# Función "recursiva": se llama a si misma
# como no se detiene, se le llama ciclo infinito
def misterio():
    print("Que estoy haciendo?")
    misterio()


misterio()
