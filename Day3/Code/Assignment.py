"""
Authors: Katie Williams and Megan Paynton

Date: Wednesday 20th January 2021

BIOL68310 Assignment: Image processing in Python - Part 1

Aim: Display the image, plot a histogram and create a function to display the CT image with different window levels

"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 

# Load the file, lungs.jpg
image = imread("lungs.jpg")

# Display the image
plt.imshow(image)
plt.title("CT Image of the Lungs")
plt.show()

# Plot a histogram of the lungs.jpg image
data = np.mean(imread("lungs.jpg"), -1) # read the image and take the mean of the channels
#plt.hist(data.flatten(), bins=254) # 0 represents black colour including border around lungs
plt.hist(data[data > 1].flatten(), bins=254) # include data > 1 to remove high number of black (0's)
plt.title("Histogram plot of the CT Lungs scan")
plt.xlabel("Pixel density value")
plt.ylabel("Frequency")
plt.show()

# Determine the min and max values of the 'mean' pixel density values
print(np.min(data), np.max(data)) 
# Output: min = 0, max = 255

# Write a function to display the CT image with different window levels
def CTwindow(window, level):
    vmin_value = level-(window/2) # get minimum value by taking away half the window from the level
    vmax_value = level+(window/2) # get maximum value by adding half the window to the level
    plt.imshow(data, cmap="Greys_r", vmin=vmin_value, vmax=vmax_value) # plot the pixels with intensity levels in the window
    plt.title("Display of the CT image, with Window = %d and Level = %d" % (window, level)) # Add a title inc window and level values
    plt.show()

# Demonstration of differnet windows/levels displaying different features of the CT scan
CTwindow(50, 25) # This window shows air
CTwindow(40, 50) # This window shows tissue and fat
CTwindow(25, 112) # This window shows soft tissue (can see specificially the kidneys and the heart)
CTwindow(50, 200) # This window shows bone
