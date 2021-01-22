"""
Authors: Katie Williams and Megan Paynton

Work done: Wednesday 20th January 2021

BIOL68310 Assignment: Image processing in Python - Part 2

Aim: Write functions which can shift and rotate an image to match a fixed image

"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate

# Load the file, lungs.jpg and Lungs2.jpg
lungs = imread("lungs.jpg", as_gray=True) # load the file with as_gray = T loads the file in 2 dimentions (black and white - grey scale)
lungs2 = imread("lungs2.jpg", as_gray=True)

# Display the images, individually
plt.imshow(lungs, cmap="Greys_r")
plt.title("Display of lungs.jpg")
plt.show()

plt.imshow(lungs2, cmap="Greys_r")
plt.title("Display of lungs2.jpg")
plt.show()

# Display lung and lungs2 on the same plot with Lungs2 with transparency
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greens_r", alpha=0.5) # alpha adds tranparency to the images
ax.imshow(lungs2, cmap="Purples_r", alpha=0.5)
plt.title("Both CT scans, on the same Axes")
plt.show()

# Start a figure, and plot the first 'fixed' (lungs) image on this
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greens_r", alpha=0.5)

# Specify a name for the moving image (lungs2)
# And set this image up on the same axes so it plots ontop of the other image
floating = ax.imshow(lungs2, alpha=0.5, cmap="Purples_r")



####### Write a function to shift lungs2 a specified number or vertical and horizontal pixels #######

# Function, shiftImage()
# The input is a list, where the first element is the number of pixels the image should move in the downwards direction,
# and the second element is the number of pixels the image should move in the right direction. 
# negative values in the input will shift the image in the opposite direction (i.e. left and up)
def shiftImage(shifts):
    global lungs2 # global allows you to access the lungs2 variable/image inside the function
    global floating
    shifted_image = interpolation.shift(lungs2, shifts) # interpolation allows you to shift the specified image 
    floating.set_data(shifted_image)
    fig.canvas.draw()

# As an example use of the function shiftImage, this input whould shift the image down 10 pixels and to the right 20 pixels
shiftImage([10,20]) 
plt.title("Shifted Images, by [10,20]")
plt.show()

# To align the images, the shifts required are [-14, -38]
# This code plots this shift
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greens_r", alpha=0.5)
floating = ax.imshow(lungs2, alpha=0.5, cmap="Purples_r")
shiftImage([-14,-38]) 
plt.title("Aligned Images, shifted by [-14,-38]")
plt.show()


####### Modify the function to rotate lungs 3 a specified number of degrees #######

# Load the file lungs3.jpg, using as_gray=TRUE to reduce the number of channels to 1
lungs3 = imread("lungs3.jpg", as_gray=True) 
fig, ax = plt.subplots()

# Plot the two images, lungs.jpg and lung3.jpg, with transparency, where the Green scan is the 'fixed' image (lungs.jpg)
ax.imshow(lungs, cmap="Greens_r", alpha=0.5) 
ax.imshow(lungs3, cmap="Purples_r", alpha=0.5)
plt.title("Both CT scans, on the same Axes")
plt.show() #view the two plots on the same axis

# Start a figure
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greens_r", alpha=0.5)

# Specify a name for the moving image (lungs2)
floating = ax.imshow(lungs3, alpha=0.5, cmap="Purples_r")


####### Write a function to shift and rotate the floating image a specified number of shifts and degrees #######

# Two input arguments, the required shifts (defined by a list, as before) 
# and the number of degrees to shift the image clockwise (if a positive number is given), 
def transformImage(shifts, rotates):
    global lungs3
    global floating
    shifted_image = interpolation.shift(lungs3, shifts) # interpolation shifts the specified image
    transformed_image = rotate(shifted_image, rotates, reshape=False) # rotate function rotates the shifted image a specific number of degrees, reshape=False stops the image being increased or decreased in size
    floating.set_data(transformed_image)
    fig.canvas.draw()

# As an example use of the function transformImage, this input whould shift the image up 12 pixels and to the left 20 pixels
# and rotate the image 2 degrees anticlockwise
transformImage([-12,-20], 20) 
plt.title("Transformed image, shifted [-12, -20], rotated 20 degrees CW")
plt.show()

# To align the images, the shifts required are [-14, -38] and 2 degrees ACW
# This code plots this aligned transformation
fig, ax = plt.subplots()
ax.imshow(lungs, cmap="Greens_r", alpha=0.5)
floating = ax.imshow(lungs3, alpha=0.5, cmap="Purples_r")
transformImage([-14,-38], -2) 
plt.title("Aligned Images, shifted by [-14,-38], rotated 2 degrees ACW")
plt.show()


####### Write code to allow the image to be shifted using the arrow keys on the keyboard #######

# Create a new figure
fig, ax = plt.subplots()
fixed = ax.imshow(lungs, cmap="Greens_r", alpha=0.5)
floating = ax.imshow(lungs2, alpha=0.5, cmap="Purples_r")

h0 = 0
w0 = 0
# Function to shift floating image with keyboard presses
def eventHandler(event):
    #global floating
    #global lungs2
    #global fig
    up = 0
    down = 0
    left = 0
    right = 0
    if event.key == "up":
        up += 1
        print("up")
    elif event.key == "down":
        down += 1
        print("down")
    elif event.key == "right":
        right += 1
        print("right")
    elif event.key == "left":
        left += 1
        print("left")
    #h0 = h0 + down - up
    #w0 = w0 + right - left
    #shiftImage([h0 + down - up, w0 + right - left])
    shiftImage([down - up, right - left])

    
#floating.figure.canvas.draw()# update the plot window

fig.canvas.mpl_connect("key_press_event", eventHandler) # call the key press event to the figure
plt.title("Shift the Image to align using the arrow keys")
plt.show()

# This current code only allows us to move the image up/down/left/right once, to improve the code we need to ensure that h0 and w0 allows us to continually press keyboard keys to keep moving the image. 
# I think there may be issues with the function reseting values each time
# each time the image switches between moving up and down, to left and right the centre reset
# I think this is to do with the setting of the variables down=0 and right=0 at the start of the function, but I need something to define them first

