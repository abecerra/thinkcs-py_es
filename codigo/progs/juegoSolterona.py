# -*- coding: utf-8 -*-
import random

class Carta:
  listaFiguras = ["Treboles", "Diamantes", "Corazones", "Picas"]
  listaValores = [ "narf", "As", "2", "3", "4", "5", "6", "7","8", "9", "10","Jota", "Reina", "Rey"]

  def __init__(self, figura=0, valor=0):
    self.figura = figura
    self.valor = valor

  def __str__(self):
    return self.listaValores[self.valor] + " de " + self.listaFiguras[self.figura]

  def __cmp__(self, otro):
    # revisa las figuras
    if self.figura > otro.figura: 
       return 1
    if self.figura < otro.figura: 
       return -1
    # las figuras son iguales ... se chequean los valores
    if self.valor > otro.valor: 
      return 1
    if self.valor < otro.valor: 
      return -1
    # los valores son iguales... hay empate
    return 0

class Mazo:
  def __init__(self):
    self.Cartas = []
    for figura in range(4):
      for valor in range(1, 14):
        self.Cartas.append(Carta(figura, valor))

  def imprimirMazo(self):
    for Carta in self.Cartas:
      print(Carta)

  def __str__(self):
    s = ""
    for i in range(len(self.Cartas)):
      s = s + " "*i + str(self.Cartas[i]) + "\n"
    return s

  def barajar(self):
    import random
    nCartas = len(self.Cartas)
    for i in range(nCartas):
      j = random.randrange(i, nCartas)
      [self.Cartas[i], self.Cartas[j]] = [self.Cartas[j], self.Cartas[i]]

  def eliminarCarta(self, Carta):
    if Carta in self.Cartas:
      self.Cartas.remove(Carta)
      return 1
    else: return 0

  def entregarCarta(self):
    return self.Cartas.pop()

  def estaVacio(self):
    return (len(self.Cartas) == 0)

  def repartir(self, manos, nCartas=999):
    nmanos = len(manos)
    for i in range(nCartas):
      if self.estaVacio(): 
         break    # rompe el ciclo si no hay cartas
      # quita la carta del tope
      Carta = self.entregarCarta()      
      # quien tiene el proximo turnoo?
      mano = manos[i % nmanos]    
      # agrega la carta a la mano
      mano.agregarCarta(Carta)         

class mano(Mazo):
  def __init__(self, nombre=""):
    self.Cartas = []
    self.nombre = nombre

  def agregarCarta(self,Carta) :
    self.Cartas.append(Carta)

  def __str__(self):
    s = "mano " + self.nombre
    if self.estaVacio():
      s = s + " esta vacia\n"
    else:
      s = s + " contiene\n"
    return s + Mazo.__str__(self)

class JuegoCartas:
  def __init__(self):
    self.Mazo = Mazo()
    self.Mazo.barajar()

class ManoJuegoSolterona(mano):
  def eliminarParejas(self):
    cont = 0
    originalCartas = self.Cartas[:]
    for carta in originalCartas:
      m = Carta(3-carta.figura, carta.valor)
      if m in self.Cartas:
        self.Cartas.remove(carta)
        self.Cartas.remove(m)
        print("mano %s: %s parejas %s" % (self.nombre,carta,m))
        cont = cont+1
    return cont

class JuegoSolterona(JuegoCartas):
  def jugar(self, nombres):
    # elimina la reina de treboles
    self.Mazo.eliminarCarta(Carta(0,12))

    # crea manos con base en los nombres
    self.manos = []
    for nombre in nombres : 
        self.manos.append(ManoJuegoSolterona(nombre))

    # reparte las Cartas
    self.Mazo.repartir(self.manos)
    print("---------- Cartas se han repartido")
    self.imprimirmanos()

    # eliminar parejas iniciales
    parejas = self.eliminarParejas()
    print("---------- parejas descartadas, empieza el juego")
    self.imprimirmanos()

    # jugar hasta que se eliminan 50 cartas
    turno = 0
    nummanos = len(self.manos)
    while parejas < 25:
      parejas = parejas + self.jugarUnturno(turno)
      turno = (turno + 1) % nummanos

    print("---------- Juego Terminado")
    self.imprimirmanos ()

  def eliminarParejas(self):
    cont = 0
    for mano in self.manos:
      cont = cont + mano.eliminarParejas()
    return cont

  def jugarUnturno(self, i):
    if self.manos[i].estaVacio():
      return 0
    vecino = self.encontrarvecino(i)
    cartaEscogida = self.manos[vecino].entregarCarta()
    self.manos[i].agregarCarta(cartaEscogida)
    print("mano", self.manos[i].nombre, "escogió", cartaEscogida)
    count = self.manos[i].eliminarParejas()
    self.manos[i].barajar()
    return count

  def encontrarvecino(self, i):
    nummanos = len(self.manos)
    for siguiente in range(1,nummanos):
      vecino = (i + siguiente) % nummanos
      if not self.manos[vecino].estaVacio():
        return vecino

  def imprimirmanos(self) :
    for mano in self.manos :
        print(mano)

j = JuegoSolterona()
j.jugar(["juan","catalina"])