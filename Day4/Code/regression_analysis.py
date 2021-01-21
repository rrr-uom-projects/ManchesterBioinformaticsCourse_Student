#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
#from skimage import io #this is used for image processing
from scipy.ndimage import interpolation
#from scipy.ndimage import rotate
#from scipy.optimize import brute
import pydicom
#To make the images bigger in size
#plt.rcParams['figure.figsize'] = (16.0, 12.0)

#Load the images
patientImage1 = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")
patientImage3 = pydicom.read_file("IMG-0004-00003.dcm")
patientImage4 = pydicom.read_file("IMG-0004-00004.dcm")

#Give the pixel_arrays sensible variable names
fixed = patientImage1.pixel_array
floating2 = patientImage2.pixel_array
floating3 = patientImage3.pixel_array
floating4 = patientImage4.pixel_array

#Put the pixel arrays in a list
floating_list = [floating2, floating3, floating4]

#Load up the registrations list from the previous script
registrations = np.load("registrations.npy")

#Define the shiftImage function again
def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts, mode="nearest")#Shift 2nd image realtive on its own axes. 2nd argument (change in y, change in x)
    return shifted_image

#Apply the registrations to the images and stick the shifted images in a list
shifted_images = []
i=0
for image in floating_list:
    new_position = shiftImage((registrations[i]), image)
    shifted_images.append(new_position)
    i += 1

#Plot all 4 registered images side-by-side in a figure with 4 subplots    
fig4 = plt.figure()
ax1 = fig4.add_subplot(221)
ax2 = fig4.add_subplot(222)
ax3 = fig4.add_subplot(223)
ax4 = fig4.add_subplot(224)
ax1.imshow(fixed, cmap='Greys_r')
ax2.imshow(shifted_images[0], cmap='Greys_r')
ax3.imshow(shifted_images[1], cmap='Greys_r')
ax4.imshow(shifted_images[2], cmap='Greys_r')
plt.show()

#Save this image as a png
fig4.savefig("compound_register.png") #matlibplot save function





print('Done')

