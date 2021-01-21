"""
BIOL68310 Assignment: Image processing in Python - Day 2, Part 2

Aim of this part is to .......

Authors: Katie Williams and Megan Paynton

Work done on Thursday 21st January 2021
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

registrations = np.load("registrations.npy")
floating_list = [img2_array, img3_array, img4_array]

# loop over floating images (and shiftImage function) to produce registered images) 
shifted_images = []
for i, floating in enumerate(floating_list):
    print(i)
    registered_images = shiftImage(registrations[i], floating)
    shifted_images.append(registered_images)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1)
ax1.imshow(img1_array, alpha=0.5, cmap="Greys_r")
ax2.imshow(shifted_images[0], alpha=0.5, cmap="Greys_r")
ax3.imshow(shifted_images[1], alpha=0.5, cmap="Greys_r")
ax4.imshow(shifted_images[2], alpha=0.5, cmap="Greys_r")
plt.show()

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(img1_array, cmap="Greys_r") # Display the fixed image


# Start with a box drawn in the centre of the image
origin = (img1_array.shape[0]/2, img1_array.shape[1]/2)
rectParams = [origin[0], origin[1], 10, 10]

# Draw a rectangle in the image

global rect
rect = patches.Rectangle((rectParams[1], rectParams[0]),rectParams[2], rectParams[3],linewidth=1, edgecolor='r',facecolor='none')

ax.add_patch(rect)

# Event handlers for the clipbox
global initPos
initPos = None



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

def onRelease(event):
    """
    This function is called whenever a mouse button is released inside the figure window
    """
    global initPos
    initPos = None # Reset the position ready for next click

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

cid1 = fig2.canvas.mpl_connect('button_press_event', onPress)
cid2 = fig2.canvas.mpl_connect('motion_notify_event', onMove)
cid3 = fig2.canvas.mpl_connect('button_release_event', onRelease)
cid4 = fig2.canvas.mpl_connect('key_press_event', keyboardInterface)

plt.show()


indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
#print(indices) #indices 37, 87, 291, 337 
indices = [37, 87, 291, 337]
roi_1 = img1_array[indices[0]:indices[1], indices[2]:indices[3]] #select area of intrest from fixed image
roi_2 = shifted_images[0][indices[0]:indices[1], indices[2]:indices[3]] #select area of interest from image 2
roi_3 = shifted_images[1][indices[0]:indices[1], indices[2]:indices[3]] #select area of interest from image 3
roi_4 = shifted_images[2][indices[0]:indices[1], indices[2]:indices[3]] #select area of interest from image 4


fig3, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
ax1.imshow(roi_1, alpha=0.5, cmap="Greys_r")
ax2.imshow(roi_2, alpha=0.5, cmap="Greys_r")
ax3.imshow(roi_3, alpha=0.5, cmap="Greys_r")
ax4.imshow(roi_4, alpha=0.5, cmap="Greys_r")
ax1.set_title("Image 1")
ax2.set_title("Image 2")
ax3.set_title("Image 3")
ax4.set_title("Image 4")
ax.set_xlabel('Time')
ax.set_ylabel('Tumour volume') 
plt.show()

plt.savefig("Tumour regression image comparison.png")