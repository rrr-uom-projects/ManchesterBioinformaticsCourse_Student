"""
BIOL68310 Assignment: Image processing in Python

Authors: Katie Williams and Megan Paynton

Work done on Wednesday 20th January 2021
"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 

# Load the file, lungs.jpg
image = imread("lungs.jpg")

# Display the image
plt.imshow(image)
plt.show()

# Plot a histogram of the lungs.jpg image
data = np.mean(io.imread("lungs.jpg"), -1) # read the image and take the mean of the channels
plt.hist(data.flatten(), bins=254) # figure out what 0 represents
plt.show()
plt.hist(data[data > 1].flatten(), bins=254) # why do we need this data > 1



#hist(image.flatten(),bins=255,facecolor="Red",edgecolor="Black")
#plt.show()