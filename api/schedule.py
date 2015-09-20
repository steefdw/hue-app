#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

class Schedule:

 def schedule(self, time, body):       
    action = 'schedules'
    payload = {
      "name":"test",
      "description":"test",
      "command":{
        "address":"/api/"+self.apiKey+"/lights/1/state",
        "method":"PUT",
        "body": body
      },
      "localtime":time
    }
        
    return self.post(action, payload)