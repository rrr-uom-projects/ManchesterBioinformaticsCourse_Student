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
#plt.show()
plt.close()

#generate a histogram showing the frequency of different intensities of pixel
image_info = np.mean(image, -1)
plt.hist(image_info[image_info > 1].flatten(), bins=254)
plt.ylabel("Frequency")
plt.xlabel("Light intensity")
plt.show()
plt.close()
'''
what does the histogram show?
a light intensity of 0 is black, so less dense objects such as the air in the lungs and the air
outside the patient's body appear black.
all the tissue appears at an intensity of 50
the muscles and organs are more dense, so appear grey.
the bones appear almost white and are close to 254
'''

def image_manipulator(window, level):
    plt.imshow(image_info, interpolation='none', cmap="Greys_r",  vmin=(level-(0.5*window)), vmax=(level+ (0.5*window)))
    plt.show()


image_manipulator(40, 110)