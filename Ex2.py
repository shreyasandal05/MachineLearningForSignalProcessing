# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:39:25 2024

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-3,3,0.01)

x=np.zeros(len(t));

for i in range(len(t)):
    if(-2<=t[i]and t[i]<-1):
        x[i]=np.exp(-2*t[i]);
    elif(-1<=t[i] and t[i]<1):
        x[i]=3*np.exp(2*t[i]);
    elif(1<=t[i] and t[i]<2):
        x[i]=3*t[i]+6;
plt.plot(t,x,c='red',linewidth=4)
