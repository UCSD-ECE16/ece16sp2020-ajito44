#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:45:07 2020

@author: joyceeito
"""

import numpy as np

cb = np.array([0,0,0,0,0])

cb[:-3] = cb[3:]
cb[-3:] = [10,12,1]
print(cb)
cb[:-3] = cb[3:]
cb[-3:] = [3,19,23]
print(cb)
cb[:-3] = cb[3:]
cb[-3:] = [24,5,78]
print(cb)
cb[:-3] = cb[3:]
cb[-3:] = [29,12,4]
print(cb)
print('\n')

cb1 = np.array([[0,0,0],[0,0,0]])
print(cb1)
cb1[:-1] = cb1[1:]
cb1[-1:] = [10,12,1]
print(cb1)
cb1[:-1] = cb1[1:]
cb1[-1:] = [3,19,23]
print(cb1)
cb1[:-1] = cb1[1:]
cb1[-1:] = [24,5,78]
print(cb1)
cb1[:-1] = cb1[1:]
cb1[-1:] = [29,13,4]
print(cb1)
