# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:49:10 2024

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt
import math as ma

t=np.arange(0,7,0.01)

x=np.zeros(len(t))
for i in range(len(t)):
    x[i]=2*np.tan(2*ma.pi*t[i])+3*np.arccos(3*ma.pi*t[i])+2*np.exp(-2*t[i])

plt.plot(t,x,c='red',linewidth=4)
    