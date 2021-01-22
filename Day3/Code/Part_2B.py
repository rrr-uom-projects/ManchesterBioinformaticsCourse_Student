
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
# path of the executing script 
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

"""
X. Load the images “lings.jpg” and “lungs2.jpg”
"""

#name of image
img_name1 = '/lungs.jpg'
img_name2 = '/lungs2.jpg'
#path to the image
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2

#import images using imread as a grey scale of values between 0 and 1
lungs1 = io.imread(img_path1, as_gray=True)
lungs2 = io.imread(img_path2, as_gray=True)


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
plt.imshow(lungs2, alpha=0.25)
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
shiftImage([10,20])





