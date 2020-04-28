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

n=0
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
plt.plot(foilx, foily,'-')


panel_xc = (foilx[1:] + foilx[:-1])/2
panel_yc = (foily[1:] + foily[:-1])/2




panel_tx = (foilx[1:]-foilx[:-1])
panel_ty = (foily[1:]-foily[:-1])
l = np.sqrt(panel_tx**2 + panel_ty**2)
panel_tx = panel_tx/l
panel_ty = panel_ty/l


panel_nx = panel_ty
panel_ny = -panel_tx

 
plt.plot(panel_xc, panel_yc,'.')
plt.quiver(panel_xc, panel_yc,
           panel_nx, panel_ny,
           scale= 10, units='xy', alpha=0.5) 
