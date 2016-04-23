from plyer import gps

global lat
global lon

lat = -1
lon = -1

def get_lat():
    if lat > 0:
        return lat
    else:
        return None

def get_lon():
    if lon > 0:
        return lon
    else:
        return None

def set_lat(val):
    lat = val

def set_lon(val):
    lon = val

def save_locations(**kwargs):
    set_lat(kwargs.pop('lat'))
    set_lat(kwargs.pop('lon'))
    
gps.configuration(on_location=save_locations)


def start_tracking():
    gps.start()

def stop_tracking():
    gps.stop()
