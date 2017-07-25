#! /usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# Para un botón
from kivy.uix.button import Button


class Triqui(GridLayout):
    def __init__(self, **kwargs):
        super(Triqui, self).__init__(**kwargs)
        # Agregamos el botón, registrando el método 'boton_presionado'
        self.add_widget(Button(font_size=100, on_press=self.boton_presionado))
    
    # Método que responde a la presión del botón
    def boton_presionado(self, w):
        pass
            
class Programa(App):
    def build(self):
        self.title = 'Triqui'
        return Triqui()

# Al correr el programa se ve un botón
if __name__ == '__main__':
    Programa().run()


# Las ventanas suelen tener muchos elementos gráficos como menús, botones, paneles
# entre otros. En kivy -- y en muchas otras bibliotecas-- se llaman widgets. Estos
# se agregan mediante el método add_widget.

# Un botón es una instancia de la clase Button.

# Como el flujo de los programas gráficos no está determinado por el programador,
# sino por el usuario al interactuar con los widgets de la ventana, el mecanismo
# que se utiliza para reaccionar es el de registrar métodos que atiendan a los eventos.
# En nuestro caso registramos un método que responde al evento de presionar el botón.

# Por ahora el método no hace nada.
