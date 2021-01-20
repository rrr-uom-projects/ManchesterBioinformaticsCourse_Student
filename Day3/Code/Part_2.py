"""
Part 2 of the assingment
Authors: Nicola Compton and Catherine Borland

This code aligns two lung images on top of each other using a shift function and a keyboard press event.
"""

# import modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io 
from skimage.io import imread
import scipy
from scipy import ndimage
from scipy.ndimage import interpolation, rotate

# load images
# it is in the same directory as we are currently working in so we do not need to specify the path
image = io.imread("lungs.jpg",as_gray=True)
image_2 = io.imread("lungs2.jpg",as_gray=True)
image_3 = io.imread("lungs3.jpg",as_gray=True)

# display the images
#plt.imshow(image, cmap="Greys_r")
#plt.show()

# use plt.show() twice to make sure the images are displayed seperately
#plt.imshow(image_2, cmap="Greys_r")
#plt.show()

# plot the images on the same axis
# alpha sets the transparency, we have used 0.5 for both images so that they are equally as transparent as each other
# set the axis of the second image to 'floating', so that later we only move image 2 / image 3

fig, ax=plt.subplots(1,1)
ax.imshow(image, alpha=0.5, cmap="Greys_r")
#floating=ax.imshow(image_2, alpha=0.5, cmap="Greys_r")
floating=ax.imshow(image_3, alpha=0.5, cmap="Greys_r")

# function to shift the image by a vector shifts and rotate by an angle
# change between image_2 and image_3 to register the lungs to lungs2 and lungs3 respectively
# we thought about including the image as a variable as an input variable but this would interfere with the global statement
def shiftImage(shifts, angle):
    
    #global image_2
    global image_3
    
    # shift the image
    
    #image_2=interpolation.shift(image_2, shifts, mode="nearest")
    image_3=interpolation.shift(image_3, shifts, mode="nearest") 
    
    # rotate the image 
    # if reshape=True then the image incrementally decreases in size as the rotated image must fit inside the original array
    # we set reshape=false to maintain the image size
    
    #image_2=ndimage.rotate(image_2,angle,reshape=False)
    image_3=ndimage.rotate(image_3,angle,reshape=False)
    
    # update the axis of the floating image
    
    #floating.set_data(image_2) 
    floating.set_data(image_3)
    fig.canvas.draw()

# the shifts needed to align lungs and lungs2 are 20 down and 44 left
#shiftImage([-20,-44],0)
#plt.show()

# the following code allows the images to be shifted using keyboard presses
# define a function
def eventHandler(event):
    
    # define the key which has been pressed
    whichKey=event.key
    
    # set 0 as the default value 
    up=0
    if whichKey=="up": # determine which key has been pressed
        up=-1    # up is -1 and down is 1 on the images lungs and lungs2 because the values on the y axis are reversed
    elif whichKey=="down":
        up=1
    
    left=0
    if whichKey=="left":
        left=-1
    elif whichKey=="right":
        left=1
        
    # determine if it has been rotated clockwise/anticlockwise
    angle=0
    if whichKey=="a":  # rotation anticlockwise
        angle=1
    elif whichKey=="c": # rotation clockwise
        angle=-1
        
    # call the shiftImage function to shift/rotate the image by the key which was pressed
    shiftImage([up,left],angle)

    
# connect the function to the figure
fig.canvas.mpl_connect('key_press_event', eventHandler)
plt.show()

# using key press we could achieve a better alignment of lungs2 on top of lungs 19 up and 39 left, shifts=[-19,-39]
# lungs3 was harder to align, we rotated it 3 degreed clockwise and shifted it up 6, 29 left
