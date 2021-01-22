"""
Authors: Katie Williams and Megan Paynton

Work done: Thursday 21st January 2021

BIOL68310 Assignment: Image processing in Python - Day 2, Part 2

Aim: Register all four lung images and use a key press event to select an area of interest around the tumour to compare tumour regression across the four images.

"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom
import os 
import matplotlib.patches as patches

# Load the images “IMG-0004-00001.dcm” and “IMG-0004-00002.dcm”. get the pixel data
img1_dcm = pydicom.read_file("IMG-0004-00001.dcm")
img2_dcm = pydicom.read_file("IMG-0004-00002.dcm")
img3_dcm = pydicom.read_file("IMG-0004-00003.dcm")
img4_dcm = pydicom.read_file("IMG-0004-00004.dcm")

# Convert dicom file to a numpy array using img_array = img_dcm.pixel_array
img1_array = img1_dcm.pixel_array 
img2_array = img2_dcm.pixel_array
img3_array = img3_dcm.pixel_array 
img4_array = img4_dcm.pixel_array

# Function to shift specified image a specified number of shifts 
def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts)
    return shifted_image

# load the registrations array (from part 1)
registrations = np.load("registrations.npy")
floating_list = [img2_array, img3_array, img4_array]

# loop over floating images (and shiftImage function) to produce registered images) 
shifted_images = []
for i, floating in enumerate(floating_list):
    print(i)
    registered_images = shiftImage(registrations[i], floating)
    shifted_images.append(registered_images)

# plot the four registered images to ensure they are registere correctly
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4) # plot in a row for comparison
ax1.imshow(img1_array, alpha=0.5, cmap="Greys_r") # plot with transparency
ax2.imshow(shifted_images[0], alpha=0.5, cmap="Greys_r")
ax3.imshow(shifted_images[1], alpha=0.5, cmap="Greys_r")
ax4.imshow(shifted_images[2], alpha=0.5, cmap="Greys_r")
plt.show()

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(img1_array, cmap="Greys_r") # Display the fixed image


# Start with a box drawn in the centre of the fixed image
origin = (img1_array.shape[0]/2, img1_array.shape[1]/2)
rectParams = [origin[0], origin[1], 10, 10]

# Draw a rectangle in the image

global rect
rect = patches.Rectangle((rectParams[1], rectParams[0]),rectParams[2], rectParams[3],linewidth=1, edgecolor='r',facecolor='none')

ax.add_patch(rect)

# Event handlers for the clipbox
global initPos
initPos = None


# Function which allows you to click on the box
def onPress(event):
    """
    This function is called when you press a mouse button inside the figure window
    """
    global rect
    if event.inaxes == None:
        return# Ignore clicks outside the axes
    contains, attr = rect.contains(event)
    if not contains:
        return# Ignore clicks outside the rectangle

    global initPos # Grab the global variable to update it
    initPos = [rect.get_x(), rect.get_y(), event.xdata, event.ydata]

# Function which allows you to drag and move the box on a mouse click
def onMove(event):
    """
    This function is called when you move the mouse inside the figure window
    """
    global initPos
    global rect
    if initPos is None:
        return# If you haven't clicked recently, we ignore the event

    if event.inaxes == None:
        return# ignore movement outside the axes

    x = initPos[2]
    y = initPos[3]
    dx = event.xdata - initPos[2]
    dy = event.ydata - initPos[3]
                                    # This code does the actual move of the rectangle
    rect.set_x(initPos[0] + dx)
    rect.set_y(initPos[1] + dy)

    rect.figure.canvas.draw()

# Function which releases the box when mouse click is released
def onRelease(event):
    """
    This function is called whenever a mouse button is released inside the figure window
    """
    global initPos
    initPos = None # Reset the position ready for next click

# Function which allows you to change the size and shape of the box with keyboard presses.
def keyboardInterface(event):
    """
    This function handles the keyboard interface. It is used to change the size of the
    rectangle.
    """
    global rect
    if event.key == "right":
        # Make the rectangle wider
        w0 = rect.get_width()
        rect.set_width(w0 + 1)
    elif event.key == "left":
        # Make the rectangle narrower
        w0 = rect.get_width()
        rect.set_width(w0 - 1)
    elif event.key == "up":
        # Make the rectangle shorter
        h0 = rect.get_height()
        rect.set_height(h0 - 1)
    elif event.key == "down":
        # Make the rectangle taller
        h0 = rect.get_height()
        rect.set_height(h0 + 1)
    elif event.key == "ctrl+right":
        # Make the rectangle wider - faster
        w0 = rect.get_width()
        rect.set_width(w0 + 10)
    elif event.key == "ctrl+left":
        # Make the rectangle narrower - faster
        w0 = rect.get_width()
        rect.set_width(w0 - 10)
    elif event.key == "ctrl+up":
        # Make the rectangle shorter - faster
        h0 = rect.get_height()
        rect.set_height(h0 - 10)
    elif event.key == "ctrl+down":
        # Make the rectangle taller - faster
        h0 = rect.get_height()
        rect.set_height(h0 + 10)

    rect.figure.canvas.draw()# update the plot window

# plot the fixed image with the rectangle for user to select an area of interest around the tumour
cid1 = fig2.canvas.mpl_connect('button_press_event', onPress)
cid2 = fig2.canvas.mpl_connect('motion_notify_event', onMove)
cid3 = fig2.canvas.mpl_connect('button_release_event', onRelease)
cid4 = fig2.canvas.mpl_connect('key_press_event', keyboardInterface)

plt.show()

# Identify the indices based off the box of interest you select 
indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
#print(indices) # print indices to view the box of interest, our box of interest is 37, 87, 291, 337 

# NB that for the sake of consistency, we have overriden the Indices output with the result we think is a good field of vision
# The following line can be commented to allow the interface to determine the indices
indices = [37, 87, 291, 337]
roi_1 = img1_array[indices[0]:indices[1], indices[2]:indices[3]] #select area of intrest from fixed image
roi_2 = shifted_images[0][indices[0]:indices[1], indices[2]:indices[3]] #select area of interest from image 2
roi_3 = shifted_images[1][indices[0]:indices[1], indices[2]:indices[3]] #select area of interest from image 3
roi_4 = shifted_images[2][indices[0]:indices[1], indices[2]:indices[3]] #select area of interest from image 4

# Plot the area of interest (using the indices from image 1) to view the changes of the tumour across the four images
fig3, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
ax1.imshow(roi_1, cmap="Greys_r")
ax2.imshow(roi_2, cmap="Greys_r")
ax3.imshow(roi_3, cmap="Greys_r")
ax4.imshow(roi_4, cmap="Greys_r")
ax1.set_title("Image 1") # set the titles of each of the plots to identify which is from which image
ax2.set_title("Image 2")
ax3.set_title("Image 3")
ax4.set_title("Image 4")
ax.set_xlabel('Time') # plotting as one axis with subplots does not work and so we have had to plot as separate plots, meaning these x and y labels do not work but this is what they would be named
ax.set_ylabel('Tumour volume') 
plt.show()

plt.savefig("Tumour regression image comparison.png") # save the image of the four tumours side by side as a png

# It can very clearly be seen on these images that the tumour has regressed with treatment. In image 1, the tumour is between 20 and 40 on the Y axis and it has high intensity. As you go through the images, the tumour is becoming less and less dense and smaller. By image 4, the tumour is barely visable and is between approximated 20 and 30. 