# -*- coding: utf-8 -*-
# implementación con listas de python
class Pila:              
  def __init__(self):
    self.items = []

  def meter(self, item):
    self.items.append(item)

  def sacar(self):
    return self.items.pop()

  def estaVacia(self):
    return(self.items == [])

def evalPostfija(expr) :
  import re
  expr = re.split("([^0-9])", expr)
  pila = Pila()
  for lexema in expr :
    if  lexema == '' or lexema == ' ':
      continue
    if  lexema == '+' :
      suma = pila.sacar() + pila.sacar()
      pila.meter(suma)
    elif lexema == '*' :
      producto = pila.sacar() * pila.sacar()
      pila.meter(producto)
    else :
      pila.meter(int(lexema))
  return pila.sacar()


p = Pila()
p.meter(4)
p.meter(9)
p.meter(16)
while not p.estaVacia():
  print(p.sacar())
  
print(evalPostfija("5 4 + 2 *"))
