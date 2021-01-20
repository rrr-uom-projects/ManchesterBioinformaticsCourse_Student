"""
BIOL68310 Assignment: Image processing in Python - Part 1

Aim of this part is to display the image, plot a histogram and create a function to display the CT image with different window levels

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
data = np.mean(imread("lungs.jpg"), -1) # read the image and take the mean of the channels
#plt.hist(data.flatten(), bins=254) # 0 represents black colour including border around lungs
plt.hist(data[data > 1].flatten(), bins=254) # include data > 1 to remove high number of black (0's)
plt.show()

# write a function to display the CT image with different window levels
print(np.min(data), np.max(data)) # min = 0, max = 255

def CTwindow(window, level):
    vmin_value = level-(window/2) 
    vmax_value = level+(window/2)
    plt.imshow(data, cmap="Greys_r", vmin=vmin_value, vmax=vmax_value)
    plt.show()
    
CTwindow(50, 25) # air
CTwindow(40, 50) # tissue, fat
CTwindow(25, 112) # soft tissue - kidneys, heart 
CTwindow(50, 200) # showing bone and heart?
