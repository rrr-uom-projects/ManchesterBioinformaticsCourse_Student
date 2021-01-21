# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:17:41 2021

@author: jaden
"""
### Name: Jadene Lewis
### Date: 20/01/21
### Title: Image Processing in Python

# Part 2 #
import numpy as np
import skimage.io
import scipy.signal
import matplotlib.pyplot as plt
from scipy.ndimage import interpolation, rotate

# Load and display images 'lungs.jpg' and 'lung2.jpg and 'lung3.jpg'
lungs_image = skimage.io.imread("lungs.jpg", as_gray=True)
plt.imshow(lungs_image)

lungs2_image = skimage.io.imread("lungs2.jpg", as_gray=True)
plt.imshow(lungs2_image)

lungs3_image = skimage.io.imread("lungs3.jpg", as_gray=True)
plt.imshow(lungs3_image)

# Make a plot where you can see both images on the same plot using transparency
floating_image = skimage.io.imread("lungs2.jpg", as_gray=True) #moving image
background_image = skimage.io.imread("lungs.jpg", as_gray=True) #fixed image


fig = plt.figure()
plt.title('Lung 1 and Lung 2 overlaid')
ax = fig.add_subplot(111)
ax.imshow(background_image, cmap="Greys_r") #puts 'lungs.jpg' in background
floating = ax.imshow(floating_image, alpha=0.5, cmap="Greys_r") #puts 'lungs2.jpg' in front and alpha=0.5 makes for partial transparency. increase or decrease alpha value to make front image less or more see through, respectively
#plt.imshow(interpolation.shift(floating_image, (10, 20), mode = "nearest") #Because RGB image so has three dimensions and thus shifting parameter requires 3 values
plt.show()

help(plt.imshow)
help(interpolation.shift)
plt.show()


##Write a function that would shift floating image
def shiftImage(shifts):
    global floating_image
    #global floating
    floating_image_shift = interpolation.shift(floating_image, shifts, mode = "nearest")
    floating.set_data(floating_image_shift) #sets changes to floating
    fig.canvas.draw() #draws update to canvas
    

shiftImage([10, 40]) #what does this do?
shiftImage(50, 40)

#Modify previous function to include rotation
def shiftImage(shifts, r):
    global floating_image
    #global floating
    floating_image_shift = interpolation.shift(floating_image, shifts, mode = "nearest")
    floating_image_rotated = scipy.ndimage.rotate(floating_image, r, reshape=True)
    floating.set_data(floating_image_shift) #not sure if this code works
    floating.set_data(floating_image_rotated) #this also
    fig.canvas.draw()
    
shiftImage(10, 20, 5)
    
#Shifting image using keyboard presses

def eventHandler(event):  
    """
    This function handles deciphering what the user wants us to do, the event knows which key has been pressed
    """
    up = 0
    whichKey == event.key
    if whichKey == "up":
        up = 1
    print(up)
        
fig.canvas.mpl_connect('key_press_event', eventHandler)


import dicom #not working
help(scipy.ndimage.rotate)

#plt.imshow(scipy.ndimage.rotate(floating_image, -5, reshape=True))
#plt.show()









