#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 4 15:46 2015

@author: steef
"""
 
from api.base import Init
import time

Hue = Init(False)
Hue.lights.getLights()
Hue.lights.toggleColorloop(True)

time.sleep(20)
Hue.lights.off()