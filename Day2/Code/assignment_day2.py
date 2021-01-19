"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#Open csv file 
def makePlot(sampleFile):
    """makes some plots"""
    #Import data
    ourFile=np.loadtxt(sampleFile,delimiter=",")
    #Data manipulation
    xValues=ourFile[0,:]
    yValues=ourFile[1,:]
    N = xValues.shape[0]/15 # Try changing the window width to see the effect on the filtered signal
    window = np.ones(int(N))
    print(int(N))
    convolved = np.convolve(window/window.sum(),yValues, mode='same')# Note - divide by the sum of the window to 
    peak_output, _ = find_peaks(convolved,height=0.6*np.max(convolved))
    print(peak_output)
    #Plotting
    fig=plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.plot(xValues,yValues)
    ax2.plot(xValues, convolved)
    ax2.plot(peak_output,convolved[peak_output],"x")
    plt.show()
    plt.close()
    


if __name__ == "__main__":
    makePlot("breathing_data\p04.csv")
