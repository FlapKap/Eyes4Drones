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
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from kivy.core.window import Window

class Main(App):
    height = 720
    width = (height/16) * 9
    Window.size = (width,height)
    
    def build(self):
        self.Layout = RelativeLayout()
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        self.Layout.add_widget(mapview)
        
        self.overlay = AnchorLayout(anchor_x='right', anchor_y='top')
        refocus = AnchorLayout(ancher_x='left', anchor_y = 'bottom', size_hint=(0.25,0.15))
        btnre = Button(background_normal='refocus_normal.png', background_down='refocus_down.png')
        refocus.add_widget(btnre)
#        btn = Button(text="test", size_hint=(.2, .2))
#        btn = Button(background_normal='Settings G.png', size=(0.2, 0.2), pos=(100,100)) 
        btn = ToggleButton(background_normal='Settings B.png', background_down="Settings G.png")
        btn.bind(on_press= self.show_dropdown)
        self.settings = StackLayout(size_hint=(0.2,0.2))
        self.settings.add_widget(btn)
        self.overlay.add_widget(self.settings)
        self.Layout.add_widget(refocus)
        self.Layout.add_widget(self.overlay)
    
        
        return self.Layout
        
    def show_dropdown(self,instance):
        print instance.state
        if instance.state == 'down':
            size = (1,0.5)
            btn1 = Button(text='Weather', size_hint = size)
            btn2 = Button(text='Level',size_hint = size)
            btn3 = Button(text='Nearby\nusers', size_hint = size)
            self.settings.add_widget(btn1)
            self.settings.add_widget(btn2)
            self.settings.add_widget(btn3)
        else:
            for child in self.settings.children[:]:
                if child.text != "":
                    self.settings.remove_widget(child)
    
        
                                  
        

Main().run()
