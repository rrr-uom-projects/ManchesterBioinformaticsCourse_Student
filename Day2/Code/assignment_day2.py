# Aim is to plot convoluted respiratory data

# import required modules
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# read first csv file
p01_data = np.loadtxt("breathing_data/p01.csv", delimiter=',')

print(p01_data)

print(p01_data[0])

plt.plot(p01_data[0], p01_data[1])
plt.show()

#plt.scatter(p01_data)
#plt.show()
