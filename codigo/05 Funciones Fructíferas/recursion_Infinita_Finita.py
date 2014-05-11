# -*- coding: utf-8 -*-

def porsiempre():
    print "*********"
    porsiempre()

def poruntiempo(t):
    if t>0:
        print "**********"
        poruntiempo(t-1)

def poruntiempo1(t):
    if t>0:
        print t
        poruntiempo1(t-1)

# Ejecutar en el intérprete 
# porsiempre()
# observar

# ahora ejecutar
# poruntiempo(2)
# poruntiempo(3)
# poruntiempo(4)
