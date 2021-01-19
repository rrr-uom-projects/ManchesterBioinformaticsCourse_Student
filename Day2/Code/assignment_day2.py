"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# Load values from 1st csv file into an array and look at the result
firstFile = np.loadtxt('breathing_data/p01.csv', delimiter=',')

print(firstFile)

x_values = firstFile[0,:]
y_values = firstFile[1,:]
print(x_values)
print(y_values)

plt.plot(x_values, y_values)
plt.show()

N = int(x_values.shape[0]/32)
window = np.ones(N)
convolved = np.convolve(window/window.sum(), y_values, mode='same')

plot2 = plt.plot(x_values, convolved)


peaks = scipy.signal.find_peaks(convolved)

plt.plot(x_values[peaks[0]], convolved[peaks[0]], marker='+', color='r', linewidth =0)

plt.savefig('plot3.png')

