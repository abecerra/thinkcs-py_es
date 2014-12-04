#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Diccionarios

# creación con {}
diccionario = {}

diccionario["one"]="uno"
diccionario["two"]="dos"
diccionario["three"]="tres"
diccionario["white"]="blanco"
diccionario["red"]="rojo"

# observar
print("print diccionario: ", diccionario)


# otra forma de crear:
d ={ "uno":"one", "dos":"two", "tres":"three"}

print("print d: ", d)


# metodos

  # items: parejas
print("print diccionario.items() ", list(diccionario.items()))
print("print d.items() ", list(d.items()))

  # keys: llaves
print("print diccionario.keys() ", list(diccionario.keys()))
print("print d.keys() ", list(d.keys()))
  

  # values: valores
print("print diccionario.values() ", list(diccionario.values()))
print("print d.values() ", list(d.values()))

# borrar pareja (sabiendo la llave):
del diccionario["two"]
print("print diccionario: ", diccionario)








