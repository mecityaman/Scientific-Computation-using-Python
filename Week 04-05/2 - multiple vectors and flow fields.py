# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:47:05 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt

fig,axes= plt.subplots()
plt.xlim(-4,4)
plt.ylim(-4,4)
axes.set_aspect(1.0)

x_coordinates = np.linspace(1,3,5)
y_coordinates = np.ones(5)

vx = np.ones(5)
vy = np.ones(5)*2

plt.plot(x_coordinates, y_coordinates,'o')
plt.quiver(x_coordinates,y_coordinates,vx,vy, scale=1, scale_units='xy')


x = np.linspace(-4,4,15)
y = np.linspace(-4,4,15)

X,Y = np.meshgrid(x,y)

vx = -X/(X**2+Y**2)
vy = -Y/(X**2+Y**2)


vx2 = -(Y-1)/((X-2)**2+(Y-1)**2)
vy2 = (X-2)/((X-2)**2+(Y-1)**2)


#plt.quiver(X,Y,vx,vy, scale=5, scale_units='xy')
#plt.streamplot(X,Y,vx+vx2,vy+vy2)


#superposition of flows

vortex_x = [-4,1,4]
vortex_y = [0,3,-3]
vortex_i = [1,5,1]

ux=np.zeros_like(X)
uy=np.zeros_like(X) 

for i,j,k in zip(vortex_x,vortex_y,vortex_i):
  R = ((X-i)**2+(Y-j)**2)
  vx = -k*(Y-j)/R
  vy = k*(X-i)/R
  
  ux += vx
  uy += vy


  
plt.streamplot(X,Y,ux,uy)
