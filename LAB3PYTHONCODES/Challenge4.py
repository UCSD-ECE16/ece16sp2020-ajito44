#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:18:50 2020

@author: joyceeito
"""


import serial
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

string_buffer = []
data_array = np.array([])


def setup_serial():
    serial_name = "/dev/cu.SLAB_USBtoUART"
    ser = serial.Serial(serial_name, 115200)
   # print(ser.name)
    return ser

def parse_input( input_char ):
    global string_buffer
    global data_array
    global sample_number
    if( input_char == '\n' ):
        # data_string will contain the cumulative buffer of newline
        # (‘\n’) separated lines data (See Hint (2) below for help)
        data_string = ''.join(string_buffer) # join with the contents of string_buffer
        print(data_string)
        #sample_number += 1
        np_buffer = np.fromstring(data_string, sep = ',') # convert CSV string_buffer to a 1x4 ndarray
        if( data_array.size == 0 ):
            data_array = np_buffer
        else:
            data_array = np.vstack((data_array, np_buffer)) # vstack np_buffer to data_array
        string_buffer = [] # reset string_buffer to []
    else:
       string_buffer.append(input_char) # append the input_char to string_buffer
       
def receive_sample(ser):
    global string_buffer
    global data_array

    c = ser.read(1).decode('utf-8')
    parse_input(c)
    
def send_start(ser):
    S = 'start data\n'
    ser.write(S.encode('utf-8'))
            
def send_stop(ser):
    S = 'stop data\n'
    ser.write(S.encode('utf-8'))
    
def receive_data(ser):
    global data_array
    sample_number = 0
    while sample_number < 100:
        try:
            receive_sample(ser)
            sample_number = sample_number + 1
        except(KeyboardInterrupt):
            send_stop(ser)
            ser.close()
            print("Exiting program due to KeyboardInterrupt")
            sys.exit()
            send_stop(ser)
        return data_array

def calc_sampling_rate(data_array):
    global t
    t = np.diff(data_array, n=1, axis=0)
    y = np.mean(t)
    print(y)
    return y

def plot_data(data_array):
    plt.clf()
    plt.subplot(311)
    plt.plot(data_array[:,0], data_array[:,1])
    plt.title("Accelerometer Values")
    plt.ylabel("X Accel")          
    plt.subplot(312)
    plt.plot(data_array[:,0], data_array[:,2])
    plt.ylabel("Y Accel")
    plt.subplot(313)
    plt.plot(data_array[:,0], data_array[:,3])
    plt.ylabel("Z Accel")
    plt.show()
    
    
def main():
    
  global data_array
  
  ser = setup_serial()
  send_start(ser)
  data_array = receive_data(ser)
  print(data_array)
  calc_sampling_rate(data_array)
  plot_data(data_array)
  ser.close()
    
if __name__ == "__main__":
    try:
        ser = setup_serial()
        while(True):
            main()
    except KeyboardInterrupt:
            ser.close()
        