# Juego de "Triqui"

def crear():
    """ Crea una matriz 3x3 vacia"""
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m



def imprimir(tablero):
    """ Imprime el tablero de juego"""
    for i in range(3):
        print "|",
        for j in range(3):
            print tablero[i][j],
        print "|"


triqui = crear()

# Solo juega un jugador por siempre 
while True:
    print "Juegue jugador O"
    f = input("fila? ")
    c = input("columna? ")
    triqui[f][c] = "O"
    imprimir(triqui)

