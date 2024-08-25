# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:59:47 2024

@author: acer
"""


import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-2,6,0.01)

x=np.zeros(len(t))

for i in range(len(t)):
    if(-1<=t[i]and t[i]<0):
        x[i]=2*t[i]+2
    elif(0<=t[i] and t[i]<1):
        x[i]=2*t[i]+2
    elif(1<=t[i] and t[i]<2):
        x[i]=2*t[i]-2
    elif(t[i]>=2 and t[i]<4):
        x[i]=2
plt.plot(t,x,c='red',linewidth=4)