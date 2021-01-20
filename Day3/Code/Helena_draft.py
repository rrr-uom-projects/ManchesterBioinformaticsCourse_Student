#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:37:52 2021

@author: robinson
"""
#import required modules
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread #Is this line correct?
from PIL import Image

#load image
image = imread('lungs.jpg')
print(f"image = {image}")

#display image using function from pillow module
img = Image.open('lungs.jpg')
img.show()

#plot a histogram of the image
histogram, bin_edges = np.histogram(image, bins=256, range=(0,1))
