#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:02:32 2021
Authors: Nermeen and Helena
Title: This is Part 2 of Day 3. 
Description: In this task we need to load several lung images, display on the 
same axes and manually align them.
"""
#Import necessary modules
import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
from skimage import io #this is used for image processing
from scipy.ndimage import interpolation

#Load the images - imread will load in 3 channels by default, using np.mean
#Averages the 3 channels so there is only 1 intensity value for each pixel.
lungs1 = np.mean(io.imread("lungs.jpg"), -1)
lungs2 = np.mean(io.imread("lungs2.jpg"), -1)

#Display each image individually using grey colormap
plt.imshow(lungs1, cmap="Greys_r")
plt.show()
plt.imshow(lungs2, cmap="Greys_r")
plt.show()

#Display both images on the same axes in different colors, with the second
#image made transparent using the alpha argument
plt.imshow(lungs1, cmap="Purples_r")
plt.imshow(lungs2, alpha=0.5, cmap="Greens_r")
plt.show()

#Move the 2nd image relative to the 1st.
fig = plt.figure()
ax = fig.add_subplot(111) #Create a 1x1 grid of subplots, with ax specifying position 1
ax.imshow(lungs1, cmap="Purples_r") #Plonks 1st image in space designated by ax
floating = ax.imshow(lungs2, alpha=0.5, cmap="Greens_r")#Specify a variable which plonks 2nd image in space designated by ax
lungs2 = interpolation.shift(lungs2, (1, 2), mode="nearest")#Shift 2nd image realtive on its own axes. 2nd argument (change in y, change in x)
floating.set_data(lungs2) #Update the shifted position of 2nd image in the variable floating
plt.show()


#Define a function to perform the above task
def shiftImage(shifts):
    global lungs2 #Global allows the function to change the values of lung2 outside the function, as well as inside
    fig = plt.figure()
    ax = fig.add_subplot(111) #Create a 1x1 grid of subplots, with ax specifying position 1
    ax.imshow(lungs1, cmap="Purples_r") #Plonks 1st image in space designated by ax
    floating = ax.imshow(lungs2, alpha=0.5, cmap="Greens_r")#Specify a variable which plonks 2nd image in space designated by ax
    lungs2 = interpolation.shift(lungs2, shifts, mode="nearest")#Shift 2nd image realtive on its own axes. 2nd argument (change in y, change in x)
    floating.set_data(lungs2)
    fig.canvas.draw()
    return

#Tries out the function
shiftImage((10, 20))

"""
If the image is first moved outside frame - the results of the function will look like a smear as any
part of the image outside the frame gets lost and the interpolator gets confused

"""