#! /usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MostrarMensaje(Popup): 
    def __init__(self, titulo, mensaje, **kwargs):
        self.size_hint_x = self.size_hint_y = .5
        self.title = titulo
        super(MostrarMensaje, self).__init__(**kwargs)
        self.add_widget(Button(text=mensaje, on_press=lambda x:self.dismiss()))
        self.open()
        
class Triqui(GridLayout):
    def __init__(self, **kwargs):
        super(Triqui, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        for i in range(3):
            for j in range(3):
                self.add_widget(Button(font_size=100, on_press=self.boton_presionado, text=' '))
        # Turno va de 'O' a 'X' cada vez que se presione el botón
        self.turno = 'O'

    #cambia el texto del botón presionado de acuerdo al turno del jugador
    def boton_presionado(self, w):
        # Si hay algun texto
        if w.text != ' ':
            MostrarMensaje('Error!', "Ya se ha jugado en esa casilla!")
            return
        # Ahora, cambia el texto y le da el turno al otro jugador
        if self.turno == 'O':
            w.text =  'O'
            self.turno = 'X'
        else:
            w.text = 'X'
            self.turno = 'O'
	 
class Programa(App):
    def build(self):
        self.title = 'Triqui'
        return Triqui()

if __name__ == '__main__':
    Programa().run()


# Creamos el esquema básico del juego: un atributo turno.
# - Cuando se presiona el botón, el turno pasa al otro jugador.
# - El atributo text de los botones nos permite ir llenando el triqui
#   con las jugadas!

# Se hace chequeo de que el jugador presione una casilla vacía.
