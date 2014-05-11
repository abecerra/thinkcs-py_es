import string

def invertir(s):
    c = len(s)-1
    invertida = ''
    while c>=0:
        invertida = invertida + s[c]
        c=c-1
    return invertida

def reflejar(s):
    reflejo = invertir(s)
    return palabra+reflejo


def elimina_letra(letra, palabra):
    start = 0
    buscar = string.find(palabra, letra, start)
    if buscar==-1:
        return palabra
    else:
##        print palabra[0:buscar]
##        print palabra[buscar+1:]
        return palabra[0:buscar]+palabra[buscar+1:]
    
def es_palindromo(s):
    return s==invertir(s)

def cuenta(sub, s):
    c = 0
    # para todas las posiciones
    for j in range (len(s)):
        # si encontramos la subcadena empezando en j
        if string.find(s, sub, j,j+len(sub))!=-1:
            c = c+1
    return c

def elimina_primeraocurrencia(sub, palabra):
    posicion_de_sub = string.find(palabra, sub)
    if posicion_de_sub == -1:
        return palabra
    else:
        return palabra[0:posicion_de_sub]+palabra[buscar+len(sub):]
        
    
def elimina_todas(palabra,sub,pos,upos):
    if upos + len(sub) >= len(palabra):
        return ""
    else:
        buscar = string.find(palabra, sub, pos, pos+len(sub))
        if buscar == -1:
            return elimina_todas(palabra,sub,pos+1,buscar+1)
        else:
            return palabra[upos:buscar] +  elimina_todas(palabra,sub,buscar+len(sub)+1,buscar+1)
    
    
