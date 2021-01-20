"""
Assignment for Day 3
Image Processing in Python
This script overlays two images.

Katherine Winfield (@kjwinfield) and Yongwon Ju (@yongwonju)

This version written on 20 January 2021
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation
from scipy import ndimage

#open the images
im1 = io.imread("lungs.jpg")
lungs = np.mean(im1, -1)
im2 = io.imread("lungs2.jpg")
lungs2 = np.mean(im2, -1)
im3 = io.imread("lungs3.jpg")
lungs3 = np.mean(im3, -1)

#display the images
plt.imshow(lungs) #displays the image using matplotlib
#plt.show()
plt.imshow(lungs2) #displays the image using matplotlib
#plt.show()

#display both images on the same plot, with transparency
plt.imshow(lungs, cmap="Greys_r")
plt.imshow(lungs2, alpha=0.3, cmap="Greys_r")
#plt.show()
plt.close()

#create function to automate overlaying shifted lungs2 image, that takes the horizontal and vertical pixel
#shift as inputs
def shift_image(vertical, horizontal, rotation=0):
    global lungs2 #make lungs2 and lungs3 global variables
    global lungs3
    fig = plt.figure() #create figure
    ax = fig.add_subplot(111) #set the axes
    ax.imshow(lungs, cmap="Greys_r") #put fixed image into the background of the figure

    #overlays the image to be moved, with transparency
    #shifts the image to be moved
    if rotation != 0:
        floating = ax.imshow(lungs3, alpha=0.3, cmap="Greys_r")
        lungs3 = ndimage.rotate(lungs3, rotation, reshape=False) #rotates the image
        floating.set_data(lungs3)
    else:
        floating = ax.imshow(lungs2, alpha=0.3, cmap="Greys_r")
        lungs2 = interpolation.shift(lungs2, (vertical, horizontal), mode="nearest")
        floating.set_data(lungs2) #updates the figure with the shifted image
    plt.show()
    plt.close()
    fig.canvas.draw()

shift_image(10, 20) #this calls the function and shifts lungs2 down 10 pixels, and right 20 pixels
shift_image(0, 0, -10)
'''
To sync up the images correctly call shift_image(-20, -40). this will align lungs and lungs2.
'''
plt.imshow(lungs3) #displays the image using matplotlib
#plt.show()

def rotate_image():
    
    fig = plt.figure() #create figure
    ax = fig.add_subplot(111) #set the axes
    ax.imshow(lungs, cmap="Greys_r") #put fixed image into the background of the figure

    floating = ax.imshow(lungs3, alpha=0.3, cmap="Greys_r") #overlays the image to be rotated, with transparency
    
    floating.set_data(lungs3) #updates the figure with the rotated image
    plt.show()
    plt.close()
    fig.canvas.draw()
