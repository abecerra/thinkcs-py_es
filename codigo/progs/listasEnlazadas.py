# -*- coding: utf-8 -*-
def imprimirlista(Nodo) :
  while Nodo :
    print(Nodo, end=' ')
    Nodo = Nodo.siguiente
  print()

def imprimirAlReves(lista) :
  if lista == None : 
      return
  cabeza = lista
  resto = lista.siguiente
  imprimirAlReves(resto)
  print(cabeza, end=' ')

def imprimirAlRevesBien(lista) :
  print("(", end=' ')
  if lista != None :
    cabeza = lista
    resto = lista.siguiente
    imprimirAlReves(resto)
    print(cabeza, end=' ')
  print(")", end=' ')

def eliminarSegundo(lista) :
  if lista == None : return
  first  = lista
  second = lista.siguiente
  first.siguiente = second.siguiente
  second.siguiente = None
  return second

class Nodo :
  def __init__(self, carga=None) :
    self.carga = carga
    self.siguiente  = None

  def __str__(self) :
    return str(self.carga)

  def imprimirAlReves(self) :
    if self.siguiente != None :
      resto = self.siguiente
      resto.imprimirAlReves()
    print(self.carga, end=' ')

class ListaEnlazada :
  def __init__(self) :
    self.numElementos = 0
    self.cabeza   = None

  def imprimirAlReves(self) :
    print("(", end=' ')
    if self.cabeza != None :
      self.cabeza.imprimirAlReves()
    print(")", end=' ')

  def agregarAlPrincipio(self, carga) :
    nodo = Nodo(carga)
    nodo.siguiente = self.cabeza
    self.cabeza = nodo
    self.numElementos = self.numElementos + 1

L = ListaEnlazada()
L.agregarAlPrincipio(5)
L.agregarAlPrincipio(8)
L.imprimirAlReves()