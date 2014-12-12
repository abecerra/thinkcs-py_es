#! /usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from validar import *

class MostrarMensaje(Popup): 
    def __init__(self, titulo, mensaje, **kwargs):
        self.size_hint_x = self.size_hint_y = .5
        self.title = titulo
        super(MostrarMensaje, self).__init__(**kwargs)
        self.add_widget(Button(text=mensaje, on_press=lambda x:self.dismiss()))
        self.open()

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
                self.add_widget(Boton(on_press=self.boton_presionado,fila=i,columna=j))
        self.turno = 'O'
        self.tablero = crear()
        
    def botones_a_matriz(self):
        for i in self.children:
            f = i.fila
            c = i.columna
            self.tablero[f][c]=i.text

    def reset(self):
        for i in self.children:
            i.text = ' '
        self.turno = 'O'
            
    def boton_presionado(self, w):
        if w.text != ' ':
            MostrarMensaje('Error!', "Ya se ha jugado en esa casilla!")
            return
        else:
            if self.turno == 'O':
                w.text =  'O'                
                self.turno = 'X'
                self.botones_a_matriz()
                if gana("O",self.tablero):
                    MostrarMensaje("Fin", "Gana el jugador O!")
                    self.reset()
            else:
                w.text = 'X'
                self.turno = 'O'
                self.botones_a_matriz()
                if gana("X",self.tablero):
                    MostrarMensaje("Fin", "Gana el jugador X!")
                    self.reset()
            # chequeamos empate
            if empate(self.tablero):
                MostrarMensaje("Fin", "Empate!")
                self.reset()
	
class Programa(App):
    def build(self):
        self.title = 'Triqui'
        return Triqui()

if __name__ == '__main__':
    Programa().run()


# Ahora chequeamos si hay empate (tablero lleno) llamando a empate del
# archivo validar.

