"""
Ed and sophie regression analysis.

This is part 2 of the assignment on day 4
"""

import os
import matplotlib.pyplot as plt 
import numpy as np
from skimage.io import imread
import scipy.optimize
import pydicom
from scipy.ndimage import interpolation
from scipy.ndimage import rotate
# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches
#load modules

def shiftImage(shifts, image):
    shiftedImage = interpolation.shift(image, shifts, mode="nearest")
    #shiftRotated = rotate(shiftedImage, rotation)
    return shiftedImage

cwd = os.getcwd()
#find current working directory
newPath = cwd +"\\Day4\\Code"
#path to folder containing lungs.jpg, this is for windows os, for othe os change to /
os.chdir(newPath)
registrations = np.load("registrations.npy")
#Load in all .dcm images
img1 = pydicom.read_file("IMG-0004-00001.dcm")
img2 = pydicom.read_file("IMG-0004-00002.dcm")
img3 = pydicom.read_file("IMG-0004-00003.dcm")
img4 = pydicom.read_file("IMG-0004-00004.dcm")
#access the object pixel_array from within img1,img2, img3, img4
img1Array = img1.pixel_array
img2Array = img2.pixel_array
img3Array = img3.pixel_array
img4Array = img4.pixel_array
#All floating images in a list
floatingList = [img2Array, img3Array, img4Array]
#empty list to store shifted images arrays
shiftedImageList = []
for (registration, floating) in zip(registrations, floatingList):
    shiftedImage = shiftImage(registration, floating)
    shiftedImageList.append(shiftedImage)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.imshow(img1Array)
ax1.title.set_text("Image 1")

ax2.imshow(shiftedImageList[0])
ax2.title.set_text("Image 2")

ax3.imshow(shiftedImageList[1])
ax3.title.set_text("Image 3")

ax4.imshow(shiftedImageList[2])
ax4.title.set_text("Image 4")

plt.show()

"""
fig2 = plt.figure(2)
ax1 = fig.add_subplot(1,1,1)
ax1.imshow(img1Array)
plt.show()
"""
"""
Below is the interface, we have selected our ROI and so have commented this
out. If you wish to choose your own ROi you must uncomment the interface (line 80 and 201).
Then comment out indices in line 211 and hard code your chosen roi in, or opt 
to choose your roi every time you run the script.
"""
"""
####---------------------INTERFACE-----------------------------------
# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(img1Array, cmap="Greys_r") # Display the fixed image (your image name may be different)

# Start with a box drawn in the centre of the image
origin = (img1Array.shape[0]/2, img1Array.shape[1]/2)
rectParams = [origin[0], origin[1], 10, 10]

# Draw a rectangle in the image

global rect
rect = patches.Rectangle((rectParams[1], rectParams[0]),rectParams[2], rectParams[3],linewidth=1, edgecolor='r',facecolor='none')

ax.add_patch(rect)

# Event handlers for the clipbox
global initPos
initPos = None



def onPress(event):

    #This function is called when you press a mouse button inside the figure window
    global rect
    if event.inaxes == None:
        return# Ignore clicks outside the axes
    contains, attr = rect.contains(event)
    if not contains:
        return# Ignore clicks outside the rectangle

    global initPos # Grab the global variable to update it
    initPos = [rect.get_x(), rect.get_y(), event.xdata, event.ydata]

def onMove(event):
    
    #This function is called when you move the mouse inside the figure window
    
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
    
    #This function is called whenever a mouse button is released inside the figure window
    
    global initPos
    initPos = None # Reset the position ready for next click

def keyboardInterface(event):

    #This function handles the keyboard interface. It is used to change the size of the
    #rectangle.
    
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

"""For the first image the indices are [50, 85, 286, 333] so we 
then commented out the interface so that the roi doesnt change every time
and then we hard coded in indices = [50, 85, 286, 333]"""

#This is the indices of the spine we tested on our metric
#indices = [117, 192, 243, 259]

#This is the real indices of the tumour
indices = [50, 85, 286, 333]
roi1 = img1Array[indices[0]:indices[1], indices[2]:indices[3]]
roi2 = shiftedImageList[0][indices[0]:indices[1], indices[2]:indices[3]]
roi3 = shiftedImageList[1][indices[0]:indices[1], indices[2]:indices[3]]
roi4 = shiftedImageList[2][indices[0]:indices[1], indices[2]:indices[3]]

fig3 = plt.figure(3)
ax1 = fig3.add_subplot(2,2,1)
ax2 = fig3.add_subplot(2,2,2)
ax3 = fig3.add_subplot(2,2,3)
ax4 = fig3.add_subplot(2,2,4)

ax1.imshow(roi1)
ax1.title.set_text("ROI 1")

ax2.imshow(roi2)
ax2.title.set_text("ROI 2")

ax3.imshow(roi3)
ax3.title.set_text("ROI 3")

ax4.imshow(roi4)
ax4.title.set_text("ROI 4")

plt.show()


"""
We decided to use the mean intensity of the image to see how the tumour volume
decreased over the images, because its brighter than the surrounding tissue so we 
would expect mean intesnity to decrease over time. 
"""

roiList = [roi1, roi2, roi3, roi4]
meanIntensityList = []
for roi in roiList:
    meanIntensity = np.mean(roi)
    meanIntensityList.append(meanIntensity)

print(meanIntensityList)

x = [1,2,3,4]

fig4 = plt.figure(4)

ax = fig4.add_subplot(1,1,1)
ax.title.set_text("Mean intensity over the 4 images")
ax.set_xlabel("Time")
ax.set_ylabel("Mean intesnsity")

plt.plot(x, meanIntensityList, label = "Mean intensity")
leg = ax.legend()
plt.show()
"""
Q23: We used our metric on the roi for the spine and there was no 
change, as expected.
"""