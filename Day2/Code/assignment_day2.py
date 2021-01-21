"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
print("Hello World")

#importing required packages and modules
import numpy as np
import matplotlib
import scipy
matplotlib.use('TKAgg')
matplotlib.interactive(True)
import matplotlib.pyplot as plt
import scipy
import skimage
import os
import io

#Change working directory
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data")
os.getcwd()


#Use numpy.loadtxt to load the first csv file.
file = open("p01.csv")
data = np.loadtxt(file, delimiter=",")
#x,y = np.loadtxt(file, delimiter=",")
x, y = data
x
y

#print(data)

#Check the documentation for this function to figure out how to load a csv.
help(np.loadtxt)

#What is the shape of the resulting array?
np.shape(data) 
#What does the shape mean?
#(2, 1107) meaning there are two dimensions and each dimension has 1107 elements

#Try plotting the data using a few different options (e.g. plot, scatter). What
#does each axis in the array refer to? x axis refers to person?; y refers to breathing value?
import matplotlib.pyplot as plt
plt.plot(data)
plt.show()

##Practice code for mapping data values from a CSV file to x and y, respectively
 #with open('p01.csv','r') as csvfile:
    #x = []
    #y = []
    #plots = np.loadtxt(csvfile, delimiter=',')
    #for row in plots:
        #x.append(int(row[0]))
        #y.append(int(row[1]))

#Creating a plot for p01.csv data
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.draw()
plt.show()

#Creating scatterplot for p01.csv data:
plt.scatter(x, y)
plt.show()

type(x)

#Convolving data
import pandas as pd #successful
import scipy.signal as signal
import matplotlib.pyplot as plt

xValues = data[0]
N = int(xValues.shape[0]/32)
window = np.ones(N)
convolved = np.convolve(window/window.sum(), data[1], mode='same')

#Plot convolved data
plt.plot(xValues, convolved)
plt.show()

##To delete:
# Plot the Raw Data
ts = rawdata[0:500]
plt.plot(ts, 'r-')
plt.ylabel('Lightpower (V)')

#    previous version
#    smooth_data = pd.rolling_mean(rawdata[0:500],5).plot(style='k')
#    changes to pandas require a change to the code as follows:
smooth_data = pd.Series(data).rolling(window=7).mean().plot(style='k')
plt.show()

# Moving averages window function
N = x.shape[0]/32 # Try changing the window width to see the effect on the filtered signal
window = np.ones(N)
convolved = np.convolve(window/window.sum(), sinWithRealNoise, mode='same')# Note - divide by the sum of the window to 
                                                                        #    maintain normalisation
plt.plot(x, convolved)
plt.plot(x, sin4, linewidth=2)
######################################################################

#Find peaks in graph
peaks_data = scipy.signal.find_peaks(convolved) #use convolved data to find peaks
print(peaks_data)
print(convolved[peaks_data[0]])

peaks = np.asarray(peaks_p01)
print(peaks)
print(type(peaks))
print(xValues[peaks])

#plot raw data and convoluted data
plt.plot(x, y, color='k')
plt.plot(xValues, convolved, color='r')
plt.scatter(xValues[peaks_data], peaks, colour='g')
plt.show()

#plot raw data and convolved data with peaks
plt.plot(p01_data[0], p01_data[1], color='g', label="Raw Data")
plt.plot(xValues, convolved, color='b', label="Convolved Data")
plt.scatter(xValues[peaks_p01[0]], convolved[peaks_p01[0]], color='r', marker='o', label="Peaks")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

plt.savefig("P01_plot.png")

