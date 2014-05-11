import string

def invertir(s):
  """
    >>> invertir('feliz')
    'zilef'
    >>> invertir('Python')
    'nohtyP'
    >>> invertir("")
    ''
    >>> invertir("P")
    'P'
  """
  c = len(s)-1
  invertida = ''
  while c>=0:
    invertida = invertida + s[c]
    c=c-1
  return invertida


def reflejar(s):
  """
    >>> reflejar("bien")
    'bienneib'
    >>> reflejar("si")
    'siis'
    >>> reflejar('Python')
    'PythonnohtyP'
    >>> reflejar("")
    ''
    >>> reflejar("a")
    'aa'
  """
  reflejo = invertir(s)
  return s+reflejo

def es_palindromo(s):
  """
    >>> es_palindromo('abba')
    True
    >>> es_palindromo('abab')
    False
    >>> es_palindromo('tenet')
    True
    >>> es_palindromo('banana')
    False
    >>> es_palindromo('zorra arroz')
    True
  """
  return s == invertir(s)

def elimina_primera_letra(letra, cadena):
  """
     >>> elimina_primera_letra('a', 'manzana')
     'mnzana'
     >>> elimina_primera_letra('a', 'banana')
     'bnana'
     >>> elimina_primera_letra('z', 'banana')
     'banana'
     >>> elimina_primera_letra('i', 'Mississippi')
     'Mssissippi'
   """
  posicion_de_letra = string.find(cadena, letra)
  if posicion_de_letra == -1:
     return cadena
  else:
     return cadena[0:posicion_de_letra]+cadena[posicion_de_letra+1:]


def elimina_letra_rec(cadena,letra,pos):
  """
    pos: posicion por donde va buscando la letra
  """
  pos_de_letra = string.find(cadena,letra,pos)
  if pos_de_letra == -1:
    # si no estA, retorna el resto de la cadena
    return cadena[pos:]
  else:
    # si estA, pega: 
    # - el segmento desde la ultima posicion en que la encontrO, hasta la posicion actual
    # - el resultado de seguir eliminando
    return cadena[pos:pos_de_letra] + elimina_letra_rec(cadena,letra,pos_de_letra+1)
 
def elimina_letra(cadena,letra):
  """
     >>> elimina_letra('manzana','a')
     'mnzn'
     >>> elimina_letra('banana','a')
     'bnn'
     >>> elimina_letra('banana','z')
     'banana'
     >>> elimina_letra('Mississippi','i')
     'Msssspp'
  """
  # Usa la funcion recursiva de arriba!
  return elimina_letra_rec(cadena,letra,0)

def cuenta(sub, s):
  """
    >>> cuenta('is', 'Mississippi')
    2
    >>> cuenta('an', 'banana')
    2
    >>> cuenta('ana', 'banana')
    2
    >>> cuenta('nana', 'banana')
    1
    >>> cuenta('nanan', 'banana')
    0
  """
  c = 0
  # para todas las posiciones
  for j in range (len(s)):
      # si encontramos la subcadena empezando en j
      if string.find(s, sub, j,j+len(sub))!=-1:
          c = c+1
  return c
  
def elimina(sub,s):
  """
   >>> elimina('an', 'banana')
   'bana'
   >>> elimina('cic', 'bicicleta')
   'bileta'
   >>> elimina('iss', 'Mississippi')
   'Mippi'
   >>> elimina('huevo', 'bicicleta')
   'bicicleta'
  """
  pos_de_sub = string.find(s,sub)
  if pos_de_sub==-1:
    return s
  else:
    #print palabra[0:buscar]
    #print palabra[buscar+1:]
    return s[0:pos_de_sub]+s[pos_de_sub+len(sub):]
  
##def elimina_todo(sub, s):
##  """
##    >>> elimina_todo('an', 'banana')
##    'ba'
##    >>> elimina_todo('cic', 'bicicleta')
##    'bileta'
##    >>> elimina_todo('iss', 'Mississippi')
##    'Mippi'
##    >>> elimina_todo('huevos', 'bicicleta')
##    'bicicleta'
##  """
##  if upos + len(sub) >= len(palabra):
##    return ""
##  else:
##    buscar = string.find(palabra, sub, pos, pos+len(sub))
##    if buscar == -1:
##      return elimina_todas(palabra,sub,pos+1,buscar+1)
##    else:
##      return palabra[upos:buscar] +  elimina_todas(palabra,sub,buscar+len(sub)+1,buscar+1)

if __name__ == '__main__':
  import doctest
  doctest.testmod()



