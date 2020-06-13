#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:48:13 2020

@author: joyceeito
"""


from Libraries.Connection import Connection
from Libraries.Visualization import Visualization
from Libraries.ppg import PPG
from Libraries.Pedometer import Pedometer
import numpy as np
import matplotlib.pyplot as plt
#from Libraries.ML import ML
from scipy import signal

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
        self.connection.setup_connection()
        self.collect_data(500)
        self.connection.calc_sampling_rate()
        data_array = self.connection.data_array
        np.savetxt('hello.csv', data_array, delimiter=',')
        data_array_from_file = np.genfromtxt('hello.csv', delimiter=',')
        self.visualization = Visualization(data_array_from_file)
        self. visualization.plotData()
        self.my_plotter = Visualization(data_array_from_file)
        s = data_array_from_file[:,4]
        self.ppg = PPG(s)
        baseline = self.ppg.baseline()
        detrend = self.ppg.detrend(baseline,15)
        filtr = self.ppg.normalize_signal(detrend)
        plt.clf()
        plt.plot(filtr)
        plt.show()
        self.ppg.signal_diff()
        heartrate = self.ppg.calc_heart_rate(filtr)
        print(heartrate)
        heartrate = str(heartrate)
        heartrate = heartrate + '\n'
        self.connection.send_serial(heartrate)
        #Lab5C3
        self.ped = Pedometer(500, data_array[:,0:4])
        step_count, inds = self.ped.process_data()
        print(step_count)
        self.my_plotter = Visualization(self.ped.data_array)
        self.my_plotter.plot_pedometer(self.ped.filtered_data,inds)
        #print(inds)
        step_count = str(step_count)
        step_count = step_count + '\n'
        self.connection.send_serial(step_count)
        self.connection.close_connection()
        
        
    
    #def lab5(self):
     #    directory = "/Users/joyceeito/Downloads/SPring2020/ece16sp2020-ajito44/src/Python/Data_Lab5_ML/Training/"
      #   testing = "/Users/joyceeito/Downloads/SPring2020/ece16sp2020-ajito44/src/Python/Data_Lab5_ML/Testing/"
       #  x = ML()
        # x.train_hr_model(directory)
         #y,z = x.test_hr_model(testing)
         #print(y)
         #print(z)
    
    
    def samples(self, num_samples):
        
        i = 0
        while i < num_samples:
             try:
                self.connection.read_serial()
                i = i+1
             except(KeyboardInterrupt):
                 self.connection.end_streaming()
                 self.connection.close_connection()
                 print("Exiting program due to KeyboardInterrupt")
                 exit()
        
    def GrandChallenge(self):
        self.connection.start_streaming()
        count = 0
        while True:
            
            self.samples(100*32)
            data_array = self.connection.data_array
            s = data_array[:,4]
            self.ppg = PPG(s)
            self.ped = Pedometer(100, data_array[:,0:4])
      
            if count == 0:
                b,a,zi_in = self.ppg.onlyonce()
                c,d,zi_in2 = self.ped.onlyonce()
                count = count + 1
            else:
                zi_in = self.ppg.lfilter(b,a,zi_in)
                plt.cla()
                plt.subplot(211)
                plt.plot(self.connection.data_array[:,0],self.ppg.signal)
                heartrate = self.ppg.calc_heart_rate(self.ppg.signal)
                print(heartrate)
                heartrate = str(heartrate)
                heartrate = heartrate + '\n'
                self.connection.send_serial(heartrate)
                zi_in2 = self.ped.lfilter(c,d,zi_in2)
                step_count, inds = self.ped.count_steps()
                plt.subplot(212)
                plt.plot(self.connection.data_array[:,0],self.ped.filtered_data)
                plt.show(block=False)
                plt.pause(0.001)
                print(step_count)
                step_count = str(step_count)
                step_count = step_count + '\n'
                self.connection.send_serial(step_count)
          
def main():
    wearable = Wearable('/dev/cu.Angela_Bluetooth-ESP32S', 115200)
    #wearable.run()
    #wearable.lab5()
    wearable.GrandChallenge()
    
        
if __name__ == "__main__":
    main()