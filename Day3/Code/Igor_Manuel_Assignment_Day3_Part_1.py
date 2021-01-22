#!/usr/bin/env python
# coding: utf-8 



# Part 1
""" I. Write some useful information like a title and your names in some comments at the top of
the code.
"""
### Image processing in Python: assignment ###

           ## By Igor and Manuel ##

"""
II. Import the modules you will need, these include matplotlib.pyplot, numpy and
imread from skimage.io
""" 
# Next lines import the modules we need.
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from scipy.ndimage import interpolation



""" III Load the file “CT.jpg” and display it"""

# Let's load the file
# According teacher instructions we must use lung.jpg instead of CT.jpg
# Next line load the picture of the specific directory where the picture is.
part1 = io.imread("/Users/monkiky/Desktop/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg")
# part1 is a numpy.ndarray 
# To display this array as picture we can use next line:
# This is done according the values of the array stored in part1.
plt.imshow(part1)



""" IV Plot a histogram of the image"""

ax.imshow(part1)
# .flatten, collapsed the array into one dimension.
# Bins to define the number of columns in the histogram
# I think 400 is ok to appreciate the differences
plt.hist(part1[part1>1].flatten(),bins=400)
# This array contains very small and very large values, 
# it makes it very difficult to create a nice histogram with such different values. 
# We are going to select only the values that are greater than 1
# For that reason I have written "part1[part1>1]"

# Now we can plot the hist with the features we have specified
plt.show()


"""
V. Write a function that displays the CT image with different lindow levels. The input variables
should be the window and the level.

"""
# Let's load the image lung again but this time, we are going to convert color images to gray-scale 
# We can do this with as_gray=True

part1 = io.imread("/Users/monkiky/Desktop/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg", as_gray=True)

def displayImageWinLevel(image, window, level):
   plt.imshow(image,cmap="Greys_r", vmin=window, vmax=level)
   plt.show()
#Min value for window and level is 0 and maximum is 1
displayImageWinLevel(image=part1, window=0.2, level=1)

"""
VI. Identify which parts of the histogram relate to which parts of the image. Record this
information in some comments in your code.
"""

"""
The histogram shows two maximum peaks at the beginning and at the end with respect to the X axis. And two minor peaks in the center that look like hills.

The peak at the beginning and at the end refers to both sides of the image where all the pixels are black.

The hills with maximum values between 2000 and 3000 respectively represent the part of the image where the lungs are.

The areas of the histogram where the values are the lowest represent the areas of the image where there are more white pixels.
""""""


