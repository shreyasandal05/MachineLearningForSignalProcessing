# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:32:36 2024

@author: acer
"""

# Introduction to signal representation and feature 

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram
import librosa
import librosa.display

#generate a simple chirp signal
fs=2000 #Sampling frequency
t = np.linspace(0, 10, fs*10) # Time vector
signal = chirp(t, f0=6, f1=1, t1=10, method ='logarithmic') # Frequnecy swept cosine generator

# Plot the signal
plt.figure(figsize=(10,4))
plt.plot(t,signal)
plt.title('Chirp signal')
plt.xlabel('Time[s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Calculate time-domain features

mean=np.mean(signal)
variance=np.var(signal)

# the skewness of X is the third moment of the standard score of X
skewness = np.mean((signal-mean)**3)/(np.std(signal)**3)

# the kurtosis of X is the fourth moment of the standard score of X
kurtosis = np.mean((signal-mean)**4)/(np.std(signal)**4)

# print the features
print(f'Mean: {mean}')
print(f'Variance: {variance}')
print(f'Skewness: {skewness}')
print(f'Kurtosis: {kurtosis}')

# Calculate the FFT of the signal
fft_signal =np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal),1/fs)

#plot the fft
plt.figure(figsize=(10,4))
plt.plot(frequencies,np.abs(fft_signal))
plt.title('FFT of the chrip signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid()
plt.show()

#Calculate the spectrogram of the signals
frequencies,times,Sxx = spectrogram(signal, fs)

#plot the spectrogram
plt.figure(figsize=(10,4))
plt.pcolormesh(times,frequencies,10*np.log10(Sxx))
plt.title('Spectrogram of the chrip signal')
plt.xlabel('Time[s]')
plt.ylabel('Frequency [Hz]')
plt.colorbar(label='Intensity [dB]')
plt.show()