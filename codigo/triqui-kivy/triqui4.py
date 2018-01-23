#! /usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
# Propiedades 
from kivy.properties import NumericProperty
# En validar están las funciones del triqui viejo
from validar import *

class MostrarMensaje(Popup): 
    def __init__(self, titulo, mensaje, **kwargs):
        self.size_hint_x = self.size_hint_y = .5
        self.title = titulo
        super(MostrarMensaje, self).__init__(**kwargs)
        self.add_widget(Button(text=mensaje, on_press=lambda x:self.dismiss()))
        self.open()

# Agregamos un boton que tiene propiedades para 
# registrar la fila y la columna
class Boton(Button):
    fila = NumericProperty(0)
    columna = NumericProperty(0)
    
    def __init__(self, **kwargs):      
        super(Boton, self).__init__(**kwargs)
        self.font_size=100
        self.text=' '
      
class Triqui(GridLayout):
   
    def __init__(self, **kwargs):
        super(Triqui, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        for i in range(3):
            for j in range(3):
                # Ahora usamos el boton personalizado
                self.add_widget(Boton(on_press=self.boton_presionado,fila=i,columna=j))
        self.turno = 'O'
        # creamos una matriz vacía
        self.tablero = crear()

    # pasa el estado de los botones a la matriz tablero
    def botones_a_matriz(self,tablero):
        for i in self.children:
            f = i.fila
            c = i.columna
            self.tablero[f][c]=i.text
        
    def boton_presionado(self, w):
        if w.text != ' ':
            MostrarMensaje('Error!', "Ya se ha jugado en esa casilla!")
            return
        else:
            if self.turno == 'O':
                w.text =  'O'
                self.turno = 'X'
            else:
                w.text = 'X'
                self.turno = 'O'
             # se pasa el estado de los botones a la matriz tablero
            self.botones_a_matriz(self)
	
class Programa(App):
    def build(self):
        self.title = 'Triqui'
        return Triqui()

if __name__ == '__main__':
    Programa().run()


# Del triqui en modo texto seleccionamos todo lo que nos sirve para validar
# y lo ponemos en validar.py. En el método init de Triqui creamos una matriz
# vacía que representa el juego llamada tablero.

# Creamos un botón personalizado para almacenar la fila y la columna.

# El método botones_a_matriz toma el estado de los botones y lo pone en la
# matriz tablero. Ahora, cada vez que se juega, se llama a éste método, esto
# nos va a permitir poder validar quien gana o si hay empate.

