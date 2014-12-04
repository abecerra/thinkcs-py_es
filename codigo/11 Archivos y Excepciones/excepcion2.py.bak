# -*- coding: utf-8 -*-


def cuadrado(n):
  if type(n)!=type(1) or type(n)!=(1.0):
    raise TypeError, "Solo se soportan números"
  else:
    return n ** 2

# Con try y except podemos evitar que los programas aborten

try:
  # Aqui se pone el bloque de código que puede fallar
  print cuadrado("2")
  # Aqui se "captura" la excepción
except TypeError:
    print "El llamado falló, cuadrado espera un número!"

