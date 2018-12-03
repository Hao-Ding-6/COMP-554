# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:40:56 2018

@author: Lenovo
"""

import csv
import matplotlib.pyplot as plt

x = []; y = []
with open('without_shuffle_results/result10.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for i, row in enumerate(spamreader):
        if i >= 2:
#            print(int(row[0]), float(row[1]))
            x.append(str(row[0]))
            y.append(float(row[1]))
    print ('\n')
    
plt.figure(figsize=(20, 6))
plt.plot(x, y, color = 'r',marker = 'o', markerfacecolor = 'blue', markersize = 6)
plt.xticks(rotation=90)
plt.xlabel('Size')
plt.ylabel('Runtime')
    
plt.show()