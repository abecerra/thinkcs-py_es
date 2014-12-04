# -*- coding: utf-8 -*-


def cuadrado(n):
  if type(n)!=type(1) or type(n)!=(1.0):
    # raise aborta el programa con la excepcion TypeError
    raise TypeError("Solo se soportan números")
  else:
    return n ** 2
  

print(cuadrado("2"))

