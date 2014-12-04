# -*- coding: utf-8 -*-
import string
# aqui se crea el diccionario codigoGenetico
# que asocia todos los tripletes posibles
# en ARN a sus aminoacidos o a Stop
from codigoGenetico import *


def traduccion(ARNm):
  n = len(ARNm)
  if n%3 != 0:
    # Lanza una excepción
    raise TypeError("El numero de nucleotidos debe ser multiplo de 3")
  else:
    prepararDiccionario()
    proteina = []
    for j in range(0,n,3):
      # triplete
      a = ARNm[j]
      b = ARNm[j+1]
      c = ARNm[j+2]
      aminoacido = codigoGenetico[a+b+c]
      #print "aminoacido = ", aminoacido
      proteina.append( aminoacido)

    # Como proteina es una lista de caracteres
    # la convertimos a cadena
    return string.join(proteina,'')
      

print traduccion("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
