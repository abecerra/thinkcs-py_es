def buscar(cad, c,ini=0):
  indice = ini
  while indice < len(cad):
    if cad[indice] == c:
      return indice
    indice = indice + 1
  return -1


print buscar("apple", "p")
print buscar("apple", "p", 2)
print buscar("apple", "p", 3)
