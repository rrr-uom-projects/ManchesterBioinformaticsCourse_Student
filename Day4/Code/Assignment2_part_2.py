"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional

Authors: Rosie Smart and Ruth Keane
Date: 21/01/2021
Title: Assignment 2 part 2 
"""


# import required functions
import matplotlib.pyplot as plt
import numpy as np
import skimage.io 
from skimage.io import imread
from scipy.ndimage import rotate
from scipy.ndimage import interpolation 
from scipy.optimize import brute
from scipy.optimize import differential_evolution
import pydicom 
# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches


def shiftImage(the_shifts,image): 
    """
    Shifts image in the xy plane. 

    Parameters
    ----------
    the_shifts : list
        Desired shifts in xy plane
    image : array
        Image to be shifted
    Returns
    -------
    image : array
        Shifted image

    """
    # Shift image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    image = interpolation.shift(image, shift = the_shifts)
    return image

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
    # The functions below here will need to be changed for use on Windows!
    elif event.key == "k":
        # Make the rectangle wider - faster
        w0 = rect.get_width()
        rect.set_width(w0 + 10)
    elif event.key == "j":
        # Make the rectangle narrower - faster
        w0 = rect.get_width()
        rect.set_width(w0 - 10)
    elif event.key == "i":
        # Make the rectangle shorter - faster
        h0 = rect.get_height()
        rect.set_height(h0 - 10)
    elif event.key == "m":
        # Make the rectangle taller - faster
        h0 = rect.get_height()
        rect.set_height(h0 + 10)

    rect.figure.canvas.draw()# update the plot window

def tumour_size(image):
    size=np.mean(image)
    return size

def main():
    ### Import images
    image1_dcm = pydicom.read_file("IMG-0004-00001.dcm",)
    image1_array=image1_dcm.pixel_array
    image2_dcm = pydicom.read_file("IMG-0004-00002.dcm")
    image2_array=image2_dcm.pixel_array
    image3_dcm = pydicom.read_file("IMG-0004-00003.dcm",)
    image3_array=image3_dcm.pixel_array
    image4_dcm = pydicom.read_file("IMG-0004-00004.dcm")
    image4_array=image4_dcm.pixel_array
    # Load optimum image shifts
    registrations=np.load("registrations_array.npy")
    
    ### 
    #make a list of images for loop
    floating_list = [image2_array, image3_array, image4_array]
    #initialise shifted list to store images once shifts have been applied
    shifted_list=[]
    # set index to 0 which will be used in for loop
    index=0
    # Loop through images in floating_list
    #apply optimum shifts to images 2 to 4 using shiftImage
    for floating in floating_list:
        #set shift to optimum shift from registrations using index
        shifted_list.append(shiftImage(registrations[index],floating))
        index = index + 1
    #initialise figure
    fig=plt.figure()
    #make four subplots
    ax1=fig.add_subplot(1,4,1)
    ax2=fig.add_subplot(1,4,2)
    ax3=fig.add_subplot(1,4,3)
    ax4=fig.add_subplot(1,4,4)
    #plot images and shifted images on subplots
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_list[0],cmap="Greys_r")
    ax3.imshow(shifted_list[1],cmap="Greys_r")
    ax4.imshow(shifted_list[2],cmap="Greys_r")
    #pictures show tumour clearly regressing
    

    # Create a new figure
    fig2 = plt.figure(2)
    ax = fig2.add_subplot(111)# Stick a subplot into the figure
    thePlot = ax.imshow(image1_array, cmap="Greys_r") # Display the fixed image (your image name may be different)

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
    #indices stores selected region
    indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
    print(indices)
   
    #initialise figure
    fig3=plt.figure()
    ax1=fig3.add_subplot(141)
    ax2=fig3.add_subplot(142)
    ax3=fig3.add_subplot(143)
    ax4=fig3.add_subplot(144)

    #access selected part of images and display
    #store image 1 selected region from shifted_list
    roi1 = image1_array[indices[0]:indices[1], indices[2]:indices[3]]
    ax1.imshow(roi1,cmap="Greys_r")
    #store image 2 selected region from shifted_list
    roi2 = shifted_list[0][indices[0]:indices[1], indices[2]:indices[3]]
    ax2.imshow(roi2,cmap="Greys_r")
    # store image 3 selected region from shifted_list
    roi3 = shifted_list[1][indices[0]:indices[1], indices[2]:indices[3]]
    ax3.imshow(roi3,cmap="Greys_r")
    # store image 4 selected region from shifted_list
    roi4 = shifted_list[2][indices[0]:indices[1], indices[2]:indices[3]]
    ax4.imshow(roi4,cmap="Greys_r")

    #Call tumour size to calculate average pixel value in selected region of each scan. Store in list.
    size_list=[tumour_size(roi1),tumour_size(roi2),tumour_size(roi3),tumour_size(roi4)]
    # Store names for images in list 
    x_values=["Image One","Image Two","Image Three","Image Four"]
    
    #Initialise plot 
    fig4=plt.figure()
    ax=fig4.add_subplot(111)
    # Make scatter plot
    ax.scatter(x_values,size_list)
    ax.set_xlabel("Image Evaluated")
    ax.set_ylabel("Mean Pixel Value of Region of Interest")
    ax.set_title("Evaluation of Tumour Shrinkage Between CT Scans")
    #title for when spine is plotted
    #ax.set_title("Mean Spine Pixel Value is Constant Between CT Scans")
    
    #Tumour_Value_Plot.png Shows tumour size decreasing with time (image pixel values decrease over time)
    #Spine_Value_Plot.png Shows spine values staying constant over time

    plt.show()

if __name__ == "__main__": 
    main()
