#!/usr/bin/env python3

import datetime
from suntime import Sun, SunTimeException

latitude = 36.873512
longitude = -90.488008

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
utcSunrise = today_sr.strftime('%H:%M')
utcSunset = today_ss.strftime('%H:%M')
print(f'Poplar Bluff sunrise {utcSunrise} sunset {utcSunset} UTC')

# On a special date in your machine's local time zone
abd = datetime.date.today()
abd_sr = sun.get_local_sunrise_time(abd)
abd_ss = sun.get_local_sunset_time(abd)
localSunrise = abd_sr.strftime('%H:%M:%S')
localSunset = abd_ss.strftime('%H:%M:%S')
print(f'{abd} Local sunrise {localSunrise} sunset {localSunset} today.')
