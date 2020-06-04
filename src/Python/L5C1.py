#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:16:15 2020

@author: joyceeito
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
from Libraries.Connection import Connection

def moving_average(s, n_avg):
    ma = np.zeros(s.size)
    for i in range(len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma

def detrend(s,n_avg):
    ma = moving_average(s, n_avg)
    s = s - ma
    return s

data_array = np.genfromtxt('lab5C1.csv', delimiter=',')
fs = 50
t = data_array[:,0]
L1norm = np.add(np.abs(data_array[:,1]),np.abs(data_array[:,2]), np.abs(data_array[:,3]))
ma_sig = detrend(L1norm, 15)
F,Pxx = sig.welch(ma_sig, fs = fs, nfft=len(t))
index = np.argmax(Pxx)
maxpower = F[index]
print(maxpower)
    
b,a = sig.butter(3, maxpower, btype='low', fs= 50)
sfilt = sig.lfilter(b, a, ma_sig)
grad_sfilt = np.gradient(sfilt)

peaks, props = sig.find_peaks(grad_sfilt)
peak_inds = peaks
inds = []
count = 0
for i in range(len(peak_inds)):
    val = grad_sfilt[peak_inds[i]]
    if val <12 and val > 3:
        count = count + 1
        inds = np.append(inds, peak_inds[i])
        print(inds)
oled = Connection("/dev/cu.Angela_Bluetooth-ESP32S",115200)
count = str(count)
count = count + '\n'
oled.send_serial(count)
oled.close_connection()
print(count)
#plt.subplot(211)
plt.plot(grad_sfilt)
plt.plot(inds,grad_sfilt[inds.astype(int)], 'rx' )
#plt.subplot(212)
#plt.psd(grad_sfilt, NFFT=len(t), Fs=fs) #plot the power spectral density
plt.show()