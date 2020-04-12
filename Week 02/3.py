# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:36:59 2020

@author: myaman
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as Animation

n=4

fig, (ax1,ax2) = plt.subplots(1,2)

matrix = np.random.rand(n,n)
matrix_graphic = ax1.matshow(matrix, vmin=0, vmax=1, cmap='gray')

line_graphic, = ax2.plot([],[])
plt.xlim(100)
plt.ylim(0,1)

x=np.arange(100)
intensity = np.zeros(100)

def animate(i_):
  global matrix
  
  i,j = np.random.randint(0,n,2)
  matrix[i,j]=1
  
  i,j = np.random.randint(0,n,2)
  matrix[i,j]= 0
  
  
  matrix = matrix * 0.99
  
  matrix_graphic.set_data(matrix)
  
  intensity[:-1]=intensity[1:]
  intensity[-1] = np.sum(matrix)/(n*n)
  
  line_graphic.set_xdata(x)
  line_graphic.set_ydata(intensity)
   
  
  return matrix_graphic, line_graphic,

Ani = Animation.FuncAnimation(fig, animate,
                              interval=25,
                              blit=True)
