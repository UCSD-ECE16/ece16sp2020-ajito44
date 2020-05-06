#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:15:13 2020

@author: joyceeito
"""


import serial
import time
import numpy as np
import sys
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
    if( input_char == '\n' ):
        # data_string will contain the cumulative buffer of newline
        # (‘\n’) separated lines data (See Hint (2) below for help)
        data_string = ''.join(string_buffer) # join with the contents of string_buffer
        print(data_string)
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
    send_start(ser)
    while sample_number < 5000:
        try:
            receive_sample(ser)
            sample_number = sample_number + 1
        except(KeyboardInterrupt):
            send_stop(ser)
            ser.close()
            print("Exiting program due to KeyboardInterrupt")
            #send_stop(ser)
            sys.exit()
           # send_stop(ser)
    return data_array
           
def calc_sampling_rate(data_array):
    t = np.diff(data_array, n=1, axis=0)
    y = np.mean(t[0])
    rate = 1000000/y
    print("Rate:", rate)
    return rate


def main():
  
  ser = setup_serial()
  data_array = receive_data(ser)
  print(data_array)
  print(calc_sampling_rate(data_array))
  send_stop(ser)
  ser.close()
    
if __name__ == "__main__":
    try:
        ser = setup_serial()
        while(True):
            main()
    except KeyboardInterrupt:
            ser.close()
        