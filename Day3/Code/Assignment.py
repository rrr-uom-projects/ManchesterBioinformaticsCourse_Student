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

