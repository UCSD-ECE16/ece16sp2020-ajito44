#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:36:47 2020

@author: joyceeito
"""
import numpy as np
import matplotlib.pyplot as plt

data_array_from_file = np.genfromtxt('appendix_b.csv', delimiter=',')
s = data_array_from_file[:,4]

def moving_average(s, n_avg):
    ma = np.zeros(s.size)
    for i in range(len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma
        
def detrend(s,n_avg):
    ma = moving_average(s, n_avg)
    s = s - ma
    return s

def signal_diff(s):
    s_diff = np.diff(s)
    s_diff = np.append(s_diff, 0)
    return s_diff

def main():
    t = detrend(s,15)
    x = signal_diff(s)
    plt.clf()
    plt.plot(x)
    plt.show()
    
main()