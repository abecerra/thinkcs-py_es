# Juego de "Triqui"

def crear():
    """ Crea una matrix 3x3 vacia"""
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m



def imprimir(tablero):
    """ Imprime el tablero de juego"""
    for i in range(3):
        print('|',end='')
        for j in range(3):
            print(tablero[i][j],end='') 
        print('|')

triqui = crear()

# Solo juega un jugador por siempre 
while True:
    print("Juegue jugador O")
    f = int(input("fila? "))
    c = int(input("columna? "))
    triqui[f][c] = "O"
    imprimir(triqui)

