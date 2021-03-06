#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:56:35 2020

@author: joyceeito
"""

import numpy as np
from scipy import signal


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
            ma[i] = np.mean(sig[i:i+n_avg])
        return ma
    
    def detrend(self, trend, n_avg):
        ma = self.moving_average(trend,10)
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
        x = x * -1
    
        for i in range(len(x)):
            if  x[i] < 0.5:
                x[i] = 0
            if x[i] >= 0.5:
                x[i] = 1 
    
        for i in range(len(x)-1):
            if x[i] == 0 and x[i+1] == 1:
                beats = beats+1
            
        beats = beats/10
        beats = beats*60
        return beats
    
    def onlyonce(self):
      F,Pxx = signal.welch(self.signal, fs = 100)
      index = np.argmax(Pxx)
      maxpower = F[index]
      b,a = signal.butter(3,maxpower,'highpass',fs= 100)
      zi_in = signal.lfilter_zi(b,a)
      zi_in = zi_in*self.signal[0] # ONLY DO THIS ONCE
      return b, a, zi_in
      # call in wearable

    def lfilter(self, b, a, zi_in):
      start = 0
      block_size = 50
      signal_out_online = np.zeros(len(self.signal))
      while start + block_size <= len(self.signal):
          signal_block = self.signal[start:start+block_size]
          signal_block,zi_out = signal.lfilter(b,a,signal_block, zi = zi_in)
          zi_in = zi_out
          signal_out_online[start:start+block_size] = signal_block
          start = start + 50
          block_size = block_size + 50
      self.signal = signal_out_online
      return zi_in
      
        