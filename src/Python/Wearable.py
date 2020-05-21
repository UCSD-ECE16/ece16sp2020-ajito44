#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:48:13 2020

@author: joyceeito
"""


from Libraries.Connection import Connection
from Libraries.Visualization import Visualization
from Libraries.ppg import PPG
import numpy as np
import matplotlib.pyplot as plt

class Wearable:
    
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
        
    def collect_data(self,num_samples):
         
         self.connection.start_streaming()
         while self.connection.get_num_samples() < 500:
             try:
                self.connection.read_serial()
             except(KeyboardInterrupt):
                 self.connection.end_streaming()
                 self.connection.close_connection()
                 print("Exiting program due to KeyboardInterrupt")
                 exit()
         self.connection.end_streaming()
         
    def run(self):
        #self.connection.setup_connection()
        self.collect_data(500)
        self.connection.calc_sampling_rate()
        data_array = self.connection.data_array
        np.savetxt('heartrate.csv', data_array, delimiter=',')
        data_array_from_file = np.genfromtxt('heartrate.csv', delimiter=',')
        self.visualization = Visualization(data_array_from_file)
        self. visualization.plotData()
        s = data_array_from_file[:,4]
        self.ppg = PPG(s)
        baseline = self.ppg.baseline()
        detrend = self.ppg.detrend(baseline,15)
        filtr = self.ppg.normalize_signal(detrend)
        plt.clf()
        plt.plot(filtr)
        plt.show()
        #self.ppg.signal_diff()
        heartrate = self.ppg.calc_heart_rate(filtr)
        print(heartrate)
        heartrate = str(heartrate)
        heartrate = heartrate + '\n'
        self.connection.send_serial(heartrate)
        self.connection.close_connection()
        
def main():
    wearable = Wearable('/dev/cu.Angela_Bluetooth-ESP32S', 115200)
    wearable.run()
        
if __name__ == "__main__":
    main()