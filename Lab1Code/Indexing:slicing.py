#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:01:51 2020

@author: joyceeito
"""


import numpy as np

e = np.array([(12,3,1,2),
              (0,0,1,2),
              (4,2,3,1)])

print(e[0])
print(e[1,0])
print(e[:,1])
print(e[2,:2]) 
print(e[2,2:]) 
print(e[:,2]) 
print(e[1,3]) 
         