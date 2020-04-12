# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:30:32 2020

@author: myaman
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,500)


freq1, freq2 = 2,2
amp1, amp2 = 1,1
phi1, phi2 = 0,0
y1 = amp1 * np.sin(freq1*t+phi1)
y2 = amp2 * np.sin(freq2*t+phi2)

plt.plot(t,y1)
plt.plot(t,y2)
plt.show()

fig,ax = plt.subplots()
ax.set_aspect(1.0)
plt.plot(y1,y2, alpha=0.75)




