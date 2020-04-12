# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:41:24 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as Animation

fig, ax = plt.subplots()
point, = ax.plot([],[],'-')

plt.xlim(0,100)
plt.ylim(0,4)

n=100

x = np.arange(n)
y = np.ones(n)

def animate(i):
  global y
  print(i)
  
  y[:-1]=y[1:]
  y[-1]= np.random.rand()+2
    
  point.set_xdata(x)
  point.set_ydata(y)
  
  return point,

ani = Animation.FuncAnimation(fig, animate,
                              interval = 50,
                              blit = True)
