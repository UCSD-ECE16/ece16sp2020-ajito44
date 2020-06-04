#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:05:46 2020

@author: joyceeito
"""


import glob
from collections import OrderedDict
import numpy as np
from Libraries.ppg import PPG
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.stats import norm
from sklearn.mixture import GaussianMixture as GMM

directory = "/Users/joyceeito/Downloads/SPring2020/ece16sp2020-ajito44/src/Python/Data_Lab5_ML/Training/"

all_files = glob.glob(directory + '*.csv')

unique_ids = sorted(list(OrderedDict.fromkeys([i.split(directory)[1].split('_')[0]for i in all_files])))
#unique_ids.sort(key=int)
#print(unique_ids) 


list_data = []
list_sub = []
list_ref = []

for sub_id in range(len(unique_ids)): #sub_id in the list of unique_ids
    sub_files = glob.glob(directory + unique_ids[sub_id] + '_*.csv')
    #print(sub_files) #using glob get the files of all files with this subject id
    for i in range(len(sub_files)):#each file in the list of files for this subject
       data = np.genfromtxt(sub_files[i], delimiter = ',')#read the csv
       hr_data = data[:500,4] * -1 #get the ppg signal from data using slicing
       ppg = PPG(hr_data)#preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
       highfrequency = sig.detrend(hr_data)
       F,Pxx = sig.welch(highfrequency, fs =50)
       index = np.argmax(Pxx)
       maxf = F[index]
       b,a = sig.butter(3,maxf,btype = 'l',fs = 50)
       low_pass = sig.lfilter(b,a,highfrequency)
       filtered = ppg.normalize_signal(low_pass)
       list_data.append(filtered)
       list_sub.append(unique_ids[sub_id])
       referencehr = sub_files[i].split(directory)[1].split('_')[2].split('.csv')[0]
       list_ref.append(referencehr)
plt.plot(list_data[0])  
plt.figure()    
#print(len(list_sub))
#print(list_ref)


plt.hist(list_data[2],bins=50, density=True)
#plt.xlim((min(list_data[6]),max(list_data[6])))

#mean = np.mean(list_data[1])
#variance = np.var(list_data[1])
#sqr = np.sqrt(variance)
#x = np.linspace(min(list_data[1]),max(list_data[1]),100)
#y = norm.pdf(x,variance,sqr)
#z = norm.pdf(y,variance,sqr)
#plt.plot(x,y)
#plt.plot(x,z)
plt.show()

train_data = np.empty(0)
hold_out_data = np.empty(0)

hold_out_subject = unique_ids[1]
for ind, sub_id in enumerate(list_sub):
    if sub_id != hold_out_subject:
        train_data = np.concatenate((train_data, list_data[ind]))
    else:
        hold_out_data = np.concatenate((hold_out_data, list_data[ind]))
        #print(len(hold_out_data))
        
#print(len(train_data))
        
gmm = GMM(n_components=2).fit(train_data.reshape(-1,1))
test_pred = gmm.predict(hold_out_data.reshape(-1,1))
#print(len(test_pred))
plt.plot(test_pred[:500])
plt.plot(hold_out_data[:500])
plt.show()


hr = []
for i in range(10):
    count = 0
    for j in range(i*500,i*500+500):
        if test_pred[j] == 0 and test_pred[j-1] == 1:
            count = count + 1
    secs = count / 10
    bpm = secs * 60
    hr.append(bpm)
    
print(hr)





    
    