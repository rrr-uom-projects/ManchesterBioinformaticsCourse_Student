"""
Assignment for Day 3
Image Processing in Python

Katherine Winfield (@kjwinfield) and Yongwon Ju (@ )

This version written on 20 January 2021
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread

#open the image
image = io.imread("lungs.jpg")
plt.imshow(image)
plt.show()