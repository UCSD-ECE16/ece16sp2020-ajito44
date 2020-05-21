#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:30:36 2020

@author: joyceeito
"""


import matplotlib.pyplot as plt

class Visualization:
  def __init__(self, data_array=None):
    (self.time, self.accelX, self.accelY, self.accelZ, self.ppg) = ([], [], [], [], [])
    if data_array is not None:
      self.addData(data_array)

  def addData(self, data_array):
    self.time = data_array[:, 0]
    self.accelX = data_array[:, 1]
    self.accelY = data_array[:, 2]
    self.accelZ = data_array[:, 3]
    if data_array.shape[1] == 5:
        self.ppg = data_array[:, 4]
    
  def plotData(self):
    self.plotAccel() 
    # plot the 3 axis accelerometer axes and the heart pulse signal into 4 subplots
    # Hint: you could call the below methods! And do not forget the time on the x-axis!

  def plotAccel(self):
    plt.clf()
    plt.subplot(411)
    plt.plot(self.time, self.accelX)
    plt.title("Accelerometer Values")
    plt.ylabel("X Accel")          
    plt.subplot(412)
    plt.plot(self.time, self.accelY)
    plt.ylabel("Y Accel")
    plt.subplot(413)
    plt.plot(self.time, self.accelZ)
    plt.ylabel("Z Accel")
    plt.subplot(414)
    plt.plot(self.time,self.ppg)
    plt.ylabel("HR")
    plt.show()
    # plot the 3 axis accelerometer data

  def plotHR(self):
      plt.subplot(414)
      plt.plot(self.time,self.ppg)
      plt.ylabel("HR")
      plt.show()
    # plot the heartbeat pulse data (covered later on in this lab)
