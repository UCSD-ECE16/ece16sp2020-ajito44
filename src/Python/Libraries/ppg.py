#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:56:35 2020

@author: joyceeito
"""

import numpy as np


class PPG:
    
    def __init__(self,signal):
        self.signal = signal
        
    def baseline(self):
        mean_signal = np.mean(self.signal)
        s = self.signal - mean_signal
        return s  
        
    def moving_average(self, sig, n_avg): 
        ma = np.zeros(sig.size)
        for i in np.arange(0,len(sig)):
            ma[i] = np.mean(sig)
        return ma
    
    def detrend(self, trend, n_avg):
        ma = self.moving_average(trend,15)
        trend = trend - ma
        return trend
    
    def normalize_signal(self, sign):
        minimum = np.amin(sign)
        zero = sign - minimum
        maximum = np.amax(zero)
        one = zero/maximum
        return one
    
    def signal_diff(self):
        signal_diff = np.diff(self.signal)
        signal_diff = np.append(signal_diff, 0)
        return signal_diff
    
    def calc_heart_rate(self, x):
    
        beats = 0
    
        for i in range(len(x)):
            if  x[i] < 0.6:
                x[i] = 0
            if x[i] >= 0.6:
                x[i] = 1 
    
        for i in range(len(x)-1):
            if x[i] == 0 and x[i+1] == 1:
                beats = beats+1
            
        beats = beats/10
        beats = beats*60
        return beats
        