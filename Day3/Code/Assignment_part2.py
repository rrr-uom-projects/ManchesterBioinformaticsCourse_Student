# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:24:01 2021

Authors: Rosie Smart and Ruth Keane
Date: 20/01/2021
Title: Image processing in Python Part 2
"""
import matplotlib.pyplot as plt
import numpy as np
import skimage.io 
from skimage.io import imread
from scipy.ndimage import rotate
from scipy.ndimage import interpolation 


    
def shiftImage(the_shifts): 
    """
    Shifts Lungs2 image in the xy plane. 

    Parameters
    ----------
    the_shifts : list
        Desired shifts in xy plane

    Returns
    -------
    None.

    """
    # bring in Lungs2 image (global so as can be edited)
    global Lungs2
    # Shift Lungs2 image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    Lungs2 = interpolation.shift(Lungs2, shift = the_shifts)
    # Updates floating image in figure space
    floating.set_data(Lungs2)
    # Draws update to canvas
    fig.canvas.draw()

if __name__ == "__main__":
    # Read data
    Lungs1 = imread("Lungs.jpg", as_gray = True)
    Lungs2 = imread("Lungs2.jpg", as_gray = True)
    
    #Create figure space and add subplots
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    # create images
    # Colour images using cmap so as to view more easily on screen 
    # Use alpha = 0.5 to make second image transparent
    ax1.imshow(Lungs1, cmap = "Greys_r")
    floating = ax2.imshow(Lungs2, alpha = 0.5, cmap = "Reds")    
    # Use shift image to find the shift required to register the images.
    # Shift required is [-16, -40]
    shiftImage([-16, -40])  
    
    # Display images
    plt.show()
    plt.close()
    