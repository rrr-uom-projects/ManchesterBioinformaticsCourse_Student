"""
Assignment for Day 3
Image Processing in Python
This script overlays two images.

Katherine Winfield (@kjwinfield) and Yongwon Ju (@yongwonju)

This version written on 20 January 2021
"""

'''
Import libraries 
'''
# ---------------------------------------IX------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation
from scipy import ndimage

'''
Read jpg files

Convert RGB data into gray scale using the mean function
'''
# ---------------------------------------X---------------------------------------------------
im1 = io.imread("lungs.jpg")
lungs = np.mean(im1, -1)
im2 = io.imread("lungs2.jpg")
lungs2 = np.mean(im2, -1)
im3 = io.imread("lungs3.jpg")
lungs3 = np.mean(im3, -1)

'''
Open files

Display both lung1 and lung2 images on the same figure space using matplotlib
'''
# ------------------------------------XI-&-XII-------------------------------------------------
plt.imshow(lungs) 
plt.title('Lung 1')
plt.show()
plt.imshow(lungs2) 
plt.title('Lung 2')
plt.show()

plt.imshow(lungs, cmap="Greys_r")
plt.imshow(lungs2, alpha=0.3, cmap="Greys_r")
plt.title('Lung 1 and 2 overlayed')
plt.show()

plt.close()

# -------------------------------------XIII---------------------------------------------------
'''
Create figure space and set first x-ray image with axis
'''
fig = plt.figure()                      # create figure
ax = fig.add_subplot(111)               # set the axes
ax.imshow(lungs, cmap="Greys_r")        # put fixed image into the background of the figure

floating = ax.imshow(lungs3, alpha=0.3) # Add a second image onto the figure space
plt.title('Lung 1 and Lung 3 overlayed \nUse arrow keys and z, x to move Lung 3')

################################
shifting_interval = 5
rotation_degree = 0.5
################################


def shift_image(vertical, horizontal, rotation=0):
    '''
    Function to translate and rotate second image and overlay it on the figure space 

    Parameters: 

                vertical    - transation in the y axis
                horizontal  - translation in the x axis
                rotation    - rotation clockwise

    Returns:    
    
                null
    '''
    global lungs3

    translated_image = ndimage.rotate(lungs3, rotation, reshape=False) # rotates the image
    lungs3           = interpolation.shift(translated_image, (vertical, horizontal), mode="nearest") # translates the image in the x and y axis

    floating.set_data(lungs3)
    fig.canvas.draw()



# ------------------------------------XIV-----------------------------------------------------
'''
    shift_image(10, 20) this calls the function and shifts lungs2 down 10 pixels, and right 20 pixels
    shift_image(0, 0, -10) rotates the image 10 degrees anticlockwise 
'''


# ------------------------------------XVII-----------------------------------------------------
'''
To sync up the images correctly call shift_image(-20, -40). this will align lungs and lungs2.
'''

# Variables used to calculate translation and rotation
up, left, right, down, right, anti, clock = 0,0,0,0,0,0,0

def eventHandler(event):
    '''
    This function takes in the user input and translates of rotates the image lung3 in the figure space

    Parameters: 
    '''
    global up, left, right, down, right, anti, clock
    
    whichKey = event.key

    if whichKey == "up":
        shift_image(-shifting_interval, 0, 0)
        up = up + 1

    elif whichKey == "down":
        shift_image(shifting_interval, 0, 0)
        down = down + 1

    elif whichKey == "left":
        shift_image(0, -shifting_interval, 0)
        left = left + 1

    elif whichKey == "right":
        shift_image(0, shifting_interval, 0)
        right = right + 1

    elif whichKey == "z":
        shift_image(0, 0, rotation_degree)
        clock = clock + 1

    elif whichKey == "x":
        shift_image(0, 0, -rotation_degree)
        anti = anti + 1

    elif whichKey == "escape":
        plt.close('all')

# -------------------------------------------------------------------------------------------
fig.canvas.mpl_connect("key_press_event", eventHandler)
plt.show()

# -------------------------------------------------------------------------------------------
print('Translated ', (down - left) * shifting_interval, 'pixels on the horizontal axis \nTranslated ', (right - left) * shifting_interval, 'pixels on the vertical axis \nRotated ', ((anti - clock) * rotation_degree + 360)%360, 'degrees clockwise')
# -------------------------------------------------------------------------------------------

# Translation and rotations from lung 3 to lung 1 using 
# -------------------------------------------------------------------------------------------
# Translated  -45 pixels on the horizontal axis 
# Translated  -35 pixels on the vertical axis 
# Rotated  3.5 degrees clockwise
# -------------------------------------------------------------------------------------------
