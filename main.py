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

kivy.require('1.9.0')

from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.garden.mapview.mapview.geojson import GeoJsonMapLayer
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import *
import api
import time

class Main(App):

    height = 720
    width = (height/16) * 9
    Window.size = (width,height)
    
    def build(self):
        self.itu_lat = 55.6593807
        self.itu_lon = 12.5910774
        self.obs_dic = None        
        self.old_time = 0.0
        self.weatherbox = AnchorLayout(anchor_x = 'center', anchor_y = 'bottom')
        self.Layout = RelativeLayout()
        self.mapview = MapView(zoom=11, lat=self.itu_lat, lon=self.itu_lon)
        mapview = self.mapview
        self.Layout.add_widget(mapview)
        # add map layer
        self.jsonmap = GeoJsonMapLayer(source='5_mile_airport.json')
        self.mapview.add_layer(self.jsonmap)        



        
        self.overlay = AnchorLayout(anchor_x='right', anchor_y='top')
        lowerLeft = AnchorLayout(anchor_x='left', anchor_y='bottom')
        self.lowerLeftStack = StackLayout(orientation='lr-bt',size_hint=(0.15,0.15))
        lowerLeft.add_widget(self.lowerLeftStack)
        btnre = Button(background_normal='refocus_normal.png', background_down='refocus_down.png', size_hint = (2,1))
        btnre.bind(on_press=self.resetloc)        
        btnnf = ToggleButton(background_normal='nofly_normal.png', background_down='nofly_down.png',size_hint = (2,1))
        btnnf.bind(on_press=self.nofly)
        self.lowerLeftStack.add_widget(btnre)
        self.lowerLeftStack.add_widget(btnnf)
        
        
        btn = ToggleButton(background_normal='Settings B.png', background_down="Settings G.png")
        btn.bind(on_press= self.show_dropdown)
        self.settings = StackLayout(size_hint=(0.2,0.2))
        self.settings.add_widget(btn)
        self.overlay.add_widget(self.settings)
        self.Layout.add_widget(lowerLeft)
        self.Layout.add_widget(self.overlay)
        
        marker = MapMarker(anchor_x = 0.5, anchor_y = 0.5, lat=self.itu_lat, lon=self.itu_lon)
        self.mapview.add_marker(marker)        
         
        return self.Layout
        
        
    def resetloc(self,instance):
        self.mapview.center_on(self.itu_lat,self.itu_lon)
    
    def nofly(self,instance):
        if instance.state == 'down':
            self.mapview.remove_layer(self.jsonmap)
        else:
            self.mapview.add_layer(self.jsonmap)
        
    def show_dropdown(self,instance):
        if instance.state == 'down':
            size = (1,0.5)
            btn1 = ToggleButton(text='Weather', size_hint = size)
            btn2 = Button(text='Level',size_hint = size)
            btn3 = Button(text='Nearby\nusers', size_hint = size)

            btn1.bind(on_press = self.show_weather_data)             
            
            self.settings.add_widget(btn1)
            self.settings.add_widget(btn2)
            self.settings.add_widget(btn3)
        else:
            for child in self.settings.children[:]:
                if child.text != "":
                    self.settings.remove_widget(child)
    
    def show_weather_data(self,instance):  
        weatherbox = self.weatherbox
        if instance.state == 'down': 
            layout = BoxLayout(orientation='vertical', size_hint = (0.2,0.1) )
            clat = self.mapview.lat
            clon = self.mapview.lon        
            
            ctime = time.time()        
            
            if(self.obs_dic == None or ctime > (self.old_time + 0.5)):            
                self.old_time = ctime
                self.obs_dic = api.loc_weather(clat,clon)
                weList = self.obs_dic['weather']
                we = weList[0]
                wi = self.obs_dic['wind']            
                l1 = Label(text = 'Current weather: ' + we['main'], color = (0.,0.,0.,1))
                main = self.obs_dic['main']
                k = main['temp']
                #Conversion from imperial to metric
                temp = k-273.15
                l2 = Label(text = 'temp: ' + str(temp) + ' ' + u'\u00B0' + 'C', color = (0.,0.,0.,1))
                hu = main['humidity']
                l3 = Label(text = 'humidity: ' + str(hu) + '%', color = (0.,0.,0.,1))
                pre = main['pressure']
                l4 = Label(text = 'pressure' + str(pre) + ' hPa', color = (0.,0.,0.,1))
                wispeed = wi['speed']
                widir = wi['deg']
                l5 = Label(text = 'wind speed: ' + str(wispeed) + 'm/s', color = (0.,0.,0.,1))
                l6 = Label(text = 'wind direction '+ str(widir) + u'\u00B0', color = (0.,0.,0.,1))
                Tdp = temp - ((100-hu)/5)
                l7 = Label(text = 'dew point: ' + str(Tdp) + ' ' + u'\u00B0' + 'C', color = (0.,0.,0.,1))

                layout.add_widget(l1)
                layout.add_widget(l2)
                layout.add_widget(l3)
                layout.add_widget(l4)
                layout.add_widget(l5)
                layout.add_widget(l6)        
                layout.add_widget(l7)            
                
                weatherbox.add_widget(layout)
                
                weatherbox.add_widget
                self.Layout.add_widget(weatherbox)
        else:
            for c in self.weatherbox.children[:]:
                for child in c.children[:]:
                    c.remove_widget(child)
                self.weatherbox.remove_widget(c)
            self.overlay.remove_widget(weatherbox)
                

Main().run()
