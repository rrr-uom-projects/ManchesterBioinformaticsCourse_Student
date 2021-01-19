#import modules
import numpy
import matplotlib
from scipy.signal import find_peaks
#open first csv
p01 = numpy.loadtxt(r"breathing_data/p01.csv", delimiter=",")
print(p01)