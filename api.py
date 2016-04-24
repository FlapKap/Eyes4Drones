# -*- coding: utf-8 -*-
"""
A module for interacting with online APIs
"""

import json
import httplib
#http://api.geonames.org/findNearByWeatherJSON?lat=43&lng=-2&username=demo
#http://forecast.weather.gov/MapClick.php?lat=38.4247341&lon=-86.9624086&FcstType=json


#geo_baseurl = r"api.geonames.org"
#f_baseurl = r"forecast.weather.gov"

owm_key = "fee04268dd271d32dbdefe59fe85f13b"
owm_baseurl = r"api.openweathermap.org"

#noaa_baseurl = r"ncdc.noaa.gov"
#noaa_key = r"zEYCMRLbHZjDKmMEPdJNdlxvtNoW"

def loc_weather(lat, lon):
    # Request JSON from OWM
    conn = httplib.HTTPConnection(owm_baseurl)
    #req = r"/findNearByWeatherJSON?lat=" + str(lat) + r"&lng=" + str(lon) + r"&username=demo"
    #req = r""
    
    req = r"/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=" + owm_key
    #req = r"/MapClick.php?lat="+str(lat)+r"&lon="+str(lon)+r"&FcstType=json"
    conn.request("GET", req, "") #, "token:"+noaa_key)
    res = conn.getresponse()
    body = res.read()
    #print body
    # Turn json into dictionary
    try:
        dic = json.loads(body)
    except:
        dic = None
    return dic
    
def httpTest():
    url = "api.openweathermap.org"
    body = "Request failed."
    conn = httplib.HTTPConnection(url)
    conn.request("GET", "/data/2.5/weather?zip=2300,dk&APPID="+owm_key, body)
    res = conn.getresponse()
    body = res.read()
    print res.status, res.reason
    print body
    dic = json.loads(body)
    print dic['weather']
    print dic['main']
    print dic['wind']
    
    weather = dic['weather']
    main = dic['main']
    wind = dic['wind']
    
    print wind['speed']
    
    
#tests
#print "test 1"
#httpTest()
#from time import sleep
#sleep(900)