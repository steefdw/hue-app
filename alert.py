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

# this gives a green alert
"""
Hue.lights.off()
Hue.lights.toggleAlert(True, 46920)
time.sleep(15)
Hue.lights.off()
#"""

# this gives a manual alert-like effect
#"""
for n in range(10):
    r = Hue.lights.toggle(200000)
    time.sleep(0.8)
    r = Hue.lights.wobble(302000)
    time.sleep(0.4)
    
Hue.lights.off()
#"""