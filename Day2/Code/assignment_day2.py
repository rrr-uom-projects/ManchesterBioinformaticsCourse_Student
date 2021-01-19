# Aim is to plot convoluted respiratory data

# import required modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# read first csv file
p01_data = np.loadtxt("breathing_data/p01.csv", dtype='int,int', delimiter=',', usecols=(0,1), unpack=True)

print(p01_data)

test_plot = plt.plot(p01_data)
