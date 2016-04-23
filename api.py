# -*- coding: utf-8 -*-
"""
A module for interacting with online APIs
"""

import json
import httplib
import googlemaps
#import android

droid = android.Android()
owm_key = "fee04268dd271d32dbdefe59fe85f13b"
owm_baseurl = r"api.openweathermap.org"
googleKey = "AIzaSyAEe6adJXOA-GtGk9_HZgJMfTzC9TIAoyc"
googleClient = googlemaps.Client(key=googleKey)

def loc_weather(lat, lon):
    # Request JSON from OWM
    conn = httplib.HTTPConnection(owm_baseurl)
    req = "/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=fee04268dd271d32dbdefe59fe85f13b"
    conn.request("GET", req, "")
    res = conn.getresponse()
    body = res.read()
    # Turn json into dictionary
    dict = json.loads(body)
    return dict

def get_location():
    droid.startLocating()
    event=droid.eventWaitFor('location', 50000)
    while 1:
        try:
            provider = event.result['data']['gps']['provider']
            if provider == 'gps':
                lat = str(event['data']['gps']['latitude'])
                lon = str(event['data']['gps']['latitude'])
                return (lat,lon)
            else: continue
        except KeyError:
            continue
    
def httpTest():
    url = "api.openweathermap.org"
    body = "Request failed."
    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/data/2.5/weather?zip=2500,dk&APPID=fee04268dd271d32dbdefe59fe85f13b", body)
    res = conn.getresponse()
    print res.status, res.reason