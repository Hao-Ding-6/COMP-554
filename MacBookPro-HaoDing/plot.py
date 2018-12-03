#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:05:55 2018

@author: dinghao
"""

import csv
import matplotlib.pyplot as plt

x = []; y = []
with open('with_shuffle_results/result10.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for i, row in enumerate(spamreader):
        if i >= 2:
            print(int(row[0]), float(row[1]))
            x.append(str(row[0]))
            y.append(float(row[1]))
    print ('\n')
    
plt.figure(figsize=(20, 6))
plt.plot(x, y, color = 'r',marker = 'o', markerfacecolor = 'blue', markersize = 6)
plt.xticks(rotation=90)
plt.xlabel('Size')
plt.ylabel('Runtime')
    
plt.legend()
plt.show()
