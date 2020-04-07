#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:20:04 2020

@author: joyceeito
"""


original_list = ['hi',1,2,'you']
new_list = original_list
newer_list = new_list[1:3]
newer_list[0:2] = ['how','are']
print(original_list)