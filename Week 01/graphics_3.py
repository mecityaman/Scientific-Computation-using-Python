# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:30:32 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt

amplitude = 1.0
phase=0.5
bias=0.3
frequency = 4.0

t = np.linspace(0,2*np.pi,50)
y1 = amplitude*np.sin(frequency*t+phase)+bias
y2 = np.cos(t)
y3 = y1+noise

plt.plot(t,y1,'-',alpha=.35)
plt.plot(t,y2,'--')
plt.plot(t,y3,'.-')




