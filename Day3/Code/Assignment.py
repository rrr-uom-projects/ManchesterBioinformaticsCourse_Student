"""
Assignment for Day 3
Image Processing in Python

Katherine Winfield (@kjwinfield) and Yongwon Ju (@yongwonju)

This version written on 20 January 2021
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread

#open the image
image = io.imread("lungs.jpg")
plt.imshow(image) #displays the image using matplotlib
plt.close()

#generate a histogram showing the frequency of different intensities of pixel
image_info = np.mean(image, -1)
plt.hist(image_info[image_info > 1].flatten(), bins=254)
plt.show()