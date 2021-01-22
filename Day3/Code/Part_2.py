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


# Let’s import needed modules with the next lines of code.
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation, rotate



# path of the executing script
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

"""
 Load the images “lings.jpg” and “lungs2.jpg”
"""

#name of image
img_name1 = '/lungs.jpg'
img_name2 = '/lungs2.jpg'
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2

#import images using imread as a grey scale of values between 0 and 1
lungs1 = io.imread(img_path1, as_gray=True)
lungs2 = io.imread(img_path2, as_gray=True)
# To increase the size of the pictures
plt.rcParams['figure.figsize'] = (16.0, 12.0)

"""
XI. Display the images
"""

fig = plt.figure()

ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.imshow(lung1)
ax2.imshow(lung2)

plt.show()

plt.imshow(lung1)
plt.imshow(lung2, alpha=0.25)
plt.show()


# path of the executing script
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

#name of image
img_name1 = '/lungs.jpg'
img_name2 = '/lungs2.jpg'
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2

lungs1 = io.imread(img_path1, as_gray=True)

lungs2 = io.imread(img_path2, as_gray=True)

#plt.imshow(lungs2,cmap="Greys_r")
shifted_image = interpolation.shift(lungs2, (-15, -40), mode="nearest")
plt.imshow(lung, cmap="Greys_r")
plt.imshow(shifted_image, alpha=0.15, cmap="Greys_r")
plt.show()


im = io.imread("/Users/monkiky/Desktop/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs2.jpg", as_gray=True)
plt.imshow(im,cmap="Greys_r")
plt.show()

shifted_image = interpolation.shift(im, (60, -30), mode="nearest")

plt.imshow(shifted_image,cmap="Greys_r")
plt.show()
