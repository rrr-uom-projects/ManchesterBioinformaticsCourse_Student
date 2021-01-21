"""
BIOL68310 Assignment: Image processing in Python - Day 2, Part 3

Aim of this part is ........

Authors: Katie Williams and Megan Paynton

Work done on Thursday 21st January 2021
"""
# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom

# Load the images “IMG-0004-00001.dcm” and “IMG-0004-00002.dcm”. get the pixel data
# from the dicom file as a numpy array using img1_array = img1_dcm.pixel_array

patientImage1 = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")

print(patientImage1)
print(patientImage2)

#img1_array = img1_dcm.pixel_array

fig1 = plt.figure()
ax = fig2.add_subplot(111)
ax.imshow(patientImage.pixel_array, cmap='Greys_r')
plt.show()