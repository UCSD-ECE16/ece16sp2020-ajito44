#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:42:14 2020

@author: joyceeito
"""


from Libraries.Connection import Connection
from Libraries.Visualization import Visualization

connect = Connection("/dev/cu.Angela_Bluetooth-ESP32S", 115200)

def hundred():
    connect.start_streaming()
    while connect.get_num_samples() < 100:
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
   # print(connect.data_array)
    connect.calc_sampling_rate()
    plot = Visualization(connect.data_array)
    plot.plotData()
    connect.close_connection()
main()