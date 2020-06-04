#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:19:32 2020

@author: joyceeito
"""


import numpy as np
from scipy import signal

class Pedometer:

  def __init__(self, max_samples, data_array):
    self.max_samples = max_samples
    self.data_array = data_array
    self.filtered_data = np.array([])

  def l1_norm(self):
    self.filtered_data = np.add(np.abs(self.data_array[:,1]),np.abs(self.data_array[:,2]), np.abs(self.data_array[:,3]))  # compute the L1 Norm using data_array

  def lpf(self):
    self.l1_norm()
    self.detrend(15)
    t = self.data_array[:,0]
    F,Pxx = signal.welch(self.filtered_data, fs = self.max_samples, nfft=len(t))
    index = np.argmax(Pxx)
    maxpower = F[index]
    #print(maxpower)# find the dominant frequency component
    b,a = signal.butter(3, maxpower, btype='low', fs= self.max_samples)# define a low pass filter
    self.filtered_data = signal.lfilter(b, a, self.filtered_data) # Apply the low-pass filter

  def moving_average(self, n_avg):
      s = self.filtered_data
      ma = np.zeros(s.size)
      for i in range(len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
      return ma

  def detrend(self, n_avg):
      ma = self.moving_average(n_avg)
      self.filtered_data = self.filtered_data - ma
     
  def get_gradient(self):
     self.lpf()
     self.filtered_data = np.gradient(self.filtered_data) # use np.gradient

  def get_peaks(self):
      peaks, props = signal.find_peaks(self.filtered_data)
      peak_inds = peaks
      return peak_inds
      
  def count_steps(self):
    peak_inds = self.get_peaks()
    inds = []
    step_count = 0
    for i in range(len(peak_inds)):
        val = self.filtered_data[peak_inds[i]]
        if val <12 and val > 3:
            step_count = step_count + 1
            inds = np.append(inds, peak_inds[i])
    return step_count, inds

  def process_data(self):
    self.get_gradient()  # filter the data 
    step_count, inds = self.count_steps() # call the count_steps() method
    return step_count, inds# return step_count


