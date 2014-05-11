class Hora:
    pass

tiempo = Hora()
tiempo.hora = 11
tiempo.minutos = 59
tiempo.segundos = 30

def sumarHoras(t1, t2):
  sum = Hora()
  sum.hora = t1.hora + t2.hora
  sum.minutos = t1.minutos + t2.minutos
  sum.segundos = t1.segundos + t2.segundos

  if sum.segundos >= 60:
    sum.segundos = sum.segundos - 60
    sum.minutos = sum.minutos + 1

  if sum.minutos >= 60:
    sum.minutos = sum.minutos - 60
    sum.hora = sum.hora + 1

  return sum

def imprimirHora(t):
    print t.hora, ":", t.minutos,":",t.segundos
    
horaActual = Hora()
horaActual.hora = 9
horaActual.minutos = 14
horaActual.segundos =  30

horaPan = Hora()
horaPan.hora =  3
horaPan.minutos =  35
horaPan.segundos =  0

horaComer = sumarHoras(horaActual, horaPan)
imprimirHora(horaComer)

def convertirASegundos(t):
  minutos = t.hora * 60 + t.minutos
  segundos = minutos * 60 + t.segundos
  return segundos


def crearHora(segundos):
  h = Hora()
  h.hora = segundos/3600
  segundos = segundos - h.hora * 3600
  h.minutos = segundos/60
  segundos = segundos - h.minutos * 60
  h.segundos = segundos
  return h


def sumarHorasG(t1, t2):
  segundos = convertirASegundos(t1) + convertirASegundos(t2)
  return crearHora(segundos)


horaComer = sumarHorasG(horaActual, horaPan)
imprimirHora(horaComer)
