"""
This is Assignment 1 by Nicola Compton and Catherine Borland
The programme loads a CT image of the lungs, displays it as a histogram and defines a level, window function
"""

# import modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io 
from skimage.io import imread

# load image
# it is in the same directory as we are currently working in so we do not need to specify the path
image = io.imread("lungs.jpg")

# display image
plt.imshow(image)
plt.show()

# plot a histogram of the image
# first we need to take a mean so there is one value for each pixel
data=np.mean(image,-1)
# we need to flatten the image to make sure only one histogram is produced
# the number of bins has been set to 254 because it is a CT image
# values less than 1 have been removed as these correspond to the black background around the image
plt.hist(data[data>1].flatten(),bins=254)
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.show()

# this function displays the CT image at different window levels
# the input variables are window, level and image
def CT(window,level,image):

    # display the image, setting vmin and vmax appropriately for the given level and window
    # all pixel values less than vmin will be set to the minimum, all greater than vmax are set to the maximum
    # the colour map is set to grey because the scan is a black and white image
    plt.imshow(image,cmap="Greys_r",vmin=level-(0.5*window),vmax=level+(0.5*window))
    plt.show()

# Identify which parts of the histogram correspond to which parts of the image
# Black is 0
# White is 255
# Using the following level and window functions on the image, we concluded that the first peak in the histogram, around 0, is air;
# The second peak around 56, is muscle;
# The third peak around 115, are the organs- liver and kidneys;
# The final peak near 255, are the bones
CT(4,2,data) # First peak
CT(20,56,data) # Second peak 
CT(40,115,data) # Third peak 
CT(4,253,data) # Final peak 
    