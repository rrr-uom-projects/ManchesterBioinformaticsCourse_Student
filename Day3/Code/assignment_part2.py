#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:09:00 2021

@author: viveckkingsley
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from scipy.ndimage import interpolation
image = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs.jpg"), -1)
plt.imshow(image)
plt.show()
image2 = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs2.jpg"), -1)
plt.show()
image3 = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs3.jpg"), -1)
fig = plt.figure()
ax = fig.add_subplot(111)
floating = ax.imshow(image, cmap="Greys_r") and ax.imshow(image2, cmap="Greys_r", alpha=0.5)
plt.show()

def eventHandler(event):
    """
    This function handles deciphering what the user wants us to do, the event knows which key has been pressed.
    """
    up = 0
    whichKey = event.key
    if whichKey == "up":
        up = 1
    print(up)
    
def shift_image(x, y, r):
    global image2
    global image3
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.imshow(image, cmap="Greys_r", alpha = 1)
    floating = interpolation.shift(image3, (y, x), mode="nearest")
    rotating = interpolation.rotate(floating, r, reshape=False)
#    ax1.imshow(floating, cmap="Greys_r", alpha = 0.5)
    ax1.imshow(rotating, cmap="Greys_r", alpha = 0.5)
    plt.show()
    fig.canvas.mpl_connect('key_press_event', eventHandler)
    plt.show()
    
shift_image(-32,-5.5, -3)


    
    
    



