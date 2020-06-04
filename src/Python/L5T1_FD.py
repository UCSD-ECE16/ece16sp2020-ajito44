#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:24:19 2020

@author: joyceeito
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig


data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.

fs = 50
t = data_array[:,0]
s = data_array[:,1]

def moving_average(s, n_avg):
    ma = np.zeros(s.size)
    for i in range(len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma
        
def detrend(s,n_avg):
    ma = moving_average(s, n_avg)
    s = s - ma
    return s

def main():
    L1norm = np.add(np.abs(data_array[:,1]),np.abs(data_array[:,2]), np.abs(data_array[:,3]))
    b,a = sig.butter(3,0.2,btype='low')
    c,d = sig.butter(3,0.5,btype='high')
    lowsignal_filtered = sig.lfilter(b, a, L1norm)
    highsignal_filtered = sig.lfilter(c, d, L1norm)
    plt.subplot(321)
    plt.plot(t,L1norm)
    plt.subplot(322)
    plt.psd(L1norm, NFFT=len(t), Fs=fs)
    plt.subplot(323)
    plt.plot(t,lowsignal_filtered)
    plt.subplot(324)
    plt.psd(lowsignal_filtered, NFFT=len(t), Fs=fs)
    plt.subplot(325)
    plt.plot(t,highsignal_filtered)
    plt.subplot(326)
    plt.psd(highsignal_filtered, NFFT=len(t), Fs=fs)
    plt.show()
    x = detrend(s, 15)
  #  plt.subplot(211)
   # plt.plot(t, x)
  #  plt.subplot(212)
   # plt.psd(x, NFFT=len(t), Fs=fs) #plot the power spectral density
   # plt.show()
    Pxx, freqs = plt.psd(x, NFFT=len(t), Fs=fs)
    index = np.argmax(Pxx)
    maxpower = freqs[index]
    print(maxpower)
    
main()

