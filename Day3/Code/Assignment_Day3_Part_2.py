#!/usr/bin/env python
# coding: utf-8
 
 
"""
VII. Start a new script
 
VIII. Write some useful information like a title and your names in some comments at the top of
the code.
"""
 
### Image processing in Python: assignment ###
 
          ## By Igor and Manuel ##
            
                 # Part 2 #
"""
IX. Import the modules that you will need. You’ll need matplotlib.pyplot and numpy, 
but also imread from skimage.io, and interpolation and rotate from
scipy.ndimage
 
"""
# Let’s import needed with the next lines of code.
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
import inspect
import os
import matplotlib.patches as patches
# path of the executing script 
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

"""
X. Load the images “lings.jpg” and “lungs2.jpg”
"""

#name of image
img_name1 = '/lungs.jpg'
img_name2 = '/lungs2.jpg'
img_name3 = '/lungs3.jpg'
#path to the image
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2
img_path3 = actual_path + img_name3
#import images using imread as a grey scale of values between 0 and 1
lungs1 = io.imread(img_path1, as_gray=True)
lungs2 = io.imread(img_path2, as_gray=True)
lungs3 = io.imread(img_path3, as_gray=True)

"""
XI. Display the images
"""

fig = plt.figure()

# SOME EXPLANATION HERE IS NEEDED
 
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
 
ax.imshow(lungs1)
ax2.imshow(lungs2)
 
plt.show()

"""
XII. Make a plot where you can see both images on the same axes using transparency.
"""
# To do this, we just need to add lungs2 over lungs1. With alpha, we blend the value, between 0 as transparent and 1 as opaque.  

plt.imshow(lungs1)
plt.imshow(lungs2, alpha=0.25) # Alhpa dneotes level of tranparancy 
plt.show()


#function that shits images. Input is a list of two values that shift the second image
def shiftImage(shifts):
    #shits is an input, which is a list of two values example [value1, value2] that shifts the second image. 
    # Value1 moves image up or down, value 2 moves image left or right.
    global lungs1, lungs2
    shifted_image = interpolation.shift(lungs2, (shifts[0], shifts[1]), mode="nearest")
    plt.imshow(lungs1, cmap="Greys_r")
    plt.imshow(shifted_image, alpha=0.15, cmap="Greys_r")
    plt.show()


#Call the function to display shifted image
#the values that perfectly overlay the images are [-15, -40]
#shiftImage([-15,-40])
#shiftImage([10,20])

"""
XIV. Evaluate your function by calling it. What does shiftImage([10,20]) do? 

this function shifts image 10 pixels to the bottom and 20 pixels to the right
"""
 
"""
XV. What are the shifts needed to align the images? 
Ansewr: [-15, -40]

"""
 
"""
XVI. Modify your code to include rotations. Load “lungs3.jpg” and use that as your floating image instead. What are the shifts/rotations required to align the images now?
"""


fig = plt.figure()
# Lets try to rotate lungs 3 over lungs 1
# This needs the degrees ndimage.rotate() rotates in the plane defined by the two axes
lung3_rotate = rotate(lungs3, -3, reshape=True)

# We have noticed that lungs3 needs to ve shift a bit to overlap with lungs1
# Let’s do it
lung3_rotated_shift = interpolation.shift(lung3_rotate, (-25, -45))

# Now we display both images as we did in exercises before.
plt.imshow(lungs1)
plt.imshow(lung3_rotated_shift, alpha=0.25)
plt.show()





"""
XVII  Event Handling 
"""
def eventHandler(event):
    up = 0
    down = 0
    right = 0
    left = 0
    whichKey = event.key
    global lungs2
    if whichKey == "up":
        up = 1
        #shiftImage([up,0])
        lungs2 = interpolation.shift(lungs2, up, 0, mode="nearest")
      
    elif whichKey == "down":
        down = -1
        #shiftImage([down,0])
        lungs2 = interpolation.shift(lungs2, down, 0, mode="nearest")
    elif whichKey == "right":
        right = 1
        #shiftImage([0,right])
        lungs2 = interpolation.shift(lungs2, 0, right, mode="nearest")
        
    elif whichKey == "left":
        left = -1
        #shiftImage([0,left])
        lungs2 = interpolation.shift(lungs2, 0, left, mode="nearest")
    


"""WORKING PROGRESS

I get this error: elif output.shape != shape:  AttributeError: 'int' object has no attribute 'shape'
Not sure how to fix this.
But getting close

"""

img = np.zeros([1000,1000,3],dtype=np.uint8)
img.fill(255)
fig, ax = plt.subplots(1,1)
xlim = [-1000,1000]
ylim = [-1000,1000]
ax.set(xlim=xlim, ylim=ylim)
ax.set_autoscaley_on(False)


#plt.imshow(img, cmap="Greys_r")
plt.imshow(lungs1, cmap="Greys_r")

fig.canvas.mpl_connect('key_press_event', eventHandler) #For some reason not shiftng image
plt.imshow(lungs2, alpha=0.15, cmap="Greys_r")
plt.show()

"""
XVIII

Was not able to complete this due to lack of time and not getting the previouse function to work. 

However should be easy to implement using the rotate function by adjusting the angle on a key event
"""