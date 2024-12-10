# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:03:14 2024

@author: acer
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:37:21 2024

@author: acer
"""

import numpy as np
from numpy import linspace,sin,cos,pi,ceil,floor,arange
from pylab import plot,show,axis

# sampling a signal bandlimited to 40Hz with samppling rate of 800 Hz

f = 40; #hz
tmin = -0.3;
tmax = 0.3;

t1=np.arange(-3,3,0.01)
x=np.zeros(len(t1));
t=linspace(tmin,tmax,400);
for i in range(len(t1)):
    if(t[i]<0):
        x[i]=0
    else x[i] = np.exp(-2*t)*t1[i] + np.exp(-4*t)*t1[i]; #signal sampling
plot(t,x[i])

# sampling the signal with sampling rate of 80Hz 
# in this case we are using the Nyquist rate

T=1/80.0
nmin = ceil(tmin/T) #round a no. upto the nearest integer 
nmax = floor(tmax/T) # the largest integer not greater than x
n=arange(nmin,nmax)
x1 = np.exp(-2*T)*t + np.exp(-4*T)*t
plot(n*T,x1,'go')

# sampling the signal with a sampling rate of 35Hz
# not that 35Hz is under the Nyquist rate

T=1/70.0
nmin = ceil(tmin/T)
nmax = floor(tmax/T)
n=arange(nmin,nmax)
x2 = numpy.exp(-2*T)*t + np.exp(-4*T)*t
plot(n*T,x2,'-r.',markersize=8)

axis([-0.3,0.3,-1.5,2.3])
show()

"""
The blue curve is the original signal, the green dots are the samples obtained with
Nyquist rate and the red dots are the samples obtained with 35 Hz. It's easy to see 
that green samples are enough to recover the blue curve, while the red ones are not
enough to capture the oscillations of the signal
"""

