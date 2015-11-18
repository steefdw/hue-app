#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

from api.lights import Lights
from api.schedule import Schedule
from api.request import Request

class Init():

  def __init__(self, debug = False):
    self.request = Request(debug)
    self.lights = Lights(self.request)
    self.schedule = Schedule(self.lights, self.request)    
    self.debug = debug
    
  def color(self, color):
    if(color == 'red'):
      return 0
    if(color == 'yellow'):
      return 12750
    if(color == 'green'):
      return 25500
    if(color == 'blue'):
      return 46920
    if(color == 'purple'):
      return 56100
    
    return 65280      