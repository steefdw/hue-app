#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

import random
from request import Request

class Lights:

  def __init__(self):
    self.lights = []
    self.states = {}
    self.request = Request(True)
    
  def getLights(self):
    content = self.request.get('lights')        
    
    for (k, v) in content.items():
      v['id'] = int(k)            
      self.lights.append(v)
      self.states[v['id']] = v['state']['on']
            
  def toggle(self, color = False):
    if(color == False):
      color = random.randint(0,65535);
            
    for lightId, state in self.states.items():
      newState = (state == False)
      action = 'lights/'+str(lightId)+'/state'            
            
      if(newState == True):
        payload = {'on':True,"sat":255, "bri":255,"hue":color}
      else:
        payload = {'on': newState}
            
      r = self.request.put(action, payload)
            
      self.states[lightId] = newState
            
    return r

  def wobble(self, color = False):
    if(color == False):
      color = random.randint(0,65535);
            
    for lightId, state in self.states.items():
      newState = (state == False)
      action = 'lights/'+str(lightId)+'/state'            
            
      if(newState == True):
        payload = {'on':True,"sat":255, "bri":255,"hue":color}
      else:
        payload = {'on':True,"sat":255, "bri":10,"hue":color}
            
      r = self.request.put(action, payload)
            
      self.states[lightId] = newState
            
    return r
        
  def toggleColorloop(self, on = True):
    for lightId, state in self.states.items():
      action = 'lights/'+str(lightId)+'/state'

      if(on == True):
        payload = {'on':True,"sat":255, "bri":255,"effect":"colorloop"}
      else:
        payload = {"effect":"none"}
            
      r = self.request.put(action, payload)
            
    return r
