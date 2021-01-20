"""
BIOL68310 Assignment: Image processing in Python - Part 2

Aim of this part is to...............

Authors: Katie Williams and Megan Paynton

Work done on Wednesday 20th January 2021
"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate

# Load the file, lungs.jpg and Lungs2.jpg
lungs = imread("lungs.jpg", as_gray=True)
lungs2 = imread("lungs2.jpg", as_gray=True)

# Display the images
plt.imshow(lungs, cmap="Greys_r")
plt.show()

plt.imshow(lungs2, cmap="Greys_r")
plt.show()

# Display lung and lungs2 on the same plot with Lungs2 transparent
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5)
ax.imshow(lungs2, cmap="Greys_r", alpha=0.5)
plt.show()

fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5)

# Specify a name for the moving image (lungs2)
floating = ax.imshow(lungs2, alpha=0.5, cmap="Greys_r")

# Write a function to shift lungs2 a specified number or vertical and horizontal pixels (e.g. 10 vertical shifts and 20 horizontal shifts)
def shiftImage(shifts):
    global lungs2
    global floating
    shifted_image = interpolation.shift(lungs2, shifts)
    floating.set_data(shifted_image)
    fig.canvas.draw()

shiftImage([10,20]) # to align shifts required are -14, -38
plt.show()



#modify the function to rotate lungs 3 a specified number of degrees 
lungs3 = imread("lungs3.jpg", as_gray=True) #load the file lungs3
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5)
ax.imshow(lungs3, cmap="Greys_r", alpha=0.5)
plt.show() #view the two plots on the same axis

fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5)

# Specify a name for the moving image (lungs2)
floating = ax.imshow(lungs3, alpha=0.5, cmap="Greys_r")

# Write a function to shift lungs2 a specified number or vertical and horizontal pixels (e.g. 10 vertical shifts and 20 horizontal shifts)
def transformImage(shifts, rotates):
    global lungs3
    global floating
    shifted_image = interpolation.shift(lungs3, shifts)
    transformed_image = rotate(shifted_image, rotates, reshape=False)
    floating.set_data(transformed_image)
    fig.canvas.draw()

transformImage([-12,-20], -2) # to align shifts required are -14, -38
plt.show()

#shift floating image with keyboard presses
#fig, ax = plt.subplots()
#fixed = ax.imshow(lungs, cmap="Greys_r", alpha=0.5)
#floating = ax.imshow(lungs2, alpha=0.5, cmap="Purples_r")
#global fig


def eventHandler(event):
    up = 0
    down = 0
    left = 0
    right = 0
    whichKey = event.key
    if whichKey == "up":
        up = -1
        print(up)
    if whichKey == "down":
        down = 1
        print(down)
    if whichKey == "right":
        right = 1
        print(right)
    if whichKey == "left":
        left = -1
        print(left)
    shiftImage([down, right])
    global floating
    global lungs2
    global fig
    
fig, ax = plt.subplots()
fixed = ax.imshow(lungs, cmap="Greys_r", alpha=0.5)
floating = ax.imshow(lungs2, alpha=0.5, cmap="Purples_r")
fig.canvas.mpl_connect("key_press_event", eventHandler)
plt.show()

#only allows us to move 1 

