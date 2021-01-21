#Assignment part 2 from ed and sophie
#20/01/2021
#This script first shows two images of the same lung side by side,
#once the user closes this window they can then use the arrow keys, enter and
#backspace to manually register a third lung image over the first lung image

import os
import matplotlib.pyplot as plt 
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation
from scipy.ndimage import rotate
#Import modules

cwd = os.getcwd()
#find current working directory
newPath = cwd +"\\Day3\\Code"
#path to folder containing lungs.jpg, this is for windows os, for othe os change to /
os.chdir(newPath)
#read in image of lungs from the new working directory
figSub, (ax1, ax2) = plt.subplots(1,2)
#returns figSUb for figure and ax1 and ax2 are the 2 axes
lungImage = imread('lungs.jpg', as_gray= True)
lungImage2 = imread("lungs2.jpg", as_gray= True)
lungImage3 = imread("lungs3.jpg", as_gray=True)
#Shows both images side by side, can be seen that lung2 is lower and to the right
ax1.imshow(lungImage)
ax1.title.set_text("Lung")

ax2.imshow(lungImage2)
ax2.title.set_text("Lung 2")
plt.show()

figLung2, axLung2 = plt.subplots(1,1)
axLung2.imshow(lungImage, alpha = 0.5)
axLung2.title.set_text("Lung 2 overlaid Lung 1")
#set alpha to 0.5 so we can see both images are transparent and we can see the overlap
#named the axes for lungImage2 so we can move it later on
floating2 = axLung2.imshow(lungImage2, alpha = 0.2)

figLung3, axLung3 = plt.subplots(1,1)
axLung3.imshow(lungImage, alpha = 0.5)
axLung3.title.set_text("Lung 3 overlaid Lung 1")
#set alpha to 0.5 so we can see both images are transparent and we can see the overlap
#named the axes for lungImage3 so we can move the image later on.
floating3 = axLung3.imshow(lungImage3, alpha = 0.2)


def shiftImage(shifts, rotation):
    global lungImage3
    lungImage2 = interpolation.shift(lungImage2, shifts, mode="nearest")
    lungImage2 = rotate(lungImage2, rotation)
    floating2.set_data(lungImage2)
    figLung2.canvas.draw()


def shiftRotateImage(shifts, rotation):
    global lungImage3
    lungImage3 = interpolation.shift(lungImage3, shifts, mode="nearest")
    lungImage3 = rotate(lungImage3, rotation, reshape=False)
    floating3.set_data(lungImage3)
    figLung3.canvas.draw()

#shiftRotateImage([0, -30], -3)
#This now shows the both the lung2 overlaid lung1 and lung 3 overlaid lung1

"""Q14 Moves it down by 10 (because the y axis is flipped), and to the right by 20
Q15 shiftImage([-20, -40]) seems to align both images 
Q16 We have added rotation and -3, [0,-30] is about right.
"""
"""This function takes a user input and alters the image: up, left, right and down translate
the image in that respective direction, enter is a clockwise rotation and backspace is reverse"""
"""Declare down , right and anticlockwise outside of function as zero. The function can then track
the changes its makes, by declaring them within the function as global variables. If not then it
would reset them to 0 every new event"""
d = 0
r = 0
acw = 0
def eventHandler(event):
    whichKey = event.key
    global d
    global r
    global acw
    if whichKey == "up":
        shiftRotateImage([-1,0],0)
        d -= 1
    elif whichKey == "down":
        shiftRotateImage([1,0],0)
        d += 1
    elif whichKey == "right":
        shiftRotateImage([0,1],0)
        r += 1
    elif whichKey == "left":
        shiftRotateImage([0,-1],0)
        r -= 1
    elif whichKey == "enter":
        shiftRotateImage([0,0],-1)
        acw -= 1
    elif whichKey == "backspace":
        shiftRotateImage([-1,0],1)
        acw += 1
    print("You moved {} down, {} right and roated {} anti-clockwise".format(d,r,acw))


figLung3.canvas.mpl_connect("key_press_event", eventHandler)
plt.show()

""" We have managed to manually register lung3 and lung1 but we ran out
of time to allow for lung2 as well. We think it would be the same as lung 3
but play with the figures. We tried but it broke the code."""
