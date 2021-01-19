"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""


#%%
#import modules
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from scipy.signal import find_peaks
#open first csv
#loads an individual csv and tells loadtxt that this file is delimited by ","
file_list = listdir('/home/ali/git_repos/ICT_module/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data/')

for file_name in file_list:
    p01 = np.loadtxt(r"/home/ali/git_repos/ICT_module/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data/" + file_name, delimiter=",")
    #p01 = np.core.defchararray.strip(p01, chars='\n')
    # Moving averages window function - ours
    N = int(p01[0,:].shape[0]/40) # Try changing the window width to see the effect on the filtered signal
    window = np.ones(N)
    convolved = np.convolve(window/window.sum(), p01[1,:], mode='same')# Note - divide by the sum of the window to 
    # maintain normalisation
    fig = plt.figure(figsize=(16,9))
    peaks, _ = find_peaks(convolved, distance=50)
    plt.plot(p01[0,:], p01[1,:], linewidth=2)
    plt.plot(p01[0,:], convolved, color='black')
    plt.plot(peaks, convolved[peaks], "x", color='r')
    savefilename = (str(file_name) + '.png')
    print(savefilename)
    plt.savefig(savefilename)






"""Various different plots we messed around with:
Variable for scatter graph, then uses matplotlib.pyplot.scatter (as plt)
They've been hashed out for now
"""
#p01 values are then called as x/y co-ords (each row)
#p01_scatter = plt.scatter(p01[0,:], p01[1,:])
#p01_plot = plt.plot(p01[0,:], p01[1,:])
#p01_scatter = plt.scatter(p01[0,:], p01[1,:])
# %%
