# -*- coding: utf-8 -*-


def RectanguloDeAsteriscos(n):
    """ Imprime n veces una línea de asteriscos"
    Parámetros:
        - n: número entero positivo
    """
    if type(n) == type(1) and n>0:
        ciclo(n)
    else:
        print("Error: el valor de n debe ser entero y positivo")
    
def ciclo(n):
    """ Se llama a si misma n veces
    Parámetros:
        - n : número entero positivo
    """
    if n==0:
        print()
    else:
        print("***********************")
        ciclo(n-1)
        


ciclo(3)
print("Ahora, con 4")
ciclo(4)
print("Ahora, con 5")
ciclo(5)
