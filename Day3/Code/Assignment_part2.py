#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:02:32 2021

@author: robinson
"""
"""We are Nermeen and Helena group. This is the first part of Day3 tasks. For this task, we need to load lungs.jpg image and plot 

a histogram image. This allows us to identify the distribution of the values of the lungs.jpg image."""

import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
from skimage import io #this is used for image processing
from scipy.ndimage import interpolation

lungs1 = np.mean(io.imread("lungs.jpg"), -1)
lungs2 = np.mean(io.imread("lungs2.jpg"), -1)


plt.imshow(lungs1, cmap="Greys_r")
plt.show()

plt.imshow(lungs2)
plt.show()


#plt.imshow(lungs1, cmap="Greys_r")
#plt.imshow(lungs2, alpha=0.5, cmap="Greys_r")
#plt.show()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(lungs1, cmap="Greys_r")
floating = ax.imshow(lungs2, alpha=0.5, cmap="Reds_r")
lungs2 = interpolation.shift(lungs2, (60, -300), mode="nearest")
floating.set_data(lungs2)

plt.show()

