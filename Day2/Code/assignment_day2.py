"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""

"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
# Resuired modules:
from matplotlib import pyplot as plt
import numpy as np
import os, inspect, chardet
from scipy import signal
from scipy.signal import find_peaks
import re

# path of the executing script
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

#paths for inout and output folders
folder_input = '/breathing_data/'
folder_output = '/output_images/'

#This is a smooth function for smoothing raw data
def smooth(y):
    box = signal.windows.hann(50)
    y_smooth = np.convolve(y, box, mode='same')/sum(box)
    return y_smooth

# get files from the directory
list_of_files = os.listdir(actual_path+folder_input)
# generate figures using a for loop
for file in list_of_files:
#file = list_of_files[1]
    input_file_name = file
    output_file_name = re.sub('.csv', '.png', file)
    output_folder=actual_path+folder_output+output_file_name
    CSV_input = actual_path+folder_input+input_file_name
    data = np.loadtxt(CSV_input, delimiter=',')
    x = data[0]
    if max(x) < 100:
        x = x*100
    y = data[1]
    y2 = smooth(y)
    #This gets the peaks:
    peaks, _ = find_peaks(y2, distance=50, height=0.2)
    y3 = _['peak_heights']
    # This makes the plot:
    plt.plot(x, y, 'g-', label='raw_data')
    plt.plot(x, y2, 'b--', label='smoothed data')
    plt.plot(peaks, y3, 'ro', label='identified peaks')
    plt.xlabel("Time(ms)")
    plt.ylabel("Breaths")
    plt.legend(loc="lower left")
    # saves the file
    plt.savefig(output_folder)
    plt.close()
    print(output_folder)


