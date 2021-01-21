#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 21 16:02:32 2021
Authors: Nermeen and Helena
Title: This is Part 1 of Day 4. 
Description: In this task we create a function to register images automatically.
"""

import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
#from skimage import io #this is used for image processing
from scipy.ndimage import interpolation
#from scipy.ndimage import rotate
from scipy.optimize import brute
import pydicom
#To make the images bigger in size
plt.rcParams['figure.figsize'] = (16.0, 12.0)

#Load DICOM objects into variables
patientImage1 = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")

#patientImage1 =pydicom.dcmread("IMG-0004-00001.dcm").pixel_array #This would load just the pixel_array into the variable
#plt.imshow(patientImage1)
#plt.show()

print(patientImage1)#Prints the DICOM header information in the console

#Plot both figures ontop of one another
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.imshow(patientImage1.pixel_array, cmap='Purples_r')#pixel_array is the image
ax.imshow(patientImage2.pixel_array, alpha=0.5, cmap='Greens_r')#pixel_array is the image, alpha makes transparent
plt.show()

#Save this image as a png
fig1.savefig("unregistered.png") #matlibplot save function
#######

#Define a function to shift and interpolate the image
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

#Save this image as a png
fig2.savefig("manual_register.png") #matlibplot save function

#Define cost function
def fcn(fixed, floating):
    return  np.mean((fixed - floating)**2)#Calculates the difference between the images - the lower the cost, the better the alignment

#Test the function - check that giving it 2 of the same image gives a result of 0
cost = fcn(patientImage1.pixel_array, patientImage1.pixel_array)
print(cost)#Check that the cost is 0 when identical images are input

#Try to define a register images function
def register(shift, fixed, floating):
    shifted_image = shiftImage(shift, floating)
    cost = fcn(fixed, shifted_image)
    #print(cost)
    return cost

cost1 = register((0, 0), patientImage1.pixel_array, patientImage2.pixel_array)
print(cost1)# = 684 showing images are not well aligned 

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

print("Done with the first bit") #Helps keep check of run progress

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
    
#print(registrations)#Checking out what's inside registrations
#print(registrations[1])#Remembering how to access lists 

print("Done the next bit") #Helps keep check of run progress

#Apply the registrations to the images and stick the shifted images in a list
shifted_images = []
i=0 #Set counter
for image in floating_list:
    new_position = shiftImage((registrations[i]), image)
    shifted_images.append(new_position)
    i += 1 #Increment counter
    
#print(shifted_images)#Check what's in here
print("Done")    
 
#Create a numpy array out of the registrations and save it
registrations_arr = np.array(registrations)
np.save("registrations.npy", registrations_arr)
    
#########Go to the next script!!!##########

