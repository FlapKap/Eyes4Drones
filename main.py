# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import kivy
<<<<<<< HEAD
import gps
from time import sleep
=======
import kivy.uix
>>>>>>> origin/master

kivy.require('1.8.0')

from kivy.garden.mapview import MapView
from kivy.app import App
<<<<<<< HEAD

class MapViewApp(App):
    
    def build(self):
        gps.start_tracking()
        sleep(0.2)
        mapview = MapView(zoom=11, lat=gps.get_lat, lon=gps.get_lon)
        return mapview

MapViewApp().run()
=======
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
class Main(App):
    
    def build(self):
        rLayout = RelativeLayout(size=(900,450))
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        rLayout.add_widget(mapview)
        
        overlay = AnchorLayout(anchor_x='right', anchor_y='top')
        btn = Button(text="test", size_hint=(.2, .2))
        overlay.add_widget(btn)
        rLayout.add_widget(overlay)
        return rLayout

Main().run()
>>>>>>> origin/master
