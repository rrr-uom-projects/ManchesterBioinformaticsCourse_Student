"""
Authors: Katie Williams and Megan Paynton

Work done: Thursday 21st January 2021

BIOL68310 Assignment: Image processing in Python - Day 2, Part 1

Aim: Create a registration function and a cost function to utilise in in an optomiser such as brute. Finally, this code will loop over a list of dicom files to automatically register and optomise the images. 


"""
# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom
import os 

# Load the images “IMG-0004-00001.dcm” and “IMG-0004-00002.dcm”. get the pixel data
img1_dcm = pydicom.read_file("IMG-0004-00001.dcm")
img2_dcm = pydicom.read_file("IMG-0004-00002.dcm")

# Convert dicom file to a numpy array using img1_array = img1_dcm.pixel_array
img1_array = img1_dcm.pixel_array 
img2_array = img2_dcm.pixel_array

# Save the overlayed figures as a png
fig, ax = plt.subplots()
plt.imshow(img1_array, alpha=0.5, cmap="Greens_r") # plot the images with transparency (alpha)
plt.imshow(img2_array, alpha=0.5, cmap="Purples_r")
plt.title("Overlayed CT scans")
plt.savefig('img1_img2_overlayed.png') # save the image
plt.show()

# start a new figure
fig, ax = plt.subplots()
ax.imshow(img1_array, alpha=0.5, cmap="Greens_r")
img2 = ax.imshow(img2_array, alpha=0.5, cmap="Purples_r")

# Function (from assignment 1 to shift specified image a specified number of shifts 
def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts)
    return shifted_image # return image so it can be used in a function later

shifted = shiftImage([10,-20], img2_array) # use [3, -25] to register the images
img2.set_data(shifted)
fig.canvas.draw()
plt.title("Shifted Images")
plt.show()

####### Create a cost function which compares two images using mean squared error #######
# This function assumes the images are the same array size
def cost(image_1, image_2):
    N = (image_1.shape[0])*(image_1.shape[1]) # calculate total number of pixels in the image to calculate mean squared error
    MSE = (1/N)*sum(sum((image_1-image_2)**2)) # calculate mean squared error
    return MSE

print(cost(img1_array, img1_array)) # check this MSE is 0 - it should be when comparing the same image
print(cost(img1_array, img2_array)) # check the MSE is working for these two images


####### Write a function called register images to evaluate the cost function between two images #######
def registerImages(shift, fixed, floating):
    shifted_image = shiftImage(shift, floating) # shift image to register the image based on the optimum we found earlier
    cost_value = cost(fixed, shifted_image) # identify the cost value based on the registered images
    return cost_value

print("The cost value = ", registerImages([3, -25], img1_array, img2_array)) # print the cost value for the registered image1 and image2

# Run optomiser brute to identify the optimum shifts for image registration, optimum shifts are 2.99566717 -25.00354501
registering_shift = brute(registerImages, ((-100, 100),(-100, 100)), args=(img1_array, img2_array))
print(registering_shift) # print the optimum shifts to register the images

# Start a new figure, to plot the optimum shift
fig, ax = plt.subplots()
ax.imshow(img1_array, alpha=0.5, cmap="Greens_r")
img2 = ax.imshow(img2_array, alpha=0.5, cmap="Purples_r")

registered_images = shiftImage(registering_shift, img2_array)
img2.set_data(registered_images)
fig.canvas.draw()
plt.title("Registered images, using brute optimiser")
plt.show()

# Load remaining dicom images
img3_dcm = pydicom.read_file("IMG-0004-00003.dcm")
img4_dcm = pydicom.read_file("IMG-0004-00004.dcm")

# Convert dicom file to a numpy array using img_array = img_dcm.pixel_array
img3_array = img3_dcm.pixel_array 
img4_array = img4_dcm.pixel_array

# Create list of floating images
floating_list = [img2_array, img3_array, img4_array]

# Loop over floating images to produce registrations (and save them after the first time to speed up the process after)
if os.path.exists("registrations.npy"): # if this loop has already been run the registrations.npy will be loaded from the files
    registrations = np.load("registrations.npy")
else: 
    registrations = []
    for floating in floating_list:
        registering_shift = brute(registerImages, ((-100, 100),(-100, 100)), args=(img1_array, floating))
        registrations.append(registering_shift)
    print(registrations)
    
    registrations = np.array(registrations)
    np.save("registrations.npy", registrations) # save registrations to a numpy array for use next time the script is run

# loop over floating images (and shiftImage function) to produce registered images
shifted_images = []
for i, floating in enumerate(floating_list): # loop through floating list
    registered_images = shiftImage(registrations[i], floating) # each "floating" will loop through registrations
    shifted_images.append(registered_images) # append each floating image to the end of the array
#print(shifted_images[2].shape) # print registered image 1 and image 4

#View registered image 1 and image 4.
fig, ax = plt.subplots(1,1)
plt.title("Registered Images of Image 1 and 4")
ax.imshow(img1_array, alpha=0.5, cmap="Greens_r") 
ax.imshow(shifted_images[2], alpha=0.5, cmap="Purples_r") # use greens and purples as these help the eyes see more of the image
plt.show()
