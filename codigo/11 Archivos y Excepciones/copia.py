def copiaArchivo(archViejo, archNuevo):
  try:
    f1 = open(archViejo, "r")
    f2 = open(archNuevo, "w")
    while True:
      texto = f1.read(50)
      if texto == "":
        break
      f2.write(texto)
    f1.close()
    f2.close()
    return
  except:
    print("no se pudieron abrir los archivos ", archViejo,archNuevo)


copiaArchivo("frases.txt", "citas.txt")
