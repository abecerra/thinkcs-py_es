# -*- coding: utf-8 -*-
class Fraccion:
    def __init__(self,numerador,denominador=1):
        self.numerador = numerador
        self.denominador = denominador
    def __str__(self):
        return "%d/%d" % (self.numerador, self.denominador)
    
    def __mul__(self, otro):
        if type(otro) == type(5):
            otro = Fraccion(otro)
        return Fraccion(self.numerador * otro.numerador,self.denominador * otro.denominador)
    
    __rmul__ = __mul__ 

    #suma de fracciones
    def __add__(self, otro):
        if type(otro) == type(5):
            otro = Fraccion(otro)
        return Fraccion(self.numerador * otro.denominador +self.denominador * otro.numerador,self.denominador * otro.denominador)
    
    __radd__ = __add__
    
    def __init__(self, numerador, denominador=1):      
        g=MDC(numerador,denominador)
        self.numerador=numerador / g
        self.denominador=denominador / g
    def __cmp__(self, otro):
        dif = (self.numerador * otro.denominador -
        otro.numerador * self.denominador)
        return dif

def MDC (m,n):
        if m%n==0:
            return n
        else:
            return MDC(n,m%n)

a = Fraccion(4,8)
b = Fraccion(2,3)
print a+b
print a*b
print 5*a
print b*5
print b+2