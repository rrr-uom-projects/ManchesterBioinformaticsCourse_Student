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
image = np.mean(imread("lungs.jpg"), -1)
#image = imread('lungs.jpg', as_gray=True)
print(f"image = {image}")
plt.hist(data[data >1].flatten(), bins 254)
#display image using function from pillow module
#img = Image.open('lungs.jpg')
#img.show()

#plt.hist(image.flatten(), bins=256, range=(0, 1))
#bins=256, range=(0, 1)


#create a histogram of the image - gives a 1d array of number of pixels of
#each possible gray value
"""
histogram, bin_edges = np.histogram(image, bins=256, range=(0,1))



plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()

print("Done")