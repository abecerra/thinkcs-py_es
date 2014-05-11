# -*- coding: utf-8 -*-
class Hora:
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
    
horaActual = Hora()
horaActual.hora = 9
horaActual.minutos = 14
horaActual.segundos =  30

#llamamos a los métodos
horaActual.incrementar(80)
horaActual.imprimirHora()



