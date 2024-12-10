# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:15:00 2024

@author: acer
"""

# Discrete linear convolution

import cv2
import numpy as np
import matplotlib.pyplot as plt

#impulse respone
h=[1,2,3,6]

#input response
x=[-1,2,2,3,6,4,8]
N1=len(x)
N2=len(h)
N=N1+N2-1
y=np.zeros(N)
#x=[[x],np.zeros(N-N1)]
#h=[h,np.zeros(N-N2)]

#Linear function using built in function using numpy
y1=np.convolve(x, h)
m=N-N1
n=N-N2

#padding zeroes to  x and h to make their len to N
x= np.pad(x,(0,m),'constant')
h= np.pad(h,(0,n),'constant')

#Linear conolution using sum formula
for n in range(N):
    for k in range(N):
        if n >= k:
            y[n]=y[n]+x[n-k]*h[k]
print("Linaer convoltuion using convolution sum formula output response y=\n",y)
print("Linear convoltuion using numpy built in function output response y=\n",y1)