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
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import api
import time


class Main(App):    
    
    def build(self):
        self.itu_lat = 55.6593807
        self.itu_lon = 12.5910774
        self.obs_dic = None        
        self.old_time = 0.0
        
        self.Layout = RelativeLayout(size=(900,450))
        self.mapview = MapView(zoom=17, lat=self.itu_lat, lon=self.itu_lon)
        self.Layout.add_widget(self.mapview)
        
        self.overlay = AnchorLayout(anchor_x='right', anchor_y='top')
#        btn = Button(text="test", size_hint=(.2, .2))
#        btn = Button(background_normal='Settings G.png', size=(0.2, 0.2), pos=(100,100)) 
        self.btn = Button(background_normal='Settings B.png', size_hint=(0.06, 0.1))        
        self.overlay.add_widget(self.btn)
        self.Layout.add_widget(self.overlay)        
        self.btn.bind(on_press = self.show_dropdown)
        
        marker = MapMarker(anchor_x = 0.5, anchor_y = 0.5, lat=self.itu_lat, lon=self.itu_lon)
        self.mapview.add_marker(marker)        
        return self.Layout
        
    def show_dropdown(self,instance):
        
        
        layout = BoxLayout(orientation='vertical',size_hint=(0.12,0.10))
        btn1 = Button(text='Weather')
        btn2 = Button(text='Level')
        btn3 = Button(text='Nearby users')
        
        btn1.bind(on_press = self.show_weather_data)      
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        self.overlay.add_widget(layout)
    
    def show_weather_data(self,instance):
        
        top = AnchorLayout(anchor_x = 'left', anchor_y = 'bottom')
        layout = BoxLayout(orientation='vertical', size_hint = (0.2,0.1))
        
        clat = self.mapview.lat
        clon = self.mapview.lon        
        
        ctime = time.time()        
        
        if(self.obs_dic == None or ctime > (self.old_time + 20.0)):            
            self.old_time = ctime
            self.obs_dic = api.loc_weather(clat,clon)
            weList = self.obs_dic['weather']
            we = weList[0]
            wi = self.obs_dic['wind']            
            l1 = Label(text = 'Current weather: ' + we['main'])
            main = self.obs_dic['main']
            k = main['temp']
            #Conversion from imperial to metric
            temp = k-273.15
            l2 = Label(text = 'temp: ' + str(temp) + ' ' + u'\u00B0' + 'C')
            hu = main['humidity']
            l3 = Label(text = 'humidity: ' + str(hu) + '%')
            pre = main['pressure']
            l4 = Label(text = 'pressure' + str(pre) + ' hPa')
            wispeed = wi['speed']
            widir = wi['deg']
            l5 = Label(text = 'wind speed: ' + str(wispeed) + 'm/s')
            l6 = Label(text = 'wind direction '+ str(widir) + u'\u00B0')
            Tdp = temp - ((100-hu)/5)
            l7 = Label(text = 'dew point: ' + str(Tdp) + ' ' + u'\u00B0' + 'C')
            
            layout.add_widget(l1)
            layout.add_widget(l2)
            layout.add_widget(l3)
            layout.add_widget(l4)
            layout.add_widget(l5)
            layout.add_widget(l6)        
            layout.add_widget(l7)            
            
            top.add_widget(layout)
            self.overlay.add_widget(top)        
            
Main().run()
