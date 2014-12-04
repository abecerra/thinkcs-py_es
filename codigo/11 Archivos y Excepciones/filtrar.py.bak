# -*- coding: utf-8 -*-
#Elimina los comentarios de un archivo
def filtraArchivo(archViejo, archNuevo):
  try:
#   Abre dos archivos 
    f1 = open(archViejo, "r")
    f2 = open(archNuevo, "w")

#   Copia las lineas del uno al otro
    while True:
      texto = f1.readline()
      if texto == "":
        break
#     Ignorando los comentarios    
      if texto[0] == '#':
#       continue sigue a la siguiente iteración         
        continue
      
      f2.write(texto)

    f1.close()
    f2.close()
  except:
    print "No se pudo abrir los archivos ", archViejo, archNuevo
  


filtraArchivo("filtrar.py", "filtrar-sincomentarios.py")


