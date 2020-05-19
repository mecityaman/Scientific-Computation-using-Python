#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:40:58 2020

@author: mecit
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# place your airfoil folder accordingly.
dir = 'airfoil_data/'
airfoil_files = os.listdir(dir)

def get_foil(n=0, draw_foil=False):

    '''
    loads the enumerated airfoil (n)
    and draws if selected
    
    input   : n 
    output  : x,y foil coordinates
    '''

    filename = dir+airfoil_files[n]
    array = np.loadtxt(filename, skiprows=1)
    foilx, foily = array[:,0], array[:,1]
    
    if draw_foil:
        plt.figure(figsize=(12,10))
        plt.plot(foilx, foily,'.-')
        plt.xlim(-.2,1.2)
        plt.ylim(-0.2,0.2)
        plt.title(filename[:-4])
        plt.axes().set_aspect(1.0)
   
    return foilx, foily

def get_panel_centers(foilx,foily):
    
    '''
    calculates panel center points
    input   :  x,y foil coordinates
    output  :  xc,yc panel centers
    '''
    
    
    xc = (foilx[1:]+foilx[:-1])/2
    yc = (foily[1:]+foily[:-1])/2
    
    return xc,yc

def get_panel_normals(foilx,foily):
    
    '''
    calculates panel normal vectors
    input   :  x,y foil coordinates
    output  :  nx,ny normalized panel normal coordiantes
    '''
    
    tx = foilx[1:]-foilx[:-1]
    ty = foily[1:]-foily[:-1]
    l = np.sqrt(tx**2 + ty**2)
    tx = tx /l
    ty = ty /l
    nx,ny = ty,-tx
    return nx,ny
    

x,y = get_foil(n=0, draw_foil=True)
xc,yc = get_panel_centers(x,y)
nx,ny = get_panel_normals(x,y)

plt.plot(xc,yc,'o')    
plt.quiver(xc,yc,
           nx,ny,
           scale=10,
           scale_units='xy',
           alpha=0.1)

# find total flow (free flow+vortices) projection
# at panel centers. Note a meshgrid is not used for this.

X,Y = xc,yc

# free flow
ux = np.ones_like(X)*10.0
uy = np.zeros_like(X)

#vortex definition
vortex_x = x
vortex_y = y
vortex_i = np.random.randn(len(x))/3

# add each vortex flow field
for i,j,k in zip(vortex_x,vortex_y,vortex_i):
  R = ((X-i)**2+(Y-j)**2)
  vx = -k*(Y-j)/R
  vy = k*(X-i)/R
  
  ux += vx
  uy += vy


#projection of total (ux,uy) vector
# along the normal (nx,ny) vector
projection = nx*ux + ny*uy
plt.quiver(xc,yc,
           projection*nx,projection*ny,
           scale=500,
           scale_units='xy',
           alpha=0.75)


# calculate total flow using
# same free flow and vortices as above.
# To draw the streamlines, a meshgrid is used.

x_ = np.linspace(-.2,1.2,50)
y_ = np.linspace(-.2,.2,50)
X,Y = np.meshgrid(x_,y_)

# source flow
R = (X**2+Y**2)
vx = X/R
vy = Y/R

# free flow
ux = np.ones_like(X)*20.0
uy = np.zeros_like(X)


plt.streamplot(X,Y,ux,uy)
