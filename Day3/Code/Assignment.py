###########################################################
#  Q1. Write some useful information eg.title & names 
#     in some comments at the top of the code
###########################################################
"""
Title = Image processing in Python: assignment 
Date = 1/20/2021 (Day 3)
Names = Jadene Lewis & Long-Ki Chan
Submission Date = 
"""

##### Part 1  ######

###########################################################
#Q2. Import the modules eg. matplotlib.pyplot, numpy and imread from skimage.io
###########################################################

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize


###########################################################
#Q3. Load the file “lungs.jpg” and display it
###########################################################

#  With the path(location where storing the image) declared
image1_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg' 
lung1 = io.imread(image1_name) 
plt.imshow(lung1) # code to show the image 
plt.show()

print(lung1.shape)
# (569, 600, 3)
# 569 = number of pixels in y axis 
# 600 = number of pixels in x axis 
# 3 = it has 3 channels, red blue and green


###########################################################
#Q4. Plot a histogram of the image
###########################################################
data = np.mean(lung1,-1) 
# np.mean = to find a mean for each pixel over the 3 channels
# from print(lung1.shape) --> this image is (569, 600, 3), -1 will take the "3" channels thing

# data[data >1] = to get rid of the black pixels (0,1) (those around the edges)?
plt.hist(data[data >1].flatten(), bins = 254)
plt.show()


###########################################################
#Q5. Write a function that displays the CT image with different lindow levels. 
#    The input variables should be the window and the level.
###########################################################




Comments are not optional
"""
### Name: Jadene Lewis
### Date: 20/01/21
### Title: Image processing in Python: assignment
"""

# Import libraries/modules required:
import numpy as np
import matplotlib.pyplot as plt
import scipy #scipy.signal basically not compatible with Windows. Can't use for signal processing because can't import scipy.signal
from scipy.ndimage import interpolation, rotate #not working
import os
import skimage.io #not working so import matplotlib.image instead
import skimage
from skimage import io
import io 
import matplotlib.image as mpimg 

# Set current working directory 
os.getcwd()
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day3/Code")

##Part 1

#To make images bigger than default size
plt.rcParams['figure.figsize'] = (16.0, 12.0)

##Switch to appropriate directory
os.getcwd()
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day3/Code")
os.getcwd()


#LOAD FILE 'lungs.jpg'
lungs_image = skimage.io.imread("lungs.jpg")
plt.imshow(lungs_image)
#plt.show(plt.imshow(lungs_image)) #what is the difference between plt.imshow() and plt.show()

print(lungs_image)
print(lungs_image.shape) #returns [569, 600, 3]= 569 pixels wide and 600 pixels tall, 3 color channels
lungs_image.shape #returns an array showing how many channels, how many pixels tall and wide
print(lungs_image.dtype) #uint8

#Plot histogram of image
data = np.mean(lungs_image,-1) 
plt.hist(data[data >1].flatten(), bins = 254)
plt.show()



#Function that displays CT image at different window levels        
def window_image(image, window_center, window_width):
    img_min = window_center - window_width // 2
    img_max = window_center + window_width // 2
    window_image = image.copy()
    window_image[window_image < img_min] = img_min
    window_image[window_image > img_max] = img_max
    
    return io.imshow(window_image)

window_image(lungs_image, 350, 700)
    

#Windowing, also known as grey-level mapping, contrast stretching, histogram modification or contrast enhancement is the process in which the CT image greyscale component of an image is manipulated via the CT numbers; doing this will change the appearance of the picture to highlight particular structures. The brightness of the image is adjusted via the window level. The contrast is adjusted via the window width.
#Window of lungs_image
print(np.min(lung_im), np.max(lung_im)) #0.0, 1.0
plt.imshow(lung_im, cmap="Greys_r", vmin=0.0, vmax=1.0) #
plt.show()

##Identify which parts of the histogram relate to which parts of the image. 
#Record info as comments in your code:
    #Parts of the histogram with higher peaks refer to those less dense regions such as soft tissue (as there is less X-ray attenuation). 
    #Parts of histogram with lower peaks refer to those increased density regions such as bone as there is higher X-ray attenuation

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:17:41 2021

@author: jaden
"""
### Name: Jadene Lewis
### Date: 20/01/21
### Title: Image Processing in Python

# Part 2 #
import numpy as np
import skimage.io
import scipy.signal
import matplotlib.pyplot as plt
from scipy.ndimage import interpolation, rotate

# Load and display images 'lungs.jpg' and 'lung2.jpg'
lungs2_image = skimage.io.imread("lungs.jpg", as_gray=True)
plt.imshow(lungs2_image)

lungs_image = skimage.io.imread("lungs.jpg", as_gray=True)
plt.imshow(lungs_image)

# Make a plot where you can see both images on the same plot using transparency
floating_image = skimage.io.imread("lungs2.jpg", as_gray=True) #moving image
background_image = skimage.io.imread("lungs.jpg", as_gray=True) #fixed image

fig = plt.figure()
plt.title('Lung 1 and Lung 2 overlayed')
ax = fig.add_subplot(111)
background = ax.imshow(background_image, cmap="Greys_r") #puts 'lungs.jpg' in background
floating = ax.imshow(floating_image, alpha=0.5, cmap="Greys_r") #puts 'lungs2.jpg' in front and alpha=0.5 makes for partial transparency. increase or decrease alpha value to make front image less or more see through, respectively
#plt.imshow(interpolation.shift(floating_image, (10, 20, 0))) #Because RGB image so has three dimensions and thus shifting parameter requires 3 values
plt.show()

help(plt.imshow)
help(interpolation.shift)
plt.show()
#M = np.float32([[1, 0, 50],
#                [0, 1, 50])
##
## apply a perspective transformation to the image
#translated_img = cv2.warpPerspective(img, M, (cols, rows))
## disable x & y axis
#plt.axis('off')
## show the resulting image
#plt.imshow(translated_img)
#plt.show()

##Write a function that would shift floating image
def shiftImage(x, y):
    global floating_image
    #global background
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.imshow(background)
    #plt.imshow(background_image,)
    #fig, ax = plt.subplots()
    floating_image = interpolation.shift(floating_image, (y, x), mode = "nearest")
    floating.set_data(floating_image)
    fig.canvas.draw() #draws update to canvas
    #return plt.imshow(floating_image)
    #plt.show()
    #image not showing?
    #return floating_image
    #return plt.show(floating_image)

shiftImage(10, 20)


