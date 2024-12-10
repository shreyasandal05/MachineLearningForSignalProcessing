# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:28:13 2024

@author: acer
"""

#Convolution of image
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename='C:/Users/acer/Downloads/images.jpg'
img=cv2.imread(filename)

# Define the matrix and kernel
matrix=img
kernel=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

# Define the size of output matrix
output_size=matrix.shape[0] - kernel.shape[0] + 1

# Initialize the output matrix
output=np.zeros((output_size,output_size))

# Perform Convolution
for i in range(output_size):
    for j in range(output_size):
        output[i,j]=np.sum(matrix[i:i+kernel.shape[0],j:j+kernel.shape[1]]*kernel)
        
#Print the result
plt.subplot(1,3,1),plt.title("original image");plt.imshow(img)
plt.subplot(1,3,2),plt.title("kernel");plt.imshow(kernel)
plt.subplot(1,3,3),plt.title("convoluted image");plt.imshow(output)