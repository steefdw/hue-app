#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

class Schedule:
  def __init__(self, Lights, Request):
    self.lights  = Lights
    self.request = Request
    self.responses = []      
    
  def add(self, time, body, permanent = False):       
    action = 'schedules'
    for light in self.lights.lights:    
      payload = self.statePayload(light['id'], time, body, permanent)
      self.responses.append(self.request.post(action, payload))
    return self.responses
    
  def get(self, scheduleId = False):
    action = 'schedules'
    
    if(scheduleId != False):
      action = 'schedules/'+scheduleId
          
    return self.request.get(action)
    
  def statePayload(self, lightId, time, body, permanent):
    return {
      #"name":"test",
      #"description":"test",
      "command":{
        "address":"/api/"+self.request.apiKey+"/lights/"+str(lightId)+"/state",
        "method":"PUT",
        "body": body,
        #"autodelete":permanent
      },
      "localtime":time
    }