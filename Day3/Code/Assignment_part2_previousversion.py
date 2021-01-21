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

def shiftRotateImage(the_shifts,rotations): 
    """
    Shifts and rotates Lungs3 image in the xy plane.

    Parameters
    ----------
    the_shifts : list
        Desired shifts in xy plane
    rotations : float
        Desired rotation in xy plane
    Returns
    -------
    None.

    """
    # bring in Lungs3 image (global so as can be edited)
    global Lungs3
    # Shift Lungs3 image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    Lungs3 = interpolation.shift(Lungs3, shift = the_shifts)
    # Rotates Lung3 image using interpolation
    # Roation is from function argument, rotate in xy plane
    Lungs3 = interpolation.rotate(Lungs3, angle=rotations, reshape=False)
    # Updates floating2 image in figure space
    floating2.set_data(Lungs3)
    # Draws update to canvas (for figure 2)
    fig2.canvas.draw()

def main():
    """
    Makes plots for Lung2 registered to Lung1 and Lung3 registered to Lung1
    """
    #make Lungs 2, floating and fig global so they can be accessed within shiftImage.
    #make Lungs 3, floating2 and fig2 global so they can be accessed within shiftImageRotate
    global Lungs2   
    global Lungs3
    global floating
    global floating2 
    global fig
    global fig2
    # Read data
    Lungs1 = imread("Lungs.jpg", as_gray = True)
    Lungs2 = imread("Lungs2.jpg", as_gray = True)
    Lungs3 = imread("Lungs3.jpg", as_gray = True)
    #Create figure space and add subplots for shift plot
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


    #Create figure space and add subplots for shift and rotation plot
    fig2 = plt.figure()
    ax1b = fig2.add_subplot(111)
    ax2b = fig2.add_subplot(111)
    # Colour images using cmap so as to view more easily on screen 
    # Use alpha = 0.5 to make second image transparent
    ax1b.imshow(Lungs1, cmap = "Greys_r")
    floating2 = ax2b.imshow(Lungs3, alpha = 0.5, cmap = "Reds")    
    # Use shift image to find the shift required to register the images.
    # Shift required is [-4, -357], rotation required is
    shiftRotateImage([-4, -35],357)  

    
    # Display images
    plt.show()
    plt.close()

if __name__ == "__main__":
# To allow main function to run
    main()
