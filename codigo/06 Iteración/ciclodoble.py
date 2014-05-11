
def horas():
    """ Imprime las horas del reloj """
    h = 0
    while h<24:
        print h
        h = h+1

def minutos():
    """ Imprime los minutos del reloj """
    m = 0
    while m<60:
        print m
        m = m+1

def reloj():
    """ Imprime todos los minutos de un dia """
    h = 0
    while h<24:
        m = 0
        while m<60:
            print h,":",m
            m = m+1
        h = h+1
