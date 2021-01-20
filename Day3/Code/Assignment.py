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





<<<<<<< HEAD
Comments are not optional
"""
### Name: Jadene Lewis
### Date: 20/01/21
### Title: Image processing in Python: assignment

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

##Load file "lungs.jpg"
    #lungs_image = ("lungs.jpg")
lungs_image = plt.imshow(mpimg.imread("lungs.jpg"))
plt.show() #what is the difference between plt.imshow() and plt.show()

print(lungs_image)
print(lungs_image.shape)
lungs_image.shape #returns an array showing how many channels, how many pixels tall and wide
print(lungs_image.dtype)

#Plot histogram of the image.
#Histogram of an image is a graphical representation of the amount of pixels of each intensity value (from 0 [black] to 255 [white])
plt.title("Histogram for Image")
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
plt.hist(x)#hist function is used to plot the histogram of an image.
plt.show()

#Plot of original image
lungs_im = mpimg.imread("lungs.jpg") #image slicing into 2D
fig= plt.figure() 
x =lungs_im[:,:,0] # x-coordinate denotation
plt.xlabel("Value") # y coorindate denotation
plt.ylabel("Pixels Frequency") # title of an image
plt.title("Original Image") # imshow function with comparison of gray value
plt.imshow(x, cmap="gray") # plot the image on a plane
plt.show()

ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax.imshow(lungs_im, interpolation = "none", cmap="Greys_r", vmin = 0.5, vmax = 0.8)
ax2(lungs_im.flatten(), bins=255, facecolor="Red",edgecolor="Black")
plt.show()

#Histogram
vals = lungs_im.mean(axis=2).flatten() #calculate mean value from RGB channel
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()

#test
blue = lungs_im[:, :, 2]
plt.hist(blue.ravel(), bins=255)
plt.title('Blue Histogram')
plt.show()

ax = plt.hist(lungs_im.ravel(), bins=10)
plt.show()
=======
from scipy.ndimage import interpolation, rotate
>>>>>>> fae673135ad296e431f3479d3f48b96ce333f838
