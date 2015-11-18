#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:59:25 2015

@author: steef
"""
 
from api.base import Init
import time

class Alert():

  def __init__(self):
    self.hue = Init(False)
    self.hue.lights.getLights()

  # this gives a manual alert-like effect
  def softblink(self, times = 10, color = 0, brightness = 254):
    for n in range(times):
        self.hue.lights.toggle(color, brightness)
        time.sleep(0.8)
        self.hue.lights.wobble(color, brightness)
        time.sleep(0.4)
        
    self.hue.lights.off()

  # this gives a manual alert-like effect
  def blink(self, times = 10, color = 0, brightness = 254):
    for n in range(times):
        self.hue.lights.toggle(color, brightness)
        time.sleep(0.8)
        
    self.hue.lights.off()
    
  # this gives a green alert
  def alert(self, duration = 15, color = 0):
    self.hue.lights.off()
    self.hue.lights.toggleAlert(True, color)
    time.sleep(duration)
    self.hue.lights.off()

  # this gives a manual alert-like effect
  def rainbow(self, duration = 10, brightness = 254):
    self.hue.lights.toggleColorloop(True, brightness)
    time.sleep(duration)
    self.hue.lights.toggleColorloop(False)
    self.hue.lights.off()
    
alert = Alert()
color = alert.hue.color('purple')
alert.blink(10, color)