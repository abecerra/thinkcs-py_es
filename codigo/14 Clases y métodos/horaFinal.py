# -*- coding: utf-8 -*-
class Hora:
    # Método init
    def __init__(self, hora=0, minutos=0, segundos=0):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos
    # Un método (función dentro de una clase)
    def imprimirHora(t):
        print t.hora, ":", t.minutos,":",t.segundos
    # Otro método
    def incrementar(self, segundos):
        self.segundos = self.segundos + segundos

        if self.segundos >= 60:
          self.segundos = self.segundos - 60
          self.minutos = self.minutos + 1

        if self.minutos >= 60:
          self.minutos = self.minutos - 60
          self.hora = self.hora + 1
        return self
    #
    def despues(self, hora2):
        if self.hora > hora2.hora:
          return True
        if self.hora < hora2.hora:
          return False

        if self.minutos > hora2.minutos:
          return True
        if self.minutos < hora2.minutos:
          return False

        if self.segundos > hora2.segundos:
          return True
        return False
    
horaActual = Hora(9,14,30)
horaActual.imprimirHora()
horaComer  = Hora(12)
horaComer.imprimirHora()
