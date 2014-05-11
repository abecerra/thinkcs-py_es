# -*- coding: utf-8 -*-
class Punto:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(' + str(self.x) + ',' + str(self.y) + ')'

  def __add__(self, otro):
    return Punto(self.x + otro.x, self.y + otro.y)

  def __sub__(self, otro):
    return Punto(self.x - otro.x, self.y - otro.y)

  def __mul__(self, otro):
    return self.x * otro.x + self.y * otro.y

  def __rmul__(self, otro):
    return Punto(otro * self.x, otro * self.y)

  def invertir(self):
    self.x, self.y = self.y, self.x

  def DerechoYAlReves(derecho):
    from copy import copy
    alreves = copy(derecho)
    alreves.invertir()
    print str(derecho) + str(alreves)

# Pruebas:
p = Punto(2,4)
q = Punto(3,5)
print p+q  #(5,9)
print p-q  #(-1,-1)
print p*q  #(6,20)
print 5*p  #5*(2,4)=(10,20)  __rmul__
p.invertir()
print p    #(4,2)
q.DerechoYAlReves()  #(3,5)(5,3)