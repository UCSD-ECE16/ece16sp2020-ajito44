#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:14:20 2020

@author: joyceeito
"""
from Libraries.Connection import Connection
from Libraries.Visualization import Visualization
import numpy as np

connect = Connection("/dev/cu.Angela_Bluetooth-ESP32S", 115200)

def hundred():
    
    connect.start_streaming()
    while connect.get_num_samples() < 500:
        try:
            connect.read_serial()
        except(KeyboardInterrupt):
            connect.end_streaming()
            connect.close_connection()
            print("Exiting program due to KeyboardInterrupt")
            exit()
    connect.end_streaming()

def main():
    connect.setup_connection()
    hundred()
    data_array = connect.data_array
    np.savetxt("challenge2.csv", data_array, delimiter=",")
    connect.calc_sampling_rate()
    plot = Visualization(data_array)
    plot.plotData()
    connect.close_connection()
main()
    

