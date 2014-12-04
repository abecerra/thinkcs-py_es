# -*- coding: utf-8 -*-
class Hora:
  def __init__(self, hora=0, minutos=0, segundos=0):
    self.hora = hora
    self.minutos = minutos
    self.segundos = segundos

  def __str__(self):
    return str(self.hora) + ":" + str(self.minutos) + ":" + str(self.segundos)

  def convertirAsegundoss(self):
    minutos = self.hora * 60 + self.minutos
    segundos = self.minutos * 60 + self.segundos
    return segundos

  def incrementar(self, segs):
    segs = segs + self.segundos

    self.hora = self.hora + segs/3600
    segs = segs % 3600
    self.minutos = self.minutos + segs/60
    segs = segs % 60
    self.segundos = segs

def crearHora(segs):
  H = Hora()
  H.hora = segs/3600
  segs = segs - H.hora * 3600
  H.minutos = segs/60
  segs = segs - H.minutos * 60
  H.segundos = segs
  return H

# Pruebas:
h = Hora(10, 20, 0) # 10:20:0
print(h) 
h.incrementar(65)
print(h)  # 10:21:5
i = crearHora(4600)
print(i)  # 1:16:40