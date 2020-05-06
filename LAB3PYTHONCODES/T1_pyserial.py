#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:09:29 2020

@author: joyceeito
"""

import numpy as np
import serial
import time
import pyowm

string_buffer = []
data_array = np.array([])

def setup_serial():
    serial_name = "/dev/cu.Angela_Bluetooth-ESP32S"
    ser = serial.Serial(serial_name, 115200)
    #print(ser.name)
    return ser

def send_serial(ser):
    S = 'Hello World\n'
    ser.write(S.encode('utf-8'))
    
def read_serial(ser):
    s = ser.read(30).decode('utf-8')
    print(s)
    
def readSerial2(ser):
    n = 0
    while(n<30):
        s = ser.read(1).decode('utf-8')
        print(s)
        n = n+1

def readSerial3(ser):
    n = 0
    full_string = []
    while(n<30):
        s = ser.read(1).decode('utf-8')
        full_string.append(s)
        n = n+1
    print(full_string)
    
def readSerial4(ser):
    while True:
        try:
            s = ser.read(1)
            print(s)
        except(KeyboardInterrupt):
            ser.close()
            print("Exiting program due to KeyboardInterrupt")
            return ser

def receive_data(ser):
    global data_array
    while True:
        try:
            receive_sample(ser)
        except(KeyboardInterrupt):
            ser.close()
            print("Exiting program due to KeyboardInterrupt")
            exit()
        return data_array
            
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
    
def weather_data(ser):
    global temp2
    global sunrise
    global sunset
    
    owm_obj = pyowm.OWM('1ecc714c7b643f2c85410de6328e1db3')
    
    seattle = owm_obj.weather_at_place('Seattle, US')
    weather = seattle.get_weather()
    temp = weather.get_temperature('celsius')
    temp2 = temp['temp_max']
    sunrise = weather.get_sunrise_time(timeformat='iso')
    sunset = weather.get_sunset_time(timeformat='iso')
    
    
def sendtemp(ser):
    global temp2
    global sunrise
    global sunset
    temp = str(temp2)
    sun = str(sunrise)
    sunset = str(sunset)
    sendtemp = temp + ',' + sun + ',' + sunset + '\n'
    ser.write(sendtemp.encode('utf-8'))
    
def sendsunrise(ser):
    global sunrise
    sun = sunrise + '\n'
    ser.write(sun.encode('utf-8'))
    
def sendsunset(ser):
    global sunset
    sun = sunset + '\n'
    ser.write(sun.encode('utf-8'))
      
def main():
   # send_serial(ser)
   # read_serial(ser)
    # readSerial2(ser)
   #  readSerial3(ser)
 # readSerial4(ser)
     
  
  ser = setup_serial()
  #send_start(ser)
  weather_data(ser)
  sendtemp(ser)
 # send_stop(ser)
  
  #send_start(ser)
 # data_array = receive_data(ser)
 # print(data_array)
  
  #send_stop(ser)
  ser.close()
    
if __name__ == "__main__":
    try:
        ser = setup_serial()
        while(True):
            main()
    except KeyboardInterrupt:
            ser.close()
            
#def read_serial(ser):
 #   s = ser.read(10).decode('utf-8')
  #  print(s)
    
#def main():
 #   ser = setup_serial()
  #  read_serial(ser)
   # ser.close()