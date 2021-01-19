"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""

import os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.signal import find_peaks

def get_filepath(filename):
    data_folder = Path('breathing_data')
    file_to_open = data_folder/filename
    return file_to_open

for file in os.listdir('breathing_data'):
    filename = get_filepath(file)
    series = np.loadtxt(filename, delimiter=',')
    print(type(series),len(series))
    print(series[0])
    #Define window size
    w=50
    #Define mask and store as an array
    mask=np.ones((1,w))/w
    mask=mask[0,:]
    #Convolve the mask with the raw data
    convolved_data=np.convolve(series[1],mask,'same')
    #Change series to data frame and add convolved data as a new column
    max_width = max(series[0])
    peaks, _ = find_peaks(convolved_data, prominence = 0.1, height = 0, width = max_width/50)
    print(peaks)

    plt.plot(series[0], series[1], color = 'gray')
    plt.plot(series[0], convolved_data, color = 'blue')
    plt.plot(peaks, convolved_data[peaks], 'x', color = 'red')

    peak_legend = mpatches.Patch(color = 'red', label = 'Peak')
    smooth_legend = mpatches.Patch(color = 'blue', label = 'Moving average')
    raw_legend = mpatches.Patch(color = 'gray', label = 'Raw trace')

    plt.xlabel('Sample no.')
    plt.ylabel('Amplitude')
    plt.legend(handles = [raw_legend, smooth_legend, peak_legend])
    plt.grid(True)
    plt.savefig(file[:-4]+'_image.png', format = 'png')
    plt.show()
