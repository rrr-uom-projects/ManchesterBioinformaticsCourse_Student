# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:35:38 2021

@author: jaden
"""
## Names: Jadene and Long-Ki
## Date: 22/01/21
## Title: Image Processing in Python

## PART 2 ##

# Import relevant libraries, modules and functions
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy.ndimage import interpolation, rotate 
import os
import skimage.io 
import skimage
from skimage import io
import io 
import matplotlib.image as mpimg 
import pydicom 
from scipy.optimize import brute, differential_evolution

#Set working directory
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day4/Code")
os.getcwd()

#Load the registrations array and the four images
np.load("registrations.npy")
image1_array = pydicom.dcmread("IMG-0004-00001.dcm").pixel_array #returns DICOM object and inside is a pixel array
image2_array=pydicom.dcmread("IMG-0004-00002.dcm").pixel_array
image3_array=pydicom.dcmread("IMG-0004-00003.dcm").pixel_array
image4_array=pydicom.dcmread("IMG-0004-00004.dcm").pixel_array

#Apply registration to each 
def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts)
    #fig3 = plt.figure()
    #ax = fig3.add_subplot(111)
    #plt.title("Overlaid images 1 & 2")
    #ax.imshow(image1_array, cmap = "Greens_r")
    #ax.imshow(shifted_image, cmap = "Purples_r", alpha = 0.5)
    plt.imshow(shifted_image, cmap="Greys_r")
    return shifted_image
    #plt.show()

shifted_image_2 = shiftImage(registrations[0], image2_array) #registrations list from previous script
shifted_image_3 = shiftImage(registrations[1], image3_array)
shifted_image_4 = shiftImage(registrations[2], image4_array)

fig = plt.figure()
#plt.title("All four images")
ax1 = fig.add_subplot(221)
ax1.set_title("Image 1")
ax2 = fig.add_subplot(222)
ax2.set_title("Image 2")
ax3 = fig.add_subplot(223)
ax3.set_title("Image 3")
ax4 = fig.add_subplot(224)
ax4.set_title("Image 4")
ax1.imshow(image1_array, cmap="Greys_r")
ax2.imshow(shifted_image_2, cmap="Greys_r")
ax3.imshow(shifted_image_3, cmap="Greys_r")
ax4.imshow(shifted_image_4, cmap="Greys_r")

plt.show()



