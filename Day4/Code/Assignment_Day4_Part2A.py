#!/usr/bin/env python
# coding: utf-8
 
# Image processing in Python: assignment Day 4
# Igor and Manuel
# Part2
 
 
"""
XIV. Start a new script, called something like regression_analysis.py. Put the usual info at the top.
"""
# Done
 
"""
XV. In the new script, import everything you will need and copy the shiftImages function
from the previous script. Load the registrations array (registrations =
np.load(registrations.npy”)) and the four images, apply the corresponding
registration to each to get back to where you were at the end of the previous script.
 
"""
 
# Let’s import needed with the next lines of code.
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute
import inspect
import os
import pydicom
# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches 
# Now we copy the shiftImages function
 
def shiftImage(shifts, image):
  #shits is an input, which is a list of two values example [value1, value2] that shifts the image.
  # Value1 moves image up or down, value 2 moves image left or right.
  shifted_image = interpolation.shift(image, (shifts[0], shifts[1]), mode="nearest")
  return shifted_image
 
 
# path of the executing script
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
#name of image
img_name1 = '/IMG-0004-00001.dcm'
img_name2 = '/IMG-0004-00002.dcm'
img_name3 = '/IMG-0004-00003.dcm'
img_name4 = '/IMG-0004-00004.dcm'

#path to the image
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2
img_path3 = actual_path + img_name3
img_path4 = actual_path + img_name4
 
#import images using pydicom.read_file
img1 = pydicom.read_file(img_path1)
img2 = pydicom.read_file(img_path2)
img3 = pydicom.read_file(img_path3)
img4 = pydicom.read_file(img_path4)
# To get the a numpy.ndarray containing the pixel data from the sataset, we just use ".pixel_array"
img1_array = img1.pixel_array
img2_array = img2.pixel_array
img3_array = img3.pixel_array
img4_array = img4.pixel_array
 

# Load registration
registrations = np.load('registrations.npy')

# Now, we will apply the registration with these four images
floating_list = [img2_array, img3_array, img4_array]

#This for loop modifies the image postion based on the registeres values obtain from the previouse function
shifted_images = floating_list # Here we copy the images from the floating list which will be modified
for i in range(0, len(floating_list), 1): # this loop is designed to get i values from 0 to the number of images in the floating_list 
    shifted_images[i] = shiftImage(registrations[i], floating_list[i]) # i is used here to call the specific image and correspoding registration values 


"""
XVI. Now you should be able to plot the four images side-by-side (i.e. on a set of subplots, not
overlaid) and see that the tumour visible in them is “regressing”. We will now attempt to
measure that regression!
To do this, we will link up some code in the “interface.py” file with a figure you will
create showing only the first image. Then, we will use the interface to put a red box over the
tumour. The red box will be used to get the indices in the pixel data array that define that
region of interest. From that we will extract the ROI and analyse the numbers within it
"""
'''
# First, let's decided the order of the images
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# Now, we write some Title
fig.suptitle('Four images side-by-side ')
# We specify the images that they were previously load
ax1.imshow(img1_array, cmap="Greys_r")
ax2.imshow(shifted_images[0], cmap="Greys_r")
ax3.imshow(shifted_images[1], cmap="Greys_r")
ax4.imshow(shifted_images[2], cmap="Greys_r")
# And plot everything
plt.show()
'''

# Now, we are going to use the code from interface.py
# We have added some modification to be able to run de code
 
 
########################## interface.py #################################
##################################################################
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
 
 
 
indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
print(indices)
 
########################## interface.py #################################
########################################################################
 
 
 
"""XVII. Display the first image in the timeseries, make sure you keep the figure handle and axes.
(look at the code in interface.py to see what things you will need)
XVIII. Copy and paste the code from interface.py into your script. Make sure nothing gets
messed up! You will have to modify the bits at the top & bottom that create/attach to
figures to make them attach to the figure you just created
XIX. Now everything is linked up, try visualising the first image. """
 
# We think we have done this already in activity number XVI. We have been able to visualise the first image and locate with the mouse the red square on the tumor.
 
"""
FOR XXII and XXIII refer to scripts called:
Assignment_Day4_Part2B.py
Assignment_Day4_Part2C.py
"""

