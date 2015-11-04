#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:59:25 2015

@author: steef
"""
 
from api.base import Init
import time

Hue = Init(False)
Hue.lights.getLights()

while True:
    r = Hue.lights.toggle()
    #r = Hue.lights.wobble()
    #print r
    time.sleep(0.8)

#current = time.time()
#newtime = time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(current+20))
#newtime = 'W124/T08:25:00'
newtime = 'PT00:00:05'
payload = {
    'on':False,
    'sat':255,
    'bri':1,
    'hue':12345
}

#Hue.schedule.add(newtime, payload, True)
#Hue.schedule.get()

#todo '''
''' 
     wobble(color, lo, hi, interval) - this changes bightness between lo,hi with interval int and color x

if color is a list, you can set a color for each lamp
     color(name) - make a hue value (0,65535) from a string. Defaults to white
     toggle(color, fadeTime) - turns lights on/off
     class Color(colorname,brightness,staturation) - create the payload with ease: color(...).payload()
'''