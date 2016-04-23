# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import kivy

kivy.require('1.8.0')

from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview

MapViewApp().run()
