#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:45:41 2020

@author: joyceeito
"""


import numpy as np

a = np.array([0,10,4,12,0,10,4,12])
b = np.array([0,10,4,12,0,10,4,12])
c = np.array([0,10,4,12,0,10,4,12])
d = np.array([0,10,4,12,0,10,4,12])

print(np.vstack((((a,b,c,d)))))

e = np.array([(0,10) ,
              (0,10) ,
              (0,10) ,
              (0,10)])
f = np.array([(4,12),
              (4,12),
              (4,12),
              (4,12)])
g = np.array([(0,10) ,
              (0,10) ,
              (0,10) ,
              (0,10)])
h = np.array([(4,12),
              (4,12),
              (4,12),
              (4,12)])

print(np.hstack((((e,f,g,h)))))