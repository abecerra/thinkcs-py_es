# -*- coding: utf-8 -*-
class Nodo:
  def __init__(self, carga=None) :
      self.carga = carga
      self.siguiente = None
  def __str__(self) :
      return str(self.carga)
  def imprimirAlReves(self) :
      if self.siguiente != None :
        resto = self.siguiente
        resto.imprimirAlReves()
        print(self.carga, end=' ')


class Cola:
  def __init__(self):
      self.numElementos = 0
      self.primero = None

  def estaVacia(self):
      return (self.numElementos == 0)

  def meter(self, carga):
      nodo = Nodo(carga) 
      nodo.siguiente = None
      if self.primero == None:
        # si esta vacia este nodo sera el primero
        self.primero = nodo
      else:
        # encontrar el ultimo nodo
        ultimo = self.primero
        while ultimo.siguiente:
          ultimo = ultimo.siguiente
        # pegar el nuevo
        ultimo.siguiente = nodo
        self.numElementos = self.numElementos + 1

  def sacar(self):
      carga = self.primero.carga
      self.primero = self.primero.siguiente
      self.numElementos = self.numElementos - 1
      return carga

class ColaMejorada:
    def __init__(self):
        self.numElementos = 0
        self.primero = None
        self.ultimo = None
        
    def estaVacia(self):
        return (self.numElementos == 0)

    def meter(self, carga):
        nodo = Nodo(carga) 
        nodo.siguiente = None
        if self.numElementos == 0:
            # si esta vacia, el nuevo nodo es primero y ultimo
            self.primero = self.ultimo = nodo
        else:
            # encontrar el ultimo nodo
            ultimo = self.ultimo
            # pegar el nuevo nodo
            ultimo.siguiente = nodo
            self.ultimo = nodo
        self.numElementos = self.numElementos + 1

    def sacar(self):
        carga = self.primero.carga
        self.primero = self.primero.siguiente
        self.numElementos = self.numElementos - 1
        if self.numElementos == 0:
            self.ultimo = None
        return carga

class ColaPrioridad:
  def __init__(self):
    self.items = []
      
  def estaVacia(self):
    return self.items == []
  
  def meter(self, item):
    self.items.append(item)

  def eliminar(self) :
    maxi = 0
    for i in range(1,len(self.items)) :
      if self.items[i] > self.items[maxi] :
        maxi = i
    item = self.items[maxi]
    self.items[maxi:maxi+1] = []
    return item

  def sacar(self):
    maxi = 0
    for i in range(0,len(self.items)): 
      if self.items[i] > self.items[maxi]:
        maxi = i
      item = self.items[maxi]
      self.items[maxi:maxi+1] = []
      return item


class golfista:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje= puntaje
    
    def __str__(self):
        return "%-16s: %d" % (self.nombre, self.puntaje)

    def __cmp__(self, otro):
        # el menor tiene mayor prioridad
        if self.puntaje < otro.puntaje: return 1
        if self.puntaje > otro.puntaje: return -1
        return 0

c = Cola()
c.meter(1)
c.meter(2)
c.sacar()
if c.estaVacia():
    print("si>")
else:
    print("no>")

a = ColaMejorada()
a.meter(1)
a.meter(2)
print(a.sacar())
print(a.sacar())
if a.estaVacia():
    print("si<")
else:
    print("no<")

q = ColaPrioridad()
q.meter(11)
q.meter(12)
q.meter(14)
q.meter(13)

while not q.estaVacia():
    print(q.eliminar())

tiger = golfista("Tiger Woods", 61)
phil = golfista("Phil Mickelson", 72)
hal = golfista("Hal Sutton", 69)

pq = ColaPrioridad()
pq.meter(tiger)
pq.meter(phil)
pq.meter(hal)
while not pq.estaVacia():
    print(pq.eliminar())
