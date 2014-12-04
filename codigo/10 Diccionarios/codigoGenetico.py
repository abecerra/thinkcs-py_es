# -*- coding: utf-8 -*-
import string

# Diccionario
# Va a asociar para cada triplete el aminoacido que corresponde
# o la cadena 'Stop'
codigoGenetico = {}

# Observe primero codigoGenetico.txt para entender esta función!
def prepararDiccionario():
  # cuando se abren archivos hay que poner el código en un try
  try:
    f = open("codigoGenetico.txt","r")
    # Lee todo el archivo
    texto = f.read()
    # Lo cierra
    f.close()
  # y si el sistema operativo no puede abrirlo se aborta el
  # programa
  except:
    print("No se pudo abrir el archivo codigogenetico.txt")

  # Separa el texto en lineas
  lineas = texto.splitlines()

  # es una lista de cadenas
  #print "print lineas:\n:", lineas


  # A cada linea le hacemos split
  #print "haciendo split"
  for l in lineas:
    par = str.split(l)
    # par es una lista de dos elementos
    #print par
    # asociamos el triplete a el aminoacido en el diccionario
    codigoGenetico[par[0]]=par[1]
  

    
  

