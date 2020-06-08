#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:49:55 2020

@author: mecit
"""


import numpy as np
import matplotlib.pyplot as plt
#np.random.seed(1)
import time

def unit_vector(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    d = distance(p1,p2)
    vx = x2-x1
    vy = y2-y1
    ux = vx/d
    uy = vy/d
    
    return ux,uy

def distance(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    d = np.sqrt((x1-x2)**2+(y1-y2)**2)
    return d
    
def force(m1,m2,p1,p2):

    '''
    calculates the force vector
    between two masses m1, m2 at p1,p2 locations
    and calculates the unit vectors pointing from m1 towards m2
    and returns the force and the unit vectors
    '''
    
    d = distance(p1,p2)
    force = G*m1*m2/(d**2)
    ux,uy = unit_vector(p1,p2)
    return force, (ux,uy)

def step(m1,m2,p1,p2,v1,v2):
    
    '''
    this function inputs the initial positions and
    veclocities of two masses and calculates the new
    positions and velocities using the force function.
    '''
    
    
    f1,(ux1,uy1) = force(m1,m2,p1,p2)
    f2,(ux2,uy2) = force(m2,m1,p2,p1)
    
    ax1, ay1 = (f1/m1)*ux1,(f1/m1)*uy1
    ax2, ay2 = (f2/m2)*ux2,(f2/m2)*uy2
    
    # update velocities
    '''
    v(t) = v0 + a * dt
    '''

    vx1,vy1 = v1
    vx2,vy2 = v2
    
    vx1 += ax1*dt
    vy1 += ay1*dt
    
    vx2 += ax2*dt
    vy2 += ay2*dt
    
    v1 = vx1, vy1
    v2 = vx2, vy2
    
    # update positions

    '''
    x(t) = x0 + v * dt
    '''

    x1,y1 = p1
    x2,y2 = p2
    
    x1 += vx1*dt
    y1 += vy1*dt
    
    x2 += vx2*dt
    y2 += vy2*dt
    
    
    p1 = x1,y1
    p2 = x2,y2
    
    return p1,p2,v1,v2
    

dt = 0.002
G = 1.0
m1, m2 = 100.0, 1.0

# initial positions
p1 = x1,y1 = np.random.rand(2)
p2 = x2,y2 = np.random.rand(2)

p1 = x1,y1 = 0.5, 0.5
p2 = x2,y2 = 0.5, 1.0


# initial velocites
v1 = np.random.rand(2)
v2 = np.random.rand(2)

v1 = 0.0, 0.0
v2 = 15.0, 0.0


fig, ax = plt.subplots(figsize=(7,7))
ax.set(xlim=(-0.2,1.2), ylim=(-0.2,1.2), aspect=1)
plt.plot(x1,y1,'bo', markersize=5,alpha=.2)
plt.plot(x2,y2,'ro', markersize=5,alpha=.2)


for i in range(500):
    (p1,p2, v1,v2) = step(m1,m2,p1,p2,v1,v2)
    #print('%d %.3f %.3f'%(i, p1[0],p1[1]))

    x1,y1 = p1
    x2,y2 = p2

    fig, ax = plt.subplots(figsize=(7,7))
    ax.set(xlim=(-0.2,1.2), ylim=(-0.2,1.2), aspect=1)

    plt.plot(x1,y1,'bo', markersize=5,alpha=0.2)
    plt.plot(x2,y2,'ro', markersize=5,alpha=0.2)
    plt.show()
    
    time.sleep(0.5)
    
    




#
#ux,uy = unit_vector(p1,p2)
#ax.quiver(x1,y1,ux,uy,
#          scale=10, scale_units='xy',alpha=.2)
#
#ux,uy = unit_vector(p2,p1)
#ax.quiver(x2,y2,ux,uy,
#          scale=10, scale_units='xy', alpha=.2)
#
#
#f, (ux,uy) = force(m1,m2,p1,p2)
#
#ax.quiver(x1,y1, f*ux, f*uy,
#          scale=30, scale_units='xy',
#          alpha=0.8)


