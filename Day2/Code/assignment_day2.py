"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks 
#import pandas

path = "/home/katherine/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data"
breathing_data_files = os.listdir(path)



for file in breathing_data_files:
    f = open(path + '/' + file)
    file_info = np.loadtxt(f, delimiter=',')
    #file_info.pyplot

    #generate values for x and y axes
    x, y = file_info[0,:], file_info[1,:]

    #create scatter plot of x and y
    plt.scatter(x, y, s=1)

    #remove noise
    # Moving averages window function
    N = 32 #window is set to 32 to smoothen the peaks
    window = np.ones(N, dtype=int)
    convolved = np.convolve(window/window.sum(), y, mode='same')# Note - divide by the sum of the window to 
                                                                            #    maintain normalisation
    print(y)
    print(convolved)
    plt.plot(x, convolved)

    #find peaks
    peaks = find_peaks(convolved)
    print(peaks[0])

    #plot peaks in grey
    plt.scatter(peaks[0], convolved[peaks[0]], marker='s', color='gray')
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    #plt.show()
    plt.savefig(file + '_plot' + '.png')
    plt.close()

# total_num_of_peaks = 0
# prev = convolved[peaks[0]]
# for point in convolved:
#    if abs(point - prev) > 0.5:
#       total_num_of_peaks = total_num_of_peaks + 1
#       prev = point
# if total_num_of_peaks % 2 == 1:
#    total_num_of_peaks = (total_num_of_peaks - 1) / 2
# else :
#    total_num_of_peaks = total_num_of_peaks / 2

# print(total_num_of_peaks)
