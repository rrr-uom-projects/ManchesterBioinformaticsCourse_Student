# -*- coding: utf-8 -*-
"""
Assignment 2 part 2 image regression_analysis
Naomi/Ali/Keith
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it the final graphs in a tab in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""

#%%
#Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy import ndimage
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom 

# Copies this function from previous assignment
def shiftimage(image,coordinate_list):
    Vertical = coordinate_list[0] #takes the vertical co-ordinate value from the input list
    Horizontal = coordinate_list[1] #takes the horizontl co-ordinate value from the input list
    #Rotational = coordinate_list[2] #takes the rotational co-ordinate from the list
    shifted_image = interpolation.shift(image, (Vertical, Horizontal), mode="nearest") #shifts the image on the x,y as per the input co-ordinates
    #shifted_image = ndimage.rotate(xy_shift, Rotational, reshape=False)#rotates as per the input co-ordinates, reshape stops it squashing the image
    return shifted_image #Changes the lungs_image_3 variable as per the above changes

registrations = np.load("registrations.npy")

# Load the DICOM files and get the pixel data from the dicom file 
patientImage = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")
patientImage3 = pydicom.read_file("IMG-0004-00003.dcm")
patientImage4 = pydicom.read_file("IMG-0004-00004.dcm")

#get the pixel data from the DICOM files as a numpy array using img1_array = img1_dcm.pixel_array
img1_array = patientImage.pixel_array 
img2_array = patientImage2.pixel_array
img3_array = patientImage3.pixel_array 
img4_array = patientImage4.pixel_array

#Arrays for all images into list as per before
floating_list = [img1_array,img2_array,img3_array,img4_array]

#Shift images calling the shift image function and putting those arrays into a list
shifted_images = []
for i in range(len(floating_list)):
    shifted = shiftimage(floating_list[i], registrations[i])
    shifted_images.append(shifted)
print(shifted_images)

#Plots all the shifted images side by side
fig = plt.figure() #set up a figure space, I had to take this out the function to be able to call it outside of the function
ax1 = fig.add_subplot(221) #add subplots for each thing - images and histogram
ax2 = fig.add_subplot(222) 
ax3 = fig.add_subplot(223) 
ax4 = fig.add_subplot(224) 
ax1.imshow(shifted_images[0], cmap="Greens_r")
ax2.imshow(shifted_images[1], cmap="Greens_r")
ax3.imshow(shifted_images[2], cmap="Greens_r")
ax4.imshow(shifted_images[3], cmap="Greens_r")  
plt.show()

# completed up to step XVII.more comments to come