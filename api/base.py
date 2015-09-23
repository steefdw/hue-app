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