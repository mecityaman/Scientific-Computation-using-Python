#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:00:36 2020

@author: mecit
"""
import os, time
import numpy as np
import matplotlib.pyplot as plt

dir = 'coord_seligFmt/'
files = os.listdir(dir)

for n in range(0,10):
    filename = dir + files[n]
    array = np.loadtxt(filename, skiprows=1)
    foilx = array[:,0]
    foily = array[:,1]
    
    foily[0], foily[-1]= 0.0, 0.0
    fig,ax = plt.subplots(figsize=(12,10))
    ax.set_aspect(1.0)
    plt.xlim(-0.2, 1.2)
    plt.ylim(-0.2, 0.2)
    plt.title(files[n][:-4])
    plt.plot(foilx, foily,'-o')
    plt.show()
    time.sleep(1.5)

