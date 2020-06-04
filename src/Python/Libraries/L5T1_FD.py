#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:24:19 2020

@author: joyceeito
"""


import numpy as np
import matplotlib.pyplot as plt

data_array = np.genfromtxt('appendix_a', delimiter=',')

fs = 50
t = data_array[:,0]
s = data_array[:,1]

plt.subplot(211)
plt.plot(t,s)
plt.subplot(212)
plt.psd(s, NFFT=len(t), Fs=fs) #plot the power spectral density
plt.show()
