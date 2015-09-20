#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:46 2015

@author: steef
"""

import requests
import json

from config import Config
from api.lights import Lights
from api.schedule import Schedule

class Init(Lights, Schedule):

  def __init__(self, debug = False):
    config = Config()
    self.apiKey = config.apiKey
    self.root = config.root
        
    self.lights = []
    self.states = {}
        
    self.debug = debug
 
  def url(self, action):
    return self.root+self.apiKey+'/'+action        
            
  def response(self, r):        
    try:
      response = json.loads(r.text)
      if(self.debug):
        print json.dumps(response, sort_keys=False, indent=2, separators=(',', ': '))
        return response
    except:
      return r.text
            
  def get(self, action, data=None):
    url = self.url(action)
    r = requests.get(url, params=data)
        
    return self.response(r)

  def post(self, action, data={}):
    url = self.url(action)
    r = requests.post(url, data=json.dumps(data))
    print json.dumps(data)
    
    return self.response(r)

  def put(self, action, data={}):
    url = self.url(action)
    r = requests.put(url, data=json.dumps(data))
    
    return self.response(r)

  def delete(self, action, data=None):
    url = self.url(action)
    r = requests.delete(url, data=json.dumps(data))
        
    return self.response(r)         