class Punto:
  pass

limpio = Punto()
limpio.x = 3.0
limpio.y = 4.0

print '(' + str(limpio.x) + ', ' + str(limpio.y) + ')'
distanciaAlCuadrado = limpio.x * limpio.x + limpio.y * limpio.y
print distanciaAlCuadrado

def imprimePunto(p):
  print '(' + str(p.x) + ', ' + str(p.y) + ')'


imprimePunto(limpio)

p1 = Punto()
p1.x = 3
p1.y = 4
p2 = Punto()
p2.x = 3
p2.y = 4
# Que sucede?
print p1 == p2 

p2 = p1
# Y ahora?
print p1 == p2

# Igualdad profunda
def mismoPunto(p1, p2) :
  return (p1.x == p2.x) and (p1.y == p2.y)

print mismoPunto(p1, p2)


class Rectangulo:	
  pass

caja = Rectangulo()
caja.ancho = 100.0
caja.altura = 200.0

caja.esquina = Punto()
caja.esquina.x = 0.0;
caja.esquina.y = 0.0;


def encuentraCentro(caja):
  p = Punto()
  p.x = caja.esquina.x + caja.ancho/2.0
  p.y = caja.esquina.y + caja.altura/2.0
  return p


centro = encuentraCentro(caja)
imprimePunto(centro)


def agrandarRect(caja, dancho, daltura):
  caja.ancho = caja.ancho + dancho
  caja.altura = caja.altura + daltura


b = Rectangulo()
b.ancho = 100.0
b.altura = 200.0
b.esquina = Punto()
b.esquina.x = 0.0;
b.esquina.y = 0.0;
agrandarRect(b, 50, 100)
print b.ancho, " ", b.altura



