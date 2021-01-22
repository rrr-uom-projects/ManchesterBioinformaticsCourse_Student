#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment Part 2 (Day 3)
_________________________

Viveck Kingsley - 10811867

Owen Williams - 10806830

_________________________

Opening Lung Images:
"""
# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from scipy.ndimage import interpolation

"""
# Use io.imread() to open the three lung images using the correct file path, 
np.mean used to average array of the last RGB channel (-1), and io.imread to load the images.
"""
# Loading the lungs images
image = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs.jpg"), -1)

image2 = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs2.jpg"), -1)

image3 = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs3.jpg"), -1)


# Overlaying images in the same axis:
fig = plt.figure() # Create Figure using matplotlib.
ax = fig.add_subplot(111) 
ax.imshow(image, cmap="Greys_r")  
floating = ax.imshow(image3, cmap="Greys_r", alpha=0.5) 

"""
XII:
MatPlotLib was used to create a figure. When creating a plot using ax.fig.add_subplot(111), the (111) meant the 
creation of a 1x1 grid, with one plot. Reverse greyscale colourmap was used for easy visualisation of the appropriate tissue
Alpha = 0.5, made image 3 - the floating image, semi transparent. 
"""

"""
XIII:
Shift_Function was made to translate/rotate the floating image3 onto the fixed image:
The arguments (shifts, r) allow for manual selection of movement in x and y planes (shifts), as well as rotation (r). 
Using the global command in this function allows changes performed on image3 to be enacted on outisde this function. 
"""

def shift_image(shifts, r):
    global image3
#    ax1.imshow(image, cmap="Greys_r", alpha = 1) 
# .shift function of image 3 is assigned to "shifting" variable, and functions by translating image 3 with shifts[0] and shifts[1].
    shifting = interpolation.shift(image3, (shifts[0], shifts[1]), mode="nearest") 
    image3 = interpolation.rotate(shifting, r, reshape=False)
#    ax1.imshow(floating, cmap="Greys_r", alpha = 0.5)
    floating.set_data(image3)
    fig.canvas.draw()

"""
XIV:
shift_image([10, 20], 0) translates image3 10 pixels down, and 20 pixels right. If these values were negative, the image would
be translated in the opposite direction. 
XV: 
The shifts needed to align image2 with the fixed image: ([-18, -40], 0)
XVI: 
The code has already implemented the rotate function (interpolation.rotate), which takes the 'shifting' translation variable 
and rotates it. Image 3 was found to align with the fixed image with the following: ([-6,-33], -3)]. To choose which image was to be translated, 
we had to manually substitute the appropriate image name into the function. 
"""    

#shift_image([10, 20], 0)
#plt.show()

"""
XVII: 

Another function with the required argument 'event' was created, which assigned a specific function to a key press.
The following code works as follows, if the up key is pressed, whichKey variable will store this, and if whichKey is indeed up,
the floating image will be translated ([-1, 0] ,0). Each direction, including rotations in both directions were assigned a key.
If an unregistered key is pressed, there is no output. This eventhandler function is called by fig.canvas.mp1_connect. print(whichKey) tells the user
what key is being pressed. 
XVIII:
The shifts and rotations matched what was found by trial and error.
"""

def eventHandler(event):
    whichKey=event.key
    print(whichKey)
    if whichKey == 'up':
        shift_image([-1, 0], 0)
    elif whichKey == 'right':
        shift_image([0, 1], 0)
    elif whichKey == 'down':
        shift_image([1, 0], 0)
    elif whichKey == 'left':
        shift_image([0, -1], 0)
    elif whichKey == 'r':
        shift_image([0, 0], 1)
    elif whichKey == 't':
        shift_image([0, 0], -1)
    
fig.canvas.mpl_connect('key_press_event', eventHandler)

plt.show()



