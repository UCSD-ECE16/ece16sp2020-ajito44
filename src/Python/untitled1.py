#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:48:51 2020

@author: joyceeito
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig

signal_in = np.genfromtxt('lab5_appendix_a.csv', delimiter=',')
fs = 100

def moving_average(s, n_avg):
    ma = np.zeros(s.size)
    for i in range(len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma

def detrend(s,n_avg):
    ma = moving_average(s, n_avg)
    s = s - ma
    return s

x = detrend(signal_in,15)
Pxx, freqs = plt.psd(x, Fs=fs)
plt.show()
index = np.argmax(Pxx)
maxpower = freqs[index]
#print(maxpower)
#dominant frequency = {5.078125, 1.5?}
b,a = sig.butter(3, 1.5, btype='high', fs= fs)
signal_out_offline = sig.lfilter(b,a,signal_in)
zi_in = sig.lfilter_zi(b,a)
zi_in = zi_in*signal_in[0]
     
start = 0
block_size = 50
signal_out_online = np.zeros(len(signal_in))
while start + block_size <= len(signal_in):
    signal_block = signal_in[start:start+block_size]
    signal_block,zi_out = sig.lfilter(b,a,signal_block, zi = zi_in)
    zi_in = zi_out
    signal_out_online[start:start+block_size] = signal_block
    start = start + 50
    block_size = block_size + 50
    
plt.subplot(221)
plt.plot(signal_out_offline)
plt.subplot(222)
plt.psd(signal_out_offline,Fs=fs)
plt.subplot(223)
plt.plot(signal_out_online)
plt.subplot(224)
plt.psd(signal_out_online,Fs=fs)
plt.show()



