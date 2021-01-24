# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:35:38 2021

@author: jaden
"""
## Names: Jadene and Long-Ki
## Date: 22/01/21
## Title: Image Processing in Python

## PART 2 ##

# Import relevant libraries, modules and functions
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy.ndimage import interpolation, rotate 
import os
import skimage.io 
import skimage
from skimage import io
import io 
import matplotlib.image as mpimg 
import pydicom 
from scipy.optimize import brute, differential_evolution

#Set working directory
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day4/Code")
os.getcwd()

#Load the registrations array and the four images
np.load("registrations.npy")
image1_array = pydicom.dcmread("IMG-0004-00001.dcm").pixel_array #returns DICOM object and inside is a pixel array
image2_array=pydicom.dcmread("IMG-0004-00002.dcm").pixel_array
image3_array=pydicom.dcmread("IMG-0004-00003.dcm").pixel_array
image4_array=pydicom.dcmread("IMG-0004-00004.dcm").pixel_array

#Apply registration to each 
def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts)
    #fig3 = plt.figure()
    #ax = fig3.add_subplot(111)
    #plt.title("Overlaid images 1 & 2")
    #ax.imshow(image1_array, cmap = "Greens_r")
    #ax.imshow(shifted_image, cmap = "Purples_r", alpha = 0.5)
    plt.imshow(shifted_image, cmap="Greys_r")
    return shifted_image
    #plt.show()

shifted_image_2 = shiftImage(registrations[0], image2_array) #registrations list from previous script
shifted_image_3 = shiftImage(registrations[1], image3_array)
shifted_image_4 = shiftImage(registrations[2], image4_array)

fig = plt.figure()
#plt.title("All four images")
ax1 = fig.add_subplot(221)
ax1.set_title("Image 1")
ax2 = fig.add_subplot(222)
ax2.set_title("Image 2")
ax3 = fig.add_subplot(223)
ax3.set_title("Image 3")
ax4 = fig.add_subplot(224)
ax4.set_title("Image 4")
ax1.imshow(image1_array, cmap="Greys_r")
ax2.imshow(shifted_image_2, cmap="Greys_r")
ax3.imshow(shifted_image_3, cmap="Greys_r")
ax4.imshow(shifted_image_4, cmap="Greys_r")

plt.show() #can see that the tumor is regressing across the images

#Display only the first image
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.imshow(image1_array, cmap="Greys_r")
plt.show()

#Copy the interface.py code:

# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
ax.imshow(image1_array, cmap="Greys_r") # Display the fixed image (your image name may be different)


#ax.add_patch(rect)

# Start with a box drawn in the centre of the image
origin = (image1_array.shape[0]/2, image1_array.shape[1]/2)
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

fig2.canvas.mpl_connect('button_press_event', onPress)
fig2.canvas.mpl_connect('motion_notify_event', onMove)
fig2.canvas.mpl_connect('button_release_event', onRelease)
fig2.canvas.mpl_connect('key_press_event', keyboardInterface)

plt.show()


indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
print(indices) #[50, 71, 305, 325]
#for our ROI: goes from x=305 to x=325; y=71 to 50 

#To extract region of interest
roi = image1_array[indices[0]:indices[1], indices[2]:indices[3]]
plt.imshow(roi, cmap="Greys_r")
plt.show()

##NB: using same ROI for each of the images for consistency
roi2 = shifted_image_2[indices[0]:indices[1], indices[2]:indices[3]]
plt.imshow(roi2, cmap = "Greys_r")
plt.show()

roi3 = shifted_image_3[indices[0]:indices[1], indices[2]:indices[3]]
plt.imshow(roi3, cmap="Greys_r")
plt.show()

roi4 = shifted_image_4[indices[0]:indices[1], indices[2]:indices[3]]
plt.imshow(roi4, cmap="Greys_r")
plt.show()

#Plot all ROIs on a subplot
fig = plt.figure()
#plt.title("Tumor region")
ax1 = fig.add_subplot(221)
ax1.set_title("Image 1")
ax2 = fig.add_subplot(222)
ax2.set_title("Image 2")
ax3 = fig.add_subplot(223)
ax3.set_title("Image 3")
ax4 = fig.add_subplot(224)
ax4.set_title("Image 4")
fig.suptitle("Tumor region in all four images")
#fig.subplots_adjust(wspace=0.5, hspace=0.3,left=0.125,right=0.9,top=0.9,bottom=0.1)
ax1.imshow(roi, cmap="Greys_r")
ax2.imshow(roi2, cmap="Greys_r")
ax3.imshow(roi3, cmap="Greys_r")
ax4.imshow(roi4, cmap="Greys_r")
#plt.savefig("ROIs.png")

#Come up with a metric that will describe the way that the tumor is regressing. 
#This can be as simple or as complex as you like
#Evaluate this metric on the four images and plot it

#Use mean squares? Mean squared pixel wise difference in intensity between image A and B.
np.mean((roi-roi2)**2) #65.84285714285714
np.mean((roi-roi3)**2) #175.48095238095237
np.mean((roi-roi4)**2) #639.6714285714286
#This shows that there is a increasing difference in the intensity of pixels between ROI in image1 compared to ROIs in image2, 3 and 4, respectively

a = np.mean((roi-roi)**2)
b = np.mean((roi-roi2)**2) #65.84285714285714
c = np.mean((roi-roi3)**2) #175.48095238095237
d = np.mean((roi-roi4)**2)

y= [a, b, c, d]
x= ["Image1", "Image2", "Image3", "Image4"]

fig = plt.figure()
plt.scatter(x,y)
plt.plot(x, y)
plt.xlabel("Image")
plt.ylabel("Mean squares (compared to image 1)")
plt.title("Evaluation metric for tumor regression (mean squares cost function)")
#plt.legend() #not sure what legend?

plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.set(title = "Evaluation metric for tumor regression (mean squares cost function)",
#       ylabel = "Mean squares (compared to image 1)",
#       xlabel = "Image")
#ax.legend(loc="upper left")
#lines = ax.plot(x, y)
#plt.scatter(x,y)
