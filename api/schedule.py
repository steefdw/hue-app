#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

from request import Request

class Schedule:
  def __init__(self):
    self.request = Request(True)

  def add(self, time, body):       
    action = 'schedules'
    payload = {
      "name":"test",
      "description":"test",
      "command":{
        "address":"/api/"+self.request.apiKey+"/lights/1/state",
        "method":"PUT",
        "body": body
      },
      "localtime":time
    }
        
    return self.request.post(action, payload)
    
  def get(self, scheduleId = False):
    action = 'schedules'
    
    if(scheduleId != False):
      action = 'schedules/'+scheduleId
          
    return self.request.get(action)