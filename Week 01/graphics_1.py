# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:30:32 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt

#x = [0,1,2,3,5,10,12]
#y = [0,2,5,1,-4,-1,3]
#
#plt.plot(x,y,'--')  #d, *


x=np.linspace(-5,5,150)

y1=x**2-12*x+5
y2=-x**3+2*x**2-5

#plt.plot(x,y1,'g-', label='quadratic')
#plt.plot(x,y2,'b-', label='cubic')
#plt.legend()
#
#plt.title('Functions')
#plt.xlabel('Time (sec)')
#plt.ylabel('Velocity (m/s)')
#
#plt.xlim(3,-2)
#plt.ylim(-20,50)
#


plt.plot(x,y1,linestyle=':',alpha=.50, lw=5, color='blue')
plt.plot(x,y2,alpha=.75, lw=2, color='red')

#
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.fill_between(x,y2,y1)
