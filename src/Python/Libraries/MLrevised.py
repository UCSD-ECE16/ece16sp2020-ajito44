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


class ML:
     def __init__(self):
         self.test_pred = []
         self.hr = []
    
    #directory = "/Users/joyceeito/Downloads/SPring2020/ece16sp2020-ajito44/src/Python/Data_Lab5_ML/Training/"
    
     def sorted_data(self, directory):
         all_files = glob.glob(directory + '*.csv')
         unique_ids = sorted(list(OrderedDict.fromkeys([i.split(directory)[1].split('_')[0]for i in all_files])))
         
         list_data = []
         list_ref = []
         list_sub = []
    
         for sub_id in range(len(unique_ids)): 
            sub_files = glob.glob(directory + unique_ids[sub_id] + '_*.csv')
            for i in range(len(sub_files)):
                data = np.genfromtxt(sub_files[i], delimiter = ',')
                hr_data = data[:500,4] * -1 
                #plt.plot(hr_data)
                #plt.show()
                ppg = PPG(hr_data) 
                hr_data = hr_data - np.mean(hr_data)
                #plt.plot(hr_data)
                #plt.show()
                highfrequency = ppg.detrend(hr_data,10)
                #plt.plot(highfrequency)
                #plt.show()
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
                
         return list_ref, list_data, list_sub, unique_ids
    
            #plt.plot(self.list_data[0])  
            #plt.figure()    
    
    #plt.hist(self.list_data[2],bins=50, density=True)
    #plt.xlim((min(list_data[6]),max(list_data[6])))
    

     
     def train_hr_model(self, directory):
         
         list_ref, list_data, list_sub, unique_ids = self.sorted_data(directory)
         
         
         train_data = np.empty(0)
         hold_out_data = np.empty(0)

         hold_out_subject = unique_ids[0]
         for ind, sub_id in enumerate(list_sub):
             if sub_id != hold_out_subject:
                 train_data = np.concatenate((train_data, list_data[ind]))
             else:
                 hold_out_data = np.concatenate((hold_out_data, list_data[ind]))
        
         self.gmm = GMM(n_components=2).fit(train_data.reshape(-1,1))
         self.test_pred = self.gmm.predict(hold_out_data.reshape(-1,1))
         #plt.plot(self.test_pred[:500])
         #plt.plot(hold_out_data[:500])
         #plt.show()
         
     def calc_hr(self,s,fs):
         hr = []
         for i in range(int(len(s)/500)):
             count = 0
             for j in range(i*500,i*500+500):
                 if s[j] == 0 and s[j-1] == 1:
                     count = count + 1
             secs = count / 10
             bpm = secs * 60
             hr.append(bpm)
         #print(self.hr)
         return hr
         
     def test_hr_model(self,directory): 
         
         list_ref, list_data, list_sub, unique_ids = self.sorted_data(directory)
         
         heartrate = []
         
         for ind, sub_id in enumerate(list_sub):
                 test_pred = self.gmm.predict(np.array(list_data[ind]).reshape(-1,1))
                 plt.plot(test_pred[:500])
                 plt.plot(np.array(list_data[ind]))
                 plt.show()
                 heartrate_sample = self.calc_hr(test_pred, 50)
                 heartrate.append(heartrate_sample[0])
                
         #testhr = np.array(self.hr[j*10:j*10+10])
         #refhr= np.array(list_ref[j*10:j*10+10])
         #combined = np.vstack((testhr,refhr))
         #print(np.shape(combined))
         #print(combined)
         return heartrate, list_ref
             #print(np.shape(combined))
         #print(combined)
         
     
def main():
   directory = "/Users/joyceeito/Downloads/SPring2020/ece16sp2020-ajito44/src/Python/Data_Lab5_ML/Training/"
   testing = "/Users/joyceeito/Downloads/SPring2020/ece16sp2020-ajito44/src/Python/Data_Lab5_ML/Testing/"
   x = ML()
   x.train_hr_model(directory)
   y,z = x.test_hr_model(testing)
   print(y)
   print(z)
   
    
     
     





    
    