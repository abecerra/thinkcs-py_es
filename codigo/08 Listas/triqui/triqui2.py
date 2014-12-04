
def crear():
    """ Crea una matriz 3x3 vacia"""
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m



def imprimir(tablero):
    """ Imprime el tablero de juego"""
    for i in range(3):
        print("|", end=' ')
        for j in range(3):
            print(tablero[i][j], end=' ')
        print("|")


triqui = crear()

# Ahora juegan los dos jugadores por siempre
while True:
    print("Juegue jugador O")
    f = eval(input("fila? "))
    c = eval(input("columna? "))
    triqui[f][c] = "O"
    imprimir(triqui)
    print("Juegue jugador X")
    f = eval(input("fila? "))
    c = eval(input("columna? "))
    triqui[f][c] = "X"
    imprimir(triqui)
