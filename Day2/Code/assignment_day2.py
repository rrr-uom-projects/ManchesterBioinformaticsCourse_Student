"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
""" 

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import find_peaks
data_files = (os.listdir("/users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data"))
for files in data_files:
    print(files)
data_files.remove(".ipynb_checkpoints")
for i in data_files:
    data=np.loadtxt("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data/"+i, delimiter=',')
    data[0] = np.arange(0,len(data[0]))
    N = int(data[0].shape[0]/40)
    window = np.ones(N)
    convolved = np.convolve(window/window.sum(), data[1], mode='same')
    plt.plot(data[0,:], data[1,:], linewidth=2, color='blue')
    plt.plot(data[0,:], convolved, color='black')
    peaks, _= find_peaks(convolved, distance=40, prominence=0.1)
    x = ((peaks[-1]-peaks[0])/len(peaks))
    print("Sample",i,"has an average respiration rate of", x)
    plt.plot(peaks, convolved[peaks], "x", color='r')
    plt.ylabel("amplitude")
    plt.xlabel("time")
    plt.legend(["Noisy single", "filtered signal", "peaks"],bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data/"+i+".png")
    plt.show()


