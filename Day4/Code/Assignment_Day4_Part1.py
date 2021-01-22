#!/usr/bin/env python
# coding: utf-8

'''
PART1 I and II
Script written by Igor Malashchuk and Manuel Dominguez 
'''

'''
PART1 III
Import the required modules
'''
# Let’s import needed with the next lines of code.
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute
import inspect
import os
import pydicom

'''
PART1 IV
Load images
'''
# path of the executing script 
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))


#name of image
img_name1 = '/IMG-0004-00001.dcm'
img_name2 = '/IMG-0004-00002.dcm'
img_name3 = '/IMG-0004-00003.dcm'
img_name4 = '/IMG-0004-00004.dcm'


#path to the image
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2
img_path3 = actual_path + img_name3
img_path4 = actual_path + img_name4

#import images using pydicom.read_file
img1 = pydicom.read_file(img_path1)
img2 = pydicom.read_file(img_path2)
img3 = pydicom.read_file(img_path3)
img4 = pydicom.read_file(img_path4)

#get the array iamges from DICOM format
img1_array = img1.pixel_array
img2_array = img2.pixel_array
img3_array = img3.pixel_array
img4_array = img4.pixel_array

'''
PART1 V
Display and save image as png file. 
'''

plt.imshow(img1_array, cmap="Greys_r")
plt.imshow(img2_array, alpha=0.25, cmap="Greys_r")
#plt.show()
plt.savefig("DICOM_images.png")
plt.close()


'''
PART1 VI
Modified shiftImage function from previouse assignment
'''
def shiftImage(shifts, image):
    #shits is an input, which is a list of two values example [value1, value2] that shifts the image. 
    # Value1 moves image up or down, value 2 moves image left or right.
    shifted_image = interpolation.shift(image, (shifts[0], shifts[1]), mode="nearest")
    return shifted_image


#Using the code below (in quatations) it was posible to determine the optimal window level [3, -25] for the second image
'''
img2_shift = shiftImage([3,-25], img2_array)
plt.imshow(img1_array, cmap="Greys_r")
plt.imshow(img2_shift, alpha=0.25, cmap="Greys_r")
plt.show()
'''


'''
PART1 VII
'''
# This function compares two images two obtain the mean squared error. Value 0 indicates a perfect overlap between the images
def mean_squared_error(im1, im2):
    """
    Return the mean of the squared difference
    """
    return np.mean((im1-im2)**2)

'''
PART1 VIII
'''

# This function is called registerImages as it ca nbe used to find the optimal shift parameters. 
def registerImages(shift, fixed, floating):
    shifted_image = shiftImage(shift, floating)
    cost_value = mean_squared_error(fixed, shifted_image)
    return cost_value


# Call the function and get the registered shift
registering_shift = brute(registerImages, ((-100, 100),(-100,100)), args=(img1_array, img2_array))

'''
PART1 IX
'''

#Shift the image and comapre them again 
image2_shifted = shiftImage(registering_shift, img2_array)

#Get error between the images
error = mean_squared_error(img1_array, image2_shifted)

print('the mean squared error difference between two images is: ', error)

#Optional dispaly the images (remove quaotations):
'''
plt.imshow(img1_array, cmap="Greys_r")
plt.imshow(image2_shifted, alpha=0.25, cmap="Greys_r")
plt.show()
'''

'''
PART X and XI
No time to do this 
'''



'''PART1 XII'''

#This list os of the images that are to be shifted in comparison to image1. 
floating_list = [img2_array, img3_array, img4_array]

#This for loop gets the registration values
registrations = []
for floating in floating_list:
    registering_shift = brute(registerImages, ((-100, 100),(-100,100)), args=(img1_array, floating))
    registrations.append(registering_shift)



#This for loop modifies the image postion based on the registeres values obtain from the previouse function
shifted_images = floating_list # Here we copy the images from the floating list which will be modified
for i in range(0, len(floating_list), 1): # this loop is designed to get i values from 0 to the number of images in the floating_list 
    shifted_images[i] = shiftImage(registrations[i], floating_list[i]) # i is used here to call the specific image and correspoding registration values 

#We can use the funcitons below to plot the shifted images (remove the quatation marks below):
'''
plt.imshow(img1_array, cmap="Greys_r")
plt.imshow(shifted_images[0], alpha=0.25, cmap="Greys_r")
plt.show()
'''

'''PART1 XIII'''

# This is where we save the file containg registered data to an array
registrations_arr = np.array(registrations)
np.save('registrations.npy', registrations_arr)

print(registrations_arr)
