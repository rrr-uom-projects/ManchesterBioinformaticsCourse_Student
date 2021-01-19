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
print(convolved[peaks_p01[0]])


#plot raw data and convolved data with peaks
plt.plot(p01_data[0], p01_data[1], color='g', label="Raw Data")
plt.plot(xValues, convolved, color='b', label="Convolved Data")
plt.scatter(xValues[peaks_p01[0]], convolved[peaks_p01[0]], color='r', marker='o', label="Peaks")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

plt.savefig("P01_plot.png")

