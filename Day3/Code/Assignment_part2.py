"""
BIOL68310 Assignment: Image processing in Python - Part 2

Aim of this part is write functions which can shift and rotate an image to match a fixed image

Authors: Katie Williams and Megan Paynton

Work done on Wednesday 20th January 2021
"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate

# Load the file, lungs.jpg and Lungs2.jpg
lungs = imread("lungs.jpg", as_gray=True) # load the file with as_gray = T loads the file in 2 dimentions (black and white - grey scale)
lungs2 = imread("lungs2.jpg", as_gray=True)

# Display the images
plt.imshow(lungs, cmap="Greys_r")
plt.show()

plt.imshow(lungs2, cmap="Greys_r")
plt.show()

# Display lung and lungs2 on the same plot with Lungs2 with transparency
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5) # alpha adds tranparency to the images
ax.imshow(lungs2, cmap="Greys_r", alpha=0.5)
plt.show()

# start a figure
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5)

# Specify a name for the moving image (lungs2)
floating = ax.imshow(lungs2, alpha=0.5, cmap="Greys_r")

# Write a function to shift lungs2 a specified number or vertical and horizontal pixels (e.g. 10 vertical shifts and 20 horizontal shifts)
def shiftImage(shifts):
    global lungs2 # global allows you to edit lungs2 inside and outside the function
    global floating
    shifted_image = interpolation.shift(lungs2, shifts) # interpolation allows you to shift the specified image 
    floating.set_data(shifted_image)
    fig.canvas.draw()

shiftImage([10,20]) # to align shifts required are -14, -38
plt.show()



#modify the function to rotate lungs 3 a specified number of degrees 
lungs3 = imread("lungs3.jpg", as_gray=True) #load the file lungs3 in 2 dimentions
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5) # plot the two images with transparency
ax.imshow(lungs3, cmap="Greys_r", alpha=0.5)
plt.show() #view the two plots on the same axis

# start a figure
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greys_r", alpha=0.5)

# Specify a name for the moving image (lungs2)
floating = ax.imshow(lungs3, alpha=0.5, cmap="Greys_r")

# Write a function to shift and rotate the floating image a specified number of shifts and degrees
def transformImage(shifts, rotates):
    global lungs3
    global floating
    shifted_image = interpolation.shift(lungs3, shifts) # interpolation shifts the specified image
    transformed_image = rotate(shifted_image, rotates, reshape=False) # rotate rotates the shifted image a specific number of degrees, reshape stops the image being increased or decreased in size
    floating.set_data(transformed_image)
    fig.canvas.draw()

transformImage([-12,-20], -2) # to align shifts and degrees required are -14, -38, -2
plt.show()

# Create a new figure
fig, ax = plt.subplots()
fixed = ax.imshow(lungs, cmap="Greys_r", alpha=0.5)
floating = ax.imshow(lungs2, alpha=0.5, cmap="Purples_r")

# Function to shift floating image with keyboard presses
def eventHandler(event):
    global floating
    global lungs2
    global fig
    up = 0
    down = 0
    left = 0
    right = 0
    if event.key == "up":
        h0 = 0
        up = h0 + 1
        print(up)
    elif event.key == "down":
        h0 = 0
        down = h0 - 1
        print(down)
    elif event.key == "right":
        w0 = 0
        right = w0 + 1
        print(right)
    elif event.key == "left":
        w0 = 0
        left = w0 - 1
        print(left)
    shiftImage([down, right])
    
    floating.figure.canvas.draw()# update the plot window

fig.canvas.mpl_connect("key_press_event", eventHandler) # call the key press event to the figure
plt.show()

# This current code only allows us to move the image up/down/left/right once, to improve the code we need to ensure that h0 and w0 allows us to continually press keyboard keys to keep moving the image. 

