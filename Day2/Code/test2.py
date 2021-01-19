#import modules
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from scipy.signal import find_peaks
from matplotlib import pyplot as plt
import numpy as np
from os import listdir
from scipy.signal import find_peaks

#file_list is a variable with the method listdir()
#listdir returns the name of the entries in the directory given by path
#a list of the .csv files in directory breathing_data has been saved to the variable file_list using the method listdir
file_list = listdir('/Users/keithgraham/PycharmProjects/ICT/ManchesterBioinformaticsCourse_Student/day2/code/breathing_data/')
#we created an empty dictionary because we are going to put stuff in it
contents = []
#we created a for loop
#file_name is the variable defined by the loop
#loop is used to iterate over a sequence (in this case a list of .cvs files saved to the variable file_list)
for file_name in file_list:
#p01 is the variable to which the method numpy.loadtxt is saved
#numpy reads structed data stored in a text file
#r tell python to treat it as a raw string(is this because of what is in the file
    p01 = np.loadtxt(r"/Users/keithgraham/PycharmProjects/ICT/ManchesterBioinformaticsCourse_Student/day2/code/breathing_data/" + file_name, delimiter=",")
    # Moving averages window function - ours
print(file_name)