# -*- coding: utf-8 -*-
try:
    f = open("frases.txt","r")
    # Lee todo el archivo en una cadena 
    texto = f.read()
    # Lo cierra
    f.close()
    print(texto) 
    # y si el sistema operativo no puede abrirlo se aborta el
    # programa
except:
    print("No se pudo abrir el archivo frases.txt")

  
    
  

