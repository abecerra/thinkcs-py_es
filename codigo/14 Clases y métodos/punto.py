# -*- coding: utf-8 -*-
class Punto:
    # init y str son métodos especiales
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    def __mul__(self, otro):
        return self.x * otro.x + self.y * otro.y
    def __rmul__(self, otro):
        return Punto(otro * self.x,  otro * self.y)


p = Punto(3, 4)
a = str(p)

print(a)
print(p)

p1 = Punto(3, 4)
p2 = Punto(5, 7)
p3 = p1 + p2
print(p3)

v = p1 * p2
print(v)

print(2*p1)
