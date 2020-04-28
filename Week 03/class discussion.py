# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:45:30 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt
import time


# gaussian
arr = np.zeros(1000)
plt.xlim(0,1000)

for i in range(125000):
  
  x = int(np.random.rand()*100)+400
  arr[x] += 1
plt.plot(arr,'.')
plt.show()



  

