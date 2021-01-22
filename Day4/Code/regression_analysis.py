# -*- coding: utf-8 -*-
"""
Assignment 2 part 2 image regression_analysis
Naomi/Ali/Keith
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it the final graphs in a tab in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""

#%%
#Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy import ndimage
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom 
import matplotlib.patches as patches # Import the bit of matplotlib that can draw rectangles

# Copies the shift image function from the previous assignment
def shiftimage(image,coordinate_list):
    Vertical = coordinate_list[0] #takes the vertical co-ordinate value from the input list
    Horizontal = coordinate_list[1] #takes the horizontl co-ordinate value from the input list
    shifted_image = interpolation.shift(image, (Vertical, Horizontal), mode="nearest") #shifts the image on the x,y as per the input co-ordinates
    return shifted_image #returns the shifted image as per the above changes

registrations = np.load("registrations.npy")

# Load the DICOM files and get the pixel data from the dicom file 
patientImage = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")
patientImage3 = pydicom.read_file("IMG-0004-00003.dcm")
patientImage4 = pydicom.read_file("IMG-0004-00004.dcm")

#get the pixel data from the DICOM files as a numpy array using "img1_array = patientImage.pixel_array" format
img1_array = patientImage.pixel_array 
img2_array = patientImage2.pixel_array
img3_array = patientImage3.pixel_array 
img4_array = patientImage4.pixel_array

#Arrays for all images into a list as per before
floating_list = [img1_array,img2_array,img3_array,img4_array]

#Shift images calling the shift image function and registrations.py and putting those arrays into a list
shifted_images = []
for i in range(len(floating_list)):
    shifted = shiftimage(floating_list[i], registrations[i])
    shifted_images.append(shifted)
print(shifted_images)

#Plots all the shifted images side by side
fig = plt.figure() #set up a figure space 
ax1 = fig.add_subplot(221) #add subplots for each image 
ax2 = fig.add_subplot(222) 
ax3 = fig.add_subplot(223) 
ax4 = fig.add_subplot(224) 
ax1.imshow(shifted_images[0], cmap="Greens_r") #Displays each image using a green colour map
ax2.imshow(shifted_images[1], cmap="Greens_r")
ax3.imshow(shifted_images[2], cmap="Greens_r")
ax4.imshow(shifted_images[3], cmap="Greens_r")  
plt.show() #Shows 4 by 4 grid of the 4 images

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(img1_array, cmap="Greys_r") # Display the fixed image (your image name may be different)

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

indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())] #Returns the indices of the interactive rectangle for cropping co-oridnates
#print(indices)

roi1 = shifted_images[0][indices[0]:indices[1], indices[2]:indices[3]] #Crops each image as deisgnated in the rectangle co-ordinates for comparison
roi2 = shifted_images[1][indices[0]:indices[1], indices[2]:indices[3]]
roi3 = shifted_images[2][indices[0]:indices[1], indices[2]:indices[3]]
roi4 = shifted_images[3][indices[0]:indices[1], indices[2]:indices[3]]

fig3 = plt.figure() #set up a figure space 
ax1_1 = fig3.add_subplot(221) #add subplots for each thing, careful to use different axis variables to circumvent terrible error
ax2_2 = fig3.add_subplot(222) 
ax3_3 = fig3.add_subplot(223) 
ax4_4 = fig3.add_subplot(224) 
ax1_1.imshow(roi1, cmap="Greens_r")
ax2_2.imshow(roi2, cmap="Greens_r")
ax3_3.imshow(roi3, cmap="Greens_r")
ax4_4.imshow(roi4, cmap="Greens_r")  
plt.show() #Shows 4 by 4 grid of the 4 images

#Work out overall pixel intensity means for each ROI, logic being as the tumour shrinks so should the intensity
#Could make this more robust by incoporating pixel range and standard errors.

Tumour_regression = [np.mean(roi1),np.mean(roi2),np.mean(roi3),np.mean(roi4)]
print(Tumour_regression) #This roughly shows a regression: [52.902255639097746, 47.07017543859649, 42.16791979949875, 30.789473684210527]

"""
"Make sure this plot:-Has labelled axes-Has a legendSave this plot as a pngand add it to your repo.
 Make some comments in your code noting what you see."
 
Again time permitting we would add labels and axes to our plot using matplotlib tools.

 "XXIII.If you still have time, change the ROIto somethingelse, e.g. a bit of thespine, and verify 
 that the metric you chose does not change over time in that ROI."

We could set up further variables to compare a bit of control tissue for this and possibly an background area outside of the tissue itself.
 """