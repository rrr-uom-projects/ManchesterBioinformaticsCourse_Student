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
#find current working directory
newPath = cwd +"\\Day2\\Code\\breathing_data"
#path to folder containing breathing data
os.chdir(newPath)
#change working directory to folder with csvs

csvFiles = os.listdir(newPath)
#load file names of all the csv files

#TODO: use this to load all files 
#for cFile in csvFiles:
#    with open(cFile, mode = "r") as f:
breathData = np.loadtxt("p01.csv", delimiter = ",")
#shape of array, p01 is (2,1107) (2 rows and 1107 columns)
print(np.shape(breathData))

#commented out to stop plotting
#plt.plot(breathData)
#plt.show()

#plt.scatter(x = breathData[0,:], y = breathData[1,:])
#plt.show()

xValues = breathData[0, :]
yValues = breathData[1,:]

#This code was copied from the jupyter notebook and convolves the fucntion to get rid of some noise
N = xValues.shape[0]/30 # Try changing the window width to see the effect on the filtered signal
window = np.ones(int(N))
convolved = np.convolve(window/window.sum(), yValues, mode='same')# Note - divide by the sum of the window to 

#This finds x values and the respective y values (those that are over 0) are in a dictionary
peaks, peakProperties = fp(convolved, height = 0) 

#PLots all 3 graphs                                                           
plt.plot(xValues, yValues, label = "True values")
plt.plot(xValues, convolved, linestyle = "--", color = "r", label = "Convolved values")
plt.scatter(x = peaks, y = peakProperties["peak_heights"], s = 50, color = "g", label = "Peaks")
plt.xlabel("Time")
plt.ylabel("Litres per second")
plt.legend(loc = 4)
plt.title("Spirometry results")

plt.show()



