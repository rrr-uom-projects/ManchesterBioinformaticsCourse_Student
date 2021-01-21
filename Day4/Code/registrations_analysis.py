"""
Assignment for Day 4
Image Processing in Python
This script performs registratios analysis.

Katherine Winfield (@kjwinfield) and Yongwon Ju (@yongwonju)

This version written on 21 January 2021
"""

'''
Import libraries 
'''
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy import ndimage
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom
import matplotlib.patches as patches

def shift_image(vector, image, rotation=0):
    '''
    Function to translate and rotate second image and overlay it on the figure space 

    Parameters: 

                vertical    - transation in the y axis
                horizontal  - translation in the x axis
                rotation    - rotation clockwise

    Returns:    
    
                null
    '''

    translated_image = ndimage.rotate(image, rotation, reshape=False) # rotates the image
    rotated_image    = interpolation.shift(translated_image, (vector[0], vector[1]), mode="nearest") # translates the image in the x and y axis

    return rotated_image

#load images
floating_list = []

image_files = os.listdir()
for file in image_files:
    if file.endswith('.dcm'):
        floating_list.append(pydicom.read_file(file).pixel_array)

#load registrations array:
registrations = np.load('registrations.npy')
print(registrations)

# #creates ampty figure plot for 4 images
# fig = plt.figure()
# ax = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

# #adds images to figure plot
# cax = ax.imshow(floating_list[0], cmap="Greys_r")
# cax2 = ax2.imshow(floating_list[1], cmap="afmhot")
# cax3 = ax3.imshow(floating_list[2], cmap="Reds")
# cax4 = ax4.imshow(floating_list[3], cmap="cool")
# plt.show() #displays all four images, showing tumour regression
# plt.close(fig)

#shift images so they all line up correctly
shifted_images = []
for i in range(len(floating_list)):
    print(i)
    shifted = shift_image(registrations[i], floating_list[i])
    shifted_images.append(shifted)
print(shifted_images)

fig = plt.figure()
ax = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# adds images to figure plot
cax = ax.imshow(shifted_images[0], cmap="Greys_r")
cax2 = ax2.imshow(shifted_images[1], cmap="afmhot")
cax3 = ax3.imshow(shifted_images[2], cmap="Reds")
cax4 = ax4.imshow(shifted_images[3], cmap="cool")
plt.show() #displays all four images, showing tumour regression

#create another figure, that only shows the first image
fig2 = plt.figure(2)
ax = fig2.add_subplot(111) #add empty plot
thePlot = ax.imshow(shifted_images[0], cmap="Greys_r") #load image into empty plot

# Start with a box drawn in the centre of the image
origin = (shifted_images[0].shape[0]/2,shifted_images[0].shape[1]/2)
rectParams = [origin[0], origin[1], 40, 25] #[40, 25] are the dimensions of the rectangle, large enough to cover the tumour

# Draw a rectangle in the image
global rect
rect = patches.Rectangle((rectParams[1], rectParams[0]),rectParams[2], rectParams[3],linewidth=1, edgecolor='r',facecolor='none')

ax.add_patch(rect) #adds the rectangle to the image

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
plt.close()

#identify the coordinates of the region of interest (in this case, the tumour)
indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
print(indices)

roi = shifted_images[0][indices[0]:indices[1], indices[2]:indices[3]]
#print(roi)

#close up on tumour region in each image:
#creates blank figure for tumour close ups
fig4 = plt.figure()
ax = fig4.add_subplot(221) #four subplots, one for each image
ax2 = fig4.add_subplot(222)
ax3 = fig4.add_subplot(223)
ax4 = fig4.add_subplot(224)

list_of_tumour_close_ups = []
mean_image_val = []

#for loop cropping each image to just show the region of interest (the tumour area)
for i in range(len(shifted_images)):
    cropped = shifted_images[i][indices[0]:indices[1], indices[2]:indices[3]]
    list_of_tumour_close_ups.append(cropped)
    mean_image_val.append(np.mean(cropped))

#adds close up tumour region images to empty figure plot
cax = ax.imshow(list_of_tumour_close_ups[0], cmap="Greys_r")
cax2 = ax2.imshow(list_of_tumour_close_ups[1], cmap="Greys_r")
cax3 = ax3.imshow(list_of_tumour_close_ups[2], cmap="Greys_r")
cax4 = ax4.imshow(list_of_tumour_close_ups[3], cmap="Greys_r")

axis_label = [ax, ax2, ax3, ax4]

for i in range(len(axis_label)) :
    axis_label[i].set_title('Close up of tumour region ' + str(i) + '\nMean value:' + str(mean_image_val[i]))


plt.show() #shows the plot
