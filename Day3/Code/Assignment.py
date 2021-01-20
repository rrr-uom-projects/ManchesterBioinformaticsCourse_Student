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
lungImage = imread('lungs.jpg')
ax1.imshow(lungImage)
ax1.title.set_text("Lung")
#Shows lungs on first axes
lungData = np.mean(lungImage, -1)
ax2.hist(lungData[lungData>1].flatten(), bins = 255)
#histogram, needs to be >1 to not count the black background
#because the scale is too large and cant read hist if include black
ax2.title.set_text("Histogram")
plt.show()

test = np.array([1,2,6,4,5,7,89])
print(test[test < 4])
'''Takes two integers, level is the centre
of the range, and window is the width of the range'''
def windowLevel(window, level):
    minRange = level - window
    maxRange = level + window
    '''want to find all values in lungImage that are less than
    the minimum and set them to 0. Then all the values greater than
    max and set those to 254'''
    minValues = lungImage < minRange
    maxValues = lungImage > maxRange
    lungImage[minValues] = 0
    lungImage[maxValues] = 254
    plt.imshow(lungImage)
    plt.show()

"""Trying windowLevel(10,125) shows us that the  second largest peak in the 
histogram is the liver the intercostal muscles, the shoulder and back muscles. The
third largest pea found in the windowLevel(10,60) shows the parts around the kidneys
and liver. The whitest parts is the heart and the lymphs and blood vessels"""
windowLevel(10,60)