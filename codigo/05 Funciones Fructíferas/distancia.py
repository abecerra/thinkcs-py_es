import math

def distancia(x1,y1,x2,y2):
    """ Calcula la distancia entre los puntos (x1,y1) y (x2,y2)
    >>> distancia(0,0,3,4)
    5.0
    >>> distancia(0,0,5,6)
    8.0
    """
    return math.sqrt( (y2-y1)**2 + (x2-x1)**2)



        
