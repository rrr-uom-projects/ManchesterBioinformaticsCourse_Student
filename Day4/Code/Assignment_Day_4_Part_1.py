"""
Authors: Nicola Compton and Catherine Borland

This code automatically registers four dicom images using a mean squared error cost metric and brute optimiser.
"""

# import modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io 
from skimage.io import imread
import scipy
from scipy import ndimage
from scipy.ndimage import interpolation
from scipy import optimize
from scipy.optimize import brute, differential_evolution
import pydicom as dc

# load all the dicom images and convert to pixel arrays
image_1=dc.read_file("IMG-0004-00001.dcm")
image_2=dc.read_file("IMG-0004-00002.dcm")
image_3=dc.read_file("IMG-0004-00003.dcm")
image_4=dc.read_file("IMG-0004-00004.dcm")
img1_pixel=image_1.pixel_array
img2_pixel=image_2.pixel_array
img3_pixel=image_3.pixel_array
img4_pixel=image_4.pixel_array

# display the images on the same plot
plt.imshow(img1_pixel,alpha=0.5,cmap="Greens_r")
plt.imshow(img2_pixel,alpha=0.5,cmap="Purples_r")
plt.show()

# shift image function
# input: vector of shifts and image to be shifted
# output: shifted image
def shiftImage(shifts, image):
    shifted_image=interpolation.shift(image, shifts, mode="nearest")
    return shifted_image

# trial and error to align the images, img1 is fixed and img2 is floating
plt.imshow(img1_pixel,alpha=0.5,cmap="Greens_r")
plt.imshow(shiftImage([0,-20],img2_pixel),alpha=0.5,cmap="Purples_r")
plt.show()

# cost function: mean squared error
# input: fixed and floating images as arrays
# output: cost
def MSE_cost(image_fixed, image_float):
    cost=np.sqrt(np.mean((image_fixed - image_float)**2))
    return cost

# checking the function acts as we expect
print('Same image cost is ',MSE_cost(img1_pixel,img1_pixel)) # should equal 0
print('Different images cost is ',MSE_cost(img1_pixel,img2_pixel)) # should be positive number

# function to register images
# input: shift a vector containing the shifts, fixed image array and floating image array
# output: cost value between the shifted and fixed images
def registerImages(shift, fixed, floating):
    shifted_image=shiftImage(shift, floating)
    cost=MSE_cost(fixed, shifted_image)
    return cost
    
# automatically register images
# registering_shift is the optimal shift which minimises the cost function
registering_shift=brute(registerImages, ((-100,100),(-100,100)), args=(img1_pixel,img2_pixel),Ns=10) # img1 first as it is fixed, img2 is floating
print("The shifts are: ", registering_shift)

# shift img2 by the optimal shift
auto_registered=shiftImage(registering_shift, img2_pixel)

# display automatically registered images on top of each other
plt.imshow(img1_pixel,alpha=0.5,cmap="Greens_r")
plt.imshow(auto_registered,alpha=0.5,cmap="Purples_r")
plt.show()
# the images look well aligned, the optimal shifts are [2.99566717 -25.00354501]

# Changing the range between (-1000,1000) and (-1,1) did not have any noticeable difference on the quality of the alignment
# Increasing the number of evalution points, Ns, significantly increases the running time and improves the accuracy of the registration
# To investigate the affect of different cost functions we would change the cost function to something else e.g. mutual information
# We attempted to use the differential_evolution optimizer, however the output was not compatible to use downstream with our shiftImage function, so we were unable to visualise the registration. We read the documentation for both brute and differential_evolution and could see the functions return different data types. We attempted to fix this but ran out of time.

# make a list of the floating images
floating_list = [img2_pixel, img3_pixel, img4_pixel]

# make an empty list to store the registrations and the shifted images
registrations=[]
shifted_images=[]

# loop through floating images
for floating in floating_list:
    
    # optimise to img 1
    registering_shift=brute(registerImages, ((-100,100),(-100,100)), args=(img1_pixel,floating))
    
    # store registration
    registrations.append(registering_shift)
    
    # shift the image by the optimisal shift
    auto_registered=shiftImage(registering_shift, floating)
    
    # store shifted image in list 
    shifted_images.append(auto_registered)
    
# save an array of all the registrations to save run time on downstream analysis
registrations_arr=np.array(registrations)
np.save("registrations.npy",registrations_arr)
    
    
    

    