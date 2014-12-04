# -*- coding: utf-8 -*-

def sumarImparesHasta(n):
  e = 1
  suma = 0
  while e <=n:
    suma = suma + e
    e = e + 2
  return suma

for i in range(11):
  print(i, sumarImparesHasta(i))
  
