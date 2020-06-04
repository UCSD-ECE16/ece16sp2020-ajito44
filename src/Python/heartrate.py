#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:09:35 2020

@author: joyceeito
"""

import numpy as np
import matplotlib.pyplot as plt

data_array_from_file = np.genfromtxt('02_0_096.csv', delimiter=',')
signal = data_array_from_file[:,4]

def baseline(signal):
    mean_signal = np.mean(signal)
    signal = signal - mean_signal
    return signal

def moving_average(signal, n_avg):
    ma = np.zeros(signal.size)
    for i in range(len(signal)):
        ma[i] = np.mean(signal[i:i+n_avg])
    return ma

def highfrequency(signal, n_avg):
    ma = moving_average(signal, n_avg)
    signal = signal - ma
    return signal

def gradient(signal):
    signal_diff = np.diff(signal)
    signal_diff = np.append(signal_diff, 0)
    return signal_diff

def calc_heart_rate(signal):
    x = baseline(signal)
    x = highfrequency(x, 10)
    x = normalize_signal(x)
    y = gradient(signal)
    plt.clf
    plt.plot(x)
    plt.show
    
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
    print(beats)
    return beats
    
def normalize_signal(signal):
    minimum = np.amin(signal)
    zero = signal - minimum
    maximum = np.amax(zero)
    one = zero/maximum
    return one

def main():
    x = normalize_signal(signal)
    x = baseline(x)
    x = highfrequency(x, 10)
    plt.clf()
    plt.plot(x)
    plt.show()

main()
