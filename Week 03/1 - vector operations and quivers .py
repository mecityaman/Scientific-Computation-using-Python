# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:46:22 2020

@author: myaman
"""
import numpy as np
import matplotlib.pyplot as plt

def get_length(a):
  ax,ay = a
  return np.sqrt((ax**2+ay**2))


def get_angle(a,b, radians=True):
  ax,ay = a
  bx,by = b
  l_a = get_length(a)
  l_b = get_length(b)
  
  angle_radians = np.arccos((ax*bx+ay*by)/(l_a*l_b))
  angle_degrees = angle_radians*180/np.pi

  if radians:
    return angle_radians
  else:
    return angle_degrees

def get_unit_vector(a):
  ax,ay = a
  l = get_length(a)
  ux,uy = ax/l,ay/l
  return ux,uy

def get_projection(a,b):
  ax,ay = a
  # normalize b to be unit vector if not already
  ux,uy = get_unit_vector(b)
  projection = ax*ux+ay*uy
  return projection



#Quiver plot
fig,axes = plt.subplots()
axes.set_aspect('equal')
plt.ylim(-3,3)
plt.xlim(-3,3)


a = ax,ay = np.random.randn(2)
b = bx,by = np.random.randn(2)

l_a = get_length(a)
l_b = get_length(b)


angle_radians = get_angle(a,b)
angle_degrees = get_angle(a,b,radians=False)


plt.quiver(0.5, 0.5,ax,ay, scale=1, units='xy', color='red' , alpha=.5)
plt.quiver(0.5, 0.5,bx,by, scale=1, units='xy', color='blue', alpha=.5)

print('Magnitude of vector a %.2f'%l_a)
print('Magnitude of vector b %.2f'%l_b)
print('Angle between a and b is %5.2f radians (%.1f degrees)'%(angle_radians, angle_degrees))


projection = get_projection(a,b)
ux,uy = get_unit_vector(b)
print('Projection magnitude %.2f '%projection)
plt.quiver(0.5, 0.5,projection*ux,projection*uy, scale=1, scale_units='xy', color='gray', alpha=75.0)

