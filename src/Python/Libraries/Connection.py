#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:38:19 2020

@author: joyceeito
"""

import serial
import numpy as np

class Connection:

  def __init__(self, serial_name, baud_rate):
    self.serial_name = serial_name
    self.baud_rate = baud_rate
    self.setup_connection()
    self.string_buffer = []
    self.data_array = np.array([])

  def setup_connection(self):
    self.ser = serial.Serial(self.serial_name,self.baud_rate) 
    # open Serial port using self.serial_name and self.baud_rate

  def close_connection(self):
    self.ser.close() #close the Serial connection

  def send_serial(self, message):
    self.ser.write(message.encode('utf-8')) # write message to Serial

  def read_serial(self):
    c = self.ser.read(1).decode('utf-8')
    self.receive_data(c)
    #read one byte at a time and call receive_data(input_char)

  def start_streaming(self):
    S = 'start data\n'
    self.ser.write(S.encode('utf-8'))
    # send 'Start Data\n' through Serial

  def receive_data(self, input_char):
    
      if( input_char == '\n' ):
        data_string = ''.join(self.string_buffer) 
        print(data_string)
        np_buffer = np.fromstring(data_string, sep = ',')
        print(self.data_array.shape, np_buffer.shape)
        if(self.data_array.size == 0 ):
            self.data_array = np_buffer
        else:
            self.data_array = np.vstack((self.data_array, np_buffer)) 
        self.string_buffer = [] 
      else:
          self.string_buffer.append(input_char)
    # This should have the same functionality as parse_input from Lab 3, but use the class
    # attributes defined above instead of global variables like you used in Lab 3

  def end_streaming(self):
    S = 'stop data\n'
    self.ser.write(S.encode('utf-8'))
    # send 'Stop Data\n' through Serial

  def clear_data(self):
    self.data_array = np.array([])
    # reset data_array to empty NumPy ndarray

  def get_num_samples(self):
    return self.data_array.shape[0] #return the size of data_array

  def calc_sampling_rate(self):
    t = np.diff(self.data_array[:,0], n=1, axis=0)
    print(t.shape)
    y = np.mean(t)
    rate = 1000000/y
    print("Rate:", rate)
    return rate # calculate the sampling rate
