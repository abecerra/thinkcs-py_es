#! /usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
# Popup = ventana emergente
from kivy.uix.popup import Popup


# clase para mostrar mensajes emergentes
class MostrarMensaje(Popup): 
    def __init__(self, titulo, mensaje, **kwargs):
        self.size_hint_x = self.size_hint_y = .5
        # Esta ventana solo tiene un título
        self.title = titulo
        super(MostrarMensaje, self).__init__(**kwargs)
        # y un botón que la cierra cuando se le presiona
        self.add_widget(Button(text=mensaje, on_press=lambda x:self.dismiss()))
        self.open()
        
class Triqui(GridLayout):
    def __init__(self, **kwargs):
        super(Triqui, self).__init__(**kwargs)
        # la geometria de la cuadrícula 3x3:
        self.cols = 3
        self.rows = 3
        # son 9 botones:
        for i in range(3):
            for j in range(3):
                self.add_widget(Button(font_size=100, on_press=self.boton_presionado))
        
    def boton_presionado(self, w):
	# Se muestra un mensaje cuando se presionan las casillas
        MostrarMensaje("Titulo","Presionaste una casilla")
            
    
class Programa(App):
    def build(self):
        self.title = 'Triqui'
        return Triqui()

if __name__ == '__main__':
    Programa().run()

# Ahora creamos 9 botones con geometría de 3x3 en la ventana principal, esto es el triqui!

# Además creamos  una clase que hereda de Popup (ventana emergente) para que se abran
# pequeñas ventanas cada vez que se presionen los botones.
# El método dismiss() de la clase Popup cierra la ventana emergente.
