#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Matrices dispersas (muchos ceros, pocos
# valores distintos de cero)
# Implementadas con diccionarios

# las llaves son tuplas (f,c)
# para la fila y la columna del valor

# los valores del diccionario son los
# valores de la matriz distintos de cero

# Aqui la matriz como lista de listas
m = [ [0,0,0,1,0],
      [0,0,0,0,0],
      [0,2,0,0,0],
      [0,0,0,0,0],
      [0,0,0,3,0],
      ]

# La misma matriz dispersa, en un diccionario:
matriz = { (0,3):1, (2,1):2, (4,3):3 }



# el acceso a m es:
print("print m[0][3]= ", m[0][3])

# el acceso a matriz es:
print("print matriz.get( (0,3), 0)=", matriz.get( (0,3), 0))







