"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
#import modules
cwd = os.getcwd()
#find current working directory
newPath = cwd +"\\Day3\\Code"
#path to folder containing lungs.jpg, this is for windows os, for othe os change to /
os.chdir(newPath)
#read in image of lungs from the new working directory

f, (ax1, ax2) = plt.subplots(2,1)
#returns f for figure and ax1 and ax2 are the 2 axes
lungImage = np.mean(imread('lungs.jpg'), -1)

ax1.imshow(lungImage)
ax1.title.set_text("Lung")
#Shows lungs on first axes
#Convert image data into greys represented 0-255
lungData = lungImage.flatten()
ax2.hist(lungData[lungData>1], bins = 255)
#histogram, needs to be >1 to not count the black background
#because the scale is too large and cant read hist if include black
ax2.title.set_text("Histogram")
plt.show()


'''Takes two integers, level is the centre
of the range, and window is the width of the range'''
def windowLevel(window, level):
    minRange = level - (window/2)
    maxRange = level + (window/2)
    '''want to find all values in lungImage that are less than
    the minimum and set them to 0. Then all the values greater than
    max and set those to 254'''
    #minValues = lungImage < minRange
    #maxValues = lungImage > maxRange
    #lungImage[minValues] = 0
    #lungImage[maxValues] = 254
    plt.imshow(lungImage, vmin = minRange, vmax= maxRange)
    plt.show()
    """vmin is used to for the min of the window and vmax is the max of the window and then this
    calculates the intensity of those in the range. Those above vmax are set to 255 and those below
    vmin are set to 0"""

"""Trying windowLevel(10,125) shows us that the  second largest peak in the 
histogram is the liver the intercostal muscles, the shoulder and back muscles. The
third largest pea found in the windowLevel(10,60) shows the parts around the kidneys
and liver. The whitest parts is the heart and the lymphs and blood vessels"""
windowLevel(10,60)