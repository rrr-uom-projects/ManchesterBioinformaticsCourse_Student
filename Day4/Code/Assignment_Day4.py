#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
from skimage import io #this is used for image processing
from scipy.ndimage import interpolation
from scipy.ndimage import rotate
from scipy.optimize import brute
import pydicom
#To make the images bigger in size
plt.rcParams['figure.figsize'] = (16.0, 12.0)

#Load images into variables
patientImage1 = pydicom.read_file("IMG-0004-00001.dcm")
#patientImage1 =pydicom.dcmread("IMG-0004-00001.dcm").pixel_array
#plt.imshow(patientImage1)
#plt.show()

patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")
#patientImage2 =pydicom.dcmread("IMG-0004-00002.dcm").pixel_array
#plt.imshow(patientImage2)
#plt.show()

#img1=pydicom.dcmread("IMG-0004-00001.dcm").pixel_array
#plt.imshow(img1)
#plt.show()

print(patientImage1)#Prints the DICOM header information in the console

#Plot both figures ontop of one another
fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.imshow(patientImage1.pixel_array, cmap='Purples_r')#pixel_array is the image
ax.imshow(patientImage2.pixel_array, alpha=0.5, cmap='Greens_r')#pixel_array is the image, alpha makes transparent
plt.show()

#Save this image as a png
fig2.savefig("unregistered.png") #matlibplot save function
#######

def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts, mode="nearest")#Shift 2nd image realtive on its own axes. 2nd argument (change in y, change in x)
    return shifted_image

#Function with parameters that approximately align the images
shifted_image = shiftImage((5, -20), patientImage2.pixel_array)

#Plot to show the figure has been shifted by the function
fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.imshow(patientImage1.pixel_array, cmap='Purples_r')#pixel_array is the image
ax.imshow(shifted_image, alpha=0.5, cmap='Greens_r')#pixel_array is the image, alpha makes transparent
plt.show()

#Define cost function
def fcn(fixed, floating):
    return  np.mean((fixed - floating)**2)

#Test the function - check that giving it 2 of the same image gives a result of 0
cost = fcn(patientImage1.pixel_array, patientImage1.pixel_array)
print(cost)

#Try to define a register images function
def register(shift, fixed, floating):
    shifted_image = shiftImage(shift, floating)
    cost = fcn(fixed, shifted_image)
    #print(cost)
    return cost

cost1 = register((0, 0), patientImage1.pixel_array, patientImage2.pixel_array)

#Automate registering of images
fixed = patientImage1.pixel_array
floating = patientImage2.pixel_array
registering_shift = brute(register, ((-100, 100), (-100,100)), args=(fixed, floating))

print(registering_shift)
##This gave an optimal shift of [  2.99566717 -25.00354501]

#Shift the image to the position identified by the optimiser
optimum_shifted_image_position = shiftImage((2.99566717, -25.00354501), floating)

#Plot the image in the position identified by the optimiser
fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.imshow(patientImage1.pixel_array, cmap='Purples_r')#pixel_array is the image
ax.imshow(optimum_shifted_image_position, alpha=0.5, cmap='Greens_r')#pixel_array is the image, alpha makes transparent
plt.show()

print("Done with the first bit")

##### Trying to register all images to the first####

#Load remaining 2 DICOM objects
patientImage3 = pydicom.read_file("IMG-0004-00003.dcm")
patientImage4 = pydicom.read_file("IMG-0004-00004.dcm")

#Give the pixel_arrays sensible variable names
fixed = patientImage1.pixel_array
floating2 = patientImage2.pixel_array
floating3 = patientImage3.pixel_array
floating4 = patientImage4.pixel_array

#Put the pixel arrays in a list
floating_list = [floating2, floating3, floating4]

#Loop over the images appending their optimal shift to a list of registrations
registrations = []
for floating in floating_list:
    registering_shift = brute(register, ((-100, 100), (-100,100)), args=(fixed, floating))
    registrations.append(registering_shift)
    
print(registrations)
print(registrations[1])

print("Done the next bit")

#Apply the registrations to the images and stick the shifted images in a list
shifted_images = []
i=0
for image in floating_list:
    new_position = shiftImage((registrations[i]), image)
    shifted_images.append(new_position)
    i += 1
    
print(shifted_images)  
print("Done")    
 
#Create a numpy array out of the registrations and save it
registrations_arr = np.array(registrations)
np.save("registrations.npy", registrations_arr)
    
#########Go to the next script!!!##########


