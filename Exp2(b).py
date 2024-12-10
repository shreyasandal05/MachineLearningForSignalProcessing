# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:06:59 2024

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-2,2,0.01)

x=np.zeros(len(t))

for i in range(len(t)):
    if(-2<=t[i]and t[i]<=-1):
        x[i]=3*t[i]+6
    elif(-1<=t[i] and t[i]<=1):
        x[i]=3
    elif(1<=t[i] and t[i]<=2):
        x[i]=-3*t[i]+6
plt.plot(t,x,c='red',linewidth=4)