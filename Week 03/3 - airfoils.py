# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:25:37 2018

@author: myaman
"""
import os, time
import numpy as np
import matplotlib.pyplot as plt

dir = "coord_seligFmt/"
airfoil_files = os.listdir(dir)

filename = dir+airfoil_files[0]
array = np.loadtxt(filename, skiprows=1)
foilx, foily = array[:,0], array[:,1]
plt.figure(figsize=(12,10))
plt.plot(foilx, foily,'.-')
plt.xlim(-.2,1.2)
plt.ylim(-0.2,0.2)
plt.title(filename[:-4])
plt.axes().set_aspect('equal')

xc = (foilx[1:]+foilx[:-1])/2
yc = (foily[1:]+foily[:-1])/2

#plt.plot(xc,yc,'o')

tx = foilx[1:]-foilx[:-1]
ty = foily[1:]-foily[:-1]

l = np.sqrt(tx**2 + ty**2)

tx = tx /l
ty = ty /l

nx,ny = ty,-tx
#plt.quiver(xc,yc,nx,ny, scale=10, scale_units='xy', alpha=.4)
n=25
plt.quiver(xc[n],yc[n],nx[n],ny[n], scale=10, scale_units='xy', alpha=.4)


x = np.linspace(-.2,1.2,50)
y = np.linspace(-.2,.2,50)
X,Y = np.meshgrid(x,y)

vortex_x = [-.1,.6,.9]
vortex_y = [0,0,0]
vortex_i = [1,1,1]

ux=np.zeros_like(X)
uy=np.zeros_like(X) 

for i,j,k in zip(vortex_x,vortex_y,vortex_i):
  R = ((X-i)**2+(Y-j)**2)
  vx = -k*(Y-j)/R
  vy = k*(X-i)/R
  
  ux += vx
  uy += vy


  
plt.streamplot(X,Y,ux,uy)


'''
for i in airfoil_files[:10]:
  
  filename = dir+i
  array = np.loadtxt(filename, skiprows=1)
  foilx, foily = array[:,0], array[:,1]
  plt.plot(foilx, foily)
  plt.xlim(-.2,1.2)
  plt.ylim(-0.2,0.2)
  plt.title(i[:-4])
  plt.axes().set_aspect('equal')
  plt.show()
  # time module slows the iteration.
  time.sleep(0.1)
'''





    