#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

import random

class Lights:

  def __init__(self, Request):
    self.lights = []
    self.states = {}
    self.request = Request
    
  def getLights(self):
    content = self.request.get('lights')        
    
    for (k, v) in content.items():
      v['id'] = int(k)            
      self.lights.append(v)
      self.states[v['id']] = v['state']['on']
            
  def toggle(self, color = False, brightness = 254):
    if(color == False):
      color = random.randint(0,65535);
            
    for lightId, state in self.states.items():
      newState = (state == False)
      action = 'lights/'+str(lightId)+'/state'            
            
      if(newState == True):
        payload = {
          'on':True,
          "sat":254,
          "bri":brightness,
          "hue":color,
          #'transitiontime':50
        }
      else:
        payload = {'on': newState}
            
      r = self.request.put(action, payload)
            
      self.states[lightId] = newState
            
    return r

  def wobble(self, color = False, brightness = 254):
    if(color == False):
      color = random.randint(0,65535);
            
    for lightId, state in self.states.items():
      newState = (state == False)
      action = 'lights/'+str(lightId)+'/state'            
            
      if(newState == True):
        payload = {'on':True,"sat":254, "bri":brightness,"hue":color}
      else:
        payload = {'on':True,"sat":254, "bri":10,"hue":color}
            
      r = self.request.put(action, payload)
            
      self.states[lightId] = newState
            
    return r
        
  def toggleColorloop(self, on = True, brightness = 254):
    for lightId, state in self.states.items():
      action = 'lights/'+str(lightId)+'/state'

      if(on == True):
        payload = {'on':True,"sat":254, "bri":brightness,"effect":"colorloop"}
      else:
        payload = {"effect":"none"}
            
      r = self.request.put(action, payload)
            
    return r

  def toggleAlert(self, on = True, color = 65535):
    for lightId, state in self.states.items():
      action = 'lights/'+str(lightId)+'/state'

      if(on == True):
        payload = {
          'on':True,          
          "sat":254, # note: setting brightness doesn' t do anything 
          "alert":"lselect",
          "hue": color
        }
      else:
        payload = {"alert":"none"}
            
      r = self.request.put(action, payload)
            
    return r
    
  def off(self):            
    for lightId, state in self.states.items():
        action = 'lights/'+str(lightId)+'/state'        
        payload = {'on': False}
            
        r = self.request.put(action, payload)
          
        self.states[lightId] = False
            
    return r