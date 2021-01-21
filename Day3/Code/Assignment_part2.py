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
    Shifts LungsNew image in the xy plane. 

    Parameters
    ----------
    the_shifts : list
        Desired shifts in xy plane

    Returns
    -------
    None.

    """
    # bring in LungsNew image (global so as can be edited)
    global LungsNew
    # Shift LungsNew image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    LungsNew = interpolation.shift(LungsNew, shift = the_shifts)
    # Updates floating image in figure space
    floating.set_data(LungsNew)
    # Draws update to canvas
    fig.canvas.draw()


def shiftRotateImage(the_shifts,rotations): 
    """
    Shifts and rotates LungsNew image in the xy plane.

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
    # bring in LungsNew image (global so as can be edited)
    global LungsNew
    # Shift LungsNew image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    LungsNew = interpolation.shift(LungsNew, shift = the_shifts)
    # Rotates Lung3 image using interpolation
    # Roation is from function argument, rotate in xy plane
    LungsNew = interpolation.rotate(LungsNew, angle=rotations, reshape=False)
    # Updates floating2 image in figure space
    floating.set_data(LungsNew)
    # Draws update to canvas (for figure 2)
    fig.canvas.draw()

def eventHandler(event):
    """
    This function calls shiftRotateImage each time a key is pressed, shifting or rotating the image by one unit. 
    The key pressed determines which movement occurs
    The changes made are used to modify the dictionary to keep track of changes happening
    Parameters
    ----------
    event : character
        key that has been pressed        
    Returns
    -------
    None.
    """
    #find the key pressed for the event
    whichKey = event.key
    #6 key options here: up, down, left, right cause shifts. o and p rotate to the left/riht respectively
    #the movement_storage dictionary is a global variable and is modified each time a relevant key is pressed
    if whichKey == 'up':
        shiftRotateImage([-1,0],0)
        movement_storage["x"]=movement_storage["x"]-1
    if whichKey == 'down':
        shiftRotateImage([1,0],0)
        movement_storage["x"]=movement_storage["x"]+1
    if whichKey == 'left':
        shiftRotateImage([0,-1],0)
        movement_storage["y"]=movement_storage["y"]-1
    if whichKey == 'right':
        shiftRotateImage([0,1],0)  
        movement_storage["y"]=movement_storage["y"]+1
    if whichKey == 'p':
        shiftRotateImage([0,0],-1)  
        movement_storage["rotation"]=movement_storage["rotation"]-1
    if whichKey == 'o':
        shiftRotateImage([0,0],1)
        movement_storage["rotation"]=movement_storage["rotation"]+1

def main():
    """
    Makes plots for Lungs2 registered to Lungs1 and Lungs3 registered to Lung1
    Makes plots for Lung1 and Lung 3, allowing user to register them using keystrokes
    Outputs changes made once image is closed
    """
    #make LungsNew, floating and fig global so they can be accessed within shiftImage and ShiftImageRotate.
    global LungsNew   
    global floating
    global fig
    #make movement_storage global so it can be accessed in eventHandler
    global movement_storage
    
    # Read data for lungs1
    Lungs1 = imread("Lungs.jpg", as_gray = True)
    
    ## lungs2 image registration
    # Read data for lungs2
    LungsNew = imread("Lungs2.jpg", as_gray = True)
    #Create figure space and add subplots for shift plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    # create images
    # Colour images using cmap so as to view more easily on screen 
    # Use alpha = 0.5 to make second image transparent
    ax1.imshow(Lungs1, cmap = "Greys_r")
    floating = ax2.imshow(LungsNew, alpha = 0.5, cmap = "Reds")    
    # Use shift image to find the shift required to register the images.
    # Shift required is [-16, -40]
    shiftImage([-16, -40])  
    
    ### lungs3 image registration
    #read in lungs3 image
    LungsNew = imread("Lungs3.jpg", as_gray = True)
    #Create figure space and add subplots for shift and rotation plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    # Colour images using cmap so as to view more easily on screen 
    # Use alpha = 0.5 to make second image transparent
    ax1.imshow(Lungs1, cmap = "Greys_r")
    floating = ax2.imshow(LungsNew, alpha = 0.5, cmap = "Reds")    
    # Use shift image to find the shift required to register the images.
    # Shift required is [-4, -357], rotation required is
    shiftRotateImage([-4, -35],357)  
    ### interactive image registration lung 3
    # Read data for lungs3
    LungsNew= imread("Lungs3.jpg", as_gray = True)

    #Create figure space and add subplots for shift and rotation plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    # Colour images using cmap so as to view more easily on screen 
    # Use alpha = 0.5 to make second image transparent
    ax1.imshow(Lungs1, cmap = "Greys_r")
    floating = ax2.imshow(LungsNew, alpha = 0.5, cmap = "Reds")    
    #link key pressing to eventHandler function
    fig.canvas.mpl_connect('key_press_event', eventHandler)
    #initialise movement_storage as dictionary
    movement_storage={"x":0,"y":0,"rotation":0}
  
    
    # Display images
    plt.show()
    plt.close()
    #output movement_storage dictionary when changes have been made
    print(movement_storage)
    #{'x': -4, 'y': -31, 'rotation': -3} which is very similar to result from before

if __name__ == "__main__":
    # To allow main function to run
    main()
