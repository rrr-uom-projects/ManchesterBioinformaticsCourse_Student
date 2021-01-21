#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
from skimage import io #this is used for image processing
from scipy.ndimage import interpolation
from scipy.ndimage import rotate
from scipy.optimize import brute
import pydicom

#Load images into variables
patientImage1 = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")

print(patientImage1)#Prints the DICOM header information in the console

#Plot both figures ontop of one another
fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.imshow(patientImage1.pixel_array, cmap='Purples_r')#pixel_array is the image
ax.imshow(patientImage2.pixel_array, alpha=0.5, cmap='Greens_r')#pixel_array is the image, alpha makes transparent
plt.show()