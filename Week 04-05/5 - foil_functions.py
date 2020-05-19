#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:40:58 2020

@author: mecit
"""

import os
import numpy as np
import matplotlib.pyplot as plt

dir = 'airfoil_data/'
airfoil_files = os.listdir(dir)

def get_foil(n=0, draw_foil=False):

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
    
    xc = (foilx[1:]+foilx[:-1])/2
    yc = (foily[1:]+foily[:-1])/2
    
    return xc,yc

def get_panel_normals(foilx,foily):
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