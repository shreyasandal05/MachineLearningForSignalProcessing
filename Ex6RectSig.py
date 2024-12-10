# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:10:25 2024

@author: acer
"""
# Convolution of two rectangular signal

import cv2
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-10,10)
x=np.zeros(len(t))
h=np.zeros(len(t))

for i in range(0,len(t)):
    if(-2<=t[i]<=2):
        x[i]=2
for i in range(0,len(t)):
    if(-3<=t[i]<=3):
        h[i]=4

conv = np.zeros(len(x) + len(h)-1)
for n in range(len(conv)):
    for k in range(len(x)):
        if n-k >= 0 and n-k < len(h):
            conv[n] += x[k] * h[n-k]
t1=np.arange(0,9.9,0.1)
plt.plot(t,x,'b')
#plt axis[-5,10,-5,5]

plt.plot(t,h,'r')
#plt aixs[-5,10,-5,5]

plt.plot(t1,conv,'g')
#plt aixs[-5,10,-5,5]

plt.legend(["First Signal","Second signal","Convoluted signal"])
plt.show()
    
