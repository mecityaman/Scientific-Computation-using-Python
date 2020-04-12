# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:29:51 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,10,1000)

x = np.sin(3*t)
y = np.cos(2*t)
z = t**2

ax.plot3D(x, y, z, '-k')
plt.xlabel('X')
plt.xticks([-1,0,1])