
def ordenar2(a,b):
    """ Imprime en pantalla la pareja (a,b) en orden ascendente """
    if a<=b:
        print a,b
    else:
        print b,a

def ordenar3(a,b,c):
    """ Imprime en pantalla la terna (a,b,c) en orden ascendente """
    if    a<=b<=c:
        print a,b,c
    elif  a<=c<=b:
        print a,c,b
    elif  b<=a<=c:
        print b,a,c
    elif  b<=c<=a:
        print b,c,a
    elif  c<=a<=b:
        print c,a,b
    else:
        print c,b,a


ordenar2(1,2)
ordenar2(5,2)
ordenar2(4,4)

ordenar3(1,2,5)
ordenar3(1,5,2)
ordenar3(2,5,1)
ordenar3(2,1,5)
ordenar3(5,1,2)
ordenar3(5,2,1)
