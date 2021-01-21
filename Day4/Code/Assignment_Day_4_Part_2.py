"""
Authors: Nicola Compton and Catherine Borland

This code allows user to draw around the ROI in the original tumour and measures tumour regression by comparing the intensity of the ROI in subsequent images. The images have already been registered.
"""

# import modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io 
from skimage.io import imread
import pydicom as dc

# shift image function
# input: vector of shifts and image to be shifted
# output: shifted image
def shiftImage(shifts, image):
    shifted_image=interpolation.shift(image, shifts, mode="nearest")
    return shifted_image

# load registrations
registrations=np.load("registrations.npy")

# load all the dicom images and convert to pixel arrays
image_1=dc.read_file("IMG-0004-00001.dcm")
image_2=dc.read_file("IMG-0004-00002.dcm")
image_3=dc.read_file("IMG-0004-00003.dcm")
image_4=dc.read_file("IMG-0004-00004.dcm")
img1_pixel=image_1.pixel_array
img2_pixel=image_2.pixel_array
img3_pixel=image_3.pixel_array
img4_pixel=image_4.pixel_array

# make a list of the floating images
floating_list = [img2_pixel, img3_pixel, img4_pixel]

# apply registrations to the images
# create an empty list to store the shifted images in
# set iterations to 0 for calling the corresponding registrations
shifted_images=[]
iteration=0

# loop around images
for floating in floating_list:
    
    # shift the image by the optimal shift
    auto_registered=shiftImage(registrations[iteration], floating)
    
    # store shifted image in list 
    shifted_images.append(auto_registered)
    
    # update iteration 
    iteration=iteration+1

# display images side by side in subplots
fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.imshow(img1_pixel,cmap="Greys_r")
ax1.set_title("Image 1")
ax2.imshow(shifted_images[0],cmap="Greys_r")
ax2.set_title("Image 2")
ax3.imshow(shifted_images[1],cmap="Greys_r")
ax3.set_title("Image 3")
ax4.imshow(shifted_images[2],cmap="Greys_r")
ax4.set_title("Image 4")
plt.show()

## this is copied from interface.py
# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(img1_pixel, cmap="Greys_r") # changed to our fixed image

# Start with a box drawn in the centre of the image
origin = (img1_pixel.shape[0]/2, img1_pixel.shape[1]/2)
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
################################################################################
# The functions below here will need to be changed for use on Windows!
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
print(indices)

## end of interface.py

# extract ROI from all shifted images
roi=[img1_pixel[indices[0]:indices[1], indices[2]:indices[3]]]

# calculate intensity within the ROI for each image
# we will use this to measure tumour regression
intensity=[sum(sum(sum(roi)))]

# loop around shifted images 
for image in shifted_images:
    
    # find ROI
    roi_shrinking=image[indices[0]:indices[1], indices[2]:indices[3]]
    roi.append(roi_shrinking) # update ROI list
    
    # calculate intensity inside ROI
    intensity.append(sum(sum(roi_shrinking))) # update intensity list
    
# display images of the ROI side by side in subplots so we can see the tumour shrinking
fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.imshow(roi[0],cmap="Greys_r")
ax1.set_title("Image 1: ROI")
ax2.imshow(roi[1],cmap="Greys_r")
ax2.set_title("Image 2: ROI")
ax3.imshow(roi[2],cmap="Greys_r")
ax3.set_title("Image 3: ROI")
ax4.imshow(roi[3],cmap="Greys_r")
ax4.set_title("Image 4: ROI")
plt.show()

# plotting the tumour regression by intensity of ROI in each image
x=["Image 1","Image 2","Image 3","Image 4"]
plt.bar(x,intensity)
plt.ylabel("Sum of Pixel Intensity Within ROI")
plt.show()

# We checked this metric did not change over time when the ROI was placed on the spine


