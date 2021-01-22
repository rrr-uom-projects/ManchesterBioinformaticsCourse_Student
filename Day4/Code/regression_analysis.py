#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment Part 2 (Day 4)
_________________________

Viveck Kingsley - 10811867

Owen Williams - 10806830

_________________________

"""
# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import interpolation
import pydicom

# Loading Images and Converting each to a pixel_array
patient_image = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00001.dcm").pixel_array
patient_image2 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00002.dcm").pixel_array
patient_image3 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00003.dcm").pixel_array
patient_image4 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00004.dcm").pixel_array

# Loading the registrations.npy array
registrations = np.load("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/registrations.npy")


def shift_image(shifts, image):
     shifting = interpolation.shift(image, (shifts), mode="nearest")
     return shifting


"""
An open list called "shifted_images" was created. 
The floating_list is a nested list with each element representing each floating image, as previously done in part 1.
A loop was created to shift each image in the floating_list in line with the fixed image. This is in accordance to optimum registrations (registrations) described in part 1. 
For each loop, 'i' increases by 1, which allow the loop to go through each element in the 'floating_list'. 
With each loop, the new image array information is stored as a nested array in the 'shifted_images' list. 
"""
shifted_images=[]
floating_list=[patient_image2, patient_image3, patient_image4]
i=0
for image in floating_list:
    new_position = shift_image((registrations[i]), image)
    shifted_images.append(new_position)
    i+=1
print(shifted_images)

"""

XVI:
Using the code below, a figure containing a 2x2 plot was constructed, showing each imported image (different stages of treatment) with colourmap Greys_r as each plot of this grid. 
    
"""

fig = plt.figure()

ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

ax1.imshow(patient_image, cmap="Greys_r")
ax2.imshow(shifted_images[0], cmap="Greys_r")
ax3.imshow(shifted_images[1], cmap="Greys_r")
ax4.imshow(shifted_images[2], cmap="Greys_r")
plt.show()

"""
____________________________________________
Start of interface.py code - adapted to accept assignment code by adding in the first image of the timeseries, which attaches the interface to the figure.
____________________________________________
This code was used to put an interactive clickable and movable red box on the patient_image (first image), where the user can use this interface to drag the red box to the ROI (the tumour)
and enlarge or shrink the box using arrow keys to contain the tumour within the box. The red box will be used to get indices in the pixel data array which define the region of interest, 
much like coordinates. Using the red box defined ROI, these indices are used for each patient_image showing different stages of the tumour treatment at the same location (ROI), and plot
each image on a 2x2 plot, to observe the image from a close-up perspective. 

"""

# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(patient_image, cmap="Greys_r") # Display the fixed image (your image name may be different)

# Start with a box drawn in the centre of the image
origin = (patient_image.shape[0]/2, patient_image.shape[1]/2)
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

"""
____________________________________________
End of interface.py code  
____________________________________________

"""

"""
XX:
The interface was used to select the region of interest to be analysed, using the indices variable, containing the x and y axis of the ROI. The ROI was extracted using the code below, and
using the indices collected by patient_image (image 1 in the timeseries) the same indices were applied to the remaining images.
"""

roi = patient_image[indices[0]:indices[1], indices[2]:indices[3]]
roi1 = shifted_images[0][indices[0]:indices[1], indices[2]:indices[3]]
roi2 = shifted_images[1][indices[0]:indices[1], indices[2]:indices[3]]
roi3 = shifted_images[2][indices[0]:indices[1], indices[2]:indices[3]]

"""
XXI:
Another 2x2 plot is made to showcase each roi variable mentioned above. 
"""
fig = plt.figure()

ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

ax1.imshow(roi, cmap="Greys_r")
ax1.set_title("Stage 1: Lung Tumour")
ax2.imshow(roi1, cmap="Greys_r")
ax2.set_title("Stage 2: Lung Tumour")
ax3.imshow(roi2, cmap="Greys_r")
ax3.set_title("Stage 3: Lung Tumour")
ax4.imshow(roi3, cmap="Greys_r")
ax4.set_title("Stage 4: Lung Tumour")
plt.show()

"""
XXII: 
To come up with a metric that will describe the way the tumour is disappearing inside the ROI, we used the mean_squared function created in part 1. 
Using the mean_squared function, the differences between images (roi, roi1, roi2, roi3) compared to the roi original demonstrates the progression of the disease.
cost compares roi against roi, which is 0 - this is our control 
cost1 compares roi1 against roi, roi being the first picture of regression gave a means_squared = 46.318
cost2 compares roi2 against roi, roi being the second picture of regression, gave a means_squared = 126.129
cost3 compares roi3 against roi, roi being the last image of regression, gave a means_squared = 452.088
ROI being increasingly different from the original shows that there is a progressive change that is taking place in the images.   
"""
def mean_squared (fixed, floating):
    return np.mean((fixed - floating)**2)
cost = mean_squared(roi, roi)
cost1 = mean_squared(roi, roi1)
cost2 = mean_squared(roi, roi2)
cost3 = mean_squared(roi, roi3)
print (cost, cost1, cost2, cost3)

"""
A scatter graph was produced to display the correlation between cost and image number in the timeseries. 
"""

x_values = ["ROI", "ROI[1]", "ROI[2]", "ROI[3]"]
y_values = [0, 46.318, 126.129, 452.055]


fig3=plt.figure()
ax=fig3.add_subplot(111)
ax.scatter(x_values, y_values, label="Cost")
ax.set_xlabel("Region of Interest")
ax.set_ylabel("Means Squared")
ax.set_title("Rate of Tumour Regression")
ax.legend()
plt.savefig("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/costregression.png")

plt.show()

"""
XXIII: When a different ROI was used for the metric plot, all the values were the same in ROIs, as there was no difference in pixel intensity. 
"""























