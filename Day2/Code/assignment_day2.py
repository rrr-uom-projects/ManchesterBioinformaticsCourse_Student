"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks as fp
#import modules

cwd = os.getcwd()
newPath = cwd +"\\breathing_data"
os.chdir(os.getcwd()+"\\Day2\\Code\\breathing_data")
#change working directory to folder with csvs

csvFiles = os.listdir(newPath)

for cFile in csvFiles:
    with open(cFile, mode = "r") as f:
        value = f.read().strip()
        breathData = np.loadtxt("p01.csv", delimiter = ",")

#shape of array, p01 is (2,1107) (2 rows and 1107 columns)
print(np.shape(breathData))

#plt.plot(breathData)
#plt.show()


#plt.scatter(x = breathData[0,:], y = breathData[1,:])
#plt.show()

xValues = breathData[0, :]
yValues = breathData[1,:]

N = xValues.shape[0]/30 # Try changing the window width to see the effect on the filtered signal
window = np.ones(int(N))
convolved = np.convolve(window/window.sum(), yValues, mode='same')# Note - divide by the sum of the window to 

peaks, peakProperties = fp(convolved, height = 0) 
                                                                      #    maintain normalisation
plt.plot(xValues, yValues, label = "True values")
plt.plot(xValues, convolved, linestyle = "--", color = "r", label = "Convolved values")
plt.scatter(x = peaks, y = peakProperties["peak_heights"], s = 50, color = "g", label = "Peaks")
plt.xlabel("Time")
plt.ylabel("Litres per second")
plt.legend(loc = 4)
plt.title("Spirometry results")

print(peakProperties)
plt.show()



