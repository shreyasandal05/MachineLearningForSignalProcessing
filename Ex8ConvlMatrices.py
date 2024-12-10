# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:43:55 2024

@author: acer
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#define matrix and kernel
matrix=np.array([[3,3,2,1,0],
                [0,0,1,3,1],
                [3,1,2,2,3],
                [2,0,0,2,2],
                [2,0,0,0,1]]
                )
kernel=np.array([[0,1,2],[2,2,0],[0,1,2]])

#define the size of output matrix
output_size=matrix.shape[0]-kernel.shape[0]+1

#initialize the output matrix
output=np.zeros((output_size,output_size))

#perform convoltuion
for i in range(output_size):
    for j in range(output_size):
        output[i,j]=np.sum(matrix[i:i+kernel.shape[0], j:j+kernel.shape[1]]*kernel)
        
#print the result
print(output)