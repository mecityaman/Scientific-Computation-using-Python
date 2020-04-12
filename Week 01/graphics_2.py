# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:30:32 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,3,4,5]
y = [10,30,20,5,20,56]

#plt.plot(y,'-o')
#plt.bar(x,y)



#y = np.random.randint(0,10,20)
#x = np.arange(len(y))
#y1=np.sort(y)
#
#plt.bar(x,y)
#plt.show()
#plt.bar(x,y1)
#
#plt.show()
#
#plt.hist(y, bins=20)
#
#

for i in range(10):
  r=np.random.rand()
  print(r)

y= np.random.rand(1000)
#plt.plot(y,'.')

#plt.hist(y, bins=10)

y= np.random.randn(1000)
plt.plot(y,'.')

#plt.hist(y, bins=10)
