#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Kivy es una biblioteca para realizar aplicaciones gráficas
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# El Triqui hereda de una clase GridLayout
# un diseño de cuadrícula
class Triqui(GridLayout):
    def __init__(self, **kwargs):
        super(Triqui, self).__init__(**kwargs)
   
# Programa hereda de App        
class Programa(App):
    def build(self):
        self.title = 'Triqui'
        return Triqui()

# Al correr el programa se ve una ventana vacía
if __name__ == '__main__':
    Programa().run()


#En muchas bibliotecas gráficas como kivy existe un ciclo que procesa
#los eventos generados a través del teclado, apuntador o la pantalla
#sensible al tacto. Este ciclo es infinito, pero se le hace un "break"
#cuando se cierra la ventana de la aplicación.
#En Kivy, el ciclo reside en la clase App, de la que heredamos la clase
#Programa. Cuando arranca el programa, al ejecutar run() se corre este
#ciclo que procesa eventos.

#El flujo del programa está determinado por lo que haga el usuario con
#los elementos gráficos de la pantalla. Kivy procesará cada evento (click,
#tecla digitada, etc.) de manera predeterminada, por ejemplo cerrar la
#ventana hará un break en el gran ciclo.

#Además, Kivy se encarga de redibujar partes de la ventana cuando otra
#ventana se pase por encima, o cuando se cambie de tamaño, o minimize en
#la barra de tareas.

#El método build de programa retorna un objeto Triqui, que es nuestra ventana.
#La clase Triqui hereda de GridLayout, una ventana que contiene elementos
#en disposición de cuadrícula (como una matriz). El método init de Triqui
#llama al médodo init de la clase madre y le pasa una lista con un número
#de argumentos variable (**kwargs). 

# Por ahora nuestra ventana, el objeto de la clase Triqui, está vacío.
