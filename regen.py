#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:50:56 2015

@author: steef
"""

from rain import Rain
"""
import requests

lat = '52.108256399999995'
lon = '5.1038214'
url = 'http://gps.buienradar.nl/getrr.php?lat='+lat+'&lon='+lon;
r = requests.get(url)
lines = r.text.split('\n')
#"""
lines = open('regen-sample-data-better.txt', 'r')

for line in lines:
  forecast = line.split('|')
  if len(forecast) == 2:
    rain_int = int(forecast[0])
    time = forecast[1].replace('\n', '').replace('\r', '')    
    rain = Rain(rain_int)

    print 'at {}, it will rain {} = {} mm/h ({})'.format(
      time, 
      rain_int, 
      round(rain.mmph,3), 
      rain.name()
    )