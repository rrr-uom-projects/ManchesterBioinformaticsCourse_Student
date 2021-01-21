"""
ICT in the Clinical Environment - Image Processing in Python: Assignment
Day 4 part 2

Thomas Scott-Adams :  9627185
Jay Miles          : 10806682
"""

# Import required modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pydicom
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
from skimage import io

#Read DICOM files
image1_dcm = pydicom.read_file('IMG-0004-00001.dcm')
image2_dcm = pydicom.read_file('IMG-0004-00002.dcm')
image3_dcm = pydicom.read_file('IMG-0004-00003.dcm')
image4_dcm = pydicom.read_file('IMG-0004-00004.dcm')

#Retrieve and store DICOM image arrays
image1_array = image1_dcm.pixel_array
image2_array = image2_dcm.pixel_array
image3_array = image3_dcm.pixel_array
image4_array = image4_dcm.pixel_array

#Function to apply a shift to an image
def shift_image(image, shifts):
    shifted_image = interpolation.shift(image, (shifts[0], shifts[1]), mode="nearest")
    return shifted_image

registrations = np.load('registrations.npy')
reg_im2 = shift_image(image2_array, registrations[0])
reg_im3 = shift_image(image3_array, registrations[1])
reg_im4 = shift_image(image4_array, registrations[2])

# fig = plt.figure() # Creating figure space
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)
# ax1.imshow(image1_array, cmap="Greys_r")
# ax2.imshow(reg_im2, cmap="Greys_r")
# ax3.imshow(reg_im3, cmap="Greys_r")
# ax4.imshow(reg_im4, cmap="Greys_r")
# plt.show()

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
    elif event.key == "d":
        # Make the rectangle wider - faster
        w0 = rect.get_width()
        rect.set_width(w0 + 10)
    elif event.key == "a":
        # Make the rectangle narrower - faster
        w0 = rect.get_width()
        rect.set_width(w0 - 10)
    elif event.key == "w":
        # Make the rectangle shorter - faster
        h0 = rect.get_height()
        rect.set_height(h0 - 10)
    elif event.key == "x":
        # Make the rectangle taller - faster
        h0 = rect.get_height()
        rect.set_height(h0 + 10)

    rect.figure.canvas.draw()# update the plot window

fig2 = plt.figure(2)
ax = fig2.add_subplot(111)
thePlot = ax.imshow(image1_array, cmap="Greys_r")

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

cid1 = fig2.canvas.mpl_connect('button_press_event', onPress)
cid2 = fig2.canvas.mpl_connect('motion_notify_event', onMove)
cid3 = fig2.canvas.mpl_connect('button_release_event', onRelease)
cid4 = fig2.canvas.mpl_connect('key_press_event', keyboardInterface)

plt.show()
indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
print(indices)

roi1 = image1_array[indices[0]:indices[1], indices[2]:indices[3]]
roi2 = reg_im2[indices[0]:indices[1], indices[2]:indices[3]]
roi3 = reg_im3[indices[0]:indices[1], indices[2]:indices[3]]
roi4 = reg_im4[indices[0]:indices[1], indices[2]:indices[3]]

means = [np.mean(roi1), np.mean(roi2), np.mean(roi3), np.mean(roi4)]

fig3 = plt.figure() # Creating figure space
ax1a = fig3.add_subplot(421)
ax1b = fig3.add_subplot(422)
ax2a = fig3.add_subplot(423)
ax2b = fig3.add_subplot(424)
ax3a = fig3.add_subplot(425)
ax3b = fig3.add_subplot(426)
ax4a = fig3.add_subplot(427)
ax4b = fig3.add_subplot(428)
ax1a.imshow(roi1, cmap="Greys_r")
ax1b.hist(roi1.flatten(), bins = 40)
ax2a.imshow(roi2, cmap="Greys_r")
ax2b.hist(roi2.flatten(), bins = 40)
ax3a.imshow(roi3, cmap="Greys_r")
ax3b.hist(roi3.flatten(), bins = 40)
ax4a.imshow(roi4, cmap="Greys_r")
ax4b.hist(roi4.flatten(), bins = 40)

axis_list1 = [ax1a, ax2a, ax3a, ax4a]
axis_list2 = [ax1b, ax2b, ax3b, ax4b]
i = 1
for axis in axis_list1:
    axis.set_title('Region of interest in image ' + str(i) + '\nMean intensity: ' + str(means[i-1]))
    i += 1
i = 1
for axis in axis_list2:
    axis.set_title('Histogram for image ' + str(i))
    axis.set_xlabel('Pixel intensity')
    axis.set_ylabel('Frequency')
    i += 1

plt.show()
