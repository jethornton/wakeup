#!/usr/bin/env python3

#from astral import Astral
from astral import Location
#city_name = 'Poplar Bluff'
#a = Astral()
#a.solar_depression = 'civil'
#a.latitude = 36.873512
#a.longitude = -90.488008
#city = a[city_name]
#sun = a.sun(date=datetime.date.today(), local=True)


# define the location
location = Location()
location.name = 'Poplar Bluff'
location.region = 'Missouri'
location.latitude = 36.873543
location.longitude = -90.488055
location.timezone = 'US/Central'
location.elevation = 110
#location.sun() Returns dawn, sunrise, noon, sunset and dusk as a dictionary.
dawn = location.sun()['dawn']
dawn.strftime('%I:%M:%S')

sunrise = location.sun()['sunrise']
sunset = location.sun()['sunset']
dusk = location.sun()['dusk']
dusk.strftime('%I:%M:%S')
print(sunrise.strftime('%I:%M:%S'))

