# -*- coding: utf-8 -*-
class Hora:
    # Un método (función dentro de una clase)
    def imprimirHora(t):
        print(t.hora, ":", t.minutos,":",t.segundos)
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
    
horaActual = Hora()
horaActual.hora = 9
horaActual.minutos = 14
horaActual.segundos =  30

horaComer  = Hora()
horaComer.hora = 12
horaComer.minutos = 0
horaComer.segundos =  0

#llamamos a los métodos
horaActual.incrementar(80)
horaActual.imprimirHora()

if horaComer.despues(horaActual):
  print("El pan estará listo para comer en un momento.")

