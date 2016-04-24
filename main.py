# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:00:49 2016

@author: lykke
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import kivy
import kivy.uix

kivy.require('1.8.0')

from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout

class Main(App):
    
    def build(self):
        self.Layout = RelativeLayout(size=(900,450))
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        self.Layout.add_widget(mapview)
        
        self.overlay = AnchorLayout(anchor_x='right', anchor_y='top')
#        btn = Button(text="test", size_hint=(.2, .2))
#        btn = Button(background_normal='Settings G.png', size=(0.2, 0.2), pos=(100,100)) 
        btn = Button(background_normal='Settings B.png', size_hint=(0.06, 0.1))
        btn.bind(on_press = self.show_dropdown)
        self.settings = BoxLayout(orientation='vertical',size_hint=(0.12,0.20))
        self.settings.add_widget(btn)
        self.overlay.add_widget(self.settings)
        self.Layout.add_widget(self.overlay)
    
        
        return self.Layout
        
    def show_dropdown(self,instance):
        
        
        
        btn1 = Button(text='Weather')
        btn2 = Button(text='Level')
        btn3 = Button(text='Nearby users')
        self.settings.add_widget(btn1)
        self.settings.add_widget(btn2)
        self.settings.add_widget(btn3)
                                  
        

Main().run()
