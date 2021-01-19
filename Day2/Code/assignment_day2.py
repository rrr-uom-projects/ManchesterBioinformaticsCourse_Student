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
from matplotlib import pyplot as plt
import numpy as np
import re
from os import listdir
from scipy.signal import find_peaks

#paths for input and output
folder_input = '/Users/keithgraham/PycharmProjects/ICT/ManchesterBioinformaticsCourse_Student/day2/code/breathing_data/'

#file_list is a variable with the method listdir()
#listdir returns the name of the entries in the directory given by path
#a list of the .csv files in directory breathing_data has been saved to the variable file_list using the method listdir
#e.g Breathing_data --> p01.csv, p02.csv
###file_list = listdir('/Users/keithgraham/PycharmProjects/ICT/ManchesterBioinformaticsCourse_Student/day2/code/breathing_data/')
file_list = listdir(folder_input)
#we created an empty dictionary because we are going to put stuff in it
#what are we putting in it, if I (#) comment the line it doesnt seem to affect the script?
contents = []
#we created a for loop
#file_name is the variable defined by the loop
#loop is used to iterate over a sequence (in this case a list of .cvs files saved to the variable file_list)
for file_name in file_list:
#p01 is the variable to which the method numpy.loadtxt is saved
#r tell python to treat it as a raw string, but why (?)
#numpy reads structured data stored in a text file ( follows the file path to the .cvs files (?)
#mumpy.loadtxt is brought to the direcroty breathing_data where the file_name variable created via the for loop tells .loadtxt to read each .cvs
#delimiter is a character that seperate text strings, we are putting "," between the data point in each .cvs file ?
    ###p01 = np.loadtxt(r'/Users/keithgraham/PycharmProjects/ICT/ManchesterBioinformaticsCourse_Student/day2/code/breathing_data/ + file_name, delimiter","
    p01 = np.loadtxt(folder_input + file_name, delimiter=",")
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

#saves teh file
    #savefilename = (str(file_name) + '.png')

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
