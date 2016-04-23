# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import kivy
import gps
from time import sleep

kivy.require('1.8.0')

from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    
    def build(self):
        gps.start_tracking()
        sleep(0.2)
        mapview = MapView(zoom=11, lat=gps.get_lat, lon=gps.get_lon)
        return mapview

MapViewApp().run()