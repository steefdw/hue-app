#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

from api.lights import Lights
from api.schedule import Schedule

class Init():

  def __init__(self, debug = False):
    self.lights = Lights()
    self.schedule = Schedule()       
    self.debug = debug