"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""

#import modules
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from scipy.signal import find_peaks

#define function to get filepath
def get_filepath(filename):
    data_folder = Path('breathing_data')
    file_to_open = data_folder/filename
    return file_to_open

#Iterate over the csv files
for file in os.listdir('breathing_data'):
    filename = get_filepath(file)
    series = np.loadtxt(filename, delimiter=',')
    print(type(series),len(series))
    print(series[0])

    #Define the mask and store it as an array
    window=50 
    mask=np.ones((1,window))/window 
    mask=mask[0,:]    

    #Identify peaks in the filtered signal
    convolved_data=np.convolve(series[1],mask,'same')
    max_width = max(series[0]) 
    peaks, _ = find_peaks(convolved_data, prominence = 0.1, height = 0, width = max_width/50)
    print(peaks)

    #Plot the raw and filtered signals and the peaks
    plt.plot(series[0], series[1], color = 'gray') 
    plt.plot(series[0], convolved_data, color = 'blue')
    plt.plot(peaks, convolved_data[peaks], 'x', color = 'red')

    #Add a legend
    peak_legend = mpatches.Patch(color = 'red', label = 'Peak')
    smooth_legend = mpatches.Patch(color = 'blue', label = 'Moving average')
    raw_legend = mpatches.Patch(color = 'gray', label = 'Raw trace')
    plt.legend(handles = [raw_legend, smooth_legend, peak_legend])

    #Add axis titles
    plt.xlabel('Sample no.')
    plt.ylabel('Amplitude')
    plt.grid(True)

    #Save figure and show image
    plt.savefig(file[:-4]+'_image.png', format = 'png')
    plt.show()
