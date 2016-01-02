# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:02:01 2016

@author: steef
"""

class Rain:

  def __init__(self, mms):
    self.mmph = self.mmph(mms)
    self.type = self.rain_type()

  """
  Op basis van lat lon coördinaten kunt u de neerslag twee uur vooruit ophalen in tekst vorm. 
  0 is droog, 255 is zware regen.
  mm/per uur = 10^((waarde-109)/32)
  Dus 77 = 0.1 mm/uur 
  """
  def mmph(self, byte_int):
    value = (float(byte_int-109)/float(32))
    return 10**value

  def rain_type(self):
    if(self.mmph < 0.01):
        return {'id':0, 'name':'droog'}
    elif(self.mmph < 0.18):
        return {'id':1, 'name':'zeeeeer lichte motregen -- test'}        
    elif(self.mmph < 0.6):
        return {'id':1, 'name':'lichte motregen'}
    elif(self.mmph < 0.9):
        return {'id':2, 'name':'motregen'}
    elif(self.mmph < 1.5):
        return {'id':3, 'name':'lichte regen'}
    elif(self.mmph < 8):
        return {'id':4, 'name':'regen'}
    elif(self.mmph < 18):
        return {'id':5, 'name':'stevige bui'}
    elif(self.mmph < 25):
        return {'id':6, 'name':'zeer zware bui'}
    elif(self.mmph < 50):
        return {'id':7, 'name':'wolkbreuk'}
    return {'id':8, 'name':'zeer zware wolkbreuk'}

  def name(self):
    return self.type['name']