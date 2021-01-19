# Aim is to plot convoluted respiratory data

# import required modules
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# read first csv file
p01_data = np.loadtxt("breathing_data/p01.csv", delimiter=',')

print(p01_data)

print(p01_data[0])

# plot raw data
#plt.plot(p01_data[0], p01_data[1])
#plt.show()

#plt.scatter(p01_data[0], p01_data[1])
#plt.show()

#convolve data
xValues = p01_data[0]
N = int(xValues.shape[0]/32)

window = np.ones(N)
convolved = np.convolve(window/window.sum(), p01_data[1], mode='same')

#plt.plot(xValues, convolved)
#plt.show()

#find peaks 
peaks_p01 = find_peaks(convolved)
print(peaks_p01)

peaks = np.asarray(peaks_p01)
print(peaks)
print(type(peaks))
print(xValues[peaks])

#plot raw data and convoluted data
#plt.plot(p01_data[0], p01_data[1], color='k')
#plt.plot(xValues, convolved, color='r')
#plt.scatter(xValues[peaks_p01], peaks, colour='g')
#plt.show()

