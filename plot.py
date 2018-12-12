# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:40:56 2018

@author: Lenovo
"""

import csv
import matplotlib.pyplot as plt
import math

x = []; y = []
with open('with_shuffle_results/result1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for i, row in enumerate(spamreader):
        if i >= 2:
#            print(int(row[0]), float(row[1]))
            x.append(math.log(int(row[0]), 2))
            y.append(math.log(float(row[1]), 2))
    print ('\n')
    
plt.figure(figsize=(10, 6))
plt.plot(x, y, color = 'r',marker = 'o', markerfacecolor = 'blue', markersize = 6)
#plt.xticks(rotation=90)
plt.xlabel('log(Size)')
plt.ylabel('log(Runtime)')
    
plt.show()