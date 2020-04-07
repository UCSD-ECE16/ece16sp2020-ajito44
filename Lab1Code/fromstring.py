#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:22:48 2020

@author: joyceeito
"""
import numpy as np

data_string = '1,2,3,4'
data_array = np.fromstring(data_string,dtype=int,sep=',')
a = data_array
b = data_array
i = 0
while i<50:
    print(np.vstack((a,b)))
    i+=1