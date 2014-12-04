

class estudiante:
    pass

def imprimeEstudiante(e):
    print(e.nombre, "\t", e.codigo)

j = estudiante()
j.nombre = "Jaime Mejia"
j.codigo = "0064857"

a = estudiante()
a.nombre = "Alejandra Jimenez"
a.codigo = "0075298"

    
imprimeEstudiante(j)
imprimeEstudiante(a)
