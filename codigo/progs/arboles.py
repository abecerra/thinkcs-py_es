# -*- coding: utf-8 -*-
class Arbol:
  def __init__(self, carga, izquierdo=None, derecho=None):
      self.carga = carga
      self.izquierdo = izquierdo
      self.derecho = derecho
      
  def __str__(self):
      return str(self.carga)
  
  def obtenerizquierdo(self):
    return self.izquierdo
  
  def obtenerderecho(self):
    return self.derecho
  
  def obtenercarga(self):
    return self.carga
    
  def asignarcarga(self, carga):
    self.carga = carga
  
  def asignarizquierdo(self, i):
    self.izquierdo = i
    
  def asignarderecho(self, d):
    self.derecho = d

  

def total(arbol):
  if arbol.izquierdo == None or arbol.derecho== None:
	return arbol.carga
  else:
      return total(arbol.izquierdo) + total(arbol.derecho)  + arbol.carga
   
def imprimirarbol(arbol):
  if arbol == None:
      return 
  else:
      print arbol.carga
      imprimirarbol(arbol.izquierdo)
      imprimirarbol(arbol.derecho)

def imprimirarbolPostorden(arbol):
  if arbol == None:
      return
  else:
      imprimirarbolPostorden(arbol.izquierdo)
      imprimirarbolPostorden(arbol.derecho)
      print arbol.carga   

def imprimirabolEnOrden(arbol):
  if arbol == None:
      return
  imprimirabolEnOrden(arbol.izquierdo)
  print arbol.carga,imprimirabolEnOrden(arbol.derecho)

def imprimirarbolSangrado(arbol, nivel=0):
  if arbol == None:
      return
  imprimirarbolSangrado(arbol.derecho, nivel+1)
  print " "*nivel + str(arbol.carga)
  imprimirarbolSangrado(arbol.izquierdo, nivel+1)


def obtenerLexema(listaLexemas, esperado):
  if listaLexemas[0] == esperado:
      del listaLexemas[0]
      return 1
  else:
      return 0

def obtenerNumero(listaLexemas):
  x = listaLexemas[0]
  if type(x) != type(0):
      return None
  del listaLexemas[0]
  return arbol (x, None, None)


def obtenerProducto(listaLexemas):
  a = obtenerNumero(listaLexemas)
  if obtenerLexema(listaLexemas, "*"):
      b = obtenerProducto(listaLexemas) 
      return arbol ("*", a, b)
  else:
      return a


def obtenerNumero(listaLexemas):
  if obtenerLexema(listaLexemas, "("):
      x = obtenerSuma(listaLexemas) # obtiene la subexpresi´on
      obtenerLexema(listaLexemas, ")") # elimina los par´entesis
      return x
  else:
      x = listaLexemas[0]
      if type(x) != type(0):
	  return None
  listaLexemas[0:1] = []
  return arbol (x, None, None)  ## error de sintaxis  (`arbol)

def si(preg):
  from string import lower
  r = lower(raw_input(preg))
  return (r[0] == 's')


def animal():
  # Un solo nodo
  raiz = Arbol("pajaro")
      # Hasta que el usuario salga
  while True:
      print
      if not si("Esta pensando en un animal? "):
	  break
      # Recorrer el arbol
      arbol = raiz
      while arbol.obtenerizquierdo() != None:
	  pregunta = arbol.obtenercarga() + "? "
	  if si(pregunta):
	      arbol = arbol.obtenerderecho()
	  else:
	      arbol = arbol.obtenerizquierdo()
      # conjetura
      conjetura = arbol.obtenercarga()
      pregunta = "¿Es un" + conjetura + "? "
      if si(pregunta):
	  print "¡Soy el mejor!"
	  continue
      # obtener mas informacion
      pregunta = "¿Cual es el nombre el animal? "
      animal = raw_input(pregunta)
      pregunta = "¿Que pregunta permitiria distinguir un %s de un %s? "
      q = raw_input(pregunta % (animal,conjetura))
      # agrega un nuevo nodo arbol
      arbol.asignarcarga(q)
      pregunta = "¿Si el animal fuera %s la respuesta ser´ıa? "
      if si(pregunta % animal):
	  arbol.asignarizquierdo(Arbol(conjetura))
	  arbol.asignarderecho(Arbol(animal))
      else:
	  arbol.asignarizquierdo(Arbol(animal))
	  arbol.asignarderecho(Arbol(conjetura))

#Hace Falta un else:
d=Arbol(1)
f=Arbol(2)
g=Arbol(3,d,f)
imprimirarbol(g)
##3
##1
##2

##Funciona
d=Arbol(1)
f=Arbol(2)
g=Arbol(3,d,f)
imprimirarbolSangrado(g)
## 2
##3
## 1
c=Arbol(4)
s=Arbol(5,c,g)
imprimirarbolSangrado(s)
##  2
## 3
##  1
##5
## 4

