#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment Part 2 (Day 3)
_________________________

Viveck Kingsley 

Owen Williams

_________________________

Opening Lung Images:
"""
# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from scipy.ndimage import interpolation

# Use io.imread() to open the three lung images using the correct file path, np.mean used to average array of the last RGB channel (-1)

image = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs.jpg"), -1)

image2 = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs2.jpg"), -1)

image3 = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs3.jpg"), -1)

"""
_______________________

Overlaying images in the same axis:
"""

fig = plt.figure() # Create Figure using matplotlib.
ax = fig.add_subplot(111) # Creating plot - (111) means the creation of a 1x1 grid, plot 1.
#""" Reverse greyscale colour map was used for easy visualisation of the appropriate tissue. """"
ax.imshow(image, cmap="Greys_r")  # Image on axis, with colormap Greys_r used.
floating = ax.imshow(image3, cmap="Greys_r", alpha=0.5) # Alpha = 0.5 to make image 3 semi transparent (0.5).

"""
_______________________

Shift_Function to translate/rotate image 3 onto image:
"""

#""" shifts argument allows for manual selection of movement in x and y planes, as well as r (=rotation), which allows for rotation of image 3 """"
def shift_image(shifts, r):
    global image3
#    ax1.imshow(image, cmap="Greys_r", alpha = 1) 
# .shift function of image 3 is assigned to "shifting" variable, and functions by translating image 3 with shifts[0] and shifts[1].
    shifting = interpolation.shift(image3, (shifts[0], shifts[1]), mode="nearest") 
    image3 = interpolation.rotate(shifting, r, reshape=False)
#    ax1.imshow(floating, cmap="Greys_r", alpha = 0.5)
    floating.set_data(image3)
    fig.canvas.draw()
    
#shift_image([-100, 20], 1)
#plt.show()

def eventHandler(event):
    up = 0
    down = 1
    whichKey=event.key
    print(whichKey)
    if whichKey == 'up':
        up = 1
        shift_image([-1, 0], 0)
        print (up)
    elif whichKey == 'left':
        shift_image([0, 1], 0)
    elif whichKey == 'down':
        shift_image([1, 0], 0)
    elif whichKey == 'right':
        shift_image([0, -1], 0)
    elif whichKey == 'r':
        shift_image([0, 0], 1)
    elif whichKey == 't':
        shift_image([0, 0], -1)
    
fig.canvas.mpl_connect('key_press_event', eventHandler)

plt.show()



