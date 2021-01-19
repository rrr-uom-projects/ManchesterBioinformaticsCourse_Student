"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
import os
import numpy as np
import matplotlib.pyplot as plt
#from scripy.signal import find_peaks 
#import pandas

path = "/home/katherine/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data"
breathing_data_files = os.listdir(path)



#for file in breathing_data_files:
 #   f = open(path + '/' + file)
  #  file_info = np.loadtxt(f, dtype=str)
   # print(file_info.shape)

f = open(path + '/' + 'p04.csv')
file_info = np.loadtxt(f, delimiter=',')
#file_info.pyplot

x, y = file_info[0,:], file_info[1,:]
print(x)
plt.scatter(x, y)

# sinValues = np.sin(x)
# sin4 = sinValues ** 4
# sinWithRealNoise = sin4 + np.random.normal(loc=0.0, scale=0.1, size=sin4.shape[0])
# Moving averages window function
# x_int = int(x)
N = x.shape # Try changing the window width to see the effect on the filtered signal
window = np.ones(N, dtype=int)
convolved = np.convolve(window/window.sum(), y, mode='same')# Note - divide by the sum of the window to 
#                                                                          #    maintain normalisation
plt.plot(x, convolved)
#plt.plot(x, sin4, linewidth=2)
plt.show()