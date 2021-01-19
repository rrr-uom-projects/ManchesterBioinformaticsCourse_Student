"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
#importing packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

#Open csv file 
def make_plot(sampleFile):
    """Finds breathing rate and plots for each file.
     Input is file name
     Output is breathing rate"""
    #Import data
    ourFile=np.loadtxt("breathing_data\\"+sampleFile,delimiter=",")
    #Data manipulation
    xValues=ourFile[0,:]
    yValues=ourFile[1,:]
    #Smoothing peak    
    N = xValues.shape[0]/30 
    window = np.ones(int(N))
    convolved = np.convolve(window/window.sum(),yValues, mode='same')
    #finding peaks
    peak_output, _ = find_peaks(convolved,prominence=0.1)
    #Plotting
    fig=plt.figure(figsize=(8, 6))
    #create subplots
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    #plot unaltered graph
    ax1.plot(xValues,yValues)
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Breathing")
    #plot smooth graph with peaks
    ax2.plot(xValues, convolved)
    ax2.plot(xValues[peak_output],convolved[peak_output],"x")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Smoothed Breathing")
    #output figure
    plt.savefig("Results\\"+sampleFile.split(".")[0]+".png")    
    #calculate breathing rate
    breathing_rate= get_breathing_rate(peak_output,xValues)
    return(breathing_rate)

def read_from_files():
    """finds files in directory, loops through files, outputting graphs and calculating breathing rate. stores and outputs breathing rates in a file"""
    #finds files in directory
    myDirectory = os.path.abspath(os.getcwd())+ "\\breathing_data"
    (_, _, actualFiles) = next(os.walk(myDirectory))
    #open breathing rate file
    f= open("Results\\breathing_rates.txt","w")
    f.write("File name \t Breathing Rate \n")
    #loop through files, to get data
    for aFile in actualFiles:
        breathing_rate= make_plot(aFile)
        f.write(str(aFile) +"\t" + str(breathing_rate) + "\n")
    print("Done!")
    f.close()

def get_breathing_rate(peak_output,xValues):
    """Finds breathing rate from data
    Inputs are peak output and xValues. peak output is an array showing the position of peaks. xValues is a list of timepoints.
    Output is breathing rate."""
    no_peaks=len(peak_output)
    #find difference in time between first and last peak
    time_difference = xValues[peak_output[-1]]-xValues[peak_output[0]]
    #number of gaps between peaks divided by time difference to find breathing rate
    breathing_rate= (no_peaks-1)/time_difference
    return(breathing_rate)

if __name__ == "__main__":
    read_from_files()


