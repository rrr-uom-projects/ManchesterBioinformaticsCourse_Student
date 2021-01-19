"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import os

# Load values from 1st csv file into an array and look at the result
firstFile = np.loadtxt('breathing_data/p01.csv', delimiter=',')

#Specify which row of the array contains x and y values
x_values = firstFile[0,:]
y_values = firstFile[1,:]

#convolving the raw signal to make an array of smoothed y_values
N = int(x_values.shape[0]/32)
window = np.ones(N)
convolved = np.convolve(window/window.sum(), y_values, mode='same')

#find the peaks
peaks = scipy.signal.find_peaks(convolved)

#plot the raw signal, smoothed signal and peak markers
plt.plot(x_values, y_values, color = "pink")
plt.plot(x_values, convolved)
plt.plot(x_values[peaks[0]], convolved[peaks[0]], marker='+', color='r', linewidth =0)
plt.show()
#plt.savefig('plot3.png')

###########TIDYING UP THE PLOT###############
#Need to crop the plot to exclude the first bit and last bit (when the 'patient'
#is taking the device on and off)

x_values_cropped = x_values[175:1050]
y_values_cropped = y_values[175:1050]
convolved_cropped = convolved[175:1050]

#find true peaks for the cropped area - set minimum height 
#and min x_distance from next peak
peaks_cropped = scipy.signal.find_peaks(convolved_cropped, 
                                        height= 0.2, distance=20)

#Replot and add axis labels and save to current folder
plt.plot(x_values_cropped, y_values_cropped, color ="pink")
plt.plot(x_values_cropped, convolved_cropped)
plt.plot(x_values_cropped[peaks_cropped[0]], 
         convolved_cropped[peaks_cropped[0]], 
         marker='+', color='r', linewidth =0)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.savefig('p01.png')

###########LOOPING OVER ALL FILES######

#For aFile in breathing files
    #open aFile
    #extract the data
    #make a plot
    #save the file
    
breathingFiles = os.listdir('breathing_data')
breathingFiles.sort()
print(breathingFiles)

#for aFile in breathingFiles:
        #with open() as file