

def imprimaMultiplos(n):
  i = 1
  while i <= 6:
    print(n*i, '\t', end=' ')
    i = i + 1
  print()


i = 1
while i <= 6:
  imprimaMultiplos(i)
  i = i + 1


def imprimirTablaMultiplicacion():
  i = 1
  while i <= 6:
    imprimaMultiplos(i)
    i = i + 1

imprimirTablaMultiplicacion()
