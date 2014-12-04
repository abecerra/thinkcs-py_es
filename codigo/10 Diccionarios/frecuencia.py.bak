# -*- coding: utf-8 -*-


def frecuencia(proteina):
  # diccionario vacio
  d = {}
  
  for aminoacido in proteina:
    # Falla!, ¿por que falla?
    #d[aminoacido] = d[aminoacido] + 1

    # Funciona!, ¿por que?
    d[aminoacido] = d.get(aminoacido,0) + 1      
      
  return d

print frecuencia("MAMAPRTEINSTRING")

# recordar que d.get(key,DefaultValue) es algo como esto:
# if d.has_key():
#    return d[key]  (el valor asociado a key)
# else:
#    return DefaultValue

# y has_key() es un método booleano que
# averigua si la llave está en el diccionario
