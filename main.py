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
from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
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
        
        marker = MapMarker(anchor_x = 0.5, anchor_y = 0.5, lat=self.itu_lat, lon=self.itu_lon)
        self.mapview.add_marker(marker)        
         
        return self.Layout
        
    def show_dropdown(self,instance):
        print instance.state
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
