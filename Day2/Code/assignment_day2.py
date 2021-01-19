"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""

# A script to extract breathing data and plot the noisy data, smoothed data and highlight peaks

# import modules
import numpy as np
import scipy
from scipy import signal
import matplotlib.pyplot as plt
import os

# set current directory
os.chdir("breathing_data")
breathing_data=os.listdir()

# loop through files
for files in breathing_data:
    data=np.loadtxt(files, delimiter=",") # read the data in the file
    
    # remove noise
    N=int(data.shape[1]/32)
    window=np.ones(N)
    convolved = np.convolve(window/window.sum(), data[1,:], mode='same')
    
    # find peaks
    peaks,_=signal.find_peaks(convolved,prominence=0.1)
    
    # plot data
    plt.scatter(data[0,:],data[1,:],label='Noisy Data')
    plt.plot(data[0,:],convolved,'r-',label='Convolved Data') 
    if data[0,-1]<100: # account for scaling differences across the data
        plt.plot(peaks/100,convolved[peaks],'x',color='yellow',label='Peaks')
    else:
        plt.plot(peaks,convolved[peaks],'x',color='yellow',label='Peaks')
    plt.xlabel('Time')
    plt.ylabel('Volume of Air Breathed Out')
    plt.legend()
    plt.show()
    plt.close()
